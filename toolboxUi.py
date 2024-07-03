# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MMdashboardPMlCos.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QToolBox,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def log_out(self):
            MainWindow.close()
    def __init__(self):

        self.frame_visible = False

        self.frame = None
    def profile_info(self):
        if not self.frame_visible:
            self.frame = QFrame(self.mainmenu)
            self.frame.setObjectName(u"frame")
            font = QFont()
            font.setPointSize(11)
            font.setBold(True)
            self.frame.setFont(font)
            self.frame.setStyleSheet(u"QFrame{\n"
                                     "background-color: rgb(35, 47, 49);\n"
                                     "border:2px solid rgb(0, 170, 0);\n"
                                     "border-radius:20px;\n"
                                     "}")
            self.frame.setGeometry(QRect(530, 70, 250, 250))
            self.frame.setFrameShape(QFrame.Shape.StyledPanel)
            self.frame.setFrameShadow(QFrame.Shadow.Raised)
            self.label = QLabel(self.frame)
            self.label.setObjectName(u"label")
            self.label.setGeometry(QRect(61, 10, 131, 31))
            font1 = QFont()
            font1.setPointSize(15)
            self.label.setFont(font1)
            self.label.setText("PROFILE INFO")
            self.label.setStyleSheet(u"QLabel{\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border:none;\n"
                                     "}")
            self.lineEdit = QLineEdit(self.frame)
            self.lineEdit.setObjectName(u"lineEdit")
            self.lineEdit.setGeometry(QRect(30, 76, 191, 20))
            self.lineEdit.setFont(font)
            self.lineEdit.setStyleSheet(u"QLineEdit{\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "border-bottom:3px solid rgb(0, 170, 0);\n"
                                        "}\n"
                                        "\n"
                                        "")
            self.lineEdit.setReadOnly(True)
            self.email_heading_3 = QLabel(self.frame)
            self.email_heading_3.setObjectName(u"email_heading_3")
            self.email_heading_3.setGeometry(QRect(32, 55, 61, 16))
            self.email_heading_3.setText("Login as")
            self.email_heading_3.setStyleSheet(u"color: rgb(0, 170, 0);\n"
                                               "border:none;\n"
                                               "")
            self.loginbutton_2 = QPushButton(self.frame)
            self.loginbutton_2.setObjectName(u"loginbutton_2")
            self.loginbutton_2.setGeometry(QRect(79, 216, 91, 21))
            font2 = QFont()
            font2.setPointSize(10)
            font2.setBold(True)
            self.loginbutton_2.setFont(font2)
            self.loginbutton_2.setText("Log Out")
            self.loginbutton_2.setStyleSheet(u"QPushButton\n"
                                             "{\n"
                                             "background-color: rgb(0, 170, 0);\n"
                                             "border-radius:10px;\n"
                                             "}\n"
                                             "QPushButton:hover\n"
                                             "{\n"
                                             "border:1px solid rgb(0, 170, 0);\n"
                                             "background-color:rgb(35, 47, 49);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "}")
            icon = QIcon()
            icon.addFile(u"../../Shivam/Downloads/logout.png", QSize(), QIcon.Normal, QIcon.Off)
            self.loginbutton_2.setIcon(icon)
            self.loginbutton_2.setIconSize(QSize(15, 15))
            self.loginbutton_2.setCheckable(True)
            self.lineEdit_2 = QLineEdit(self.frame)
            self.lineEdit_2.setObjectName(u"lineEdit_2")
            self.lineEdit_2.setGeometry(QRect(30, 124, 191, 20))
            self.lineEdit_2.setFont(font)
            self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "border-bottom:3px solid rgb(0, 170, 0);\n"
                                          "}\n"
                                          "\n"
                                          "")
            self.lineEdit_2.setReadOnly(True)
            self.email_heading_4 = QLabel(self.frame)
            self.email_heading_4.setObjectName(u"email_heading_4")
            self.email_heading_4.setGeometry(QRect(32, 103, 61, 16))
            self.email_heading_4.setText("Login Date")
            self.email_heading_4.setStyleSheet(u"color: rgb(0, 170, 0);\n"
                                               "border:none;\n"
                                               "")
            self.email_heading_5 = QLabel(self.frame)
            self.email_heading_5.setObjectName(u"email_heading_5")
            self.email_heading_5.setGeometry(QRect(33, 148, 61, 16))
            self.email_heading_5.setText("Login Time")
            self.email_heading_5.setStyleSheet(u"color: rgb(0, 170, 0);\n"
                                               "border:none;\n"
                                               "")
            self.lineEdit_3 = QLineEdit(self.frame)
            self.lineEdit_3.setObjectName(u"lineEdit_3")
            self.lineEdit_3.setGeometry(QRect(31, 169, 191, 20))
            self.lineEdit_3.setFont(font)
            self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "border-bottom:3px solid rgb(0, 170, 0);\n"
                                          "}\n"
                                          "\n"
                                          "")
            self.lineEdit_3.setReadOnly(True)
            self.loginbutton_2.clicked.connect(self.log_out)
            self.frame.show()
            self.frame_visible = True
        else:
            self.frame.hide()
            self.frame_visible = False

       
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(966, 624)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setMinimumSize(QSize(160, 0))
        self.icon_name_widget.setMaximumSize(QSize(160, 16777215))
        self.icon_name_widget.setAutoFillBackground(False)
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(35, 47, 49);\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"      color:white;\n"
"text-align:left;\n"
"height:35px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:rgb(236, 219, 186);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(139, 139, 139);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        self.widget_7 = QWidget(self.icon_name_widget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(0, 0, 160, 55))
        self.widget_7.setMinimumSize(QSize(0, 55))
        self.widget_7.setMaximumSize(QSize(16777215, 55))
        self.widget_7.setStyleSheet(u"background-color: rgb(0, 170, 0);")
        self.layoutWidget = QWidget(self.widget_7)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 161, 51))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 5, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(40, 40))
        self.label_5.setMaximumSize(QSize(40, 40))
        self.label_5.setPixmap(QPixmap(u"../../Shivam/Downloads/prof_pic.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.pushButton_24 = QPushButton(self.icon_name_widget)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(0, 584, 145, 40))
        self.pushButton_24.setMinimumSize(QSize(145, 40))
        self.pushButton_24.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(11)
        self.pushButton_24.setFont(font1)
        icon = QIcon()
        icon.addFile(u"../Sidebar/slidemenubar/log_out_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_24.setIcon(icon)
        self.pushButton_24.setIconSize(QSize(20, 20))
        self.pushButton_24.setCheckable(True)
        self.toolBox = QToolBox(self.icon_name_widget)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setGeometry(QRect(20, 86, 140, 401))
        self.toolBox.setMinimumSize(QSize(140, 50))
        self.toolBox.setMaximumSize(QSize(140, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.toolBox.setFont(font2)
        self.toolBox.setStyleSheet(u"QToolBox:tab{\n"
"	background-color:rgb(0, 170, 0);\n"
"	color: rgb(0, 0, 0);\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 140, 151))
        self.layoutWidget1 = QWidget(self.page)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 160, 121))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(15, 0, 0, 0)
        self.Dashboard_2 = QPushButton(self.layoutWidget1)
        self.Dashboard_2.setObjectName(u"Dashboard_2")
        self.Dashboard_2.setFont(font1)
        self.Dashboard_2.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../Shivam/Downloads/location.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_2.setIcon(icon1)
        self.Dashboard_2.setIconSize(QSize(25, 25))
        self.Dashboard_2.setCheckable(True)
        self.Dashboard_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Dashboard_2)

        self.Profile_2 = QPushButton(self.layoutWidget1)
        self.Profile_2.setObjectName(u"Profile_2")
        self.Profile_2.setFont(font1)
        self.Profile_2.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        self.Profile_2.setIcon(icon1)
        self.Profile_2.setIconSize(QSize(25, 25))
        self.Profile_2.setCheckable(True)
        self.Profile_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Profile_2)

        self.Messages_2 = QPushButton(self.layoutWidget1)
        self.Messages_2.setObjectName(u"Messages_2")
        self.Messages_2.setFont(font1)
        self.Messages_2.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        self.Messages_2.setIcon(icon1)
        self.Messages_2.setIconSize(QSize(25, 25))
        self.Messages_2.setCheckable(True)
        self.Messages_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Messages_2)

        icon2 = QIcon()
        icon2.addFile(u"../../Shivam/Downloads/zoom-in.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page, icon2, u"New Project")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 140, 151))
        self.layoutWidget2 = QWidget(self.page_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(-3, 0, 142, 161))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Messages_3 = QPushButton(self.layoutWidget2)
        self.Messages_3.setObjectName(u"Messages_3")
        self.Messages_3.setFont(font1)
        self.Messages_3.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../../Shivam/Downloads/washing-removebg-preview (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.Messages_3.setIcon(icon3)
        self.Messages_3.setIconSize(QSize(25, 25))
        self.Messages_3.setCheckable(True)
        self.Messages_3.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.Messages_3)

        self.Dashboard_3 = QPushButton(self.layoutWidget2)
        self.Dashboard_3.setObjectName(u"Dashboard_3")
        self.Dashboard_3.setFont(font1)
        self.Dashboard_3.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../../Shivam/Downloads/paint-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_3.setIcon(icon4)
        self.Dashboard_3.setIconSize(QSize(25, 25))
        self.Dashboard_3.setCheckable(True)
        self.Dashboard_3.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.Dashboard_3)

        self.Profile_3 = QPushButton(self.layoutWidget2)
        self.Profile_3.setObjectName(u"Profile_3")
        self.Profile_3.setFont(font1)
        self.Profile_3.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../../Shivam/Downloads/svg-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Profile_3.setIcon(icon5)
        self.Profile_3.setIconSize(QSize(25, 25))
        self.Profile_3.setCheckable(True)
        self.Profile_3.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.Profile_3)

        self.Dashboard_5 = QPushButton(self.layoutWidget2)
        self.Dashboard_5.setObjectName(u"Dashboard_5")
        self.Dashboard_5.setFont(font1)
        self.Dashboard_5.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../../Shivam/Downloads/construction-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_5.setIcon(icon6)
        self.Dashboard_5.setIconSize(QSize(25, 25))
        self.Dashboard_5.setCheckable(True)
        self.Dashboard_5.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.Dashboard_5)

        icon7 = QIcon()
        icon7.addFile(u"../../Shivam/Downloads/center.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_2, icon7, u"Other Services")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 140, 151))
        self.layoutWidget_2 = QWidget(self.page_3)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(-10, 0, 160, 3107))
        self.verticalLayout_21 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(15, 0, 0, 0)
        self.Dashboard_4 = QPushButton(self.layoutWidget_2)
        self.Dashboard_4.setObjectName(u"Dashboard_4")
        self.Dashboard_4.setFont(font1)
        self.Dashboard_4.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"../../Shivam/Downloads/note-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_4.setIcon(icon8)
        self.Dashboard_4.setIconSize(QSize(25, 25))
        self.Dashboard_4.setCheckable(True)
        self.Dashboard_4.setAutoExclusive(True)

        self.verticalLayout_21.addWidget(self.Dashboard_4)

        self.Profile_4 = QPushButton(self.layoutWidget_2)
        self.Profile_4.setObjectName(u"Profile_4")
        self.Profile_4.setFont(font1)
        self.Profile_4.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        self.Profile_4.setIconSize(QSize(0, 0))
        self.Profile_4.setCheckable(True)
        self.Profile_4.setAutoExclusive(True)

        self.verticalLayout_21.addWidget(self.Profile_4)

        self.Messages_4 = QPushButton(self.layoutWidget_2)
        self.Messages_4.setObjectName(u"Messages_4")
        self.Messages_4.setFont(font1)
        self.Messages_4.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        self.Messages_4.setIconSize(QSize(20, 20))
        self.Messages_4.setCheckable(True)
        self.Messages_4.setAutoExclusive(True)

        self.verticalLayout_21.addWidget(self.Messages_4)

        self.frame_3 = QFrame(self.layoutWidget_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 3000))
        self.frame_3.setStyleSheet(u"")

        self.verticalLayout_21.addWidget(self.frame_3)

        icon9 = QIcon()
        icon9.addFile(u"../../Shivam/Downloads/documentation.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_3, icon9, u"Agreements")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 140, 151))
        self.Dashboard_6 = QPushButton(self.page_4)
        self.Dashboard_6.setObjectName(u"Dashboard_6")
        self.Dashboard_6.setGeometry(QRect(10, 0, 141, 33))
        self.Dashboard_6.setFont(font1)
        self.Dashboard_6.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        self.Dashboard_6.setIconSize(QSize(25, 25))
        self.Dashboard_6.setCheckable(True)
        self.Dashboard_6.setAutoExclusive(True)
        icon10 = QIcon()
        icon10.addFile(u"../../Shivam/Downloads/money-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_4, icon10, u"Click and Earn")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 140, 151))
        self.layoutWidget_3 = QWidget(self.page_5)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(-4, -7, 160, 121))
        self.verticalLayout_22 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(15, 0, 0, 0)
        self.Dashboard_7 = QPushButton(self.layoutWidget_3)
        self.Dashboard_7.setObjectName(u"Dashboard_7")
        self.Dashboard_7.setFont(font1)
        self.Dashboard_7.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"../../Shivam/Downloads/rating-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_7.setIcon(icon11)
        self.Dashboard_7.setIconSize(QSize(25, 25))
        self.Dashboard_7.setCheckable(True)
        self.Dashboard_7.setAutoExclusive(True)

        self.verticalLayout_22.addWidget(self.Dashboard_7)

        self.Profile_5 = QPushButton(self.layoutWidget_3)
        self.Profile_5.setObjectName(u"Profile_5")
        self.Profile_5.setFont(font1)
        self.Profile_5.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"../../Shivam/Downloads/phone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Profile_5.setIcon(icon12)
        self.Profile_5.setIconSize(QSize(30, 30))
        self.Profile_5.setCheckable(True)
        self.Profile_5.setAutoExclusive(True)

        self.verticalLayout_22.addWidget(self.Profile_5)

        self.Messages_5 = QPushButton(self.layoutWidget_3)
        self.Messages_5.setObjectName(u"Messages_5")
        self.Messages_5.setFont(font1)
        self.Messages_5.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u"../../Shivam/Downloads/round.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Messages_5.setIcon(icon13)
        self.Messages_5.setIconSize(QSize(25, 25))
        self.Messages_5.setCheckable(True)
        self.Messages_5.setAutoExclusive(True)

        self.verticalLayout_22.addWidget(self.Messages_5)

        icon14 = QIcon()
        icon14.addFile(u"../../Shivam/Downloads/smartphone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_5, icon14, u" Others")

        self.horizontalLayout.addWidget(self.icon_name_widget)

        self.mainmenu = QWidget(self.centralwidget)
        self.mainmenu.setObjectName(u"mainmenu")
        self.mainmenu.setAutoFillBackground(False)
        self.mainmenu.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.verticalLayout = QVBoxLayout(self.mainmenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.mainmenu)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 55))
        self.widget_3.setStyleSheet(u"background-color:rgb(0, 170, 0);")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.Menu = QPushButton(self.widget_3)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setStyleSheet(u"border:none;")
        icon15 = QIcon()
        icon15.addFile(u"../Sidebar/slidemenubar/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu.setIcon(icon15)
        self.Menu.setIconSize(QSize(25, 25))
        self.Menu.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.Menu)

        self.horizontalSpacer_5 = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lineEdit_3 = QLineEdit(self.widget_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 25))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_10.addWidget(self.lineEdit_3)

        self.pushButton_32 = QPushButton(self.widget_3)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        icon16 = QIcon()
        icon16.addFile(u"../Sidebar/slidemenubar/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_32.setIcon(icon16)

        self.horizontalLayout_10.addWidget(self.pushButton_32)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)

        self.horizontalSpacer_6 = QSpacerItem(97, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.pushButton_33 = QPushButton(self.widget_3)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setStyleSheet(u"border:none;\n"
"background-color: rgb(166, 197, 255);\n"
"")
        icon17 = QIcon()
        icon17.addFile(u"../Sidebar/slidemenubar/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_33.setIcon(icon17)
        self.pushButton_33.setIconSize(QSize(25, 25))
        self.pushButton_33.setCheckable(True)
        self.pushButton_33.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.pushButton_33)


        self.verticalLayout.addWidget(self.widget_3)

        self.stackedWidget_3 = QStackedWidget(self.mainmenu)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setMaximumSize(QSize(16770, 16770))
        self.stackedWidget_3.setStyleSheet(u"background-color: rgb(35, 47, 49);")
        self.dashboardpage = QWidget()
        self.dashboardpage.setObjectName(u"dashboardpage")
        self.verticalLayout_17 = QVBoxLayout(self.dashboardpage)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.dashboardpage)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_19 = QVBoxLayout(self.widget_6)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_6 = QScrollArea(self.widget_6)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(0, 170, 0);\n"
