# -- coding: utf-8 --

################################################################################
## Form generated from reading UI file 'newMMdashGDHlxh.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextEdit, QToolBox,
    QVBoxLayout, QWidget)
import ressanket_rc
import resshivam_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1552, 685)
        MainWindow.setMinimumSize(QSize(0, 0))
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
        self.verticalLayout_39 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_39.setSpacing(25)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 15)
        self.widget_7 = QWidget(self.icon_name_widget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 55))
        self.widget_7.setMaximumSize(QSize(16777215, 55))
        self.widget_7.setStyleSheet(u"\n"
"background-color: rgb(7, 94, 84);\n"
"")
        self.layoutWidget = QWidget(self.widget_7)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(-2, 2, 151, 52))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_39 = QPushButton(self.layoutWidget)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setMinimumSize(QSize(50, 50))
        self.pushButton_39.setMaximumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(u":/sanket/images/prof_pic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_39.setIcon(icon)
        self.pushButton_39.setIconSize(QSize(40, 40))
        self.pushButton_39.setCheckable(True)
        self.pushButton_39.setAutoExclusive(True)

        self.horizontalLayout_7.addWidget(self.pushButton_39)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_7.addWidget(self.label_6)


        self.verticalLayout_39.addWidget(self.widget_7, 0, Qt.AlignmentFlag.AlignTop)

        self.toolBox = QToolBox(self.icon_name_widget)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(140, 410))
        self.toolBox.setMaximumSize(QSize(140, 410))
        self.toolBox.setBaseSize(QSize(140, 0))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.toolBox.setFont(font1)
        self.toolBox.setStyleSheet(u"QToolBox:tab{\n"
"	background-color:rgb(7, 94, 84);\n"
"	color:rgb(255, 255, 255);\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"}")
        self.toolBox.setLineWidth(1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 140, 210))
        self.layoutWidget1 = QWidget(self.page)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 160, 121))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(15, 0, 0, 0)
        self.Dashboard_2 = QPushButton(self.layoutWidget1)
        self.Dashboard_2.setObjectName(u"Dashboard_2")
        font2 = QFont()
        font2.setPointSize(11)
        self.Dashboard_2.setFont(font2)
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
        icon1.addFile(u"C:/Users/Shivam/Downloads/location.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_2.setIcon(icon1)
        self.Dashboard_2.setIconSize(QSize(25, 25))
        self.Dashboard_2.setCheckable(True)
        self.Dashboard_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Dashboard_2)

        self.Profile_2 = QPushButton(self.layoutWidget1)
        self.Profile_2.setObjectName(u"Profile_2")
        self.Profile_2.setFont(font2)
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
        self.Messages_2.setFont(font2)
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
        icon2.addFile(u"PropImages/newhomeicom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page, icon2, u"New Project")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 140, 210))
        self.layoutWidget2 = QWidget(self.page_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(-3, 0, 142, 161))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Messages_3 = QPushButton(self.layoutWidget2)
        self.Messages_3.setObjectName(u"Messages_3")
        self.Messages_3.setFont(font2)
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
        icon3.addFile(u":/shivam/PropImages/washing-removebg-preview (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.Messages_3.setIcon(icon3)
        self.Messages_3.setIconSize(QSize(25, 25))
        self.Messages_3.setCheckable(True)
        self.Messages_3.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.Messages_3)

        self.Dashboard_3 = QPushButton(self.layoutWidget2)
        self.Dashboard_3.setObjectName(u"Dashboard_3")
        self.Dashboard_3.setFont(font2)
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
        icon4.addFile(u":/shivam/PropImages/paint-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_3.setIcon(icon4)
        self.Dashboard_3.setIconSize(QSize(25, 25))
        self.Dashboard_3.setCheckable(True)
        self.Dashboard_3.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.Dashboard_3)

        self.Profile_3 = QPushButton(self.layoutWidget2)
        self.Profile_3.setObjectName(u"Profile_3")
        self.Profile_3.setFont(font2)
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
        icon5.addFile(u":/shivam/PropImages/svg-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Profile_3.setIcon(icon5)
        self.Profile_3.setIconSize(QSize(25, 25))
        self.Profile_3.setCheckable(True)
        self.Profile_3.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.Profile_3)

        self.Dashboard_5 = QPushButton(self.layoutWidget2)
        self.Dashboard_5.setObjectName(u"Dashboard_5")
        self.Dashboard_5.setFont(font2)
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
        icon6.addFile(u":/shivam/PropImages/construction-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_5.setIcon(icon6)
        self.Dashboard_5.setIconSize(QSize(25, 25))
        self.Dashboard_5.setCheckable(True)
        self.Dashboard_5.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.Dashboard_5)

        icon7 = QIcon()
        icon7.addFile(u"C:/Users/Shivam/Downloads/ervice.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_2, icon7, u"Other Services")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 140, 210))
        self.Dashboard_6 = QPushButton(self.page_4)
        self.Dashboard_6.setObjectName(u"Dashboard_6")
        self.Dashboard_6.setGeometry(QRect(10, 0, 141, 33))
        self.Dashboard_6.setFont(font2)
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
        self.Dashboard_8 = QPushButton(self.page_4)
        self.Dashboard_8.setObjectName(u"Dashboard_8")
        self.Dashboard_8.setGeometry(QRect(9, 43, 141, 33))
        self.Dashboard_8.setFont(font2)
        self.Dashboard_8.setStyleSheet(u"\n"
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
        self.Dashboard_8.setIconSize(QSize(25, 25))
        self.Dashboard_8.setCheckable(True)
        self.Dashboard_8.setAutoExclusive(True)
        icon8 = QIcon()
        icon8.addFile(u"C:/Users/Shivam/Downloads/ervice (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_4, icon8, u"Click and Earn")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 140, 210))
        self.layoutWidget_3 = QWidget(self.page_5)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(-4, -7, 160, 121))
        self.verticalLayout_22 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(15, 0, 0, 0)
        self.Dashboard_7 = QPushButton(self.layoutWidget_3)
        self.Dashboard_7.setObjectName(u"Dashboard_7")
        self.Dashboard_7.setFont(font2)
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
        icon9 = QIcon()
        icon9.addFile(u":/shivam/PropImages/rating-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_7.setIcon(icon9)
        self.Dashboard_7.setIconSize(QSize(25, 25))
        self.Dashboard_7.setCheckable(True)
        self.Dashboard_7.setAutoExclusive(True)

        self.verticalLayout_22.addWidget(self.Dashboard_7)

        self.Profile_5 = QPushButton(self.layoutWidget_3)
        self.Profile_5.setObjectName(u"Profile_5")
        self.Profile_5.setFont(font2)
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
        icon10 = QIcon()
        icon10.addFile(u"C:/Users/Shivam/Downloads/phone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Profile_5.setIcon(icon10)
        self.Profile_5.setIconSize(QSize(30, 30))
        self.Profile_5.setCheckable(True)
        self.Profile_5.setAutoExclusive(True)

        self.verticalLayout_22.addWidget(self.Profile_5)

        self.Messages_5 = QPushButton(self.layoutWidget_3)
        self.Messages_5.setObjectName(u"Messages_5")
        self.Messages_5.setFont(font2)
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
        icon11 = QIcon()
        icon11.addFile(u"C:/Users/Shivam/Downloads/round.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Messages_5.setIcon(icon11)
        self.Messages_5.setIconSize(QSize(25, 25))
        self.Messages_5.setCheckable(True)
        self.Messages_5.setAutoExclusive(True)

        self.verticalLayout_22.addWidget(self.Messages_5)

        icon12 = QIcon()
        icon12.addFile(u"C:/Users/Shivam/Downloads/Untitled design (8).png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_5, icon12, u" Others")

        self.verticalLayout_39.addWidget(self.toolBox, 0, Qt.AlignmentFlag.AlignRight)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer)

        self.pushButton_11 = QPushButton(self.icon_name_widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"border:none;")
        icon13 = QIcon()
        icon13.addFile(u"C:/Users/Shivam/Downloads/notification-bell.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon13)
        self.pushButton_11.setIconSize(QSize(30, 30))

        self.verticalLayout_39.addWidget(self.pushButton_11, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


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
        self.widget_3.setStyleSheet(u"background-color: rgb(7, 94, 84);")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.Menu = QPushButton(self.widget_3)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setStyleSheet(u"border:none;")
        icon14 = QIcon()
        icon14.addFile(u"PropImages/DASHHH.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu.setIcon(icon14)
        self.Menu.setIconSize(QSize(30, 30))
        self.Menu.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.Menu)

        self.horizontalSpacer = QSpacerItem(250, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 25))
        self.pushButton.setMaximumSize(QSize(90, 25))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(7, 94, 84);\n"
"")
        icon15 = QIcon()
        icon15.addFile(u"C:/Users/Shivam/Downloads/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon15)
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.pushButton)

        self.comboBox = QComboBox(self.widget_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(150, 25))
        self.comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"boder-radius:125px;\n"
"}")
        self.comboBox.setEditable(False)

        self.horizontalLayout_9.addWidget(self.comboBox)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, -1, -1, -1)
        self.lineEdit_3 = QLineEdit(self.widget_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(300, 25))
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

        self.horizontalSpacer_6 = QSpacerItem(188, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.label_129 = QLabel(self.widget_3)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMinimumSize(QSize(40, 20))
        self.label_129.setMaximumSize(QSize(40, 20))
        self.label_129.setStyleSheet(u"background-color:rgb(37, 211, 102);\n"
"border:1px solid rgb(7, 94, 84);\n"
"color:rgb(70, 70, 70);\n"
"border-radius:10px;")
        self.label_129.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_129)

        self.pushButton_6 = QPushButton(self.widget_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(30, 30))
        self.pushButton_6.setMaximumSize(QSize(30, 30))
        self.pushButton_6.setStyleSheet(u"border:none;\n"
"")
        icon17 = QIcon()
        icon17.addFile(u"C:/Users/Shivam/Downloads/Coffe-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon17)
        self.pushButton_6.setIconSize(QSize(30, 30))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.pushButton_6)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.pushButton_33 = QPushButton(self.widget_3)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setStyleSheet(u"border:none;\n"
"")
        icon18 = QIcon()
        icon18.addFile(u"../Sidebar/slidemenubar/profile_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_33.setIcon(icon18)
        self.pushButton_33.setIconSize(QSize(25, 25))
        self.pushButton_33.setCheckable(True)
        self.pushButton_33.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.pushButton_33)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)


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
"    background:rgb(7, 94, 84);\n"
" }")
        self.scrollArea_6.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 1374, 2000))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 2000))
        self.frame_6.setStyleSheet(u"")
        self.horizontalLayout_13 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_6)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 2000))
        self.frame_30.setStyleSheet(u"")
        self.verticalLayout_37 = QVBoxLayout(self.frame_30)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setContentsMargins(50, 35, -1, 60)
        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        font3 = QFont()
        font3.setFamilies([u"Sitka Banner Semibold"])
        self.frame_32.setFont(font3)
        self.frame_32.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.label_200 = QLabel(self.frame_32)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setGeometry(QRect(13, 10, 181, 33))
        font4 = QFont()
        font4.setFamilies([u"Sitka Subheading"])
        font4.setPointSize(25)
        self.label_200.setFont(font4)
        self.label_200.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_201 = QLabel(self.frame_32)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setGeometry(QRect(16, 49, 16, 16))
        self.label_201.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_202 = QLabel(self.frame_32)
        self.label_202.setObjectName(u"label_202")
        self.label_202.setGeometry(QRect(35, 49, 81, 16))
        self.label_202.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_19 = QPushButton(self.frame_32)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_19.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_203 = QLabel(self.frame_32)
        self.label_203.setObjectName(u"label_203")
        self.label_203.setGeometry(QRect(300, 10, 182, 31))
        font5 = QFont()
        font5.setPointSize(17)
        self.label_203.setFont(font5)
        self.label_203.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_204 = QLabel(self.frame_32)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setGeometry(QRect(467, 17, 91, 20))
        self.label_204.setFont(font2)
        self.label_204.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_205 = QLabel(self.frame_32)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setGeometry(QRect(354, 44, 151, 20))
        self.label_205.setFont(font2)
        self.label_205.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.line_52 = QFrame(self.frame_32)
        self.line_52.setObjectName(u"line_52")
        self.line_52.setGeometry(QRect(307, 99, 16, 269))
        self.line_52.setFrameShape(QFrame.Shape.VLine)
        self.line_52.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_207 = QLabel(self.frame_32)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setGeometry(QRect(377, 99, 175, 44))
        font6 = QFont()
        font6.setPointSize(12)
        self.label_207.setFont(font6)
        self.label_207.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_53 = QFrame(self.frame_32)
        self.line_53.setObjectName(u"line_53")
        self.line_53.setGeometry(QRect(316, 185, 274, 16))
        self.line_53.setFrameShape(QFrame.Shape.HLine)
        self.line_53.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_208 = QLabel(self.frame_32)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setGeometry(QRect(377, 194, 120, 44))
        self.label_208.setFont(font6)
        self.label_208.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_209 = QLabel(self.frame_32)
        self.label_209.setObjectName(u"label_209")
        self.label_209.setGeometry(QRect(377, 289, 152, 66))
        self.label_209.setFont(font6)
        self.label_209.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_210 = QLabel(self.frame_32)
        self.label_210.setObjectName(u"label_210")
        self.label_210.setGeometry(QRect(10, 75, 191, 18))
        font7 = QFont()
        font7.setPointSize(10)
        self.label_210.setFont(font7)
        self.label_210.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_54 = QFrame(self.frame_32)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setGeometry(QRect(316, 279, 274, 16))
        self.line_54.setFrameShape(QFrame.Shape.HLine)
        self.line_54.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_206 = QLabel(self.frame_32)
        self.label_206.setObjectName(u"label_206")
        self.label_206.setGeometry(QRect(10, 99, 291, 269))
        self.label_206.setStyleSheet(u"border-radius:5px;")
        self.label_206.setPixmap(QPixmap(u"PropImages/Thane/Thane-AsharMerac/Thane-2.1.Elevtion.jpg"))
        self.label_206.setScaledContents(True)

        self.gridLayout_3.addWidget(self.frame_32, 0, 1, 1, 1)

        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFont(font3)
        self.frame_33.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.label_211 = QLabel(self.frame_33)
        self.label_211.setObjectName(u"label_211")
        self.label_211.setGeometry(QRect(13, 10, 261, 33))
        self.label_211.setFont(font4)
        self.label_211.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_212 = QLabel(self.frame_33)
        self.label_212.setObjectName(u"label_212")
        self.label_212.setGeometry(QRect(16, 49, 16, 16))
        self.label_212.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_213 = QLabel(self.frame_33)
        self.label_213.setObjectName(u"label_213")
        self.label_213.setGeometry(QRect(35, 49, 71, 16))
        self.label_213.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_20 = QPushButton(self.frame_33)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_20.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_214 = QLabel(self.frame_33)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setGeometry(QRect(298, 10, 231, 31))
        font8 = QFont()
        font8.setPointSize(16)
        self.label_214.setFont(font8)
        self.label_214.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_215 = QLabel(self.frame_33)
        self.label_215.setObjectName(u"label_215")
        self.label_215.setGeometry(QRect(477, 17, 75, 20))
        self.label_215.setFont(font2)
        self.label_215.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_216 = QLabel(self.frame_33)
        self.label_216.setObjectName(u"label_216")
        self.label_216.setGeometry(QRect(354, 44, 151, 20))
        self.label_216.setFont(font2)
        self.label_216.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_217 = QLabel(self.frame_33)
        self.label_217.setObjectName(u"label_217")
        self.label_217.setGeometry(QRect(10, 99, 291, 269))
        self.label_217.setStyleSheet(u"border-radius:5px;")
        self.label_217.setPixmap(QPixmap(u"PropImages/Thane/Thane-ShivlayaHeights/Thane-3.jpg"))
        self.label_217.setScaledContents(True)
        self.line_55 = QFrame(self.frame_33)
        self.line_55.setObjectName(u"line_55")
        self.line_55.setGeometry(QRect(307, 99, 16, 269))
        self.line_55.setFrameShape(QFrame.Shape.VLine)
        self.line_55.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_218 = QLabel(self.frame_33)
        self.label_218.setObjectName(u"label_218")
        self.label_218.setGeometry(QRect(377, 99, 175, 44))
        self.label_218.setFont(font6)
        self.label_218.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_56 = QFrame(self.frame_33)
        self.line_56.setObjectName(u"line_56")
        self.line_56.setGeometry(QRect(316, 185, 274, 16))
        self.line_56.setFrameShape(QFrame.Shape.HLine)
        self.line_56.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_219 = QLabel(self.frame_33)
        self.label_219.setObjectName(u"label_219")
        self.label_219.setGeometry(QRect(377, 194, 120, 44))
        self.label_219.setFont(font6)
        self.label_219.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_220 = QLabel(self.frame_33)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setGeometry(QRect(377, 290, 152, 66))
        self.label_220.setFont(font6)
        self.label_220.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_221 = QLabel(self.frame_33)
        self.label_221.setObjectName(u"label_221")
        self.label_221.setGeometry(QRect(10, 75, 421, 18))
        self.label_221.setFont(font7)
        self.label_221.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_57 = QFrame(self.frame_33)
        self.line_57.setObjectName(u"line_57")
        self.line_57.setGeometry(QRect(316, 279, 274, 16))
        self.line_57.setFrameShape(QFrame.Shape.HLine)
        self.line_57.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.frame_33, 1, 0, 1, 1)

        self.frame_38 = QFrame(self.frame_30)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFont(font3)
        self.frame_38.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_38.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)
        self.label_266 = QLabel(self.frame_38)
        self.label_266.setObjectName(u"label_266")
        self.label_266.setGeometry(QRect(13, 10, 161, 33))
        self.label_266.setFont(font4)
        self.label_266.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_267 = QLabel(self.frame_38)
        self.label_267.setObjectName(u"label_267")
        self.label_267.setGeometry(QRect(16, 49, 16, 16))
        self.label_267.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_268 = QLabel(self.frame_38)
        self.label_268.setObjectName(u"label_268")
        self.label_268.setGeometry(QRect(35, 49, 111, 16))
        self.label_268.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_25 = QPushButton(self.frame_38)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_25.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_269 = QLabel(self.frame_38)
        self.label_269.setObjectName(u"label_269")
        self.label_269.setGeometry(QRect(285, 10, 191, 31))
        self.label_269.setFont(font5)
        self.label_269.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_270 = QLabel(self.frame_38)
        self.label_270.setObjectName(u"label_270")
        self.label_270.setGeometry(QRect(477, 17, 91, 20))
        self.label_270.setFont(font2)
        self.label_270.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_271 = QLabel(self.frame_38)
        self.label_271.setObjectName(u"label_271")
        self.label_271.setGeometry(QRect(354, 44, 151, 20))
        self.label_271.setFont(font2)
        self.label_271.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_272 = QLabel(self.frame_38)
        self.label_272.setObjectName(u"label_272")
        self.label_272.setGeometry(QRect(10, 99, 291, 269))
        self.label_272.setStyleSheet(u"border-radius:5px;")
        self.label_272.setPixmap(QPixmap(u"C:/Users/Shivam/Downloads/WhatsApp Image 2024-06-26 at 19.16.15_a6f43295.jpg"))
        self.label_272.setScaledContents(True)
        self.line_70 = QFrame(self.frame_38)
        self.line_70.setObjectName(u"line_70")
        self.line_70.setGeometry(QRect(307, 99, 16, 269))
        self.line_70.setFrameShape(QFrame.Shape.VLine)
        self.line_70.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_273 = QLabel(self.frame_38)
        self.label_273.setObjectName(u"label_273")
        self.label_273.setGeometry(QRect(377, 99, 175, 44))
        self.label_273.setFont(font6)
        self.label_273.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_71 = QFrame(self.frame_38)
        self.line_71.setObjectName(u"line_71")
        self.line_71.setGeometry(QRect(316, 185, 274, 16))
        self.line_71.setFrameShape(QFrame.Shape.HLine)
        self.line_71.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_274 = QLabel(self.frame_38)
        self.label_274.setObjectName(u"label_274")
        self.label_274.setGeometry(QRect(377, 194, 120, 44))
        self.label_274.setFont(font6)
        self.label_274.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_275 = QLabel(self.frame_38)
        self.label_275.setObjectName(u"label_275")
        self.label_275.setGeometry(QRect(377, 290, 152, 66))
        self.label_275.setFont(font6)
        self.label_275.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_276 = QLabel(self.frame_38)
        self.label_276.setObjectName(u"label_276")
        self.label_276.setGeometry(QRect(10, 75, 410, 18))
        self.label_276.setFont(font7)
        self.label_276.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_72 = QFrame(self.frame_38)
        self.line_72.setObjectName(u"line_72")
        self.line_72.setGeometry(QRect(316, 279, 274, 16))
        self.line_72.setFrameShape(QFrame.Shape.HLine)
        self.line_72.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.frame_38, 3, 1, 1, 1)

        self.frame_37 = QFrame(self.frame_30)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFont(font3)
        self.frame_37.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_37.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.label_255 = QLabel(self.frame_37)
        self.label_255.setObjectName(u"label_255")
        self.label_255.setGeometry(QRect(13, 10, 181, 33))
        self.label_255.setFont(font4)
        self.label_255.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_256 = QLabel(self.frame_37)
        self.label_256.setObjectName(u"label_256")
        self.label_256.setGeometry(QRect(16, 49, 16, 16))
        self.label_256.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_257 = QLabel(self.frame_37)
        self.label_257.setObjectName(u"label_257")
        self.label_257.setGeometry(QRect(35, 49, 81, 16))
        self.label_257.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_24 = QPushButton(self.frame_37)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_24.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_258 = QLabel(self.frame_37)
        self.label_258.setObjectName(u"label_258")
        self.label_258.setGeometry(QRect(298, 10, 182, 31))
        self.label_258.setFont(font5)
        self.label_258.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_259 = QLabel(self.frame_37)
        self.label_259.setObjectName(u"label_259")
        self.label_259.setGeometry(QRect(472, 17, 75, 20))
        self.label_259.setFont(font2)
        self.label_259.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_260 = QLabel(self.frame_37)
        self.label_260.setObjectName(u"label_260")
        self.label_260.setGeometry(QRect(354, 44, 151, 20))
        self.label_260.setFont(font2)
        self.label_260.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_261 = QLabel(self.frame_37)
        self.label_261.setObjectName(u"label_261")
        self.label_261.setGeometry(QRect(10, 99, 291, 269))
        self.label_261.setStyleSheet(u"border-radius:5px;")
        self.label_261.setPixmap(QPixmap(u"PropImages/WhatsApp Image 2024-07-05 at 20.11.02_1a624b3c.jpg"))
        self.label_261.setScaledContents(True)
        self.line_67 = QFrame(self.frame_37)
        self.line_67.setObjectName(u"line_67")
        self.line_67.setGeometry(QRect(307, 99, 16, 269))
        self.line_67.setFrameShape(QFrame.Shape.VLine)
        self.line_67.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_262 = QLabel(self.frame_37)
        self.label_262.setObjectName(u"label_262")
        self.label_262.setGeometry(QRect(377, 99, 175, 44))
        self.label_262.setFont(font6)
        self.label_262.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_68 = QFrame(self.frame_37)
        self.line_68.setObjectName(u"line_68")
        self.line_68.setGeometry(QRect(316, 185, 274, 16))
        self.line_68.setFrameShape(QFrame.Shape.HLine)
        self.line_68.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_263 = QLabel(self.frame_37)
        self.label_263.setObjectName(u"label_263")
        self.label_263.setGeometry(QRect(377, 194, 120, 44))
        self.label_263.setFont(font6)
        self.label_263.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_264 = QLabel(self.frame_37)
        self.label_264.setObjectName(u"label_264")
        self.label_264.setGeometry(QRect(377, 290, 152, 66))
        self.label_264.setFont(font6)
        self.label_264.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_265 = QLabel(self.frame_37)
        self.label_265.setObjectName(u"label_265")
        self.label_265.setGeometry(QRect(10, 75, 421, 18))
        self.label_265.setFont(font7)
        self.label_265.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_69 = QFrame(self.frame_37)
        self.line_69.setObjectName(u"line_69")
        self.line_69.setGeometry(QRect(316, 279, 274, 16))
        self.line_69.setFrameShape(QFrame.Shape.HLine)
        self.line_69.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.frame_37, 3, 0, 1, 1)

        self.frame_34 = QFrame(self.frame_30)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFont(font3)
        self.frame_34.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.label_222 = QLabel(self.frame_34)
        self.label_222.setObjectName(u"label_222")
        self.label_222.setGeometry(QRect(13, 10, 171, 33))
        self.label_222.setFont(font4)
        self.label_222.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_223 = QLabel(self.frame_34)
        self.label_223.setObjectName(u"label_223")
        self.label_223.setGeometry(QRect(16, 49, 16, 16))
        self.label_223.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_224 = QLabel(self.frame_34)
        self.label_224.setObjectName(u"label_224")
        self.label_224.setGeometry(QRect(35, 49, 81, 16))
        self.label_224.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_21 = QPushButton(self.frame_34)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_21.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_225 = QLabel(self.frame_34)
        self.label_225.setObjectName(u"label_225")
        self.label_225.setGeometry(QRect(294, 10, 182, 31))
        self.label_225.setFont(font5)
        self.label_225.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_226 = QLabel(self.frame_34)
        self.label_226.setObjectName(u"label_226")
        self.label_226.setGeometry(QRect(461, 17, 91, 20))
        self.label_226.setFont(font2)
        self.label_226.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_227 = QLabel(self.frame_34)
        self.label_227.setObjectName(u"label_227")
        self.label_227.setGeometry(QRect(354, 44, 141, 20))
        self.label_227.setFont(font2)
        self.label_227.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_228 = QLabel(self.frame_34)
        self.label_228.setObjectName(u"label_228")
        self.label_228.setGeometry(QRect(10, 99, 291, 269))
        self.label_228.setStyleSheet(u"border-radius:5px;")
        self.label_228.setPixmap(QPixmap(u"PropImages/Thane/Thane-DostiHeron/Thane-4.1Elev.jpg"))
        self.label_228.setScaledContents(True)
        self.line_58 = QFrame(self.frame_34)
        self.line_58.setObjectName(u"line_58")
        self.line_58.setGeometry(QRect(307, 99, 16, 269))
        self.line_58.setFrameShape(QFrame.Shape.VLine)
        self.line_58.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_229 = QLabel(self.frame_34)
        self.label_229.setObjectName(u"label_229")
        self.label_229.setGeometry(QRect(377, 99, 175, 44))
        self.label_229.setFont(font6)
        self.label_229.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_59 = QFrame(self.frame_34)
        self.line_59.setObjectName(u"line_59")
        self.line_59.setGeometry(QRect(316, 185, 274, 16))
        self.line_59.setFrameShape(QFrame.Shape.HLine)
        self.line_59.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_230 = QLabel(self.frame_34)
        self.label_230.setObjectName(u"label_230")
        self.label_230.setGeometry(QRect(377, 194, 120, 44))
        self.label_230.setFont(font6)
        self.label_230.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_231 = QLabel(self.frame_34)
        self.label_231.setObjectName(u"label_231")
        self.label_231.setGeometry(QRect(377, 290, 152, 66))
        self.label_231.setFont(font6)
        self.label_231.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_232 = QLabel(self.frame_34)
        self.label_232.setObjectName(u"label_232")
        self.label_232.setGeometry(QRect(10, 75, 241, 18))
        self.label_232.setFont(font7)
        self.label_232.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_60 = QFrame(self.frame_34)
        self.line_60.setObjectName(u"line_60")
        self.line_60.setGeometry(QRect(316, 279, 274, 16))
        self.line_60.setFrameShape(QFrame.Shape.HLine)
        self.line_60.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.frame_34, 1, 1, 1, 1)

        self.frame_35 = QFrame(self.frame_30)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFont(font3)
        self.frame_35.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_35.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.label_233 = QLabel(self.frame_35)
        self.label_233.setObjectName(u"label_233")
        self.label_233.setGeometry(QRect(13, 10, 231, 33))
        self.label_233.setFont(font4)
        self.label_233.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_234 = QLabel(self.frame_35)
        self.label_234.setObjectName(u"label_234")
        self.label_234.setGeometry(QRect(16, 49, 16, 16))
        self.label_234.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_235 = QLabel(self.frame_35)
        self.label_235.setObjectName(u"label_235")
        self.label_235.setGeometry(QRect(35, 49, 90, 16))
        self.label_235.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_22 = QPushButton(self.frame_35)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_22.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_236 = QLabel(self.frame_35)
        self.label_236.setObjectName(u"label_236")
        self.label_236.setGeometry(QRect(298, 10, 182, 31))
        self.label_236.setFont(font5)
        self.label_236.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_237 = QLabel(self.frame_35)
        self.label_237.setObjectName(u"label_237")
        self.label_237.setGeometry(QRect(471, 17, 81, 20))
        self.label_237.setFont(font2)
        self.label_237.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_238 = QLabel(self.frame_35)
        self.label_238.setObjectName(u"label_238")
        self.label_238.setGeometry(QRect(354, 44, 151, 20))
        self.label_238.setFont(font2)
        self.label_238.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_239 = QLabel(self.frame_35)
        self.label_239.setObjectName(u"label_239")
        self.label_239.setGeometry(QRect(10, 99, 291, 269))
        self.label_239.setStyleSheet(u"border-radius:5px;")
        self.label_239.setPixmap(QPixmap(u"PropImages/Thane/Thane-ParijasHorizon/Thane-5.jpg"))
        self.label_239.setScaledContents(True)
        self.line_61 = QFrame(self.frame_35)
        self.line_61.setObjectName(u"line_61")
        self.line_61.setGeometry(QRect(307, 99, 16, 269))
        self.line_61.setFrameShape(QFrame.Shape.VLine)
        self.line_61.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_240 = QLabel(self.frame_35)
        self.label_240.setObjectName(u"label_240")
        self.label_240.setGeometry(QRect(377, 99, 175, 44))
        self.label_240.setFont(font6)
        self.label_240.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_62 = QFrame(self.frame_35)
        self.line_62.setObjectName(u"line_62")
        self.line_62.setGeometry(QRect(316, 185, 274, 16))
        self.line_62.setFrameShape(QFrame.Shape.HLine)
        self.line_62.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_241 = QLabel(self.frame_35)
        self.label_241.setObjectName(u"label_241")
        self.label_241.setGeometry(QRect(377, 194, 120, 44))
        self.label_241.setFont(font6)
        self.label_241.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_242 = QLabel(self.frame_35)
        self.label_242.setObjectName(u"label_242")
        self.label_242.setGeometry(QRect(377, 290, 152, 66))
        self.label_242.setFont(font6)
        self.label_242.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_243 = QLabel(self.frame_35)
        self.label_243.setObjectName(u"label_243")
        self.label_243.setGeometry(QRect(10, 75, 281, 18))
        self.label_243.setFont(font7)
        self.label_243.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_63 = QFrame(self.frame_35)
        self.line_63.setObjectName(u"line_63")
        self.line_63.setGeometry(QRect(316, 279, 274, 16))
        self.line_63.setFrameShape(QFrame.Shape.HLine)
        self.line_63.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.frame_35, 2, 0, 1, 1)

        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFont(font3)
        self.frame_31.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.label_189 = QLabel(self.frame_31)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setGeometry(QRect(13, 10, 161, 33))
        self.label_189.setFont(font4)
        self.label_189.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_190 = QLabel(self.frame_31)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setGeometry(QRect(16, 49, 16, 16))
        self.label_190.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_191 = QLabel(self.frame_31)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setGeometry(QRect(35, 49, 81, 16))
        self.label_191.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_18 = QPushButton(self.frame_31)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_18.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_192 = QLabel(self.frame_31)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setGeometry(QRect(287, 10, 191, 31))
        self.label_192.setFont(font5)
        self.label_192.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_193 = QLabel(self.frame_31)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setGeometry(QRect(477, 17, 75, 20))
        self.label_193.setFont(font2)
        self.label_193.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_194 = QLabel(self.frame_31)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setGeometry(QRect(354, 44, 151, 20))
        self.label_194.setFont(font2)
        self.label_194.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_195 = QLabel(self.frame_31)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setGeometry(QRect(10, 99, 291, 269))
        self.label_195.setStyleSheet(u"border-radius:5px;")
        self.label_195.setPixmap(QPixmap(u"PropImages/Thane/Thane-Balkum.Thane.west/Thane-1.jpg"))
        self.label_195.setScaledContents(True)
        self.line_49 = QFrame(self.frame_31)
        self.line_49.setObjectName(u"line_49")
        self.line_49.setGeometry(QRect(307, 99, 16, 269))
        self.line_49.setFrameShape(QFrame.Shape.VLine)
        self.line_49.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_196 = QLabel(self.frame_31)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setGeometry(QRect(377, 99, 175, 44))
        self.label_196.setFont(font6)
        self.label_196.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_50 = QFrame(self.frame_31)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setGeometry(QRect(316, 185, 274, 16))
        self.line_50.setFrameShape(QFrame.Shape.HLine)
        self.line_50.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_197 = QLabel(self.frame_31)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setGeometry(QRect(377, 194, 120, 44))
        self.label_197.setFont(font6)
        self.label_197.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_198 = QLabel(self.frame_31)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setGeometry(QRect(377, 290, 152, 66))
        self.label_198.setFont(font6)
        self.label_198.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_199 = QLabel(self.frame_31)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setGeometry(QRect(10, 75, 410, 18))
        self.label_199.setFont(font7)
        self.label_199.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_51 = QFrame(self.frame_31)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setGeometry(QRect(316, 279, 274, 16))
        self.line_51.setFrameShape(QFrame.Shape.HLine)
        self.line_51.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.frame_31, 0, 0, 1, 1)

        self.frame_36 = QFrame(self.frame_30)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFont(font3)
        self.frame_36.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_36.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
        self.label_244 = QLabel(self.frame_36)
        self.label_244.setObjectName(u"label_244")
        self.label_244.setGeometry(QRect(13, 10, 231, 33))
        self.label_244.setFont(font4)
        self.label_244.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_245 = QLabel(self.frame_36)
        self.label_245.setObjectName(u"label_245")
        self.label_245.setGeometry(QRect(16, 49, 16, 16))
        self.label_245.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_246 = QLabel(self.frame_36)
        self.label_246.setObjectName(u"label_246")
        self.label_246.setGeometry(QRect(35, 49, 71, 16))
        self.label_246.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_23 = QPushButton(self.frame_36)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_23.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_247 = QLabel(self.frame_36)
        self.label_247.setObjectName(u"label_247")
        self.label_247.setGeometry(QRect(280, 10, 201, 31))
        self.label_247.setFont(font5)
        self.label_247.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_248 = QLabel(self.frame_36)
        self.label_248.setObjectName(u"label_248")
        self.label_248.setGeometry(QRect(484, 17, 75, 20))
        self.label_248.setFont(font2)
        self.label_248.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_249 = QLabel(self.frame_36)
        self.label_249.setObjectName(u"label_249")
        self.label_249.setGeometry(QRect(354, 44, 151, 20))
        self.label_249.setFont(font2)
        self.label_249.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_250 = QLabel(self.frame_36)
        self.label_250.setObjectName(u"label_250")
        self.label_250.setGeometry(QRect(10, 99, 291, 269))
        self.label_250.setStyleSheet(u"border-radius:5px;")
        self.label_250.setPixmap(QPixmap(u"PropImages/WhatsApp Image 2024-07-05 at 20.01.08_33b1ab10.jpg"))
        self.label_250.setScaledContents(True)
        self.line_64 = QFrame(self.frame_36)
        self.line_64.setObjectName(u"line_64")
        self.line_64.setGeometry(QRect(307, 99, 16, 269))
        self.line_64.setFrameShape(QFrame.Shape.VLine)
        self.line_64.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_251 = QLabel(self.frame_36)
        self.label_251.setObjectName(u"label_251")
        self.label_251.setGeometry(QRect(377, 99, 175, 44))
        self.label_251.setFont(font6)
        self.label_251.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_65 = QFrame(self.frame_36)
        self.line_65.setObjectName(u"line_65")
        self.line_65.setGeometry(QRect(316, 185, 274, 16))
        self.line_65.setFrameShape(QFrame.Shape.HLine)
        self.line_65.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_252 = QLabel(self.frame_36)
        self.label_252.setObjectName(u"label_252")
        self.label_252.setGeometry(QRect(377, 194, 120, 44))
        self.label_252.setFont(font6)
        self.label_252.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_253 = QLabel(self.frame_36)
        self.label_253.setObjectName(u"label_253")
        self.label_253.setGeometry(QRect(377, 292, 152, 66))
        self.label_253.setFont(font6)
        self.label_253.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_254 = QLabel(self.frame_36)
        self.label_254.setObjectName(u"label_254")
        self.label_254.setGeometry(QRect(10, 75, 410, 18))
        self.label_254.setFont(font7)
        self.label_254.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_66 = QFrame(self.frame_36)
        self.line_66.setObjectName(u"line_66")
        self.line_66.setGeometry(QRect(316, 279, 274, 16))
        self.line_66.setFrameShape(QFrame.Shape.HLine)
        self.line_66.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.frame_36, 2, 1, 1, 1)


        self.verticalLayout_37.addLayout(self.gridLayout_3)


        self.horizontalLayout_13.addWidget(self.frame_30)


        self.verticalLayout_18.addWidget(self.frame_6)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_19.addWidget(self.scrollArea_6)


        self.verticalLayout_17.addWidget(self.widget_6)

        self.stackedWidget_3.addWidget(self.dashboardpage)
        self.meassagespage = QWidget()
        self.meassagespage.setObjectName(u"meassagespage")
        self.verticalLayout_2 = QVBoxLayout(self.meassagespage)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObje