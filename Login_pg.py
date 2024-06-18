# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerxCNqeW.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel, QLineEdit, QPushButton,QMessageBox)

class Ui_Dialog(object):
    # def __init__(self):
    #     self.new_email_entry = None
    def backen_pymysql(self): # Yadynesh tu ithun code kr pymysql cha hya function mdhe 
        pass
    
    def sign_up(self):
        self.frame.deleteLater()
        self.setup_sign_up_frame()
        
    def rgister_button_show_nm(self):
        if (self.new_email_entry.text() == "" or
            self.new_password_entry.text() == "" or
            self.confirm_password_entry.text() == ""):
            QMessageBox.critical(self.Dialog, "Error", "Please fill all the fields")
        else:
            if self.confirm_password_entry.text() != self.new_password_entry.text():
                QMessageBox.warning(self.Dialog, "Error", "Password and confirm password don't match")
            else:
                QMessageBox.information(self.Dialog, "Sign Up", "Sign Up is successful")
                print(self.new_email_entry.text())
                print(self.new_password_entry.text())
                print(self.confirm_password_entry.text())
                self.backen_pymysql()

        
    def login_button_show_nm(self):
        if self.Email_entry == " " and self.Password_entry == " ":
            self.login_pop_up = QMessageBox.critical(None, "Login", "Login is succesfull ")
        else:
            self.login_up_pop_up = QMessageBox.information(None, "Log in", "Login is succesfull")
            print(self.Email_entry.text())
            print(self.Password_entry.text())
            self.backen_pymysql()
        
        
    def setup_sign_up_frame(self):
        self.frame = QFrame(self.Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 300, 430))
        font = QFont()
        font.setPointSize(9)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.sign_up_label = QLabel(self.frame)
        self.sign_up_label.setObjectName(u"sign_up_label")
        self.sign_up_label.setGeometry(QRect(120, 10, 121, 41))
        font1 = QFont()
        font1.setPointSize(15)
        self.sign_up_label.setFont(font1)
        
        self.new_email_entry = QLineEdit(self.frame)
        self.new_email_entry.setObjectName(u"new_email_entry")
        self.new_email_entry.setGeometry(QRect(50, 80, 191, 31))
        # print(self.new_email_entry)
        
        self.new_password_entry = QLineEdit(self.frame)
        self.new_password_entry.setObjectName(u"new_password_entry")
        self.new_password_entry.setGeometry(QRect(50, 150, 191, 31))
        
        self.confirm_password_entry = QLineEdit(self.frame)
        self.confirm_password_entry.setObjectName(u"confirm_password_entry")
        self.confirm_password_entry.setGeometry(QRect(50, 220, 191, 31))

        self.register_button = QPushButton(self.frame)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setGeometry(QRect(110, 300, 75, 31))
        
        self.retranslate_sign_up_ui()
        self.frame.show()
        self.register_button.clicked.connect(self.rgister_button_show_nm)
        QMetaObject.connectSlotsByName(self.Dialog)

    def retranslate_sign_up_ui(self):
        self.sign_up_label.setText(QCoreApplication.translate("Dialog", u"Sign Up", None))
        self.new_email_entry.setPlaceholderText(QCoreApplication.translate("Dialog", u"Email", None))
        self.new_password_entry.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.confirm_password_entry.setPlaceholderText(QCoreApplication.translate("Dialog", u"Confirm Password", None))
        self.register_button.setText(QCoreApplication.translate("Dialog", u"Register", None))

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(338, 442)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 300, 430))
        font = QFont()
        font.setPointSize(9)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.sign_up_button = QPushButton(self.frame)
        self.sign_up_button.setObjectName(u"sign_up_button")
        self.sign_up_button.setGeometry(QRect(110, 383, 75, 31))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 10, 121, 41))
        font1 = QFont()
        font1.setPointSize(15)
        self.label.setFont(font1)
        self.Email_entry = QLineEdit(self.frame)
        self.Email_entry.setObjectName(u"Email_entry")
        self.Email_entry.setGeometry(QRect(50, 80, 191, 31))
        self.Password_entry = QLineEdit(self.frame)
        self.Password_entry.setObjectName(u"Password_entry")
        self.Password_entry.setGeometry(QRect(50, 150, 191, 31))
        self.Log_in_button = QPushButton(self.frame)
        self.Log_in_button.setObjectName(u"Log_in_button")
        self.Log_in_button.setGeometry(QRect(90, 240, 121, 31))
        self.forget_pass_label = QLabel(self.frame)
        self.forget_pass_label.setObjectName(u"forget_pass_label")
        self.forget_pass_label.setGeometry(QRect(160, 190, 101, 16))

                
        self.Log_in_button.clicked.connect(self.login_button_show_nm)
        self.sign_up_button.clicked.connect(self.sign_up)
        # self.show_data()
        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.sign_up_button.setText(QCoreApplication.translate("Dialog", u"Sign Up", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Log In", None))
        self.Email_entry.setPlaceholderText(QCoreApplication.translate("Dialog", u"Email", None))
        self.Password_entry.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.Log_in_button.setText(QCoreApplication.translate("Dialog", u"Log In", None))
        self.forget_pass_label.setText(QCoreApplication.translate("Dialog", u"forget Password ?", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
