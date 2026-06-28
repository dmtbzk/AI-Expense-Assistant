from app.database.connection import get_connection, close_connection

def add_expense(amount: float, category: str, description: str):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)", (amount, category, description))
    connection.commit()
    expense_id = cursor.lastrowid
    close_connection(connection)
    return {
        "id": expense_id,
        "amount": amount,
        "category": category,
        "description": description
        }

def get_expenses():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    close_connection(connection)
    return expenses