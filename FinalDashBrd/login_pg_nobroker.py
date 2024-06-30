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

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 480)
        MainWindow.setMinimumSize(QSize(400, 480))
        MainWindow.setMaximumSize(QSize(400, 480))
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 382, 462))
        self.frame.setStyleSheet(u"")
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(30, 0, 321, 451))
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
        self.forgetpassbutton.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.loginbutton = QPushButton(self.widget_2)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setGeometry(QRect(72, 270, 170, 25))
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
        self.signupbutton.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.layoutWidget = QWidget(self.widget_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(53, 101, 211, 54))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.email_heading = QLabel(self.layoutWidget)
        self.email_heading.setObjectName(u"email_heading")
        self.email_heading.setStyleSheet(u"color: rgb(0, 170, 0);")

        self.verticalLayout_2.addWidget(self.email_heading)

        self.email_entry = QLineEdit(self.layoutWidget)
        self.email_entry.setObjectName(u"email_entry")
        self.email_entry.setMinimumSize(QSize(0, 30))
        font4 = QFont()
        font4.setFamilies([u"Segoe MDL2 Assets"])
        self.email_entry.setFont(font4)
        self.email_entry.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-bottom:2px solid rgb(0, 170, 0);\n"
"}")

        self.verticalLayout_2.addWidget(self.email_entry)

        self.layoutWidget_2 = QWidget(self.widget_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(52, 173, 211, 54))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.password_heading = QLabel(self.layoutWidget_2)
        self.password_heading.setObjectName(u"password_heading")
        self.password_heading.setStyleSheet(u"color: rgb(0, 170, 0);")

        self.verticalLayout_3.addWidget(self.password_heading)

        self.password_entry = QLineEdit(self.layoutWidget_2)
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

        self.login_window_closer = QPushButton(self.frame)
        self.login_window_closer.setObjectName(u"login_window_closer")
        self.login_window_closer.setGeometry(QRect(336, 1, 21, 20))
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.login_window_closer.setFont(font5)
        self.login_window_closer.setStyleSheet(u"QPushButton {\n"
"border:none;\n"
"color:rgb(0, 170, 0);}\n"
"\n"
"QPushButton:hover{\n"
"color:rgb(35, 47, 49);\n"
"}")
        self.login_window_closer.setCheckable(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.login_window_closer.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
        
        # Initialize variables for moving the window
        self.moving = False
        self.offset = QPoint()
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moving = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.moving:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        self.moving = False

    def retranslateUi(self, MainWindow):
        icon = QIcon("images/prof_pic.png")
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login Window", None))
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
        self.login_window_closer.setText(QCoreApplication.translate("MainWindow", u"x", None))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec())