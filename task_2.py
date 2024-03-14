# Function to add income
def add_income(amount):
    global total_income
    total_income += amount
    print(f"Income of ${amount} added successfully.")

# Function to add an expense
def add_expense(category, amount):
    global total_expenses, expenses
    total_expenses += amount
    expenses.append({"category": category, "amount": amount})
    print(f"Expense of ${amount} under '{category}' category added successfully.")

# Function to calculate remaining budget
def calculate_budget():
    return total_income - total_expenses

# Function to analyze expenses by category
def analyze_expenses():
    category_expenses = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        if category in category_expenses:
            category_expenses[category] += amount
        else:
            category_expenses[category] = amount

    print("\nExpense Analysis:")
    for category, amount in category_expenses.items():
        print(f"{category}: ${amount}")

# Main function
def main():
    while True:
        print("\n===== Budget Tracker Menu =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Remaining Budget")
        print("4. Analyze Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            add_income(amount)

        elif choice == "2":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_expense(category, amount)

        elif choice == "3":
            remaining_budget = calculate_budget()
            print(f"\nRemaining Budget: ${remaining_budget}")

        elif choice == "4":
            analyze_expenses()

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    total_income = 0
    total_expenses = 0
    expenses = []
    main()
