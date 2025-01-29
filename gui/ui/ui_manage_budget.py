
# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QDialog, QLabel, QTableWidget, QVBoxLayout, QHBoxLayout, 
                               QPushButton, QHeaderView, QSizePolicy, QSpinBox)


class Ui_ManageBudgetsDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"ManageBudgetsDialog")
        Dialog.resize(900, 700)
        Dialog.setMinimumSize(900, 700)

        # Main layout
        self.manage_budgets_layout = QVBoxLayout(Dialog)

        # Title Section
        self.manage_budgets_title_label = QLabel(Dialog)
        self.manage_budgets_title_label.setObjectName(u"manage_budgets_title_label")
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(True)
        self.manage_budgets_title_label.setFont(font)
        self.manage_budgets_title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.manage_budgets_layout.addWidget(self.manage_budgets_title_label)

        # Budget Table Section
        self.manage_budgets_table = QTableWidget(Dialog)
        self.manage_budgets_table.setObjectName(u"manage_budgets_table")
        self.manage_budgets_table.setColumnCount(5)
        self.manage_budgets_table.setHorizontalHeaderLabels(
            ["Category", "Budget Amount ($)", "Spent Amount ($)", "Remaining Budget ($)", "Progress"]
        )
        self.manage_budgets_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.manage_budgets_table.horizontalHeader().setStretchLastSection(True)
        self.manage_budgets_table.setAlternatingRowColors(True)

        # Ensure the table resizes dynamically
        self.manage_budgets_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.manage_budgets_layout.addWidget(self.manage_budgets_table)

        # Month and Year Selection Section
        self.manage_budgets_selection_layout = QHBoxLayout()

        self.manage_budgets_month_spinbox = QSpinBox(Dialog)
        self.manage_budgets_month_spinbox.setObjectName(u"manage_budgets_month_spinbox")
        self.manage_budgets_month_spinbox.setRange(1, 12)
        self.manage_budgets_selection_layout.addWidget(QLabel("Month:"))
        self.manage_budgets_selection_layout.addWidget(self.manage_budgets_month_spinbox)

        self.manage_budgets_year_spinbox = QSpinBox(Dialog)
        self.manage_budgets_year_spinbox.setObjectName(u"manage_budgets_year_spinbox")
        self.manage_budgets_year_spinbox.setRange(2000, 2100)
        self.manage_budgets_selection_layout.addWidget(QLabel("Year:"))
        self.manage_budgets_selection_layout.addWidget(self.manage_budgets_year_spinbox)

        self.manage_budgets_layout.addLayout(self.manage_budgets_selection_layout)

        # Control Buttons Section
        self.manage_budgets_button_layout = QHBoxLayout()

        self.manage_budgets_save_button = QPushButton(Dialog)
        self.manage_budgets_save_button.setObjectName(u"manage_budgets_save_button")
        self.manage_budgets_save_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.manage_budgets_button_layout.addWidget(self.manage_budgets_save_button)

        self.manage_budgets_reset_button = QPushButton(Dialog)
        self.manage_budgets_reset_button.setObjectName(u"manage_budgets_reset_button")
        self.manage_budgets_reset_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.manage_budgets_button_layout.addWidget(self.manage_budgets_reset_button)

        self.manage_budgets_back_button = QPushButton(Dialog)
        self.manage_budgets_back_button.setObjectName(u"manage_budgets_back_button")
        self.manage_budgets_back_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.manage_budgets_button_layout.addWidget(self.manage_budgets_back_button)

        self.manage_budgets_layout.addLayout(self.manage_budgets_button_layout)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Manage Budgets", None))
        self.manage_budgets_title_label.setText(QCoreApplication.translate("Dialog", u"Manage Budgets", None))
        self.manage_budgets_save_button.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.manage_budgets_reset_button.setText(QCoreApplication.translate("Dialog", u"Reset", None))
        self.manage_budgets_back_button.setText(QCoreApplication.translate("Dialog", u"Back", None))