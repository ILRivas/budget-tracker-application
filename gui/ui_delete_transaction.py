# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_delete_transaction.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget, QPushButton)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(863, 576)
        self.delete_transaction_table = QTableWidget(Dialog)
        if (self.delete_transaction_table.columnCount() < 5):
            self.delete_transaction_table.setColumnCount(5)
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.delete_transaction_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.delete_transaction_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(True)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.delete_transaction_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.delete_transaction_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.delete_transaction_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.delete_transaction_table.setObjectName(u"delete_transaction_table")
        self.delete_transaction_table.setGeometry(QRect(10, 50, 831, 381))
        palette = QPalette()
        brush = QBrush(QColor(64, 64, 64, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        self.delete_transaction_table.setPalette(palette)
        self.delete_transaction_table.horizontalHeader().setDefaultSectionSize(115)
        self.delete_transaction_label = QLabel(Dialog)
        self.delete_transaction_label.setObjectName(u"delete_transaction_label")
        self.delete_transaction_label.setGeometry(QRect(30, 10, 801, 31))
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setUnderline(True)
        self.delete_transaction_label.setFont(font2)
        self.delete_transaction_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cancel_button = QPushButton(Dialog)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(20, 450, 351, 101))
        palette1 = QPalette()
        brush1 = QBrush(QColor(255, 23, 23, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        self.cancel_button.setPalette(palette1)
        self.cancel_button.setAutoFillBackground(True)
        self.submit_button = QPushButton(Dialog)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(490, 450, 351, 101))
        palette2 = QPalette()
        brush2 = QBrush(QColor(255, 50, 50, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush2)
        brush3 = QBrush(QColor(0, 50, 50, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        self.submit_button.setPalette(palette2)
        self.submit_button.setAutoFillBackground(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        ___qtablewidgetitem = self.delete_transaction_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Date", None));
        ___qtablewidgetitem1 = self.delete_transaction_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Type", None));
        ___qtablewidgetitem2 = self.delete_transaction_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Amount", None));
        ___qtablewidgetitem3 = self.delete_transaction_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Category", None));
        ___qtablewidgetitem4 = self.delete_transaction_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Description", None));
        self.delete_transaction_label.setText(QCoreApplication.translate("Dialog", u"Delete Transaction", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"CANCEL", None))
        self.submit_button.setText(QCoreApplication.translate("Dialog", u"DELETE", None))
    # retranslateUi

