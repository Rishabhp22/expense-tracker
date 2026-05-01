import json
from datetime import datetime

# ---------- UTIL FUNCTIONS ----------

def load_data():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: Data file corrupted. Starting fresh.")
        return []

def save_data(data):
    with open("expenses.json", "w") as file:
        json.dump(data, file, indent=4)

def get_valid_date():
    while True:
        print("1. Enter date manually")
        print("2. Use today's date")

        choice = input("Choose option: ")

        if choice == "2":
            return datetime.today().strftime("%d-%m-%Y")

        elif choice == "1":
            date_input = input("Enter date (DD-MM-YYYY): ")
            try:
                valid_date = datetime.strptime(date_input, "%d-%m-%Y")
                return valid_date.strftime("%d-%m-%Y")
            except:
                print("Invalid date format! Try again.")
        else:
            print("Invalid choice.")

# ---------- MAIN ----------

expenses = load_data()

while True:
    print("\n====== PERSONAL EXPENSE TRACKER ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Filter by Category")
    print("5. Delete Expense")
    print("6. Edit Expense")
    print("7. Search")
    print("8. Monthly Summary")
    print("9. Category Analysis")
    print("10. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid input!")
        continue

    # ---------- ADD ----------
    if choice == 1:
        try:
            amount = float(input("Enter amount: "))
            if amount < 0:
                print("Amount cannot be negative.")
                continue
        except:
            print("Invalid amount.")
            continue

        category = input("Enter category: ").strip().lower()
        date = get_valid_date()

        expenses.append({
            "amount": amount,
            "category": category,
            "date": date
        })

        save_data(expenses)
        print("Expense added.")

    # ---------- VIEW ----------
    elif choice == 2:
        if not expenses:
            print("No expenses found.")
        else:
            for i, exp in enumerate(expenses, 1):
                print("-" * 30)
                print(f"{i}. {exp['category'].capitalize()}")
                print(f"Amount: {exp['amount']}")
                print(f"Date: {exp['date']}")

    # ---------- TOTAL ----------
    elif choice == 3:
        total = sum(exp["amount"] for exp in expenses)
        print(f"Total Expense: {total}")

    # ---------- FILTER ----------
    elif choice == 4:
        cat = input("Enter category: ").lower()
        found = False

        for exp in expenses:
            if exp["category"] == cat:
                print(exp)
                found = True

        if not found:
            print("No data found.")

    # ---------- DELETE ----------
    elif choice == 5:
        for i, exp in enumerate(expenses, 1):
            print(f"{i}. {exp['category']} - {exp['amount']}")

        try:
            idx = int(input("Enter number to delete: "))
            if 1 <= idx <= len(expenses):
                removed = expenses.pop(idx - 1)
                save_data(expenses)
                print("Deleted:", removed)
            else:
                print("Invalid number.")
        except:
            print("Invalid input.")

    # ---------- EDIT ----------
    elif choice == 6:
        for i, exp in enumerate(expenses, 1):
            print(f"{i}. {exp['category']} - {exp['amount']}")

        try:
            idx = int(input("Enter number to edit: "))
            if 1 <= idx <= len(expenses):
                exp = expenses[idx - 1]

                new_amount = input("New amount: ")
                if new_amount:
                    exp["amount"] = float(new_amount)

                new_cat = input("New category: ")
                if new_cat:
                    exp["category"] = new_cat.lower()

                new_date = input("New date (DD-MM-YYYY): ")
                if new_date:
                    try:
                        exp["date"] = datetime.strptime(new_date, "%d-%m-%Y").strftime("%d-%m-%Y")
                    except:
                        print("Invalid date skipped.")

                save_data(expenses)
                print("Updated.")
            else:
                print("Invalid index.")
        except:
            print("Invalid input.")

    # ---------- SEARCH ----------
    elif choice == 7:
        keyword = input("Search: ").lower()
        found = False

        for exp in expenses:
            if keyword in exp["category"] or keyword in exp["date"]:
                print(exp)
                found = True

        if not found:
            print("No match.")

    # ---------- MONTHLY SUMMARY ----------
    elif choice == 8:
        month = input("Enter month (MM-YYYY): ")

        total = count = 0
        max_amt = 0
        min_amt = float("inf")
        max_cat = ""
        found = False

        for exp in expenses:
            d, m, y = exp["date"].split("-")

            if f"{m}-{y}" == month:
                amt = exp["amount"]
                total += amt
                count += 1
                found = True

                if amt > max_amt:
                    max_amt = amt
                    max_cat = exp["category"]

                if amt < min_amt:
                    min_amt = amt

        if found:
            print(f"Total: {total}")
            print(f"Average: {total/count}")
            print(f"Highest: {max_cat} ({max_amt})")
            print(f"Lowest: {min_amt}")
        else:
            print("No data.")

    # ---------- CATEGORY ANALYSIS ----------
    elif choice == 9:
        summary = {}

        for exp in expenses:
            cat = exp["category"]
            summary[cat] = summary.get(cat, 0) + exp["amount"]

        print("\n--- Category Analysis ---")
        for cat, total in sorted(summary.items(), key=lambda x: x[1], reverse=True):
            print(f"{cat.capitalize()}: {total}")

        if summary:
            top = max(summary, key=summary.get)
            print(f"Top: {top.capitalize()} ({summary[top]})")

    # ---------- EXIT ----------
    elif choice == 10:
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")