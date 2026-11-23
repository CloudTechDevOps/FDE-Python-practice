## 1. What is a Database?

A **Database** is an organized collection of data that allows applications to store, retrieve, update, and delete information.

---

# 2. Types of Databases

There are several types of databases. The most commonly used categories are:

1. Relational Database (SQL)
2. NoSQL Database
3. Vector Database

## A. Relational Database (SQL)

Relational databases store data in the form of tables consisting of rows and columns.

### Example: Employees Table

| **ID** | **Name** | **Age** | **Department** |
| ------ | -------- | ------- | -------------- |
| 1      | Veera    | 30      | DevOps         |
| 2      | Ravi     | 25      | Python         |
| 3      | Kumar    | 28      | Cloud          |

### Characteristics

- Data is stored in tables.
- Each table contains rows and columns.
- Tables can be connected using Primary Keys and Foreign Keys.
- Uses SQL (Structured Query Language).
- Generally follows a predefined schema.
- Supports transactions and data consistency.

### Popular Relational Databases

| **Database**         | **Description**                             |
| -------------------- | ------------------------------------------- |
| MySQL                | Popular open-source relational database     |
| PostgreSQL           | Advanced open-source relational database    |
| Oracle Database      | Enterprise-level relational database        |
| Microsoft SQL Server | Microsoft's relational database             |
| SQLite               | Lightweight database stored in a local file |
| MariaDB              | MySQL-compatible relational database        |

### Real-Time Use Cases

- Banking applications
- E-commerce applications
- Hospital management systems
- Employee management systems
- Inventory management systems
- Financial applications

---

## B. NoSQL Database

NoSQL databases store data in different formats instead of relying exclusively on traditional relational tables.

They are useful when applications need flexible data structures, distributed storage, or specific access patterns.

### Types of NoSQL Databases

| **Type**      | **Description**                        | **Example** |
| ------------- | -------------------------------------- | ----------- |
| Document      | Stores JSON-like documents             | MongoDB     |
| Key-Value     | Stores data as key-value pairs         | Redis       |
| Column-Family | Stores data in column families         | Cassandra   |
| Graph         | Stores data as nodes and relationships | Neo4j       |

### Example: MongoDB Document

json

```
{
    "id": 1,
    "name": "Veera",
    "age": 30,
    "department": "DevOps",
    "skills": ["AWS", "Python", "Docker"]
}

```

### Characteristics

- Flexible data models.
- Supports different data structures.
- Some databases support horizontal scaling across multiple servers.
- Useful for applications handling diverse or rapidly changing data.
- Query methods differ depending on the database.

### Real-Time Use Cases

| **Application**          | **Database** | **Use Case**                       |
| ------------------------ | ------------ | ---------------------------------- |
| Social Media             | MongoDB      | Flexible application data          |
| Real-Time Chat           | Redis        | Fast data access and caching       |
| Distributed Applications | Cassandra    | Distributed data storage           |
| Social Networks          | Neo4j        | User connections and relationships |

---

## C. Vector Database (Vector DB)

A **Vector Database** is designed to store, index, and search vector embeddings based on similarity.

It is widely used in:

- Artificial Intelligence (AI)
- Generative AI (GenAI)
- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Recommendation Systems

### What is a Vector?

A vector is a numerical representation of information.

For example:

Text:

"Python is a programming language."

An embedding model converts this text into a numerical vector.

python

```
[0.23, 0.45, 0.67, 0.12, 0.89]

```

These numbers represent information about the text in a mathematical form.

A Vector Database uses these embeddings to find similar content.

### How Does Vector Database Work?

Imagine an AI chatbot for a company.

The company has three documents:

1. Python Fundamentals
2. AWS DevOps
3. Kubernetes

A user asks:

"How can I deploy containers in AWS?"

The Vector Database searches for relevant information based on semantic similarity.

Even when the question and documents use different words, the system can retrieve content with similar meaning.

### Popular Vector Databases and Tools

| **Name** | **Description**                                   |
| -------- | ------------------------------------------------- |
| Pinecone | Managed Vector Database                           |
| ChromaDB | Open-source Vector Database                       |
| Milvus   | Open-source Vector Database                       |
| Weaviate | Vector Database                                   |
| Qdrant   | Vector Database                                   |
| pgvector | Vector similarity search extension for PostgreSQL |
| FAISS    | Vector similarity search library                  |

