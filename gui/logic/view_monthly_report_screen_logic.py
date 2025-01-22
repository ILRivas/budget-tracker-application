from PySide6.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView, QMessageBox, QHeaderView
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

    def populate_table(self, filtered_transactions):
        """
        Populate the table with filtered transactions.
        """
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
        self.ui.net_balance_label.setText(f"NetBalance: ${net_balance:.2f}")


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
        Export transactions to a CSV file.
        """
        try:
            with open(self.csv_filename, mode="w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                # Write headers
                writer.writerow(["Date", "Type", "Amount", "Category", "Description"])
                # Write transaction rows
                for transaction in self.filtered_transactions:
                    writer.writerow([
                        transaction.get("date", ""),
                        transaction.get("type", ""),
                        f"${transaction.get('amount', 0):.2f}",
                        transaction.get("category", ""),
                        transaction.get("transaction_description", "None"),
                    ])
            QMessageBox.information(
                self, "Export Successful",
                f"Transactions successfully exported to {self.csv_filename}.",
                QMessageBox.Ok
            )
        except Exception as e:
            QMessageBox.critical(
                self, "Export Failed",
                f"An error occurred while exporting the transactions: {e}",
                QMessageBox.Ok
            )