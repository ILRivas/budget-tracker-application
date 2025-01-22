from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QDoubleValidator
from gui.ui_add_transaction import Ui_Dialog
from PySide6.QtWidgets import QDialog
from logic.transactions import add_transaction
from logic.transactions import load_transactions, save_transactions, sort_existing_json

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
            added_transaction = add_transaction(
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
            
            msg_box = QMessageBox(self)
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Success")
            msg_box.setText("Transaction added successfully!")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()
            self.accept()
        except ValueError as e:
            print("Error adding transaction:", e)
        
    def connect_buttons(self):
        """
        Connect buttons to their respective methods.
        """
        self.ui.cancel_button.clicked.connect(self.close)
        self.ui.submit_button.clicked.connect(self.submit_transaction)




        