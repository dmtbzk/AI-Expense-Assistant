import sqlite3

DB_PATH = "database.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def close_connection(connection):
    connection.close()

def create_expense_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    category TEXT,
    created_at TEXT DEFAULT CURRENT_DATE,
    description TEXT
    )"""
    )
    connection.commit()
    close_connection(connection)