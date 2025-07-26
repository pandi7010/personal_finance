import sqlite3

def get_transaction_history(user_id):
    conn = sqlite3.connect("finance.db")
    c = conn.cursor()
    c.execute("SELECT type, amount, category, timestamp FROM transactions WHERE user_id = ? ORDER BY timestamp DESC", (user_id,))
    rows = c.fetchall()
    conn.close()
    return rows
