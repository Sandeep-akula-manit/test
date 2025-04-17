from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Backend World!"

@app.route('/users')
def get_users():
    try:
        conn = psycopg2.connect(
            dbname="test_db",
            user="postgres",
            password="Postgres",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(100))")
        cur.execute("INSERT INTO users (name) VALUES ('Alice') ON CONFLICT DO NOTHING")
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return {"users": users}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(debug=True)