import pymysql

#pymysql = Third-party library.

# MySQL Connection
def get_db_connection(): # connect DB
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="student_db",
        
    )


# Retrieve all students

def get_students():

    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students")

        students = cursor.fetchall()

        return students

    finally:
        cursor.close()
        conn.close() # memory cosume, concurancy , locking, security 


# Calling the function
result = get_students()

print("All Student Records:")

for student in result:
    print(student)