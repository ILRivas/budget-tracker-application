import matplotlib.pyplot as plt
from PySide6.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView, QMessageBox, QHeaderView, QFileDialog
from gui.ui_view_monthly_report import Ui_Dialog
import csv
from logic.transactions import load_transactions

# Load transactions from JSON file
transactions = load_transactions("data/transactions.json")

class ViewMonthlyReportLogic(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Make the table and export button initially invisible
        self.ui.monthly_report_table.setVisible(False)
        self.ui.export_pushButton.setVisible(False)
        self.ui.expense_label.setVisible(False)
        self.ui.income_label.setVisible(False)
        self.ui.net_balance_label.setVisible(False)
        # Adjust column sizes and table behavior
        self.ui.monthly_report_table.resizeColumnsToContents()
        self.ui.monthly_report_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.monthly_report_table.setSelectionMode(QAbstractItemView.SingleSelection)

        # Connect buttons
        self.ui.generate_pushButton.clicked.connect(self.generate_report)
        self.ui.back_pushButton.clicked.connect(self.close)  # Closes the current dialog and returns to the main menu
        self.ui.export_pushButton.clicked.connect(self.confirm_export)
        self.ui.view_chart_pushButton.clicked.connect(self.show_chart)

    def populate_table(self, filtered_transactions):
        """
        Populate the table with filtered transactions.
        """
        load_transactions()
        
        self.ui.monthly_report_table.setRowCount(len(filtered_transactions))
        for row, transaction in enumerate(filtered_transactions):
            self.ui.monthly_report_table.setItem(row, 0, QTableWidgetItem(transaction.get("date", "")))
            self.ui.monthly_report_table.setItem(row, 1, QTableWidgetItem(transaction.get("type", "")))
            self.ui.monthly_report_table.setItem(row, 2, QTableWidgetItem(f"${transaction.get('amount', 0):.2f}"))
            self.ui.monthly_report_table.setItem(row, 3, QTableWidgetItem(transaction.get("category", "")))
            self.ui.monthly_report_table.setItem(row, 4, QTableWidgetItem(transaction.get("transaction_description", "")))

    def generate_report(self):
        """
        Generate the monthly report and populate the table.
        """
        # Get the month and year from spin boxes
        month = self.ui.month_spinBox.value()
        year = self.ui.year_spinBox.value()
        transactions = load_transactions()

        # Filter transactions by month and year
        filtered_transactions = [
            t for t in transactions
            if int(t["date"].split("-")[0]) == year and int(t["date"].split("-")[1]) == month
        ]

        if not filtered_transactions:
            QMessageBox.information(
                self, "No Transactions Found",
                f"No transactions found for {month:02d}/{year}.",
                QMessageBox.Ok
            )
            return

        # Populate the table with filtered transactions
        self.populate_table(filtered_transactions)
        #Calculate net_balance
        total_income = sum(t["amount"] for t in filtered_transactions if t["type"] == "Income")
        total_expenses = sum(t["amount"] for t in filtered_transactions if t["type"] == "Expense")
        net_balance = total_income - total_expenses
        #update UI
        self.ui.income_label.setText(f"Total Income: ${total_income:.2f}")
        self.ui.expense_label.setText(f"Total Expenses: ${total_expenses:.2f}")
        self.ui.net_balance_label.setText(f"Net Balance: ${net_balance:.2f}")


        # Make the table and export button visible
        self.ui.expense_label.setVisible(True)
        self.ui.income_label.setVisible(True)
        self.ui.net_balance_label.setVisible(True)
        self.ui.monthly_report_table.setVisible(True)
        self.ui.export_pushButton.setVisible(True)

        #adjust the table column widths to fill the table
        self.ui.monthly_report_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.monthly_report_table.horizontalHeader().setStretchLastSection(True)
        # Store the filtered transactions for exporting
        self.filtered_transactions = filtered_transactions
        self.csv_filename = f"{month:02d}_{year}_report.csv"

    def resizeEvent(self, event):
        self.ui.monthly_report_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        super().resizeEvent(event)

    def confirm_export(self):
        """
        Confirm and export the table to a CSV file.
        """
        response = QMessageBox.question(
            self, "Confirm Export",
            f"Are you sure you want to export the report to {self.csv_filename}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if response == QMessageBox.Yes:
            self.export_to_csv()

    def export_to_csv(self):
        """
        Export transactions and category breakdown to a CSV file.
        """
        try:
            # Open the CSV file for writing
            with open(self.csv_filename, mode="w", newline="") as csvfile:
                writer = csv.writer(csvfile)

                total_income = sum(t["amount"] for t in self.filtered_transactions if t["type"] == "Income")
                total_expenses = sum(t["amount"] for t in self.filtered_transactions if t["type"] == "Expense")
                net_balance = total_income - total_expenses
                writer.writerow(["Monthly Summary"])
                writer.writerow(["Total Income", f"${total_income:.2f}"])
                writer.writerow(["Total Expenses", f"${total_expenses:.2f}"])
                writer.writerow(["Net Balance", f"${net_balance:.2f}"])
                writer.writerow([]) 
                # Write transactions section
                writer.writerow(["Date", "Type", "Amount", "Category", "Description"])
                #Write Transaction rows
                for transaction in self.filtered_transactions:
                    writer.writerow([
                        transaction.get("date", ""),
                        transaction.get("type", ""),
                        f"${transaction.get('amount', 0):.2f}",
                        transaction.get("category", ""),
                        transaction.get("transaction_description", "None"),
                    ])

                # Add a blank line to separate sections
                writer.writerow([])

                # Calculate spending by category for the filtered transactions
                spending_by_category = self.calculate_spending_by_category(self.filtered_transactions)

                # Write category breakdown section
                writer.writerow(["Category", "Total Spending"])
                for category, total in spending_by_category.items():
                    writer.writerow([category, f"${total:.2f}"])

            # Notify user of success
            QMessageBox.information(
                self, "Export Successful",
                f"Transactions and category breakdown successfully exported to {self.csv_filename}.",
                QMessageBox.Ok
            )
        except Exception as e:
            # Notify user of failure
            QMessageBox.critical(
                self, "Export Failed",
                f"An error occurred while exporting the data: {e}",
                QMessageBox.Ok
            )

    def calculate_spending_by_category(self, filtered_transactions):
        """
        Calculate the total spending by category for the filtered transactions.
        """
        spending_by_category = {}
        for transaction in filtered_transactions:
            if transaction.get("type", "") == "Expense":  # Only consider expenses
                category = transaction.get("category", "Uncategorized")
                amount = float(transaction.get("amount", 0))
                spending_by_category[category] = spending_by_category.get(category, 0) + amount
        return spending_by_category

    def calculate_spending_by_category(self, filtered_transactions):
        """
        Calculate the total spending by category for the filtered transactions.
        """
        spending_by_category = {}
        for transaction in filtered_transactions:
            if transaction.get("type", "") == "Expense":  # Only consider expenses
                category = transaction.get("category", "Uncategorized")
                amount = float(transaction.get("amount", 0))
                spending_by_category[category] = spending_by_category.get(category, 0) + amount
        return spending_by_category

    def show_chart(self):
        """
        Generate and display a pie chart for spending by category for the selected month and year.
        Additionally, display a numerical breakdown of the spending.
        """
        month = self.ui.month_spinBox.value()
        year = self.ui.year_spinBox.value()

        filtered_transactions = [
            t for t in self.filtered_transactions
            if int(t["date"].split("-")[0]) == year and int(t["date"].split("-")[1]) == month
        ]
        if not filtered_transactions:
            QMessageBox.warning(self, "No Data", f"No Transactions found for {month}/{year}.")
            return
        spending_by_category = self.calculate_spending_by_category(filtered_transactions)
        if not spending_by_category:
            QMessageBox.warning(self, "No Data", f"No expenses found to display in the chart.")
            return

        # Generate Pie Chart
        categories = list(spending_by_category.keys())
        amounts = list(spending_by_category.values())

        # Custom function to format the labels with percentage and amount
        def autopct_format(pct, all_values):
            total = sum(all_values)
            value = pct * total / 100
            return f"{pct:.1f}%\n(${value:.2f})"

        plt.figure(figsize=(8, 8))
        plt.pie(
            amounts,
            labels=categories,
            autopct=lambda pct: autopct_format(pct, amounts),  # Use custom format
            startangle=140,
        )
        plt.title(f"Spending by Category - {month:02d}/{year}")
        plt.show()

        # Populate the category breakdown table
        self.ui.category_breakdown_table.setRowCount(0)
        for row, (category, amount) in enumerate(spending_by_category.items()):
            self.ui.category_breakdown_table.insertRow(row)
            self.ui.category_breakdown_table.setItem(row, 0, QTableWidgetItem(category))
            self.ui.category_breakdown_table.setItem(row, 1, QTableWidgetItem(f"${amount:.2f}"))

        # Enable export chart button and set its action
        self.ui.export_chart_pushButton.setEnabled(True)
        self.ui.export_chart_pushButton.clicked.disconnect()
        self.ui.export_chart_pushButton.clicked.connect(lambda: self.export_chart(spending_by_category, month, year))
    
    def export_chart(self, spending_by_category, month, year):
        """
        Export the pie chart and numerical breakdown.
        """
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Chart and Data", f"{month:02d}_{year}_spending",
        )
        if not file_path:
            return
        
        chart_file = f"{file_path}_chart.png"
        plt.figure(figsize=(8,8))
        categories = list(spending_by_category.keys())
        amounts = list(spending_by_category.values())
        plt.pie(amounts, labels = categories, autopct="%1.1f%%", startangle=140)
        plt.title(f"Spending by Category - {month:02d}/{year}")
        plt.savefig(chart_file)
        plt.close()