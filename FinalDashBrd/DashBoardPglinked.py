# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MMdashboardPwTFTk.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)
from sign_main import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MiddleMan")
        MainWindow.resize(1014, 624)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setMinimumSize(QSize(130, 0))
        self.icon_name_widget.setMaximumSize(QSize(145, 16777215))
        self.icon_name_widget.setAutoFillBackground(False)
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(35, 47, 49);\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"      color:white;\n"
"text-align:left;\n"
"height:30px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:rgb(0, 170, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(84, 113, 118);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.icon_name_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(40, 40))
        self.label_5.setMaximumSize(QSize(40, 40))
        self.label_5.setPixmap(QPixmap(u"prof_pic.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.icon_name_widget)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_7.addWidget(self.label_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 15, -1, -1)
        self.Dashboard_2 = QPushButton(self.icon_name_widget)
        self.Dashboard_2.setObjectName(u"Dashboard_2")
        icon = QIcon()
        icon.addFile(u"dashboard_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_2.setIcon(icon)
        self.Dashboard_2.setCheckable(True)
        self.Dashboard_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Dashboard_2)
        
        self.dashboardpage = QWidget()

        self.dashboardpage.setObjectName(u"dashboardpage")

        self.label = QLabel(self.dashboardpage)

        self.label.setObjectName(u"label")

        self.label.setGeometry(QRect(140, 150, 211, 41))

        font1 = QFont()

        font1.setPointSize(20)

        self.label.setFont(font1)

        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        # self.stackedWidget_3.addWidget(self.dashboardpage)

        self.Profile_2 = QPushButton(self.icon_name_widget)
        self.Profile_2.setObjectName(u"Profile_2")
        icon1 = QIcon()
        icon1.addFile(u"profile_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Profile_2.setIcon(icon1)
        self.Profile_2.setCheckable(True)
        self.Profile_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Profile_2)

        self.Messages_2 = QPushButton(self.icon_name_widget)
        self.Messages_2.setObjectName(u"Messages_2")
        icon2 = QIcon()
        icon2.addFile(u"messages_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Messages_2.setIcon(icon2)
        self.Messages_2.setCheckable(True)
        self.Messages_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Messages_2)

        self.Notifications_2 = QPushButton(self.icon_name_widget)
        self.Notifications_2.setObjectName(u"Notifications_2")
        icon3 = QIcon()
        icon3.addFile(u"notifications_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Notifications_2.setIcon(icon3)
        self.Notifications_2.setCheckable(True)
        self.Notifications_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Notifications_2)

        self.Setting_2 = QPushButton(self.icon_name_widget)
        self.Setting_2.setObjectName(u"Setting_2")
        icon4 = QIcon()
        icon4.addFile(u"settings_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Setting_2.setIcon(icon4)
        self.Setting_2.setCheckable(True)
        self.Setting_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Setting_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 136, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.pushButton_24 = QPushButton(self.icon_name_widget)
        self.pushButton_24.setObjectName(u"pushButton_24")
        icon5 = QIcon()
        icon5.addFile(u"log_out_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_24.setIcon(icon5)
        self.pushButton_24.setCheckable(True)

        self.verticalLayout_5.addWidget(self.pushButton_24)


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
        self.widget_3.setStyleSheet(u"background-color:rgb(0, 170, 0);")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.Menu = QPushButton(self.widget_3)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setStyleSheet(u"border:none;")
        icon6 = QIcon()
        icon6.addFile(u"menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu.setIcon(icon6)
        self.Menu.setIconSize(QSize(20, 20))
        self.Menu.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.Menu)

        self.horizontalSpacer_5 = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lineEdit_3 = QLineEdit(self.widget_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_10.addWidget(self.lineEdit_3)

        self.pushButton_32 = QPushButton(self.widget_3)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon7 = QIcon()
        icon7.addFile(u"search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_32.setIcon(icon7)

        self.horizontalLayout_10.addWidget(self.pushButton_32)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)

        self.horizontalSpacer_6 = QSpacerItem(97, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.pushButton_33 = QPushButton(self.widget_3)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setStyleSheet(u"border:none;\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_33.setIcon(icon8)
        # self.pushButton_33.connect()

        self.horizontalLayout_9.addWidget(self.pushButton_33)


        self.verticalLayout.addWidget(self.widget_3)

        self.stackedWidget_3 = QStackedWidget(self.mainmenu)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setStyleSheet(u"background-color: rgb(35, 47, 49);")
        self.dashboardpage = QWidget()
        self.dashboardpage.setObjectName(u"dashboardpage")
        self.label = QLabel(self.dashboardpage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 150, 211, 41))
        font1 = QFont()
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget_3.addWidget(self.dashboardpage)
        self.meassagespage = QWidget()
        self.meassagespage.setObjectName(u"meassagespage")
        self.label_8 = QLabel(self.meassagespage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(120, 140, 231, 51))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget_3.addWidget(self.meassagespage)
        self.notificationspage = QWidget()
        self.notificationspage.setObjectName(u"notificationspage")
        self.label_9 = QLabel(self.notificationspage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(120, 140, 231, 51))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget_3.addWidget(self.notificationspage)
        self.settingpage = QWidget()
        self.settingpage.setObjectName(u"settingpage")
        self.label_11 = QLabel(self.settingpage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(140, 130, 211, 51))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget_3.addWidget(self.settingpage)
        self.profilepage = QWidget()
        self.profilepage.setObjectName(u"profilepage")
        self.label_10 = QLabel(self.profilepage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(150, 150, 161, 51))
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget_3.addWidget(self.profilepage)

        self.verticalLayout.addWidget(self.stackedWidget_3)


        self.horizontalLayout.addWidget(self.mainmenu)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Menu.toggled.connect(self.icon_name_widget.setHidden)
        self.pushButton_24.toggled.connect(MainWindow.close)
        self.Dashboard_2.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(0))
        self.Profile_2.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(4))
        self.Messages_2.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(1))
        self.Notifications_2.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(2))
        self.Setting_2.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(3))

        self.stackedWidget_3.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"SlideBar", None))
        self.Dashboard_2.setText(QCoreApplication.translate("MainWindow", u" Dashboard", None))
        self.Profile_2.setText(QCoreApplication.translate("MainWindow", u" Profile", None))
        self.Messages_2.setText(QCoreApplication.translate("MainWindow", u" Messages", None))
        self.Notifications_2.setText(QCoreApplication.translate("MainWindow", u" Notifications", None))
        self.Setting_2.setText(QCoreApplication.translate("MainWindow", u" Settings", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u" Signout", None))
        self.Menu.setText("")
        self.pushButton_32.setText("")
        self.pushButton_33.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dashboard Page", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Notification Page", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Setting  Page", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Profile Page", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Message Page", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())