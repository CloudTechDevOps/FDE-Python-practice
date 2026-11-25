# FastAPI + MySQL CRUD Operations

## 1. Install Dependencies

```bash
pip install fastapi uvicorn mysql-connector-python email-validator
```

## 2. Create Database and Table

```sql
CREATE DATABASE IF NOT EXISTS dev;

USE dev;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);
```

## 3. Application File (app.py)

```python

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import mysql.connector
from mysql.connector import IntegrityError

app = FastAPI()


# Pydantic Model
class User(BaseModel):
    name: str
    email: EmailStr


# Database Connection
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="dev"
    )


# GET - All users
@app.get("/users")
def get_users():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    conn.close()
    return data


# GET - One user
@app.get("/users/{id}")
def get_user(id: int):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
    data = cursor.fetchone()

    conn.close()
    return data


# POST - Add user
# POST - Add user
@app.post("/users")
def add_user(user: User):
    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            (user.name, user.email)
        )

        conn.commit()
        return {"message": "User added successfully"}

    except IntegrityError:
        return {"error": "Email already exists"}

    finally:
        cursor.close()
        conn.close()


# PUT - Update user
@app.put("/users/{id}")
def update_user(id: int, user: User):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET name=%s, email=%s WHERE id=%s",
        (user.name, user.email, id)
    )

    conn.commit()
    conn.close()

    return {"message": "User updated successfully"}


# DELETE - Delete user
@app.delete("/users/{id}")
def delete_user(id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id=%s", (id,))

    conn.commit()
    conn.close()

    return {"message": "User deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)

```

## 4. Run Application

```bash
python app.py
```

Application URL:

```text
http://127.0.0.1:8000
```

## 5. cURL Commands

### GET - All Users

```bash
curl -X GET "http://127.0.0.1:8000/users"
```

### GET - Single User

```bash
curl -X GET "http://127.0.0.1:8000/users/1"
```

### POST - Create User

```bash
curl -X POST "http://127.0.0.1:8000/users" -H "Content-Type: application/json" -d "{\"name\":\"Veera\",\"email\":\"veera@gmail.com\"}"
```

### PUT - Update User

```bash
curl -X PUT "http://127.0.0.1:8000/users/1" -H "Content-Type: application/json" -d "{\"name\":\"Veera Updated\",\"email\":\"updated@gmail.com\"}"
```

### DELETE - Delete User

```bash
curl -X DELETE "http://127.0.0.1:8000/users/1"
```

## 6. Swagger UI

```text
http://127.0.0.1:8000/docs
```
