import sqlite3

DB_PATH = "sample.db"

def fetch_user_names():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users")
    results = [row[0] for row in cursor.fetchall()]
    conn.close()
    return results

def insert_user(name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
