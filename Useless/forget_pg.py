# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forgetpasspgqvECkM.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 3, 400, 480))
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
        self.login_heading.setGeometry(QRect(44, 23, 241, 61))
        font = QFont()
        font.setFamilies([u"Sitka Display Semibold"])
        font.setPointSize(24)
        font.setItalic(False)
        font.setUnderline(False)
        self.login_heading.setFont(font)
        self.login_heading.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.backbutton = QPushButton(self.widget_2)
        self.backbutton.setObjectName(u"backbutton")
        self.backbutton.setGeometry(QRect(135, 418, 51, 21))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.backbutton.setFont(font1)
        self.backbutton.setStyleSheet(u"QPushButton{\n"
"color:rgb(18, 140, 126);\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(255, 255,255);\n"
"}")
        self.backbutton.setIconSize(QSize(15, 15))
        self.backbutton.setCheckable(False)
        self.verify = QPushButton(self.widget_2)
        self.verify.setObjectName(u"verify")
        self.verify.setGeometry(QRect(72, 365, 170, 25))
        font2 = QFont()
        font2.setPointSize(10)
        self.verify.setFont(font2)
        self.verify.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(18, 140, 126);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(18, 140, 126);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.verify.setCheckable(True)
        self.layoutWidget_2 = QWidget(self.widget_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(37, 86, 251, 54))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.email_heading = QLabel(self.layoutWidget_2)
        self.email_heading.setObjectName(u"email_heading")
        self.email_heading.setStyleSheet(u"color:rgb(18, 140, 126);")

        self.verticalLayout_2.addWidget(self.email_heading)

        self.email_entry = QLineEdit(self.layoutWidget_2)
        self.email_entry.setObjectName(u"email_entry")
        self.email_entry.setMinimumSize(QSize(0, 30))
        font3 = QFont()
        font3.setFamilies([u"Segoe MDL2 Assets"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setKerning(False)
        self.email_entry.setFont(font3)
        self.email_entry.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.email_entry.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-bottom:2px solid rgb(0, 170, 0);\n"
"}\n"
"")
        self.email_entry.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.email_entry.setMaxLength(1000)
        self.email_entry.setEchoMode(QLineEdit.EchoMode.Normal)
        self.email_entry.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.verticalLayout_2.addWidget(self.email_entry)

        self.password_heading_2 = QLabel(self.widget_2)
        self.password_heading_2.setObjectName(u"password_heading_2")
        self.password_heading_2.setGeometry(QRect(106, 266, 111, 16))
        self.password_heading_2.setStyleSheet(u"color:rgb(18, 140, 126);")
        self.layoutWidget = QWidget(self.widget_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 297, 245, 32))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(25)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.otp2 = QLineEdit(self.layoutWidget)
        self.otp2.setObjectName(u"otp2")
        self.otp2.setMinimumSize(QSize(0, 30))
        font4 = QFont()
        font4.setFamilies([u"Segoe MDL2 Assets"])
        font4.setPointSize(11)
        self.otp2.setFont(font4)
        self.otp2.setCursor(QCursor(Qt.IBeamCursor))
        self.otp2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.otp2.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-bottom:2px solid rgb(0, 170, 0);\n"
"}")
        self.otp2.setMaxLength(1)
        self.otp2.setCursorPosition(0)
        self.otp2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.otp2.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.otp2, 0, 0, 1, 1)

        self.otp1 = QLineEdit(self.layoutWidget)
        self.otp1.setObjectName(u"otp1")
        self.otp1.setMinimumSize(QSize(0, 30))
        self.otp1.setFont(font4)
        self.otp1.setCursor(QCursor(Qt.IBeamCursor))
        self.otp1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.otp1.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-bottom:2px solid rgb(0, 170, 0);\n"
"}")
        self.otp1.setMaxLength(1)
        self.otp1.setCursorPosition(0)
        self.otp1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.otp1.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.otp1, 0, 1, 1, 1)

        self.otp3 = QLineEdit(self.layoutWidget)
        self.otp3.setObjectName(u"otp3")
        self.otp3.setMinimumSize(QSize(0, 30))
        self.otp3.setFont(font4)
        self.otp3.setCursor(QCursor(Qt.IBeamCursor))
        self.otp3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.otp3.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-bottom:2px solid rgb(0, 170, 0);\n"
