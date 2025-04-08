from flask import Flask
import psycopg2

app = Flask(__name__)

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="mydb",
            user="myuser",
            password="mypassword",
            host="db"
        )
        return conn
    except Exception as e:
        return str(e)

@app.route('/')
def home():
    return "Flask App with PostgreSQL!"

@app.route('/db')
def test_db():
    conn = connect_db()
    if isinstance(conn, str):
        return f"Database connection failed: {conn}"
    return "Connected to the database!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
