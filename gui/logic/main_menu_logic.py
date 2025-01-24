# main_menu_logic.py
from PySide6.QtWidgets import QMainWindow, QApplication
from gui.ui.ui_main_menu import Ui_Form
from gui.logic.add_transaction_screen_logic import AddTransactionScreenLogic
from gui.logic.delete_transaction_screen_logic import DeleteTransactionScreenLogic
from gui.logic.view_monthly_report_screen_logic import ViewMonthlyReportLogic

class MainMenuLogic(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Connect buttons to functions
        self.ui.add_trans_button.clicked.connect(self.open_add_transaction_screen)
        self.ui.del_trans_button.clicked.connect(self.open_delete_transaction_screen)
        self.ui.month_summ_button.clicked.connect(self.open_view_monthly_report_screen)
        self.ui.exit_button.clicked.connect(self.exit_application)

    def open_add_transaction_screen(self):
        """Open the Add Transaction screen."""
        self.add_transaction_screen = AddTransactionScreenLogic()
        self.add_transaction_screen.show()

    def open_delete_transaction_screen(self):
        self.delete_transaction_screen = DeleteTransactionScreenLogic()
        self.delete_transaction_screen.show()

    def open_view_monthly_report_screen(self):
        self.view_monthly_report_screen = ViewMonthlyReportLogic()
        self.view_monthly_report_screen.show()


    def exit_application(self):
        QApplication.quit()