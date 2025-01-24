Budget Tracker Application

Description

A personal finance management application designed to track transactions, generate monthly summaries, visualize spending by category, and export reports to CSV. This application provides a clear overview of income, expenses, and net balances, empowering users to make informed financial decisions.

Features
	•	Add, Delete, and Manage Transactions: Easily record income or expenses.
	•	Monthly Summaries: View a detailed table of transactions for a selected month and year.
	•	Spending Visualization: Generate pie charts to visualize spending by category.
	•	CSV Export: Export detailed reports, including income, expenses, net balance, and categorical breakdowns, for further analysis.
	•	User-Friendly UI: Intuitive design built with PySide6 for easy navigation.

Requirements

The project requires Python and several dependencies. Install the dependencies listed in the requirements.txt file to run the project. To install them, use:
    pip install -r requirements.txt

File Structure

The project structure is organized as follows:
Budget_Project/
│
├── data/
│   └── transactions.json         # Stores transaction data
│
├── gui/
│   ├── logic/
│   │   ├── add_transaction_screen_logic.py
│   │   ├── delete_transaction_screen_logic.py
│   │   ├── main_menu_logic.py
│   │   ├── view_monthly_report_screen_logic.py
│   │
│   ├── ui_add_transaction.py      # UI for adding transactions
│   ├── ui_delete_transaction.py   # UI for deleting transactions
│   ├── ui_main_menu.py            # Main menu UI
│   └── ui_view_monthly_report.py  # UI for viewing monthly reports
│
├── logic/
│   ├── budgets.py                 # Budget-related calculations
│   ├── menu_logic.py              # Main menu logic
│   ├── reports.py                 # Report generation logic
│   ├── transactions.py            # Core transaction logic
│   └── utils.py                   # Helper utilities
│
├── .gitignore                     # Files and directories ignored by Git
├── LICENSE                        # License details (GPL-3.0)
├── main.py                        # Main entry point for the application
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies

Installation and Usage
 1.	Clone the Repository:
    - git clone https://github.com/ILRivas/budget-tracker-application.git 
    - cd budget-tracker-application
 2.	Set Up Virtual Environment:
    python3 -m venv venv
    source venv/bin/activate
 3. Install Dependencies:
    pip install -r requirements.txt
 4. Run the application:
    python main.py

Usage Instructions

Adding Transactions
	1.	Navigate to the “Add Transaction” section.
	2.	Enter the transaction details, including the date, type, amount, category, and optional description.
	3.	Click “Submit” to save the transaction.

Viewing Monthly Reports
	1.	Select a month and year from the dropdown.
	2.	Click “Generate” to display all transactions for the selected period.
	3.	Export the data to CSV or visualize spending with the “View Chart” button.


Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.


License

This project is licensed under the GPL-3.0 License.

Future Improvements
	•	Recurring Transactions: Automatically add recurring transactions (e.g., rent, subscriptions).
	•	User Accounts: Add multi-user support for personalized tracking.
	•	Cloud Sync: Enable saving and retrieving data from the cloud.
	•	Data Analysis: Provide insights and recommendations based on spending trends.

