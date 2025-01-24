import json
from PySide6.QtWidgets import QDialog, QTableWidgetItem, QMessageBox, QAbstractItemView
from PySide6.QtCore import Qt
from gui.ui_delete_transaction import Ui_Dialog
from gui.logic.utils import load_transactions, save_transactions, sort_existing_json
class DeleteTransactionScreenLogic(QDialog):
    def __init__(self, transactions_file = "data/transactions.json"):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.transactions_file = transactions_file
        self.transactions = load_transactions(transactions_file)

        self.populate_table()
        self.connect_buttons()
    
    def connect_buttons(self):
        """
        Connect buttons to their respective methonds.
        """
        self.ui.cancel_button.clicked.connect(self.close)
        self.ui.submit_button.clicked.connect(self.delete_selected_transaction)
    def populate_table(self):
        """
        Populate the QTableWidget with transactions.
        """
        load_transactions()
        self.ui.delete_transaction_table.setRowCount(len(self.transactions))
        for row, transaction in enumerate(self.transactions):
            self.ui.delete_transaction_table.setItem(row, 0, QTableWidgetItem(transaction.get("date", "")))
            self.ui.delete_transaction_table.setItem(row, 1, QTableWidgetItem(transaction.get("type", "")))
            self.ui.delete_transaction_table.setItem(row, 2, QTableWidgetItem(str((transaction.get("amount", "")))))
            self.ui.delete_transaction_table.setItem(row, 3, QTableWidgetItem(transaction.get("category", "")))
            self.ui.delete_transaction_table.setItem(row, 4, QTableWidgetItem(transaction.get("transaction_description", "")))

        #Adjust column sizes and set behaviors.
        self.ui.delete_transaction_table.resizeColumnsToContents()
        self.ui.delete_transaction_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.delete_transaction_table.setSelectionMode(QAbstractItemView.SingleSelection)

    
    def delete_selected_transaction(self):
        """
        Delete the selected transaction from the table and transaction list.
        """
        selected_row = self.ui.delete_transaction_table.currentRow()
        if selected_row < 0:
            print("No Transaction Selected!")
            return
        confirmation = self.confirm_deletion()
        if not confirmation:
            return
        del self.transactions[selected_row]
        self.populate_table()
        save_transactions(self.transactions, self.transactions_file)
        sort_existing_json(self.transactions_file)
        print("Transaction deleted successfully")

    def confirm_deletion(self):
        """
        Confirms the deletion of a transaction to avoid 
        """
        selected_row = self.ui.delete_transaction_table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select a transaction to delete.")
            return False
        transaction_details = {
            "date": self.ui.delete_transaction_table.item(selected_row, 0).text(),
            "type": self.ui.delete_transaction_table.item(selected_row, 1).text(),
            "amount": self.ui.delete_transaction_table.item(selected_row, 2).text(),
            "category": self.ui.delete_transaction_table.item(selected_row, 3).text(),
            "description": self.ui.delete_transaction_table.item(selected_row, 4).text(),
        }
        message = (
            f"Are you sure you want to delete this transaction?\n\n"
            f"Date: {transaction_details['date']}\n"
            f"Type: {transaction_details['type']}\n"
            f"Amount: {transaction_details['amount']}\n"
            f"Category: {transaction_details['category']}\n"
            f"Description: {transaction_details['description']}"
        )
        
        confirmation_box = QMessageBox(self)
        confirmation_box.setIcon(QMessageBox.Warning)
        confirmation_box.setWindowTitle("Confirm Deletion")
        confirmation_box.setText(message)
        confirmation_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        response = confirmation_box.exec()

        if response == QMessageBox.Yes:
            return True
        return False