# 💰 Personal Expense Tracker (CLI)

A command-line based application built using Python to manage and analyze daily expenses efficiently.

---

## 🚀 Features

* ➕ Add new expenses with category and date
* 📋 View all expenses in a structured format
* ✏️ Edit existing expenses
* ❌ Delete expenses
* 🔍 Search by category or date
* 📊 Monthly summary:

  * Total spending
  * Average spending
  * Highest & lowest expense
* 📈 Category-wise analysis (sorted by spending)
* 💾 Data persistence using JSON file

---

## 🛠️ Technologies Used

* Python
* JSON (for data storage)
* datetime module (for date validation and formatting)

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

2. Run the program:

```bash
python main.py
```

---

## 📂 Project Structure

```
expense-tracker/
│
├── main.py
├── expenses.json   # (ignored in .gitignore)
├── README.md
```

---

## ⚠️ Note

* The `expenses.json` file is used to store data locally.
* It is excluded from GitHub using `.gitignore` for privacy.

---

## 📚 What I Learned

* Working with lists and dictionaries in real applications
* File handling using JSON (data persistence)
* Input validation and error handling
* Writing structured and modular Python code
* Building real-world logic step-by-step

---

## 🚀 Future Improvements

* Graph visualization using matplotlib
* GUI version (Tkinter or Web app)
* Database integration (SQLite / MongoDB)

----

## 🎯 Purpose

This project was built to practice real-world Python concepts like:
- Data handling using lists and dictionaries  
- File handling using JSON  
- Input validation and error handling  
- Designing a CLI-based application  

---

## 📸 Sample Output

====== PERSONAL EXPENSE TRACKER ======
1. Add Expense
2. View Expenses
3. Total Expense
4. Filter by Category
5. Delete Expense
6. Edit Expense
7. Search
8. Monthly Summary
9. Category Analysis
10. Exit
=====================================

Enter your choice: 1

Enter amount: 500
Enter category: food

1. Enter date manually
2. Use today's date
Choose option: 2

Expense added.

## 👨‍💻 Author

Rishabh Poddar
