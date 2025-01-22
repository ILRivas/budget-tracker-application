# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.add_transaction.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(873, 558)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(340, 50, 221, 421))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.date_input = QDateEdit(self.formLayoutWidget)
        self.date_input.setObjectName(u"date_input")
        self.date_input.setEnabled(True)
        self.date_input.setMinimumSize(QSize(0, 50))
        self.date_input.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(False)
        self.date_input.setFont(font)
        self.date_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date_input.setCalendarPopup(True)
        self.date_input.setMinimumDate(QDate(1900, 1, 1))
        self.date_input.setMaximumDate(QDate(2100, 12, 31))

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.date_input)

        self.date_label_2 = QLabel(self.formLayoutWidget)
        self.date_label_2.setObjectName(u"date_label_2")
        self.date_label_2.setMinimumSize(QSize(1, 50))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setUnderline(True)
        self.date_label_2.setFont(font1)
        self.date_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.date_label_2)

        self.type_input = QComboBox(self.formLayoutWidget)
        self.type_input.addItem("")
        self.type_input.addItem("")
        self.type_input.setObjectName(u"type_input")
        self.type_input.setFont(font)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.type_input)

        self.date_label_3 = QLabel(self.formLayoutWidget)
        self.date_label_3.setObjectName(u"date_label_3")
        self.date_label_3.setMinimumSize(QSize(1, 50))
        self.date_label_3.setFont(font1)
        self.date_label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.date_label_3)

        self.amount_input = QLineEdit(self.formLayoutWidget)
        self.amount_input.setObjectName(u"amount_input")
        self.amount_input.setMinimumSize(QSize(0, 35))
        self.amount_input.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.amount_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.amount_input)

        self.date_label_4 = QLabel(self.formLayoutWidget)
        self.date_label_4.setObjectName(u"date_label_4")
        self.date_label_4.setMinimumSize(QSize(1, 50))
        self.date_label_4.setFont(font1)
        self.date_label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.date_label_4)

        self.comboBox = QComboBox(self.formLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.comboBox)

        self.date_label_5 = QLabel(self.formLayoutWidget)
        self.date_label_5.setObjectName(u"date_label_5")
        self.date_label_5.setMinimumSize(QSize(1, 50))
        self.date_label_5.setFont(font1)
        self.date_label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.date_label_5)

        self.lineEdit_2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 35))
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.lineEdit_2)

        self.date_label = QLabel(self.formLayoutWidget)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setMinimumSize(QSize(1, 50))
        self.date_label.setFont(font1)
        self.date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.date_label)

        self.AddTransactionLabel = QLabel(Dialog)
        self.AddTransactionLabel.setObjectName(u"AddTransactionLabel")
        self.AddTransactionLabel.setGeometry(QRect(300, 0, 321, 41))
        font2 = QFont()
        font2.setPointSize(35)
        font2.setBold(True)
        font2.setUnderline(True)
        self.AddTransactionLabel.setFont(font2)
        self.AddTransactionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(340, 480, 221, 71))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cancel_button = QPushButton(self.widget)
        self.cancel_button.setObjectName(u"cancel_button")
        font3 = QFont()
        font3.setBold(True)
        self.cancel_button.setFont(font3)

        self.horizontalLayout.addWidget(self.cancel_button)

        self.submit_button = QPushButton(self.widget)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setFont(font3)

        self.horizontalLayout.addWidget(self.submit_button)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.date_input.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy/MM/dd", None))
        self.date_label_2.setText(QCoreApplication.translate("Dialog", u"Type", None))
        self.type_input.setItemText(0, QCoreApplication.translate("Dialog", u"Income", None))
        self.type_input.setItemText(1, QCoreApplication.translate("Dialog", u"Expense", None))

        self.date_label_3.setText(QCoreApplication.translate("Dialog", u"Amount", None))
        self.amount_input.setText(QCoreApplication.translate("Dialog", u"1,000.50", None))
        self.amount_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"1,000.50", None))
        self.date_label_4.setText(QCoreApplication.translate("Dialog", u"Category", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Paycheck", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Utilities", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Groceries", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Auto", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"Entertainment", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Dialog", u"Dining Out", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Dialog", u"Savings", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Dialog", u"Debt Payment", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Dialog", u"Health", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Dialog", u"Subscriptions", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("Dialog", u"Phone Payment", None))

        self.date_label_5.setText(QCoreApplication.translate("Dialog", u"Description", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"(Optional)", None))
        self.date_label.setText(QCoreApplication.translate("Dialog", u"Date", None))
        self.AddTransactionLabel.setText(QCoreApplication.translate("Dialog", u"Add Transaction", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.submit_button.setText(QCoreApplication.translate("Dialog", u"Submit", None))
    # retranslateUi