" }")
        self.scrollArea_6.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 788, 3000))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 3000))
        self.frame_6.setStyleSheet(u"")
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(390, 240, 49, 16))

        self.verticalLayout_18.addWidget(self.frame_6)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_19.addWidget(self.scrollArea_6)


        self.verticalLayout_17.addWidget(self.widget_6)

        self.stackedWidget_3.addWidget(self.dashboardpage)
        self.meassagespage = QWidget()
        self.meassagespage.setObjectName(u"meassagespage")
        self.verticalLayout_2 = QVBoxLayout(self.meassagespage)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.meassagespage)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_7 = QScrollArea(self.widget)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(0, 170, 0);\n"
" }")
        self.scrollArea_7.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 788, 3000))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 3000))
        self.frame_7.setStyleSheet(u"")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(390, 240, 49, 16))

        self.verticalLayout_20.addWidget(self.frame_7)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_3.addWidget(self.scrollArea_7)


        self.verticalLayout_2.addWidget(self.widget)

        self.stackedWidget_3.addWidget(self.meassagespage)
        self.notificationspage = QWidget()
        self.notificationspage.setObjectName(u"notificationspage")
        self.verticalLayout_7 = QVBoxLayout(self.notificationspage)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.notificationspage)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_9 = QVBoxLayout(self.widget_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.widget_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(0, 170, 0);\n"
" }")
        self.scrollArea_2.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 83, 3000))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 3000))
        self.frame_2.setStyleSheet(u"")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(470, 230, 49, 16))

        self.verticalLayout_8.addWidget(self.frame_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_9.addWidget(self.scrollArea_2)


        self.verticalLayout_7.addWidget(self.widget_2)

        self.stackedWidget_3.addWidget(self.notificationspage)
        self.settingpage = QWidget()
        self.settingpage.setObjectName(u"settingpage")
        self.verticalLayout_10 = QVBoxLayout(self.settingpage)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.settingpage)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_12 = QVBoxLayout(self.widget_4)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.widget_4)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(0, 170, 0);\n"
