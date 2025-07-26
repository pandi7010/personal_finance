from database import connect
from banking import create_account, deposit, withdraw, check_balance
from transactions import get_transaction_history
from reports import get_monthly_summary

connect()

print("\n=== Personal Finance Banking System ===")
user_id = int(input("Enter your user ID (or 0 to create a new account): "))

if user_id == 0:
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    create_account(name, email)
    print("Account created.")
    exit()

while True:
    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. View Transactions\n5. View Monthly Summary\n6. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        print("Balance:", check_balance(user_id))

    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        deposit(user_id, amount)

    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        withdraw(user_id, amount)

    elif choice == '4':
        history = get_transaction_history(user_id)
        for tx in history:
            print(tx)

    elif choice == '5':
        summary = get_monthly_summary(user_id)
        for row in summary:
            print("Month:", row[0], "Income:", row[1], "Expense:", row[2])

    elif choice == '6':
        break
