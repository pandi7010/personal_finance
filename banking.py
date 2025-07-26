import sqlite3

def create_account(name, email):
    conn = sqlite3.connect("finance.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

def deposit(user_id, amount):
    conn = sqlite3.connect("finance.db")
    c = conn.cursor()
    c.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (amount, user_id))
    c.execute("INSERT INTO transactions (user_id, type, amount, category) VALUES (?, 'deposit', ?, 'income')", (user_id, amount))
    conn.commit()
    conn.close()

def withdraw(user_id, amount):
    conn = sqlite3.connect("finance.db")
    c = conn.cursor()
    c.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
    balance = c.fetchone()[0]
    if balance >= amount:
        c.execute("UPDATE users SET balance = balance - ? WHERE id = ?", (amount, user_id))
        c.execute("INSERT INTO transactions (user_id, type, amount, category) VALUES (?, 'withdraw', ?, 'expense')", (user_id, amount))
        conn.commit()
    else:
        print("Insufficient funds")
    conn.close()

def check_balance(user_id):
    conn = sqlite3.connect("finance.db")
    c = conn.cursor()
    c.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
    balance = c.fetchone()[0]
    conn.close()
    return balance