**Note:** FAISS is a vector similarity search library, not a traditional standalone database.

### Real-Time Use Cases

| **Application**       | **Use Case**                           |
| --------------------- | -------------------------------------- |
| AI Chatbot            | Search relevant documents              |
| Resume Screening      | Find resumes matching job descriptions |
| E-commerce            | Find similar products                  |
| AI Search Engine      | Search information based on meaning    |
| Customer Support      | Retrieve answers from company FAQs     |
| Recommendation System | Recommend similar content              |

---

# 3. SQL vs NoSQL vs Vector Database

| **Feature** | **SQL**              | **NoSQL**                   | **Vector DB**                  |
| ----------- | -------------------- | --------------------------- | ------------------------------ |
| Stores      | Tables               | Documents, key-value, etc.  | Vector embeddings and metadata |
| Structure   | Structured           | Flexible, depending on type | Vector-based                   |
| Search      | SQL queries          | Database-specific queries   | Similarity search              |
| Schema      | Generally predefined | Often flexible              | Depends on implementation      |
| Examples    | MySQL                | MongoDB                     | Pinecone                       |
| Usage       | Banking              | Social Media                | AI Chatbot                     |

**Important:**

- SQL databases are designed for relational data and transactions.
- NoSQL databases support different data models and access patterns.
- Vector databases are optimized for similarity search.

These technologies can work together in the same application.

---

# 4. Popular Databases – Easy Way to Remember

| **Database** | **Remember It As**                     |
| ------------ | -------------------------------------- |
| MySQL        | Tables and relationships               |
| PostgreSQL   | Advanced relational database           |
| MongoDB      | JSON documents                         |
| Redis        | Fast in-memory data access and caching |
| Cassandra    | Large-scale distributed data           |
| Neo4j        | Relationships and connections          |
| SQLite       | Local application storage              |
| InfluxDB     | Time-series data                       |
| ChromaDB     | Vector search                          |
| Pinecone     | Managed vector database                |

---

# 5. Real-Time Application Examples

Modern applications can use multiple databases together. Each database handles a particular requirement.

## Example 1: Amazon Shopping Application

| **Database**       | **Purpose**                             |
| ------------------ | --------------------------------------- |
| MySQL / PostgreSQL | Customer and order details              |
| Redis              | Caching and shopping cart data          |
| MongoDB            | Product catalogue (one possible design) |
| Vector DB          | Similar product recommendations         |

## Example 2: Instagram

| **Database**        | **Purpose**                                       |
| ------------------- | ------------------------------------------------- |
| Relational Database | User accounts and structured records              |
| NoSQL Database      | Large-scale application activity and content data |
| Redis               | Caching frequently accessed information           |
| Vector DB           | Similar content recommendations                   |

## Example 3: Netflix

| **Database**        | **Purpose**                              |
| ------------------- | ---------------------------------------- |
| Cassandra           | Distributed data storage                 |
| Redis               | Caching                                  |
| Relational Database | Billing and subscription information     |
| Vector DB           | Similarity-based content recommendations |

## Example 4: Uber

| **Database** | **Purpose**                                 |
| ------------ | ------------------------------------------- |
| PostgreSQL   | Structured ride and customer records        |
| Redis        | Real-time data access and caching           |
| MongoDB      | Flexible application data                   |
| Vector DB    | Recommendation and semantic search features |

## Example 5: Banking Application

| **Database**       | **Purpose**                              |
| ------------------ | ---------------------------------------- |
| MySQL / PostgreSQL | Customer accounts and transactions       |
| Redis              | Frequently accessed information          |
| Vector DB          | Semantic search across banking documents |

**Note:** These are illustrative technology choices. Actual production architectures may use different databases and services.

---

# 6. How Does an Application Interact With a Database?

An application communicates with a database through a database driver or connector.

### Basic Architecture

text

```
          USER
            |
            v
         FRONTEND
        (HTML/React)
            |
            v
        BACKEND API
        (Python/FastAPI)
            |
            v
      DATABASE DRIVER
         (PyMySQL)
            |
            v
         DATABASE
           (MySQL)
            |
            v
        STORED DATA

```

### Explanation

