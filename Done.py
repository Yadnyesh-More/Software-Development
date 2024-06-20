# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerDbgqMp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import (QFont, QCursor)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit, QPushButton)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(346, 496)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 290, 101, 31))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 110, 191, 31))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 30, 81, 31))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 220, 101, 16))
        self.label_2.setCursor(QCursor(Qt.PointingHandCursor))  # Set cursor to pointing hand
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(90, 180, 191, 31))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 460, 101, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Log In", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Email", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Log In", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"forgt password ?", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Sign Up", None))
    # retranslateUi

class Ui_ForgetPass(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(346, 496)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 330, 101, 31))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 120, 221, 41))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 30, 121, 41))
        font = QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(60, 230, 41, 51))
        self.lineEdit_2.setStyleSheet(u"*{\n"
"border-radius:8px\n"
"}")
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(120, 230, 41, 51))
        self.lineEdit_3.setStyleSheet(u"*{\n"
"border-radius:8px\n"
"}")
        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(180, 230, 41, 51))
        self.lineEdit_4.setStyleSheet(u"*{\n"
"border-radius:8px\n"
"}")
        self.lineEdit_5 = QLineEdit(Dialog)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(240, 230, 41, 51))
        self.lineEdit_5.setStyleSheet(u"*{\n"
"border-radius:8px\n"
"}")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 200, 91, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Verify", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter you phone no.", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Forget Password ", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Enter otp here  \u2192", None))
    # retranslateUi

class Ui_SignUpDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(346, 496)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 320, 101, 31))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 110, 191, 31))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 40, 81, 31))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(80, 180, 191, 31))
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(80, 250, 191, 31))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 111, 16))
        font1 = QFont()
        font1.setPointSize(11)
        self.label_2.setFont(font1)
        self.label_2.setCursor(QCursor(Qt.PointingHandCursor))  # Set cursor to pointing hand

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Register", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Email", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Sign Up", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"Confirm password", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u2190 Back to login ", None))
    # retranslateUi

class Ui_ChangeNewPass(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(346, 333)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 260, 111, 31))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 120, 221, 41))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 141, 41))
        font = QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(60, 190, 221, 41))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 90, 271, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Change Password ", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"New password", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Reset Your Password", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Re-enter new password", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Please choose a new password to finish signing in ", None))
    # retranslateUi

class MainDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(MainDialog, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.open_signup_dialog)
        self.label_2.mousePressEvent = self.open_forget_pass_dialog
    
    def open_signup_dialog(self):
        self.signup_dialog = SignUpDialog()
        self.signup_dialog.show()
        self.close()

    def open_forget_pass_dialog(self, event):
        self.forget_pass_dialog = ForgetPass()
        self.forget_pass_dialog.show()
        self.close()

class SignUpDialog(QDialog):
    def __init__(self):
        super(SignUpDialog, self).__init__()
        self.ui = Ui_SignUpDialog()
        self.ui.setupUi(self)
        self.ui.label_2.mousePressEvent = self.back_to_login

    def back_to_login(self, event):
        self.main_dialog = MainDialog()
        self.main_dialog.show()
        self.close()

class ForgetPass(QDialog):
    def __init__(self):
        super(ForgetPass, self).__init__()
        self.ui = Ui_ForgetPass()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_change_pass_dialog)

    def open_change_pass_dialog(self):
        self.change_pass_dialog = ChangeNewPass()
        self.change_pass_dialog.show()
        self.close()

class ChangeNewPass(QDialog):
    def __init__(self):
        super(ChangeNewPass, self).__init__()
        self.ui = Ui_ChangeNewPass()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.back_to_login)

    def back_to_login(self):
        self.main_dialog = MainDialog()
        self.main_dialog.show()
        self.close()

if __name__ == "__main__":
    app = QApplication([])
    main_dialog = MainDialog()
    main_dialog.show()
    app.exec()
