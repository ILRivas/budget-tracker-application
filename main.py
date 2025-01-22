import sys
from PySide6.QtWidgets import QApplication
from gui.logic.main_menu_logic import MainMenuLogic

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_menu = MainMenuLogic()
    main_menu.show()
    sys.exit(app.exec())