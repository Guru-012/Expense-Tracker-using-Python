import os

FILE_NAME = "expenses.txt"

def load_expenses():
    expenses = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                amount, category, note = line.strip().split(",")
                expenses.append({
                    "amount": float(amount),
                    "category": category,
                    "note": note
                })
    return expenses

def save_expense(expense):
    with open(FILE_NAME, "a") as file:
        file.write(f"{expense['amount']},{expense['category']},{expense['note']}\n")

def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, etc): ")
    note = input("Enter note: ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }

    expenses.append(expense)
    save_expense(expense)
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    for i, exp in enumerate(expenses, 1):
        print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['note']}")

def total_expense(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total Expense: ₹{total}")

def filter_by_category(expenses):
    category = input("Enter category to filter: ")
    filtered = [exp for exp in expenses if exp["category"].lower() == category.lower()]

    if not filtered:
        print("No expenses found for this category.")
        return

    for exp in filtered:
        print(f"₹{exp['amount']} | {exp['note']}")

def menu():
    expenses = load_expenses()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Filter by Category")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expense(expenses)
        elif choice == "4":
            filter_by_category(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

menu()
