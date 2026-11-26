from fastapi import FastAPI, Header, HTTPException, Depends
from fastapi import WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator
from typing import Optional
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
import mysql.connector
import bcrypt

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["GET", "POST", "PUT", "PATCH"],
    allow_headers=["*"]
)

# JWT Configuration
SECRET_KEY = "my-secret-key-change-in-production"
ALGORITHM = "HS256"


# MySQL Connection
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="student_db"
    )
class User(BaseModel):
    username: str
    password: str

    @field_validator("username")
    @classmethod
    def check_username(cls, value):
        if value.isdigit():
            raise ValueError("Username cannot contain only numbers")
        return value

class Student(BaseModel):
    name: str
    age: int
    course: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    course: Optional[str] = None


# SIGNUP - Register User
@app.post("/signup")
def signup(user: User):

    conn = get_db()
    cursor = conn.cursor()

    try:
        # Hash password
        hashed_password = bcrypt.hashpw(
            user.password.encode("utf-8"),
            bcrypt.gensalt()
        )

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (user.username, hashed_password.decode("utf-8"))
        )

        conn.commit()

        return {"message": "User registered successfully"}

    except mysql.connector.IntegrityError:
        conn.rollback()
        raise HTTPException(
            status_code=409,
            detail="Username already exists"
        )

    finally:
        cursor.close()
        conn.close()


# LOGIN - Generate JWT Token
@app.post("/login")
def login(user: User):

    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            "SELECT * FROM users WHERE username=%s",
            (user.username,)
        )

        db_user = cursor.fetchone()

    finally:
        cursor.close()
        conn.close()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    # Verify password
    if not bcrypt.checkpw(
        user.password.encode("utf-8"),
        db_user["password"].encode("utf-8")
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    # Generate JWT
    token = jwt.encode({
        "sub": user.username,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
    }, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# JWT Verification
def verify_token(authorization: str = Header(...)):

    try:
        scheme, token = authorization.split()

        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=401,
                detail="Invalid token scheme"
            )

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if not username:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return username

    except (JWTError, ValueError):
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )


# GET - All Students (Query Parameter)
@app.get("/students")
def get_students(
    course: Optional[str] = None,
    user=Depends(verify_token)
):

    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    try:
        if course:
            cursor.execute(
                "SELECT * FROM students WHERE course=%s",
                (course,)
            )
        else:
            cursor.execute("SELECT * FROM students")

        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


# GET - Student by ID (Path Parameter)
@app.get("/students/{id}")
def get_student(
    id: int,
    user=Depends(verify_token)
):

    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            "SELECT * FROM students WHERE id=%s",
            (id,)
        )

        data = cursor.fetchone()

        if not data:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return data

    finally:
        cursor.close()
        conn.close()


# POST - Create Student
@app.post("/students")
def create_student(
    student: Student,
    user=Depends(verify_token)
):

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO students (name, age, course) VALUES (%s,%s,%s)",
            (student.name, student.age, student.course)
        )

        conn.commit()

        return {"message": "Student created successfully"}

    finally:
        cursor.close()
        conn.close()


# PUT - Full Update
@app.put("/students/{id}")
def update_student(
    id: int,
    student: Student,
    user=Depends(verify_token)
):

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s",
            (student.name, student.age, student.course, id)
        )

        if cursor.rowcount == 0:
            cursor.execute(
                "SELECT id FROM students WHERE id=%s",
                (id,)
            )

            if cursor.fetchone() is None:
                raise HTTPException(
                    status_code=404,
                    detail="Student not found"
                )

        conn.commit()

        return {"message": "Student updated successfully"}

    finally:
        cursor.close()
        conn.close()


# PATCH - Partial Update
@app.patch("/students/{id}")
def patch_student(
    id: int,
    student: UpdateStudent,
    user=Depends(verify_token)
):

    data = student.model_dump(exclude_unset=True)

    if not data:
        raise HTTPException(
            status_code=400,
            detail="No data provided"
        )

    allowed_fields = {"name", "age", "course"}

    if not set(data).issubset(allowed_fields):
        raise HTTPException(
            status_code=400,
            detail="Invalid fields"
        )

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT id FROM students WHERE id=%s",
            (id,)
        )

        if cursor.fetchone() is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        fields = ", ".join(f"{key}=%s" for key in data)
        values = list(data.values()) + [id]

        cursor.execute(
            f"UPDATE students SET {fields} WHERE id=%s",
            values
        )

        conn.commit()

        return {"message": "Student partially updated"}

    finally:
        cursor.close()
        conn.close()


# DELETE - Student
@app.delete("/students/{id}")
def delete_student(
    id: int,
    user=Depends(verify_token)
):

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "DELETE FROM students WHERE id=%s",
            (id,)
        )

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        conn.commit()

        return {"message": "Student deleted successfully"}

    finally:
        cursor.close()
        conn.close()


# WEBSOCKET
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    try:
        while True:
            message = await websocket.receive_text()

            await websocket.send_text(
                "Server received: " + message
            )

    except WebSocketDisconnect:
        print("Client disconnected")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
