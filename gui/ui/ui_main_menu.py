# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(871, 563)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.title_label = QLabel(Form)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setEnabled(True)
        self.title_label.setGeometry(QRect(50, 0, 800, 100))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy1)
        self.title_label.setMinimumSize(QSize(800, 100))
        self.title_label.setMaximumSize(QSize(800, 100))
        font = QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setUnderline(True)
        self.title_label.setFont(font)
        self.title_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.title_label.setTextFormat(Qt.TextFormat.RichText)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label_2 = QLabel(Form)
        self.title_label_2.setObjectName(u"title_label_2")
        self.title_label_2.setEnabled(True)
        self.title_label_2.setGeometry(QRect(360, 510, 200, 50))
        sizePolicy1.setHeightForWidth(self.title_label_2.sizePolicy().hasHeightForWidth())
        self.title_label_2.setSizePolicy(sizePolicy1)
        self.title_label_2.setMinimumSize(QSize(200, 50))
        self.title_label_2.setMaximumSize(QSize(200, 50))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setUnderline(True)
        self.title_label_2.setFont(font1)
        self.title_label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.title_label_2.setTextFormat(Qt.TextFormat.RichText)
        self.title_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(300, 130, 311, 361))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.add_trans_button = QPushButton(self.widget)
        self.add_trans_button.setObjectName(u"add_trans_button")
        self.add_trans_button.setAutoFillBackground(True)

        self.verticalLayout.addWidget(self.add_trans_button)

        self.del_trans_button = QPushButton(self.widget)
        self.del_trans_button.setObjectName(u"del_trans_button")
        self.del_trans_button.setAutoFillBackground(True)

        self.verticalLayout.addWidget(self.del_trans_button)

        self.month_summ_button = QPushButton(self.widget)
        self.month_summ_button.setObjectName(u"month_summ_button")
        self.month_summ_button.setAutoFillBackground(True)

        self.verticalLayout.addWidget(self.month_summ_button)

        self.set_budget_button = QPushButton(self.widget)
        self.set_budget_button.setObjectName(u"set_budget_button")
        self.set_budget_button.setAutoFillBackground(True)

        self.verticalLayout.addWidget(self.set_budget_button)

        self.exit_button = QPushButton(self.widget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setAutoFillBackground(True)

        self.verticalLayout.addWidget(self.exit_button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("Form", u"Budgeting App", None))
        self.title_label_2.setText(QCoreApplication.translate("Form", u"App Version 1.0", None))
        self.add_trans_button.setText(QCoreApplication.translate("Form", u"Add Transaction", None))
        self.del_trans_button.setText(QCoreApplication.translate("Form", u"Delete Transaction", None))
        self.month_summ_button.setText(QCoreApplication.translate("Form", u"View Monthly Summary", None))
        self.set_budget_button.setText(QCoreApplication.translate("Form", u"Manage Budgets", None))
        self.exit_button.setText(QCoreApplication.translate("Form", u"Exit", None))
    # retranslateUi

