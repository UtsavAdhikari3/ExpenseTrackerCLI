import argparse,os,json
import datetime

EXPENSE_FILE = "expense.json"


def load_expense():
    if not os.path.exists(EXPENSE_FILE):
        return []
    with open(EXPENSE_FILE,"r") as f:
        return json.load(f)

def save_expense(expense):
    with open(EXPENSE_FILE,"w") as f:
        json.dump(expense, f, indent=4)


def add_expense(description,amount):
    expenses = load_expense()
    new_id = 1 if not expenses else max(expense["id"] for expense in expenses) + 1
    new_expense = {
        "id":new_id,
        "description":description,
        "amount":amount,
        "date":datetime.datetime.now()
    }
    expenses.append(new_expense)
    save_expense(expenses)
    print(f"Expense added successfully (ID: {id})")

def main():
    parser = argparse.ArgumentParser(
        prog='ExpenseTrackerCLI',
        description='Track your expenses easily.',
        epilog='Built By UtsavAdhikari3'
    )
    sub = parser.add_subparsers(dest="command", required=False)

    # add Subcommands
    add = sub.add_parser("add", help="Add an expense with --description and amount")
    add.add_argument("--description", type=str,required=True)
    add.add_argument("--ammount", type=int, required=True)







if __name__ == "__main__":
    main()