"}")
        self.otp3.setMaxLength(1)
        self.otp3.setCursorPosition(0)
        self.otp3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.otp3.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.otp3, 0, 2, 1, 1)

        self.otp4 = QLineEdit(self.layoutWidget)
        self.otp4.setObjectName(u"otp4")
        self.otp4.setMinimumSize(QSize(0, 30))
        self.otp4.setFont(font4)
        self.otp4.setCursor(QCursor(Qt.IBeamCursor))
        self.otp4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.otp4.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-bottom:2px solid rgb(0, 170, 0);\n"
"}")
        self.otp4.setMaxLength(1)
        self.otp4.setCursorPosition(0)
        self.otp4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.otp4.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.otp4, 0, 3, 1, 1)

        self.email_verify = QPushButton(self.widget_2)
        self.email_verify.setObjectName(u"email_verify")
        self.email_verify.setGeometry(QRect(200, 141, 101, 20))
        font5 = QFont()
        font5.setPointSize(8)
        font5.setUnderline(True)
        self.email_verify.setFont(font5)
        self.email_verify.setStyleSheet(u"QPushButton{\n"
"color:rgb(18, 140, 126);\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.layoutWidget_3 = QWidget(self.widget_2)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(37, 177, 251, 54))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.email_heading_2 = QLabel(self.layoutWidget_3)
        self.email_heading_2.setObjectName(u"email_heading_2")
        self.email_heading_2.setStyleSheet(u"color:rgb(18, 140, 126);")

        self.verticalLayout_3.addWidget(self.email_heading_2)

        self.contact_entry = QLineEdit(self.layoutWidget_3)
        self.contact_entry.setObjectName(u"contact_entry")
        self.contact_entry.setMinimumSize(QSize(0, 30))
        self.contact_entry.setFont(font3)
        self.contact_entry.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.contact_entry.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-bottom:2px solid rgb(0, 170, 0);\n"
"}\n"
"")
        self.contact_entry.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.contact_entry.setMaxLength(10)
        self.contact_entry.setEchoMode(QLineEdit.EchoMode.Normal)
        self.contact_entry.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.verticalLayout_3.addWidget(self.contact_entry)

        self.contact_verify = QPushButton(self.widget_2)
        self.contact_verify.setObjectName(u"contact_verify")
        self.contact_verify.setGeometry(QRect(200, 231, 101, 20))
        self.contact_verify.setFont(font5)
        self.contact_verify.setStyleSheet(u"QPushButton{\n"
"color:rgb(18, 140, 126);\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label1 = QLabel(self.widget_2)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(153, 159, 16, 16))
        self.label1.setFont(font2)
        self.label1.setStyleSheet(u"color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.otp1.cursorPositionChanged.connect(self.otp3.setFocus)
        self.otp2.cursorPositionChanged.connect(self.otp1.setFocus)
        self.otp3.cursorPositionChanged.connect(self.otp4.setFocus)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.login_heading.setText(QCoreApplication.translate("MainWindow", u" Forget Password", None))
        self.backbutton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.verify.setText(QCoreApplication.translate("MainWindow", u"Verify", None))
        self.email_heading.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.email_entry.setText("")
        self.email_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your Email Id", None))
        self.password_heading_2.setText(QCoreApplication.translate("MainWindow", u"-- Enter OTP Here --", None))
        self.otp2.setText("")
        self.otp2.setPlaceholderText("")
        self.otp1.setText("")
        self.otp1.setPlaceholderText("")
        self.otp3.setText("")
        self.otp3.setPlaceholderText("")
        self.otp4.setText("")
        self.otp4.setPlaceholderText("")
        self.email_verify.setText(QCoreApplication.translate("MainWindow", u"Press to Verify", None))
        self.email_heading_2.setText(QCoreApplication.translate("MainWindow", u"Contact No.", None))
        self.contact_entry.setText("")
        self.contact_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your Contact Number", None))
        self.contact_verify.setText(QCoreApplication.translate("MainWindow", u"Press to Verify", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"or", None))
    # retranslateUi

