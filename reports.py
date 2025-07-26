import sqlite3

def get_monthly_summary(user_id):
    conn = sqlite3.connect("finance.db")
    c = conn.cursor()
    c.execute('''SELECT strftime('%Y-%m', timestamp) as month, 
                        SUM(CASE WHEN type='deposit' THEN amount ELSE 0 END) as income,
                        SUM(CASE WHEN type='withdraw' THEN amount ELSE 0 END) as expense
                 FROM transactions
                 WHERE user_id = ?
                 GROUP BY month
                 ORDER BY month DESC''', (user_id,))
    summary = c.fetchall()
    conn.close()
    return summary
