# -*- coding: utf-8 -*-

################################################################################
## Form generated and customized for the View/Export Monthly Summary
##
## WARNING! Changes here are persistent.
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QTableWidget,
    QTableWidgetItem, QWidget, QScrollArea, QVBoxLayout, QGridLayout)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(900, 700)
        Dialog.setMinimumSize(900, 700)

        # Main layout
        self.layout = QVBoxLayout(Dialog)

        # Title
        self.Monthly_Summary_Title = QLabel(Dialog)
        self.Monthly_Summary_Title.setObjectName(u"Monthly_Summary_Title")
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(True)
        self.Monthly_Summary_Title.setFont(font)
        self.Monthly_Summary_Title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.Monthly_Summary_Title)

        # Month and year selection
        self.selection_layout = QGridLayout()
        self.month_and_year_label = QLabel(Dialog)
        self.month_and_year_label.setObjectName(u"month_and_year_label")
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.month_and_year_label.setFont(font2)
        self.month_and_year_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.selection_layout.addWidget(self.month_and_year_label, 0, 0, 1, 2)

        self.month_spinBox = QSpinBox(Dialog)
        self.month_spinBox.setObjectName(u"month_spinBox")
        font1 = QFont()
        font1.setPointSize(16)
        self.month_spinBox.setFont(font1)
        self.month_spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.month_spinBox.setMinimum(1)
        self.month_spinBox.setMaximum(12)
        self.selection_layout.addWidget(self.month_spinBox, 1, 0)

        self.year_spinBox = QSpinBox(Dialog)
        self.year_spinBox.setObjectName(u"year_spinBox")
        self.year_spinBox.setFont(font1)
        self.year_spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.year_spinBox.setMinimum(2000)
        self.year_spinBox.setMaximum(2100)
        self.selection_layout.addWidget(self.year_spinBox, 1, 1)

        self.generate_pushButton = QPushButton(Dialog)
        self.generate_pushButton.setObjectName(u"generate_pushButton")
        font3 = QFont()
        font3.setBold(True)
        font3.setUnderline(True)
        self.generate_pushButton.setFont(font3)
        self.selection_layout.addWidget(self.generate_pushButton, 2, 0, 1, 2)
        self.layout.addLayout(self.selection_layout)

        # Scrollable main area
        self.scroll_area = QScrollArea(Dialog)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_widget.setObjectName(u"scroll_widget")
        self.scroll_layout = QVBoxLayout(self.scroll_widget)

        # Table for transactions
        self.monthly_report_table = QTableWidget(self.scroll_widget)
        self.monthly_report_table.setObjectName(u"monthly_report_table")
        if (self.monthly_report_table.columnCount() < 5):
            self.monthly_report_table.setColumnCount(5)
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        self.monthly_report_table.horizontalHeader().setStretchLastSection(True)
        self.monthly_report_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.scroll_layout.addWidget(self.monthly_report_table)

        # Summary Section
        self.summary_layout = QVBoxLayout()
        self.income_label = QLabel(self.scroll_widget)
        self.income_label.setObjectName(u"income_label")
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(True)
        self.income_label.setFont(font5)
        self.summary_layout.addWidget(self.income_label)

        self.expense_label = QLabel(self.scroll_widget)
        self.expense_label.setObjectName(u"expense_label")
        self.expense_label.setFont(font5)
        self.summary_layout.addWidget(self.expense_label)

        self.net_balance_label = QLabel(self.scroll_widget)
        self.net_balance_label.setObjectName(u"net_balance_label")
        self.net_balance_label.setFont(font5)
        self.summary_layout.addWidget(self.net_balance_label)

        self.scroll_layout.addLayout(self.summary_layout)
        self.scroll_area.setWidget(self.scroll_widget)
        self.layout.addWidget(self.scroll_area)

        # Export Button
        self.button_layout = QGridLayout()
        self.export_pushButton = QPushButton(Dialog)
        self.export_pushButton.setObjectName(u"export_pushButton")
        self.export_pushButton.setFont(font3)
        self.button_layout.addWidget(self.export_pushButton, 0, 0)

        #ViewTable Button
        self.view_chart_pushButton = QPushButton(Dialog)
        self.view_chart_pushButton.setObjectName(u"view_chart_pushButton")
        self.view_chart_pushButton.setFont(font3)
        self.button_layout.addWidget(self.view_chart_pushButton, 0 , 1)

        #Back Button
        self.back_pushButton = QPushButton(Dialog)
        self.back_pushButton.setObjectName(u"back_pushButton")
        self.back_pushButton.setFont(font3)
        self.button_layout.addWidget(self.back_pushButton, 0, 2)
        self.layout.addLayout(self.button_layout)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Monthly Summary", None))
        self.Monthly_Summary_Title.setText(QCoreApplication.translate("Dialog", u"View / Export Monthly Summary", None))
        self.month_and_year_label.setText(QCoreApplication.translate("Dialog", u"Month / Year Selection", None))
        self.generate_pushButton.setText(QCoreApplication.translate("Dialog", u"Generate", None))
        self.export_pushButton.setText(QCoreApplication.translate("Dialog", u"Export to CSV", None))
        self.view_chart_pushButton.setText(QCoreApplication.translate("Dialog", u"View Chart", None))
        self.back_pushButton.setText(QCoreApplication.translate("Dialog", u"Back", None))
        ___qtablewidgetitem = QTableWidgetItem()
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Date", None))
        self.monthly_report_table.setHorizontalHeaderItem(0, ___qtablewidgetitem)
        ___qtablewidgetitem1 = QTableWidgetItem()
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Type", None))
        self.monthly_report_table.setHorizontalHeaderItem(1, ___qtablewidgetitem1)
        ___qtablewidgetitem2 = QTableWidgetItem()
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Amount", None))
        self.monthly_report_table.setHorizontalHeaderItem(2, ___qtablewidgetitem2)
        ___qtablewidgetitem3 = QTableWidgetItem()
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Category", None))
        self.monthly_report_table.setHorizontalHeaderItem(3, ___qtablewidgetitem3)
        ___qtablewidgetitem4 = QTableWidgetItem()
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Description", None))
        self.monthly_report_table.setHorizontalHeaderItem(4, ___qtablewidgetitem4)
        self.income_label.setText(QCoreApplication.translate("Dialog", u"Total Income: $0.00", None))
        self.expense_label.setText(QCoreApplication.translate("Dialog", u"Total Expenses: $0.00", None))
        self.net_balance_label.setText(QCoreApplication.translate("Dialog", u"Net Balance: $0.00", None))