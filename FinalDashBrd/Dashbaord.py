# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MMdashboardpwkKFT.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import subprocess
# from Sign_upFn import window
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1014, 624)
        # self.setWindowIco
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
        self.label_5.setPixmap(QPixmap(u"images/prof_pic.png"))
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
        self.verticalLayout_6.setSpacing(25)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 15, -1, -1)
        self.Dashboard_2 = QPushButton(self.icon_name_widget)
        self.Dashboard_2.setObjectName(u"Dashboard_2")
        font1 = QFont()
        font1.setPointSize(11)
        self.Dashboard_2.setFont(font1)
        icon = QIcon()
        icon.addFile(u"images/dashboard_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_2.setIcon(icon)
        self.Dashboard_2.setIconSize(QSize(20, 20))
        self.Dashboard_2.setCheckable(True)
        self.Dashboard_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Dashboard_2)

        self.Profile_2 = QPushButton(self.icon_name_widget)
        self.Profile_2.setObjectName(u"Profile_2")
        self.Profile_2.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u"images/profile_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Profile_2.setIcon(icon1)
        self.Profile_2.setIconSize(QSize(20, 20))
        self.Profile_2.setCheckable(True)
        self.Profile_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Profile_2)

        self.Messages_2 = QPushButton(self.icon_name_widget)
        self.Messages_2.setObjectName(u"Messages_2")
        self.Messages_2.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u"images/messages_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Messages_2.setIcon(icon2)
        self.Messages_2.setIconSize(QSize(20, 20))
        self.Messages_2.setCheckable(True)
        self.Messages_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Messages_2)

        self.Notifications_2 = QPushButton(self.icon_name_widget)
        self.Notifications_2.setObjectName(u"Notifications_2")
        self.Notifications_2.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u"images/notifications_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Notifications_2.setIcon(icon3)
        self.Notifications_2.setIconSize(QSize(20, 20))
        self.Notifications_2.setCheckable(True)
        self.Notifications_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Notifications_2)

        self.Setting_2 = QPushButton(self.icon_name_widget)
        self.Setting_2.setObjectName(u"Setting_2")
        self.Setting_2.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u"images/settings_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Setting_2.setIcon(icon4)
        self.Setting_2.setIconSize(QSize(20, 20))
        self.Setting_2.setCheckable(True)
        self.Setting_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Setting_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 136, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.pushButton_24 = QPushButton(self.icon_name_widget)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u"images/log_out_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_24.setIcon(icon5)
        self.pushButton_24.setIconSize(QSize(20, 20))
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
        self.widget_3.setMinimumSize(QSize(0, 55))
        self.widget_3.setStyleSheet(u"background-color:rgb(0, 170, 0);")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.Menu = QPushButton(self.widget_3)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setStyleSheet(u"border:none;")
        icon6 = QIcon()
        icon6.addFile(u"images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu.setIcon(icon6)
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
        icon7 = QIcon()
        icon7.addFile(u"images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_32.setIcon(icon7)

        self.horizontalLayout_10.addWidget(self.pushButton_32)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)

        self.horizontalSpacer_6 = QSpacerItem(97, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.pushButton_33 = QPushButton(self.widget_3)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setStyleSheet(u"border:none;\n"
"")     
        def login_wind_apperae():
                subprocess.run(["python", "Sign_appera.py"])
                print("Hello")
                # app = QApplication(sys.argv)
                # window.show()
                # sys.exit(app.exec_())
                        
                
        icon8 = QIcon()
        icon8.addFile(u"images/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_33.setIcon(icon8)
        self.pushButton_33.setIconSize(QSize(25, 25))
        self.pushButton_33.clicked.connect(login_wind_apperae)
       
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
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 836, 3000))
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
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 836, 3000))
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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 836, 3000))
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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 836, 3000))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 3000))
        self.frame_3.setStyleSheet(u"")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(380, 250, 49, 16))

        self.verticalLayout_11.addWidget(self.frame_3)

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
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 836, 3000))
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
        self.Dashboard_2.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(0))
        self.Profile_2.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(4))
        self.Messages_2.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(1))
        self.Notifications_2.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(2))
        self.Setting_2.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(3))

        self.stackedWidget_3.setCurrentIndex(3)
        

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        icon = QIcon("images/prof_pic.png")
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Middle Man", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"SlideBar", None))
        self.Dashboard_2.setText(QCoreApplication.translate("MainWindow", u"  Dashboard", None))
        self.Profile_2.setText(QCoreApplication.translate("MainWindow", u"  Profile", None))
        self.Messages_2.setText(QCoreApplication.translate("MainWindow", u"  Messages", None))
        self.Notifications_2.setText(QCoreApplication.translate("MainWindow", u"  Notifications", None))
        self.Setting_2.setText(QCoreApplication.translate("MainWindow", u"  Settings", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u" Signout", None))
        self.Menu.setText("")
        self.pushButton_32.setText("")
        self.pushButton_33.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"dash", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"message", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Notify", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"setting", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"profile", None))
    # retranslateUi
    



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())