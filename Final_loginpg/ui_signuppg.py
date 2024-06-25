# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signuppglyjpLP.ui'
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
                # Set frameless window and translucent background
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
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
        self.loginbutton = QPushButton(self.widget_2)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setGeometry(QRect(72, 335, 170, 25))
        font2 = QFont()
        font2.setPointSize(10)
        self.loginbutton.setFont(font2)
        self.loginbutton.setStyleSheet(u"QPushButton\n"
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
        self.loginbutton.setCheckable(True)
        self.signupbutton = QPushButton(self.widget_2)
        self.signupbutton.setObjectName(u"signupbutton")
        self.signupbutton.setGeometry(QRect(92, 380, 141, 20))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setUnderline(True)
        self.signupbutton.setFont(font3)
        self.signupbutton.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.signupbutton.setCheckable(True)
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

        self.password_entry_2 = QLineEdit(self.layoutWidget)
        self.password_entry_2.setObjectName(u"password_entry_2")
        self.password_entry_2.setMinimumSize(QSize(0, 30))
        font4 = QFont()
        font4.setFamilies([u"Segoe MDL2 Assets"])
        self.password_entry_2.setFont(font4)
        self.password_entry_2.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-bottom:2px solid rgb(0, 170, 0);\n"
"}")

        self.verticalLayout_4.addWidget(self.password_entry_2)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(53, 101, 211, 54))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.email_heading = QLabel(self.widget)
        self.email_heading.setObjectName(u"email_heading")
        self.email_heading.setStyleSheet(u"color: rgb(0, 170, 0);")

        self.verticalLayout_2.addWidget(self.email_heading)

        self.email_entry = QLineEdit(self.widget)
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

        self.widget1 = QWidget(self.widget_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(52, 173, 211, 54))
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.password_heading = QLabel(self.widget1)
        self.password_heading.setObjectName(u"password_heading")
        self.password_heading.setStyleSheet(u"color: rgb(0, 170, 0);")

        self.verticalLayout_3.addWidget(self.password_heading)

        self.password_entry = QLineEdit(self.widget1)
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
        self.sig_up_close_bar.setStyleSheet(u"border:none;\n"
"color:rgb(0, 170, 0);")
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
        self.loginbutton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.signupbutton.setText(QCoreApplication.translate("MainWindow", u"already on MiddleMan ?", None))
        self.password_heading_2.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.password_entry_2.setText("")
        self.password_entry_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your Password", None))
        self.email_heading.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.email_entry.setText("")
        self.email_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your Email", None))
        self.password_heading.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.password_entry.setText("")
        self.password_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your Password", None))
        self.sig_up_close_bar.setText(QCoreApplication.translate("MainWindow", u"x", None))
    # retranslateUi

