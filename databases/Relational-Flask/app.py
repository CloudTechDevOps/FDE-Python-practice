from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

# =========================
# RDS MASTER / WRITER CONFIG
# =========================
HOST = 'localhost'  # master endpoint
USER = 'root'
PASSWORD = 'root'
DB_NAME = 'dev'
TABLE_NAME = 'users'

# =========================
# GET ALL USERS
# =========================
@app.route('/users', methods=['GET'])
def get_users():
    try:
        # Connect to master DB
        connection = pymysql.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor  # rows as dict
        )

        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {TABLE_NAME} LIMIT 10;")
            users = cursor.fetchall()

        # ✅ Return only the user data
        return jsonify(users)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if 'connection' in locals():
            connection.close()

# =========================
# Health Check
# =========================
@app.route('/')
def index():
    return "Localhost API running"

# =========================
# Entry Point
# =========================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)