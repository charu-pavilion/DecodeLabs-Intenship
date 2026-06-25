expenses=[]

while(True):
    print("***Expense Tracker***")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        expense_name = input("Enter expense name: ")
        expense_amount = float(input("Enter expense amount: "))
        expenses.append((expense_name, expense_amount))
        print("Expense added successfully!")                                                  

    elif choice == '2':
        if not expenses:
            print("No expenses recorded.")
        else:
            print("Expenses:")
            for expense in expenses:
                print(f"{expense[0]}: Rs{expense[1]:.2f}")

    elif choice == '3':
        total = 0
        for expense in expenses:
            total += expense[1]
        print(f"Total Expenses: Rs{total:.2f}")

    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")