

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AIBROKERFYPcTn.ui'
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
        self.frame.setStyleSheet(u"")
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(30, 5, 321, 451))
        self.widget_2.setStyleSheet(u"border-radius:50px;\n"
"background-color:rgb(35, 47, 49);\n"
"\n"
"")
        self.login_heading = QLabel(self.widget_2)
        self.login_heading.setObjectName(u"login_heading")
        self.login_heading.setGeometry(QRect(110, 23, 111, 61))
        font = QFont()
        font.setFamilies([u"Sitka Display Semibold"])
        font.setPointSize(32)
        font.setItalic(False)
        font.setUnderline(False)
        self.login_heading.setFont(font)
        self.login_heading.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.forgetpassbutton = QPushButton(self.widget_2)
        self.forgetpassbutton.setObjectName(u"forgetpassbutton")
        self.forgetpassbutton.setGeometry(QRect(167, 227, 101, 20))
        font1 = QFont()
        font1.setPointSize(8)
        self.forgetpassbutton.setFont(font1)
        self.forgetpassbutton.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.loginbutton = QPushButton(self.widget_2)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setGeometry(QRect(72, 270, 170, 25))
        font2 = QFont()
        font2.setPointSize(10)
        self.loginbutton.setFont(font2)
        self.loginbutton.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"border-radius:10px;")
        self.facebook = QPushButton(self.widget_2)
        self.facebook.setObjectName(u"facebook")
        self.facebook.setGeometry(QRect(58, 341, 32, 28))
        icon = QIcon()
        icon.addFile(u"C:/Users/Shivam/Downloads/facebook (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.facebook.setIcon(icon)
        self.facebook.setIconSize(QSize(28, 28))
        self.twitter = QPushButton(self.widget_2)
        self.twitter.setObjectName(u"twitter")
        self.twitter.setGeometry(QRect(142, 341, 32, 28))
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/Shivam/Downloads/twitter (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.twitter.setIcon(icon1)
        self.twitter.setIconSize(QSize(28, 28))
        self.google = QPushButton(self.widget_2)
        self.google.setObjectName(u"google")
        self.google.setGeometry(QRect(227, 341, 32, 28))
        icon2 = QIcon()
        icon2.addFile(u"C:/Users/Shivam/Downloads/google.png", QSize(), QIcon.Normal, QIcon.Off)
        self.google.setIcon(icon2)
        self.google.setIconSize(QSize(28, 28))
        self.label1 = QLabel(self.widget_2)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(118, 315, 91, 16))
        self.label1.setFont(font1)
        self.label1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label2 = QLabel(self.widget_2)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(120, 389, 91, 16))
        self.label2.setFont(font1)
        self.label2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.signupbutton = QPushButton(self.widget_2)
        self.signupbutton.setObjectName(u"signupbutton")
        self.signupbutton.setGeometry(QRect(110, 410, 101, 20))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setUnderline(True)
        self.signupbutton.setFont(font3)
        self.signupbutton.setStyleSheet(u"color: rgb(0, 170, 0);")
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
        font4 = QFont()
        font4.setFamilies([u"Segoe MDL2 Assets"])
        self.email_entry.setFont(font4)
        self.email_entry.setStyleSheet(u"background-color: rgb(255, 255, 255);")

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
        self.password_entry.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.password_entry)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(336, 1, 21, 20))
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.pushButton.setFont(font5)
        self.pushButton.setStyleSheet(u"border:none;\n"
"color:rgb(0, 170, 0);")
        self.pushButton.setCheckable(True)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.toggled.connect(self.frame.close)
        self.pushButton.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.login_heading.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.forgetpassbutton.setText(QCoreApplication.translate("MainWindow", u"Forget Password ?", None))
        self.loginbutton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.facebook.setText("")
        self.twitter.setText("")
        self.google.setText("")
        self.label1.setText(QCoreApplication.translate("MainWindow", u"or sign up using", None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"or sign up using", None))
        self.signupbutton.setText(QCoreApplication.translate("MainWindow", u"Signup", None))
        self.email_heading.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.email_entry.setText("")
        self.email_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your Email", None))
        self.password_heading.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.password_entry.setText("")
        self.password_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"x", None))
    # retranslateUi

