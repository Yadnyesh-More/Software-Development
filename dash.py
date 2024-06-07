# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceQkzczm.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QToolBox, QVBoxLayout, QWidget)
# import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 421)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"backgrount-color:rgb(24,24,36);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slide_menu_container = QFrame(self.centralwidget)
        self.slide_menu_container.setObjectName(u"slide_menu_container")
        self.slide_menu_container.setMaximumSize(QSize(200, 16777215))
        self.slide_menu_container.setStyleSheet(u"background-color:rgb(9,5,13);\n"
"")
        self.slide_menu_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.slide_menu_container.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.slide_menu_container)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.slide_menu = QFrame(self.slide_menu_container)
        self.slide_menu.setObjectName(u"slide_menu")
        self.slide_menu.setMinimumSize(QSize(198, 0))
        self.slide_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.slide_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.slide_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.slide_menu)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(32, 32))
        self.label_3.setMaximumSize(QSize(32, 32))
        self.label_3.setPixmap(QPixmap(u"D:\MyFiles\Dashboard\icons/briefcase.svg"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_3)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.frame_7, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_8 = QFrame(self.slide_menu)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 25, 0, 0)
        self.toolBox = QToolBox(self.frame_8)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"QToolBox{\n"
"background-color:rgb(24,24,36);\n"
"text-align:left;\n"
"}\n"
"QToolBox::tab{\n"
"border-radius:5px;\n"
"background-color:rgb(17,16,24);\n"
"text-align:left;\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 83, 138))
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_10 = QFrame(self.page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_10 = QPushButton(self.frame_10)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(20, 40))
        self.pushButton_10.setMaximumSize(QSize(16777215, 40))
        icon = QIcon()
        icon.addFile(u"D:\MyFiles\Dashboard\icons/alert-triangle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon)

        self.verticalLayout_6.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame_10)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 40))
        self.pushButton_11.setMaximumSize(QSize(16777215, 40))
        icon1 = QIcon()
        icon1.addFile(u"D:\MyFiles\Dashboard\icons/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon1)

        self.verticalLayout_6.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.frame_10)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 40))
        self.pushButton_12.setMaximumSize(QSize(16777215, 40))
        icon2 = QIcon()
        icon2.addFile(u":/icons/key.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon2)

        self.verticalLayout_6.addWidget(self.pushButton_12)


        self.verticalLayout_5.addWidget(self.frame_10, 0, Qt.AlignmentFlag.AlignTop)

        icon3 = QIcon()
        icon3.addFile(u"D:\MyFiles\Dashboard\icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page, icon3, u"Drop Menu 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 200, 266))
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_11 = QFrame(self.page_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_13 = QPushButton(self.frame_11)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(0, 40))
        self.pushButton_13.setMaximumSize(QSize(16777215, 40))
        icon4 = QIcon()
        icon4.addFile(u"D:\MyFiles\Dashboard\icons/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon4)
        self.pushButton_13.setIconSize(QSize(20, 20))

        self.verticalLayout_8.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.frame_11)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(0, 40))
        self.pushButton_14.setMaximumSize(QSize(16777215, 40))
        icon5 = QIcon()
        icon5.addFile(u":D:\MyFiles\Dashboard\icons/phone-incoming.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon5)
        self.pushButton_14.setIconSize(QSize(20, 20))

        self.verticalLayout_8.addWidget(self.pushButton_14)


        self.verticalLayout_7.addWidget(self.frame_11, 0, Qt.AlignmentFlag.AlignTop)

        self.toolBox.addItem(self.page_2, icon3, u"Drop Menu 2")

        self.horizontalLayout_11.addWidget(self.toolBox)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.slide_menu)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.frame_9)
        self.pushButton_9.setObjectName(u"pushButton_9")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon6 = QIcon()
        icon6.addFile(u"D:\MyFiles\Dashboard\icons/external-link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon6)
        self.pushButton_9.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.pushButton_9, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_3.addWidget(self.frame_9, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_4.addWidget(self.slide_menu)


        self.horizontalLayout.addWidget(self.slide_menu_container)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main_body)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color:rgb(9,5,13);\n"
"")
        self.header_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 6, 0, 0)
        self.frame_6 = QFrame(self.header_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.frame_6)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon7 = QIcon()
        icon7.addFile(u"D:\MyFiles\Dashboard\icons/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.pushButton_8, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_2.addWidget(self.frame_6)

        self.frame = QFrame(self.header_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(132, 0))
        self.lineEdit.setStyleSheet(u"color: rgb(167, 167, 167);\n"
"border-bottom : 3px solid rgb(230,5,64)")

        self.horizontalLayout_7.addWidget(self.lineEdit, 0, Qt.AlignmentFlag.AlignLeft)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(30, 0))
        self.pushButton_7.setMaximumSize(QSize(5, 16777215))
        icon8 = QIcon()
        icon8.addFile(u"D:\MyFiles\Dashboard\icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon8)

        self.horizontalLayout_7.addWidget(self.pushButton_7, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.header_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon9 = QIcon()
        icon9.addFile(u"D:\MyFiles\Dashboard\icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon9)

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon10 = QIcon()
        icon10.addFile(u"D:\MyFiles\Dashboard\icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon10)

        self.horizontalLayout_6.addWidget(self.pushButton_5)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.header_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        icon11 = QIcon()
        icon11.addFile(u"D:\MyFiles\Dashboard\icons/arrow-down-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon11)

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon12 = QIcon()
        icon12.addFile(u"D:\MyFiles\Dashboard\icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon12)

        self.horizontalLayout_5.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon13 = QIcon()
        icon13.addFile(u"D:\MyFiles\Dashboard\icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon13)

        self.horizontalLayout_5.addWidget(self.pushButton_2)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.header_frame)

        self.main_body_contents = QFrame(self.main_body)
        self.main_body_contents.setObjectName(u"main_body_contents")
        sizePolicy.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy)
        self.main_body_contents.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.main_body_contents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(60, 60))
        self.label_5.setMaximumSize(QSize(60, 60))
        self.label_5.setStyleSheet(u"border:5px solid rgb(230,5,64);\n"
"border-radius:30px;")
        self.label_5.setPixmap(QPixmap(u"D:\MyFiles\Dashboard\icons/briefcase.svg"))
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.label_4 = QLabel(self.main_body_contents)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.main_body_contents)

        self.footer = QFrame(self.main_body)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.footer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.footer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.frame_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon14 = QIcon()
        icon14.addFile(u"D:\MyFiles\Dashboard\icons/box.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon14)

        self.horizontalLayout_8.addWidget(self.pushButton_6, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.Shape.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3.addWidget(self.size_grip, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"AI Broker", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u" Item 1", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u" Item 2", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u" Item 3", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Drop Menu 1", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u" Sub Menu", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u" Sub Menu", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Drop Menu 2", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u" Exit", None))
        self.pushButton_8.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_7.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton.setText("")
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
        self.label_5.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"AI Broker", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"version ui 3.0", None))
        self.pushButton_6.setText("")
    # retranslateUi

