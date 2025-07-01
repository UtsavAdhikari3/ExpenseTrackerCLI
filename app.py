import argparse
import os
import json
import datetime

EXPENSE_FILE = "expense.json"

def load_expense():
    if not os.path.exists(EXPENSE_FILE):
        return []
    with open(EXPENSE_FILE, "r") as f:
        return json.load(f)

def save_expense(expenses):
    with open(EXPENSE_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(description, amount):
    expenses = load_expense()
    new_id = 1 if not expenses else max(exp["id"] for exp in expenses) + 1
    new_expense = {
        "id": new_id,
        "description": description,
        "amount": amount,
        "date": datetime.date.today().strftime("%Y-%m-%d")
    }
    expenses.append(new_expense)
    save_expense(expenses)
    print(f"Expense added successfully (ID: {new_id})")

def list_expense():
    expenses = load_expense()
    if not expenses:
        print("No expense found.")
    else:
        print(f"id    date                      description     amount")
        for expense in expenses:
            print(f"{expense["id"]}     {expense["date"]}       {expense["description"]}           {expense["amount"]}")

def summary():
    expenses = load_expense()
    add = 0
    if not expenses:
        print("No expenses found.")
    for expense in expenses:
        total = expense["amount"] + add
        add = total
    
    print(f"Total expense: ${total}")


def delete(id):
    expenses = load_expense()
    for expense in expenses:
        if expense["id"] == id:
            expenses.remove(expense)
            save_expense(expenses)
    print(expenses)

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='ExpenseTrackerCLI',
        description='Track your expenses easily.',
        epilog='Built By UtsavAdhikari3'
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # Add subcommand
    add = sub.add_parser("add", help="Add an expense")
    add.add_argument("--description", type=str, required=True, help="Description of the expense")
    add.add_argument("--amount", type=int, required=True, help="Amount spent")


    # List subcommand
    list_expenditure = sub.add_parser("list",help="List all your expenses")

    # Summary submcommand
    summarise_expense = sub.add_parser("summary",help="Get a total of all your expenses.")

    # Delete Subcommand
    delete_expense = sub.add_parser("delete",help="Delete an expense")
    delete_expense.add_argument("--id",type=int, required=True,help="Enter the id of the expense you want to delete")

    return parser  

def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "list":
        list_expense()
    elif args.command == "summary":
        summary()
    elif args.command == "delete":
        delete(args.id)

if __name__ == "__main__":
    main()
