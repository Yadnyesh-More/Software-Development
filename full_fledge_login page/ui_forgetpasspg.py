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
                # Set frameless window and translucent background
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
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
        self.login_heading.setGeometry(QRect(54, 20, 221, 61))
        font = QFont()
        font.setFamilies([u"Sitka Display Semibold"])
        font.setPointSize(24)
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
        self.layoutWidget_2 = QWidget(self.widget_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(37, 107, 251, 54))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.email_heading = QLabel(self.layoutWidget_2)
        self.email_heading.setObjectName(u"email_heading")
        self.email_heading.setStyleSheet(u"color: rgb(0, 170, 0);")

        self.verticalLayout_2.addWidget(self.email_heading)

        self.phone_entry = QLineEdit(self.layoutWidget_2)
        self.phone_entry.setObjectName(u"phone_entry")
        self.phone_entry.setMinimumSize(QSize(0, 30))
        font3 = QFont()
        font3.setFamilies([u"Segoe MDL2 Assets"])
        self.phone_entry.setFont(font3)
        self.phone_entry.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-bottom:2px solid rgb(0, 170, 0);\n"
"}")

        self.verticalLayout_2.addWidget(self.phone_entry)

        self.password_heading_2 = QLabel(self.widget_2)
        self.password_heading_2.setObjectName(u"password_heading_2")
        self.password_heading_2.setGeometry(QRect(104, 210, 111, 16))
        self.password_heading_2.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 246, 245, 32))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(25)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.otp_1 = QLineEdit(self.widget)
        self.otp_1.setObjectName(u"otp_1")
        self.otp_1.setMinimumSize(QSize(0, 30))
        font4 = QFont()
        font4.setFamilies([u"Segoe MDL2 Assets"])
        font4.setPointSize(11)
        self.otp_1.setFont(font4)
        self.otp_1.setCursor(QCursor(Qt.IBeamCursor))
        self.otp_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.otp_1.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-bottom:2px solid rgb(0, 170, 0);\n"
"}")
        self.otp_1.setMaxLength(1)
        self.otp_1.setCursorPosition(0)
        self.otp_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.otp_1.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.otp_1, 0, 0, 1, 1)

        self.otp_2 = QLineEdit(self.widget)
        self.otp_2.setObjectName(u"otp_2")
        self.otp_2.setMinimumSize(QSize(0, 30))
        self.otp_2.setFont(font4)
        self.otp_2.setCursor(QCursor(Qt.IBeamCursor))
        self.otp_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.otp_2.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-bottom:2px solid rgb(0, 170, 0);\n"
"}")
        self.otp_2.setMaxLength(1)
        self.otp_2.setCursorPosition(0)
        self.otp_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.otp_2.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.otp_2, 0, 1, 1, 1)

        self.otp_3 = QLineEdit(self.widget)
        self.otp_3.setObjectName(u"otp_3")
        self.otp_3.setMinimumSize(QSize(0, 30))
        self.otp_3.setFont(font4)
        self.otp_3.setCursor(QCursor(Qt.IBeamCursor))
        self.otp_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.otp_3.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-bottom:2px solid rgb(0, 170, 0);\n"
"}")
        self.otp_3.setMaxLength(1)
        self.otp_3.setCursorPosition(0)
        self.otp_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.otp_3.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.otp_3, 0, 2, 1, 1)

        self.otp_4 = QLineEdit(self.widget)
        self.otp_4.setObjectName(u"otp_4")
        self.otp_4.setMinimumSize(QSize(0, 30))
        self.otp_4.setFont(font4)
        self.otp_4.setCursor(QCursor(Qt.IBeamCursor))
        self.otp_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.otp_4.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-bottom:2px solid rgb(0, 170, 0);\n"
"}")
        self.otp_4.setMaxLength(1)
        self.otp_4.setCursorPosition(0)
        self.otp_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.otp_4.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.otp_4, 0, 3, 1, 1)

        self.verify_pushbutton = QPushButton(self.frame)
        self.verify_pushbutton.setObjectName(u"verify_pushbutton")
        self.verify_pushbutton.setGeometry(QRect(336, 1, 21, 20))
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.verify_pushbutton.setFont(font5)
        self.verify_pushbutton.setStyleSheet(u"QPushButton {\n"
"border:none;\n"
"color:rgb(0, 170, 0);}\n"
"\n"
"QPushButton:hover{\n"
"color:rgb(35, 47, 49);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.verify_pushbutton.clicked.connect(MainWindow.close)
        self.otp_1.cursorPositionChanged.connect(self.otp_2.setFocus)
        self.otp_2.cursorPositionChanged.connect(self.otp_3.setFocus)
        self.otp_3.cursorPositionChanged.connect(self.otp_4.setFocus)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.login_heading.setText(QCoreApplication.translate("MainWindow", u"Forget Password", None))
        self.backbutton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.loginbutton.setText(QCoreApplication.translate("MainWindow", u"Verify", None))
        self.email_heading.setText(QCoreApplication.translate("MainWindow", u"Contact No.", None))
        self.phone_entry.setText("")
        self.phone_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your Contact Number", None))
        self.password_heading_2.setText(QCoreApplication.translate("MainWindow", u"-- Enter OTP Here --", None))
        self.otp_1.setText("")
        self.otp_1.setPlaceholderText("")
        self.otp_2.setText("")
        self.otp_2.setPlaceholderText("")
        self.otp_3.setText("")
        self.otp_3.setPlaceholderText("")
        self.otp_4.setText("")
        self.otp_4.setPlaceholderText("")
        # self.verify_pushbutton.setText(QCoreApplication.translate("MainWindow", u"x", None))
    # retranslateUi