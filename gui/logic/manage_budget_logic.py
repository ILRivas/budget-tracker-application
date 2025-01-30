import os
import json
from PySide6.QtWidgets import (
    QDialog,
    QTableWidgetItem,
    QMessageBox,
    QProgressBar
)
from PySide6.QtCore import Qt
from gui.ui.ui_manage_budget import Ui_ManageBudgetsDialog

BUDGETS_FILE = "data/budgets.json"
TRANSACTIONS_FILE = "data/transactions.json"

class ManageBudgetLogic(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ManageBudgetsDialog()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.manage_budgets_save_button.clicked.connect(self.save_budget)
        self.ui.manage_budgets_reset_button.clicked.connect(self.reset_table)
        self.ui.manage_budgets_back_button.clicked.connect(self.close)

        # Ensure budget file exists
        self.budget_file_check()

        # Load budget data when user changes month or year
        self.ui.manage_budgets_month_spinbox.valueChanged.connect(self.load_budget)
        self.ui.manage_budgets_year_spinbox.valueChanged.connect(self.load_budget)

        # Load budget initially
        self.load_budget()

    def get_month_year(self):
        """
        Retrieve the user-selected month and year.
        """
        month = self.ui.manage_budgets_month_spinbox.value()
        year = self.ui.manage_budgets_year_spinbox.value()
        return f"{year}-{month:02d}"

    def budget_file_check(self):
        """
        Ensure the budget file exists.
        """
        budget_dir = os.path.dirname(BUDGETS_FILE)
        if budget_dir and not os.path.exists(budget_dir):
            os.makedirs(budget_dir)
        if not os.path.exists(BUDGETS_FILE):
            with open(BUDGETS_FILE, "w") as file:
                json.dump({}, file)

    def load_budget(self):
        """Loads budget data for the selected month and year."""
        self.budget_file_check()
        selected_period = self.get_month_year()

        # Load budgets from file
        with open(BUDGETS_FILE, "r") as file:
            budgets = json.load(file)

        # Load transactions from file
        transactions = []
        if os.path.exists(TRANSACTIONS_FILE):
            with open(TRANSACTIONS_FILE, "r") as file:
                transactions = json.load(file)

        # Calculate spent amounts per category
        spent_per_category = {}
        total_income = 0
        selected_month = self.ui.manage_budgets_month_spinbox.value()
        selected_year = self.ui.manage_budgets_year_spinbox.value()

        for transaction in transactions:
            try:
                t_month = int(transaction["date"].split("-")[1])
                t_year = int(transaction["date"].split("-")[0])
                if t_month == selected_month and t_year == selected_year:
                    category = transaction["category"]
                    amount = float(transaction["amount"])
                    if transaction["type"].lower() == "income":
                        total_income += amount
                    elif transaction["type"].lower() == "expense":
                        spent_per_category[category] = spent_per_category.get(category, 0) + amount 
            except (KeyError, ValueError):
                continue  # Skip any invalid transactions

        # Load existing budget data for this month
        budget_data = budgets.get(selected_period, {})

        # Get all categories (both from budgets and transactions)
        all_categories = set(budget_data.keys()).union(spent_per_category.keys())

        # Ensure predefined categories are always present
        predefined_categories = {"Entertainment", "Utilities", "Phone Payment",
                                "Auto (Gas, Insurance, Repairs, Payment)", "Dining Out", "Debt Payment"}
        all_categories.update(predefined_categories)

        # Update budget data dynamically
        updated_budget_data = {}
        total_budgeted = 0
        user_savings_goal = budget_data.get("Savings", {}).get("budget", 0)
        for category in all_categories:
            budget_amount = budget_data.get(category, {}).get("budget", 0)
            spent_amount = spent_per_category.get(category, 0)
            remaining = budget_amount - spent_amount

            updated_budget_data[category] = {
                "budget": budget_amount,
                "spent": spent_amount,
                "remaining": remaining
            }
            total_budgeted += budget_amount

        # Calculate potential savings
        potential_savings = total_income - total_budgeted

        # Populate the table with updated data
        self.populate_budget_table(updated_budget_data, user_savings_goal, potential_savings)

    def populate_budget_table(self, budget_data, user_savings_goal, potential_savings):
        """
        Fill the budget table with budget values.
        """
        self.ui.manage_budgets_table.setRowCount(0)

        for row, (category, values) in enumerate(budget_data.items()):
            self.ui.manage_budgets_table.insertRow(row)
            
            # Category
            self.ui.manage_budgets_table.setItem(row, 0, QTableWidgetItem(category))

            # Budget Amount
            budget_item = QTableWidgetItem(f"{values['budget']:.2f}")
            budget_item.setFlags(budget_item.flags() | Qt.ItemIsEditable)  # Allow editing
            self.ui.manage_budgets_table.setItem(row, 1, budget_item)

            # Spent Amount (Read-Only)
            spent_item = QTableWidgetItem(f"{values['spent']:.2f}")
            spent_item.setFlags(spent_item.flags() & ~Qt.ItemIsEditable)  # Make read-only
            self.ui.manage_budgets_table.setItem(row, 2, spent_item)

            # Remaining Budget (Read-Only)
            remaining = values["budget"] - values["spent"]
            remaining_item = QTableWidgetItem(f"{remaining:.2f}")
            remaining_item.setFlags(remaining_item.flags() & ~Qt.ItemIsEditable)  # Make read-only
            self.ui.manage_budgets_table.setItem(row, 3, remaining_item)

            # Progress Bar (Spending Percentage)
            progress = int((values["spent"] / values["budget"]) * 100) if values["budget"] > 0 else 0
            progress_widget = QProgressBar()
            progress_widget.setValue(progress)
            progress_widget.setFormat(f"{progress}%")  # Display percentage
            self.ui.manage_budgets_table.setCellWidget(row, 4, progress_widget)  # Add to table

        # Add Savings Rows that are editable
        row += 1
        self.ui.manage_budgets_table.insertRow(row)
        savings_item = QTableWidgetItem("Savings Goal")
        savings_item.setFlags(savings_item.flags() & ~Qt.ItemIsEditable)
        self.ui.manage_budgets_table.setItem(row, 0, savings_item)

        savings_goal_item = QTableWidgetItem(f"{user_savings_goal:.2f}")
        savings_goal_item.setFlags(savings_goal_item.flags() | Qt.ItemIsEditable)  # Allow editing
        self.ui.manage_budgets_table.setItem(row, 1, savings_goal_item)

        potential_savings_item = QTableWidgetItem(f"{potential_savings:.2f}")
        potential_savings_item.setFlags(potential_savings_item.flags() & ~Qt.ItemIsEditable)  # Read-only
        self.ui.manage_budgets_table.setItem(row, 3, potential_savings_item)

    def save_budget(self):
        """
        Save the user's budget input.
        """
        selected_period = self.get_month_year()
        with open(BUDGETS_FILE, "r") as file:
            budgets = json.load(file)

        budgets[selected_period] = {}

        for row in range(self.ui.manage_budgets_table.rowCount()):
            category = self.ui.manage_budgets_table.item(row, 0).text()
            budget_amount = float(self.ui.manage_budgets_table.item(row, 1).text() or 0)
            spent_amount = float(self.ui.manage_budgets_table.item(row, 2).text() or 0)
            budgets[selected_period][category] = {"budget": budget_amount, "spent": spent_amount}

        with open(BUDGETS_FILE, "w") as file:
            json.dump(budgets, file, indent=4)

        QMessageBox.information(self, "Budget Saved", "Your budget has been saved successfully!")

    def reset_table(self):
        """Resets the budget table to zero."""
        confirmation = QMessageBox.question(
            self, "Reset Budget?", "Are you sure you want to reset this budget?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirmation == QMessageBox.Yes:
            for row in range(self.ui.manage_budgets_table.rowCount()):
                self.ui.manage_budgets_table.setItem(row, 1, QTableWidgetItem("0.00"))
                self.ui.manage_budgets_table.setItem(row, 2, QTableWidgetItem("0.00"))
                self.ui.manage_budgets_table.setItem(row, 3, QTableWidgetItem("0.00"))