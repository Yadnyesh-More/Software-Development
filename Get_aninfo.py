# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PropertyBBUIILGKGb.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Frame(object):
    def hideFrame(self):
        self.frame.hide()
        pass
    def setupUi(self, Frame):
        if not get_an_info_frame.objectName():
            get_an_info_frame.setObjectName(u"get_an_info_frame")
        get_an_info_frame.resize(700, 400)
        get_an_info_frame.setMinimumSize(QSize(700, 400))
        get_an_info_frame.setMaximumSize(QSize(700, 400))
        self.frame = QFrame(get_an_info_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 700, 400))
        font = QFont()
        font.setFamilies([u"Sitka Banner Semibold"])
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"border:3px solid rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(371, 52, 261, 61))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"border:none;\n"
"color:white")
        self.user_nm = QLineEdit(self.frame)
        self.user_nm.setObjectName(u"user_nm")
        self.user_nm.setGeometry(QRect(371, 167, 291, 31))
        font2 = QFont()
        font2.setPointSize(11)
        self.user_nm.setFont(font2)
        self.user_nm.setStyleSheet(u"QLineEdit{\n"
"border:none;\n"
"background-color:white;\n"
"border-radius:0px;\n"
"}\n"
"QLineEdit:hover{\n"
"border-bottom:2px solid rgb(18, 140, 126);\n"
"}")
        self.user_nm.setCursorPosition(0)
        self.info_username = QLabel(self.frame)
        self.info_username.setObjectName(u"info_username")
        self.info_username.setGeometry(QRect(371, 146, 101, 18))
        font3 = QFont()
        font3.setPointSize(10)
        self.info_username.setFont(font3)
        self.info_username.setStyleSheet(u"border:none;\n"
"color:rgb(18, 140, 126);")
        self.info_contact = QLabel(self.frame)
        self.info_contact.setObjectName(u"info_contact")
        self.info_contact.setGeometry(QRect(370, 224, 101, 18))
        self.info_contact.setFont(font3)
        self.info_contact.setStyleSheet(u"border:none;\n"
"color:rgb(18, 140, 126);")
        self.cntct_num = QLineEdit(self.frame)
        self.cntct_num.setObjectName(u"cntct_num")
        self.cntct_num.setGeometry(QRect(371, 245, 291, 31))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(False)
        self.cntct_num.setFont(font4)
        self.cntct_num.setStyleSheet(u"QLineEdit{\n"
"border:none;\n"
"background-color:white;\n"
"border-radius:0px;\n"
"}\n"
"QLineEdit:hover{\n"
"border-bottom:2px solid rgb(18, 140, 126);\n"
"}")
        self.cntct_num.setMaxLength(10)
        self.cntct_num.setCursorPosition(0)
        self.snd_email_img = QPushButton(self.frame)
        self.snd_email_img.setObjectName(u"snd_email_img")
        self.snd_email_img.setGeometry(QRect(433, 319, 170, 31))
        font5 = QFont()
        font5.setPointSize(12)
        self.snd_email_img.setFont(font5)
        self.snd_email_img.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(18, 140, 126);\n"
"border:none;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(18, 140, 126);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.snd_email_img.setCheckable(True)
        self.info_close = QPushButton(self.frame)
        self.info_close.setObjectName(u"info_close")
        self.info_close.setGeometry(QRect(674, 4, 20, 20))
        font6 = QFont()
        font6.setPointSize(13)
        self.info_close.setFont(font6)
        self.info_close.setStyleSheet(u"border:none; color:white;")
        self.info_close.setCheckable(True)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 351, 371))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.retranslateUi(get_an_info_frame)
        self.info_close.toggled.connect(get_an_info_frame.close)
        

        QMetaObject.connectSlotsByName(get_an_info_frame)
    # setupUi

    def retranslateUi(self, get_an_info_frame):
        get_an_info_frame.setWindowTitle(QCoreApplication.translate("get_an_info_frame", u"get_an_info_frame", None))
        self.label_6.setText(QCoreApplication.translate("get_an_info_frame", u"<html><head/><body><p>Get personalized assistance <br/>from our experts for <span style=\" font-weight:700; color:#128c7e;\">FREE</span></p></body></html>", None))
        self.user_nm.setText("")
        self.user_nm.setPlaceholderText("")
        self.info_username.setText(QCoreApplication.translate("get_an_info_frame", u"User Name", None))
        self.info_contact.setText(QCoreApplication.translate("get_an_info_frame", u"Phone Number", None))
        self.cntct_num.setText("")
        self.cntct_num.setPlaceholderText("")
        self.snd_email_img.setText(QCoreApplication.translate("get_an_info_frame", u"Connect", None))
        self.info_close.setText(QCoreApplication.translate("get_an_info_frame", u"x", None))
    # retranslateUi

if __name__ == "__main__":
        import sys
        app = QApplication(sys.argv)
        get_an_info_frame = QWidget()
        ui = Ui_Frame()
        ui.setupUi(get_an_info_frame)
        get_an_info_frame.show()
        sys.exit(app.exec())
        