" }")
        self.scrollArea_3.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 805, 569))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_12.addWidget(self.scrollArea_3)


        self.verticalLayout_10.addWidget(self.widget_4)

        self.stackedWidget_3.addWidget(self.settingpage)
        self.profilepage = QWidget()
        self.profilepage.setObjectName(u"profilepage")
        self.verticalLayout_14 = QVBoxLayout(self.profilepage)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.profilepage)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_16 = QVBoxLayout(self.widget_5)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_5 = QScrollArea(self.widget_5)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(0, 170, 0);\n"
" }")
        self.scrollArea_5.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 788, 3000))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 3000))
        self.frame_5.setStyleSheet(u"")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(410, 220, 49, 16))
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(600, 40, 81, 41))

        self.verticalLayout_15.addWidget(self.frame_5)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_16.addWidget(self.scrollArea_5)


        self.verticalLayout_14.addWidget(self.widget_5)

        self.stackedWidget_3.addWidget(self.profilepage)

        self.verticalLayout.addWidget(self.stackedWidget_3)


        self.horizontalLayout.addWidget(self.mainmenu)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Menu.toggled.connect(self.icon_name_widget.setHidden)
        self.pushButton_24.toggled.connect(MainWindow.close)
        self.pushButton_33.clicked.connect(self.profile_info)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(22)
        self.stackedWidget_3.setCurrentIndex(4)
        self.Dashboard_2.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(0))
        self.Profile_2.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(1))
        self.Messages_2.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(2))
        self.Dashboard_3.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(0))
        self.Profile_3.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(1))
        self.Messages_3.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(2))
        self.Dashboard_5.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(3))
        self.Dashboard_4.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(0))
        self.Profile_4.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(1))
        self.Messages_4.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(2))
        self.Dashboard_6.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(3))
        self.Dashboard_7.clicked.connect(lambda:self.stackedWidget_3.setCurrentIndex(0))
        self.Profile_5.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(1))
        self.Messages_5.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(2))
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<strong>M</strong>iddle <strong>M</strong>an", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u" Signout", None))
        self.Dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Mumbai", None))
        self.Profile_2.setText(QCoreApplication.translate("MainWindow", u"Thane", None))
        self.Messages_2.setText(QCoreApplication.translate("MainWindow", u"Pune", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"New Project", None))
        self.Messages_3.setText(QCoreApplication.translate("MainWindow", u"Plumbing", None))
        self.Dashboard_3.setText(QCoreApplication.translate("MainWindow", u"Interior Design", None))
        self.Profile_3.setText(QCoreApplication.translate("MainWindow", u"Ac Services", None))
        self.Dashboard_5.setText(QCoreApplication.translate("MainWindow", u"Carpentry", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Other Services", None))
        self.Dashboard_4.setText(QCoreApplication.translate("MainWindow", u"Rent Reciept", None))
        self.Profile_4.setText(QCoreApplication.translate("MainWindow", u"Tenant Verification", None))
        self.Messages_4.setText(QCoreApplication.translate("MainWindow", u"      Pune", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"Agreements", None))
        self.Dashboard_6.setText(QCoreApplication.translate("MainWindow", u"Click Here...", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"Click and Earn", None))
        self.Dashboard_7.setText(QCoreApplication.translate("MainWindow", u"Feedback", None))
        self.Profile_5.setText(QCoreApplication.translate("MainWindow", u"Contact Us", None))
        self.Messages_5.setText(QCoreApplication.translate("MainWindow", u"About Us", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u" Others", None))
        self.Menu.setText("")
        self.pushButton_32.setText("")
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"Hel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"dash", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"message", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Notify", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"profile", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

if __name__ == "__main__":
        import sys
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec())
        
        