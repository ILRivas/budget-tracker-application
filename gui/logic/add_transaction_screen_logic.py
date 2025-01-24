from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QDoubleValidator
from gui.ui.ui_add_transaction import Ui_Dialog
from PySide6.QtWidgets import QDialog
from gui.logic.utils import load_transactions, save_transactions, sort_existing_json

transactions = load_transactions()

class AddTransactionScreenLogic(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.setup_inputs()
        self.connect_buttons()

    def setup_inputs(self):
        """
        Set up input field properties like validators
        """
        validator = QDoubleValidator(0.0, 999999.99, 2)
        self.ui.amount_input.setValidator(validator)

        
    def add_transaction(self, date, t_type, amount, category, description):
        """
        Adds a new transaction to the list and saves it to the JSON file.
        """
        try:
            # Validate input data
            if not date or not t_type or not amount or not category:
                raise ValueError("All fields except 'description' are required.")

            # Create the transaction dictionary
            transaction = {
                "date": date,
                "type": t_type,
                "amount": amount,
                "category": category,
                "transaction_description": description or None,
            }

            # Append to the transactions list
            transactions.append(transaction)

            # Save the updated transactions and sort the JSON
            save_transactions(transactions)
            sort_existing_json()

            return transaction
        except Exception as e:
            print(f"Error adding transaction: {e}")
            raise

    def submit_transaction(self):
        """
        Handle the submission of the form.
        """
        transaction_data = {
            "date": self.ui.date_input.date().toString("yyyy-MM-dd"),
            "t_type": self.ui.type_input.currentText().lower(),
            "amount": float(self.ui.amount_input.text().replace(",", "")),
            "category": self.ui.comboBox.currentText(),
            "description": self.ui.lineEdit_2.text() or None
        }
        print("Saving Transaction:", transaction_data)
        print(self.ui.lineEdit_2.text())
        try:
        # Pass arguments to the add_transaction function in the correct order
            added_transaction = self.add_transaction(
                transactions,
                transaction_data["date"],
                transaction_data["t_type"],
                transaction_data["amount"],
                transaction_data["category"],
                transaction_data["description"]
            )
            
            print("Transaction added successfully:", added_transaction)
            save_transactions(transactions)
            sort_existing_json()
            response = QMessageBox.question(
                self,
                "Transaction Added",
                "Transaction added successfully! Would you like to add another?",
                QMessageBox.Yes | QMessageBox.No
            )
            if response == QMessageBox.Yes:
                self.ui.amount_input.clear()
                self.ui.lineEdit_2.clear()
                self.ui.date_input.setDate(self.ui.date_input.minimumDate())
                self.ui.type_input.setCurrentIndex(0)
                self.ui.comboBox.setCurrentIndex(0)
            else:
                self.accept()
        except ValueError as e:
            print("Error adding transaction:", e)
        
    def connect_buttons(self):
        """
        Connect buttons to their respective methods.
        """
        self.ui.cancel_button.clicked.connect(self.close)
        self.ui.submit_button.clicked.connect(self.submit_transaction)




        