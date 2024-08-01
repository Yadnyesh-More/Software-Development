# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resetpasspghMZKng.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

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
"QWidget{\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"")
        self.login_heading = QLabel(self.widget_2)
        self.login_heading.setObjectName(u"login_heading")
        self.login_heading.setGeometry(QRect(28, 30, 271, 81))
        font = QFont()
        font.setFamilies([u"Sitka Display Semibold"])
        font.setPointSize(22)
        font.setItalic(False)
        font.setUnderline(False)
        self.login_heading.setFont(font)
        self.login_heading.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.backbutton = QPushButton(self.widget_2)
        self.backbutton.setObjectName(u"backbutton")
        self.backbutton.setGeometry(QRect(134, 418, 51, 21))
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
        self.loginbutton = QPushButton(self.widget_2)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setGeometry(QRect(72, 339, 170, 25))
        font2 = QFont()
        font2.setPointSize(10)
        self.loginbutton.setFont(font2)
        self.loginbutton.setStyleSheet(u"QPushButton\n"
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
        self.loginbutton.setCheckable(True)
        self.layoutWidget_2 = QWidget(self.widget_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(37, 130, 251, 56))
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
        self.email_entry.setMaxLength(10)
        self.email_entry.setEchoMode(QLineEdit.EchoMode.Normal)
        self.email_entry.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.verticalLayout_2.addWidget(self.email_entry)

        self.layoutWidget_3 = QWidget(self.widget_2)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(37, 215, 251, 56))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.email_heading_2 = QLabel(self.layoutWidget_3)
        self.email_heading_2.setObjectName(u"email_heading_2")
        self.email_heading_2.setStyleSheet(u"color:rgb(18, 140, 126);")

        self.verticalLayout_3.addWidget(self.email_heading_2)

        self.email_entry_2 = QLineEdit(self.layoutWidget_3)
        self.email_entry_2.setObjectName(u"email_entry_2")
        self.email_entry_2.setMinimumSize(QSize(0, 30))
        self.email_entry_2.setFont(font3)
        self.email_entry_2.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.email_entry_2.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-bottom:2px solid rgb(0, 170, 0);\n"
"}\n"
"")
        self.email_entry_2.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.email_entry_2.setMaxLength(10)
        self.email_entry_2.setEchoMode(QLineEdit.EchoMode.Normal)
        self.email_entry_2.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.verticalLayout_3.addWidget(self.email_entry_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.login_heading.setText(QCoreApplication.translate("MainWindow", u" Reset Your password", None))
        self.backbutton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.loginbutton.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.email_heading.setText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.email_entry.setText("")
        self.email_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your Password", None))
        self.email_heading_2.setText(QCoreApplication.translate("MainWindow", u"Re-Enter Password", None))
        self.email_entry_2.setText("")
        self.email_entry_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Re-Enter your Password", None))
    # retranslateUi

