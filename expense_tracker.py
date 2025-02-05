def show_menu():
    print("\n===== Expense Tracker Menu =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. View Total Expenses")
    print("5. Exit")

def add_expenses(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, Shopping, Bills, Other): ").capitalize()
    date = input("Enter date (YYYY-MM-DD): ")
    if category not in expenses:
        expenses[category] = []
    
    expenses[category].append({"Amount": amount, "Date": date})
    print("Expense added successfully!")

def view_expenses(expenses):
    print("\n===== Expense List =====")
    if not expenses:
        print("No expenses found!")
    else:
        expense_number = 1
        for category, expense_list in expenses.items():
            for expense in expense_list:
                print(f"{expense_number}. {expense['Amount']} - {category} - {expense['Date']}")
                expense_number += 1

def delete_expenses(expenses):
    if not expenses:
        print("No expenses to delete!")
    else:
        expense_number = int(input("Enter the expense number to delete: "))
        count = 1
        for category, expense_list in expenses.items():
            for expense in expense_list:
                if count == expense_number:
                    expense_list.remove(expense)
                    print("Expense deleted successfully!")
                    return
                count += 1

def total_expenses(expenses):
    total = 0
    if not expenses:
        print("Total Expenses: 0")

    else:
        for category, expense_list in expenses.items():
            for expense in expense_list:
                total += expense['Amount']
        print(f"Total Expenses: {total}")


def main():
    expenses = {}  
    while True:
        show_menu()
        choice = input("Choose your choice: ")

        if choice == "1":
            add_expenses(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            delete_expenses(expenses)

        elif choice == "4":
            total_expenses(expenses)

        elif choice == "5":
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

