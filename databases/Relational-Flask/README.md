# Flask – MySQL CRUD Operations

## 1. What is Flask?

Flask is a lightweight Python web framework used to build web applications and REST APIs.

A framework provides ready-made tools and functions that help developers build applications easily.

**Why Flask?**
- Build REST APIs.
- Connect frontend with backend.
- Connect with databases like MySQL.
- Perform CRUD operations.

## 2. Required Libraries

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
```

| Library | Purpose |
|---|---|
| Flask | Creates the backend application |
| request | Receives data from the frontend |
| jsonify | Sends responses in JSON format |
| CORS | Allows frontend applications from different origins to access the backend |
| mysql.connector | Connects Python with MySQL |

## 3. Create Flask Application

```python
app = Flask(__name__)
CORS(app)
```

- `Flask(__name__)` creates the Flask application.
- `CORS(app)` enables CORS for the application.

## 4. Database Configuration

```python
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'dev'
}
```

These are the MySQL database connection details.

| Field | Meaning |
|---|---|
| host | Database server address |
| user | MySQL username |
| password | MySQL password |
| database | Database name |

## 5. Connect to MySQL

```python
def get_db_connection():
    return mysql.connector.connect(**db_config)
```

This function establishes a connection between Python and MySQL.

Whenever we need database operations, we call this function.

## 6. CRUD Operations

CRUD stands for:

- Create – Add new data.
- Read – Retrieve existing data.
- Update – Modify existing data.
- Delete – Remove existing data.

### 1. GET – Retrieve All Users

```python
@app.route('/users', methods=['GET'])
def get_users():
```

- `@app.route()` defines the API URL.
- `GET` is used to retrieve data.
- `cursor(dictionary=True)` returns records in dictionary format.
- `fetchall()` retrieves all records.
- `jsonify()` converts the result into JSON.

**API:**

```text
GET http://127.0.0.1:5000/users
```

### 2. GET – Retrieve User by ID

```python
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
```

- `<int:user_id>` accepts an integer from the URL.
- `WHERE id = %s` searches for a particular user.
- `fetchone()` retrieves one record.
- If the user does not exist, it returns a 404 error.

**API:**

```text
GET http://127.0.0.1:5000/users/1
```

### 3. POST – Add a New User

```python
@app.route('/users/add', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')
```

- `POST` is used to insert new data.
- `request.json` receives JSON data from the frontend.
- `data.get()` retrieves the values.
- `INSERT INTO` inserts the record into MySQL.
- `conn.commit()` saves the changes permanently.

**API:**

```text
POST http://127.0.0.1:5000/users/add
```

Request Body:

```json
{
    "name": "Veera",
    "email": "veera@gmail.com"
}
```

### 4. PUT – Update User by ID

```python
@app.route('/users/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
```

- `PUT` is used to update existing data.
- `user_id` identifies which user to update.
- First, the code checks whether the user exists.
- `UPDATE` modifies the existing record.
- `conn.commit()` saves the changes.

**API:**

```text
PUT http://127.0.0.1:5000/users/update/1
```

Request Body:

```json
{
    "name": "Veera Updated",
    "email": "updated@gmail.com"
}
```

### 5. DELETE – Delete User by ID

```python
@app.route('/users/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
```

- `DELETE` removes an existing user.
- `user_id` identifies the user.
- First, the code checks whether the user exists.
- `DELETE FROM` removes the record.
- `conn.commit()` saves the deletion.

**API:**

```text
DELETE http://127.0.0.1:5000/users/delete/1
```

## 7. Simple Hello Route

```python
@app.route('/')
def index():
    return "Hello"
```

When we open the root URL, Flask returns the message Hello.

```text
http://127.0.0.1:5000/
```

## 8. Application Entry Point

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

| Parameter | Purpose |
|---|---|
| `__name__` | Checks whether the file is executed directly |
| `host='0.0.0.0'` | Makes the server listen on all network interfaces |
| `port=5000` | Runs Flask on port 5000 |
| `debug=True` | Enables debugging and automatic reloading |
