expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Expense Name: ")
        amount = float(input("Amount: ₹"))
        expenses.append((item, amount))
        print("✅ Expense Added!")

    elif choice == "2":
        print("\nYour Expenses:")
        for item, amount in expenses:
            print(f"{item}: ₹{amount}")

    elif choice == "3":
        total = sum(amount for item, amount in expenses)
        print(f"💰 Total Spending: ₹{total}")

    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid Choice")
