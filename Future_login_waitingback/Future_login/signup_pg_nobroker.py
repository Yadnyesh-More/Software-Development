# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signuppgopeeWh.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 480)
        MainWindow.setMinimumSize(QSize(400, 480))
        MainWindow.setMaximumSize(QSize(400, 480))
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(400, 480))
        self.frame.setMaximumSize(QSize(400, 480))
        self.frame.setStyleSheet(u"")
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(30, 5, 321, 451))
        self.widget_2.setStyleSheet(u"\n"
"border-radius:50px;\n"
"background-color:rgb(35, 47, 49);\n"
"\n"
"\n"
"")
        self.login_heading = QLabel(self.widget_2)
        self.login_heading.setObjectName(u"login_heading")
        self.login_heading.setGeometry(QRect(93, 23, 141, 61))
        font = QFont()
        font.setFamilies([u"Sitka Display Semibold"])
        font.setPointSize(32)
        font.setItalic(False)
        font.setUnderline(False)
        self.login_heading.setFont(font)
        self.login_heading.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.backbutton = QPushButton(self.widget_2)
        self.backbutton.setObjectName(u"backbutton")
        self.backbutton.setGeometry(QRect(130, 418, 51, 21))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.backbutton.setFont(font1)
        self.backbutton.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(255, 255,255);\n"
"}")
        icon = QIcon()
        icon.addFile(u"C:/Users/Shivam/Downloads/arrows.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backbutton.setIcon(icon)
        self.backbutton.setIconSize(QSize(15, 15))
        self.backbutton.setCheckable(False)
        self.register_button = QPushButton(self.widget_2)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setGeometry(QRect(72, 335, 170, 25))
        font2 = QFont()
        font2.setPointSize(10)
        self.register_button.setFont(font2)
        self.register_button.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(0, 170, 0);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(0, 170, 0);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.register_button.setCheckable(True)
        self.alrdy_button = QPushButton(self.widget_2)
        self.alrdy_button.setObjectName(u"alrdy_button")
        self.alrdy_button.setGeometry(QRect(92, 380, 141, 20))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setUnderline(True)
        self.alrdy_button.setFont(font3)
        self.alrdy_button.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.alrdy_button.setCheckable(True)
        self.layoutWidget = QWidget(self.widget_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(51, 244, 211, 54))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.password_heading_2 = QLabel(self.layoutWidget)
        self.password_heading_2.setObjectName(u"password_heading_2")
        self.password_heading_2.setStyleSheet(u"color: rgb(0, 170, 0);")

        self.verticalLayout_4.addWidget(self.password_heading_2)

        self.confirm_password_entry = QLineEdit(self.layoutWidget)
        self.confirm_password_entry.setObjectName(u"confirm_password_entry")
        self.confirm_password_entry.setMinimumSize(QSize(0, 30))
        font4 = QFont()
        font4.setFamilies([u"Segoe MDL2 Assets"])
        self.confirm_password_entry.setFont(font4)
        self.confirm_password_entry.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-bottom:2px solid rgb(0, 170, 0);\n"
"}")

        self.verticalLayout_4.addWidget(self.confirm_password_entry)

        self.layoutWidget1 = QWidget(self.widget_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(53, 101, 211, 54))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.email_heading = QLabel(self.layoutWidget1)
        self.email_heading.setObjectName(u"email_heading")
        self.email_heading.setStyleSheet(u"color: rgb(0, 170, 0);")

        self.verticalLayout_2.addWidget(self.email_heading)

        self.email_entry = QLineEdit(self.layoutWidget1)
        self.email_entry.setObjectName(u"email_entry")
        self.email_entry.setMinimumSize(QSize(0, 30))
        self.email_entry.setFont(font4)
        self.email_entry.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-bottom:2px solid rgb(0, 170, 0);\n"
"}")

        self.verticalLayout_2.addWidget(self.email_entry)

        self.layoutWidget2 = QWidget(self.widget_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(52, 173, 211, 54))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.password_heading = QLabel(self.layoutWidget2)
        self.password_heading.setObjectName(u"password_heading")
        self.password_heading.setStyleSheet(u"color: rgb(0, 170, 0);")

        self.verticalLayout_3.addWidget(self.password_heading)

        self.password_entry = QLineEdit(self.layoutWidget2)
        self.password_entry.setObjectName(u"password_entry")
        self.password_entry.setMinimumSize(QSize(0, 30))
        self.password_entry.setFont(font4)
        self.password_entry.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-bottom:2px solid rgb(0, 170, 0);\n"
"}")

        self.verticalLayout_3.addWidget(self.password_entry)

        self.sig_up_close_bar = QPushButton(self.frame)
        self.sig_up_close_bar.setObjectName(u"sig_up_close_bar")
        self.sig_up_close_bar.setGeometry(QRect(336, 1, 21, 20))
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.sig_up_close_bar.setFont(font5)
        self.sig_up_close_bar.setStyleSheet(u"QPushButton {\n"
"border:none;\n"
"color:rgb(0, 170, 0);}\n"
"\n"
"QPushButton:hover{\n"
"color:rgb(35, 47, 49);\n"
"}")
        self.sig_up_close_bar.setCheckable(True)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.sig_up_close_bar.toggled.connect(self.frame.close)
        self.sig_up_close_bar.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.login_heading.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.backbutton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.register_button.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.alrdy_button.setText(QCoreApplication.translate("MainWindow", u"already on MiddleMan ?", None))
        self.password_heading_2.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.confirm_password_entry.setText("")
        self.confirm_password_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your Password", None))
        self.email_heading.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.email_entry.setText("")
        self.email_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your Email", None))
        self.password_heading.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.password_entry.setText("")
        self.password_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your Password", None))
        self.sig_up_close_bar.setText(QCoreApplication.translate("MainWindow", u"x", None))
    # retranslateUi

