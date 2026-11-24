# MongoDB CRUD Operations

This notebook uses **PyMongo** to perform the four basic CRUD operations
in MongoDB.

-   **Create** -- Add a trainee
-   **Read** -- Display all trainees
-   **Update** -- Change a trainee's age
-   **Delete** -- Remove a trainee

## Prerequisites

Before starting, make sure:

1.  MongoDB Community Server is installed on your computer.
2.  The MongoDB server is running.
3.  Python and Jupyter Notebook are installed.

## 1. Install PyMongo

Run this cell once to install the Python package:

``` python
%pip install pymongo
```

## 2. Connect to MongoDB

`MongoClient` connects Python to the MongoDB server running on your
computer. The default MongoDB address is `localhost:27017`.

``` python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
print("Connected to MongoDB!")
```

## 3. Select a database and collection

-   **Database name:** `training_center`
-   **Collection name:** `trainees`

A MongoDB collection is similar to a table in a relational database. A
document is similar to a row, and in Python it is represented using a
dictionary.

``` python
db = client["training_center"]
trainees = db["trainees"]

print("Database and collection selected!")
```

## 4. CREATE -- Add one trainee

The `insert_one()` method adds one document to the collection.

Change the name, age, or course and run the cell again to add another
trainee.

``` python
trainee = {"name": "Veera", "age": 30, "course": "Python"}

trainees.insert_one(trainee)
print("Trainee added!")
```

## 5. READ -- Show all trainees

The `find()` method retrieves documents from the collection.

The `for` loop displays one document at a time. Here, `trainee_doc` is
the variable that stores the current document.

``` python
for trainee_doc in trainees.find():
    print(trainee_doc["name"], trainee_doc["age"], trainee_doc["course"])
```

## 6. UPDATE -- Change a trainee's age

The `update_one()` method finds a document using the filter and updates
the specified field.

-   **First dictionary:** Identifies the trainee to find.
-   **Second dictionary:** Specifies what to update.
-   **`$set`:** Updates the given field without replacing the entire
    document.

``` python
result = trainees.update_one(
    {"name": "Veera"},
    {"$set": {"age": 31}}
)

print("Matched:", result.matched_count)
print("Modified:", result.modified_count)

if result.matched_count == 0:
    print("No trainee found with the name Veera.")
else:
    print("Trainee update operation completed!")
```

### Check the updated trainee

The `find_one()` method retrieves the first document matching the
filter.

``` python
updated_trainee = trainees.find_one({"name": "Veera"})

if updated_trainee:
    print(updated_trainee)
else:
    print("No trainee found with the name Veera.")
```

## 7. DELETE -- Remove a trainee

The `delete_one()` method removes the first document that matches the
filter.

**Warning:** Deleting a document is permanent unless you have a backup.

``` python
result = trainees.delete_one({"name": "Veera"})

print("Deleted:", result.deleted_count)

if result.deleted_count == 0:
    print("No trainee found with the name Veera.")
else:
    print("Trainee deleted!")
```

### Check all remaining trainees

Run `find()` again to display the documents that remain in the
collection.

``` python
for trainee_doc in trainees.find():
    print(trainee_doc["name"], trainee_doc["age"], trainee_doc["course"])
```

## 8. Close the MongoDB connection

When you finish working with MongoDB, close the client connection.

``` python
client.close()
print("MongoDB connection closed.")
```

## CRUD Methods Summary

  Operation   PyMongo method   Purpose
  ----------- ---------------- ---------------------------------------
  Create      `insert_one()`   Inserts one document
  Read        `find()`         Retrieves matching documents
  Read one    `find_one()`     Retrieves the first matching document
  Update      `update_one()`   Updates one matching document
  Delete      `delete_one()`   Deletes one matching document
