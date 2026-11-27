# Project Setup and Execution Guide

Follow the steps below to clone, configure, run, and test the project on your local machine.

## 1. Clone the GitHub Repository

Open VS Code terminal or Git Bash and execute:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate into the project directory:

```bash
cd <PROJECT_FOLDER_NAME>
```

## 2. Install Required Python Packages

Make sure Python is installed on your system.

Check Python version:

```bash
python --version
```

Install all the required dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install all the Python packages required for the backend application.

## 3. Configure MySQL Credentials

Open `app.py` in VS Code.

Locate the MySQL database configuration and update the credentials according to your local MySQL setup.

Example:

```python
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "dev"
}
```

Update the following details:

- **host:** localhost
- **user:** Your MySQL username
- **password:** Your MySQL password
- **database:** Your database name

Save the changes.

**Important:** Make sure your MySQL server is running.

## 4. Execute the SQL Script in MySQL Workbench

1. Open MySQL Workbench.
2. Connect to your local MySQL server.
3. Open the SQL script provided in the project.
4. Review the database and table creation queries.
5. Execute the complete SQL script by clicking the lightning icon.
6. Refresh the Schemas section.
7. Verify that the database and required tables are created successfully.

Make sure the database name in `app.py` matches the database created using the SQL script.

## 5. Install Live Server Extension in VS Code

We are using the frontend locally.

Follow these steps:

1. Open VS Code.
2. Navigate to Extensions.
3. Search for **Live Server**.
4. Install the Live Server extension.
5. Open the project folder in VS Code.

No frontend-backend IP address changes are required because we are running both applications locally.

The frontend is configured to communicate with the backend using:

```javascript
http://127.0.0.1:8000
```

## 6. Start the FastAPI Backend

Open a terminal in VS Code.

Make sure you are inside the project directory.

Start the backend application:


```bash
python app.py
```

Once the application starts successfully, the backend will be available at:

**Backend URL:**

```text
http://127.0.0.1:8000
```

**Swagger API Documentation:**

```text
http://127.0.0.1:8000/docs
```

Keep this terminal running.

## 7. Start the Frontend Using Live Server

1. Navigate to the frontend folder.
2. Locate `index.html`.
3. Right-click on `index.html`.
4. Select **Open with Live Server**.