1. User sends a request through the frontend.
2. Backend API receives the request.
3. Backend validates the incoming data.
4. Database driver establishes communication with the database.
5. Backend executes the required query.
6. Database processes the query.
7. Database returns the result.
8. Backend sends the response to the frontend.

---

# 7. Different Ways to Connect Databases Using Python

Python provides different libraries and connectors for communicating with databases.

| **Database** | **Python Library / Connector**   |
| ------------ | -------------------------------- |
| MySQL        | PyMySQL / mysql-connector-python |
| PostgreSQL   | psycopg                          |
| MongoDB      | PyMongo                          |
| Redis        | redis-py                         |
| SQLite       | sqlite3                          |
| ChromaDB     | chromadb                         |
| Pinecone     | Pinecone SDK                     |
| SQL Server   | pyodbc                           |
| Oracle       | python-oracledb                  |

---

# 8. Practical Example: Python + MySQL Database Connection

Let's understand how Python communicates with MySQL.

### Step 1: Install PyMySQL

bash

```
pip install pymysql

```

### Step 2: Create a MySQL Database

sql

```
CREATE DATABASE company_db;

USE company_db;

```

### Step 3: Create an Employees Table

sql

```
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    department VARCHAR(100)
);

```

### Step 4: Connect Python to MySQL

Create a Python file named `db_connection.py`.

python

```
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="company_db"
)

print("Database Connected Successfully")

```

### Step 5: Understand the Connection Components

| **Component** | **Purpose**                             |
| ------------- | --------------------------------------- |
| pymysql       | Python database connector               |
| conn          | Database connection object              |
| cursor        | Executes SQL queries                    |
| execute()     | Sends SQL query to MySQL                |
| fetchall()    | Retrieves all returned records          |
| fetchone()    | Retrieves one record                    |
| fetchmany()   | Retrieves a specified number of records |
| commit()      | Saves transaction changes               |
| close()       | Closes the database connection          |

---

# 9. CRUD Operations Using Python and MySQL


### Basic Database Operations (CRUD)

| **Operation** | **Purpose**            | **SQL Command** |
| ------------- | ---------------------- | --------------- |
| Create        | Insert new data        | INSERT          |
| Read          | Retrieve existing data | SELECT          |
| Update        | Modify existing data   | UPDATE          |
| Delete        | Remove existing data   | DELETE          |

CRUD stands for:

- C – Create
- R – Read
- U – Update
- D – Delete

Let's perform all four operations using Python and MySQL.

### 1. CREATE – Insert Data

Insert a new employee record into the database.

python

```
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="company_db"
)

cursor = conn.cursor()

query = """
INSERT INTO employees (name, age, department)
VALUES (%s, %s, %s)
"""

values = ("Veera", 30, "DevOps")

cursor.execute(query, values)

conn.commit()

print("Employee inserted successfully")

cursor.close()
conn.close()

```

**Explanation:**

- `cursor.execute()` executes the INSERT query.
- `%s` represents parameter placeholders.
- `values` contains the actual data.
- `conn.commit()` saves the changes permanently.

### 2. READ – Retrieve Data

Retrieve all employee records from MySQL.

python

```
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="company_db"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")

data = cursor.fetchall()

for employee in data:
    print(employee)

cursor.close()
conn.close()

```

**Explanation:**

- `SELECT` retrieves records.
- `fetchall()` retrieves all returned records.
- `for` loop displays each record.

### 3. UPDATE – Modify Data

Update an employee's department.

python

```
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="company_db"
)

cursor = conn.cursor()

query = """
UPDATE employees
SET department = %s
WHERE id = %s
"""

values = ("Cloud DevOps", 1)

cursor.execute(query, values)

conn.commit()

print("Employee updated successfully")

cursor.close()
conn.close()

```

**Explanation:**

- `UPDATE` modifies existing records.
- `SET` specifies the new value.
- `WHERE` identifies which record should be updated.
- `commit()` saves the modification.

### 4. DELETE – Remove Data

Delete an employee record.

python

```
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="company_db"
)

cursor = conn.cursor()

query = "DELETE FROM employees WHERE id = %s"

cursor.execute(query, (1,))

conn.commit()

print("Employee deleted successfully")

cursor.close()
conn.close()

```

**Explanation:**

- `DELETE` removes records.
- `WHERE` identifies the record to delete.
- `commit()` saves the deletion.

