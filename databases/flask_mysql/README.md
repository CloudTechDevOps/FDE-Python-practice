# Flask + MySQL CRUD Operations

## 1. Install Dependencies

```bash
pip install flask flask-cors mysql-connector-python email-validator
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

from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import IntegrityError

app = Flask(__name__)
CORS(app)


# Database Connection
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="dev"
    )


# GET - All users
@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    conn.close()
    return jsonify(data)


# GET - Single user
@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
    data = cursor.fetchone()

    conn.close()

    if not data:
        return jsonify({"error": "User not found"}), 404

    return jsonify(data)


# POST - Add user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            (data["name"], data["email"])
        )
        conn.commit()

        return jsonify({"message": "User added successfully"}), 201

    except IntegrityError:
        return jsonify({"error": "Email already exists"}), 409

    finally:
        conn.close()


# PUT - Update user
@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET name=%s, email=%s WHERE id=%s",
        (data["name"], data["email"], id)
    )

    conn.commit()
    updated = cursor.rowcount
    conn.close()

    if updated == 0:
        return jsonify({"error": "User not found or no changes"}), 404

    return jsonify({"message": "User updated successfully"})


# DELETE - Delete user
@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    conn.commit()

    deleted = cursor.rowcount
    conn.close()

    if deleted == 0:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": "User deleted successfully"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

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