**Important:** Always use a WHERE condition when updating or deleting a specific record. Without it, the operation can affect every record in the table.

---

# 10. Understanding Database Communication

There are three important components involved in database communication.

### 1. Database

Where application data is stored.

Examples:

- MySQL
- MongoDB
- PostgreSQL
- Redis

### 2. Database Driver

Helps the application communicate with the database.

Examples:

- PyMySQL
- PyMongo
- psycopg
- redis-py

### 3. Query / API

Used to perform operations on the database.

Examples:

sql

```
INSERT
SELECT
UPDATE
DELETE

```

### Complete Communication Flow

text

```
        Python Application
                |
                v
        Database Connector
             PyMySQL
                |
                v
             Cursor
                |
                v
          SQL Query
                |
                v
            MySQL
                |
                v
          Database Data
                |
                v
          Query Result
                |
                v
        Python Application

```

---

# 11. How FastAPI Interacts With MySQL

FastAPI acts as the backend API between the frontend and the database.

### Architecture

text

```
       FRONTEND
      (HTML/React)
            |
            |
        HTTP Request
            |
            v
         FASTAPI
       (Python API)
            |
            v
        PYDANTIC
     (Data Validation)
            |
            v
      DATABASE DRIVER
         (PyMySQL)
            |
            v
           MySQL
            |
            v
        Database Data
            |
            v
        API Response
            |
            v
         FRONTEND

```

### Example: Employee Registration

Frontend sends the following JSON data:

json

```
{
    "name": "Veera",
    "age": 30,
    "department": "DevOps"
}

```

The process:

1. Frontend sends a POST request.
2. FastAPI receives the request.
3. Pydantic validates the incoming data.
4. PyMySQL communicates with MySQL.
5. MySQL executes the INSERT query.
6. Database stores the employee information.
7. FastAPI returns a response to the frontend.

---
# 12. Final Summary

| **Technology**  | **Main Purpose**                           |
| --------------- | ------------------------------------------ |
| SQL Database    | Store structured relational data           |
| NoSQL Database  | Store flexible and diverse data            |
| Vector Database | Store and search vector embeddings         |
| Redis           | Fast in-memory data access and caching     |
| Database Driver | Connect application with database          |
| FastAPI         | Expose backend functionality through APIs  |
| Semantic Layer  | Define business meaning over existing data |

### Remember:

- Database = Stores data.
- Database Driver = Connects application to database.
- SQL Query = Performs database operations.
- CRUD = Create, Read, Update and Delete.
- Backend API = Handles application requests.
- Vector Database = Finds information based on similarity.
- Semantic Layer = Helps applications understand business data and metrics.

**Conclusion:**

Understanding SQL, NoSQL, Vector Databases, CRUD operations, and Python database connectivity provides a strong foundation for Backend Development, Cloud Applications, and Generative AI Development.




# MongoDB Shell Commands

## 1. Create Connection

Connect to MongoDB using the MongoDB Shell (`mongosh`).

```bash
mongosh
```

## 2. Create Collection

Create a collection named `students`.

```javascript
db.createCollection("students")
```

## 3. Insert Documents

Insert multiple student documents into the `students` collection.

```javascript
db.students.insertMany([
    {name: "Veera", age: 30, course: "Python"},
    {name: "Ravi", age: 25, course: "AWS"},
    {name: "Kiran", age: 28, course: "DevOps"}
])
```

## 4. Read Documents

Display all documents from the `students` collection.

```javascript
db.students.find()
```

## 5. Update Documents

Update Veera's age from 30 to 31.

```javascript
db.students.updateOne(
    {name: "Veera"},
    {$set: {age: 31}}
)
```

## 6. Show Databases

Display all databases available in MongoDB.

```javascript
show dbs
```

## 7. Show Collections

Display all collections in the current database.

```javascript
show collections
```

## 8. Delete a Document

Delete a student whose name is Ravi.

```javascript
db.students.deleteOne(
    {name: "Ravi"}
)
```

## 9. Drop Collection

Delete the entire students collection.

```javascript
db.students.drop()
```

## 10. Drop Database

Delete the current database.

```javascript
db.dropDatabase()
```

---

**Note:**
- `db` refers to the current database.
- `students` is the collection name.
- Documents are stored in BSON format.
- `mongosh` is the MongoDB command-line shell.
