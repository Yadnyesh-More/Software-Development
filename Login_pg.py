from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel, QLineEdit, QPushButton,QMessageBox)
import pymysql as psql 
import re

class Ui_Dialog(object):
    # def __init__(self):
    #     self.new_email_entry = None
    def mysql(self):
        self.a = psql.connect(host='localhost',user="root",password="root",charset='utf8',port=3307,database="test")
        self.curr = self.a.cursor()


    def backen_pymysql(self): # Yadynesh tu ithun code kr pymysql cha hya function mdhe 
        self.mysql()
        print("start")
        print("start loop")
        #self.curr.execute("show databases")
        self.curr.execute("create table if not exists users (email varchar(50) not null,password varchar(20) not null)")
        self.curr.execute("insert into users values(%s,%s)",(self.new_email_entry.text(),self.confirm_password_entry.text()))
        self.curr.execute("select * from users")
        for i in self.curr:
            print(i)
        
        self.a.commit()
        


    def sign_up(self):
        self.frame.deleteLater()
        self.setup_sign_up_frame()
        
    def rgister_button_show_nm(self):
        if (self.new_email_entry.text() == "" or
            self.new_password_entry.text() == "" or
            self.confirm_password_entry.text() == ""):
            QMessageBox.critical(self.Dialog, "Error", "Please fill all the fields")
            
        else:
            pat = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
            if pat.match(self.new_email_entry.text()):
                print("Valid Email")
                if self.confirm_password_entry.text() != self.new_password_entry.text():
                    QMessageBox.warning(self.Dialog, "Error", "Password and confirm password don't match")

                else:
                    self.mysql()
                    q = "SELECT * FROM users WHERE email = %s"
                    self.curr.execute(q, (self.new_email_entry.text()))
                    self.result = self.curr.fetchone()
                    if self.result is not None:
                        self.login_up_pop_up = QMessageBox.critical(None,"Result", "Account exist, Please SignIn! ")

                    else:
                        QMessageBox.information(self.Dialog, "Sign Up", "Sign Up is successful")
                        print(self.new_email_entry.text())
                        print(self.new_password_entry.text())
                        print(self.confirm_password_entry.text())
                        self.backen_pymysql()
            else:
                self.login_pop_up = QMessageBox.critical(None, "Error", "Please Enter Valid Email !!")

        
    def login_button_show_nm(self):
        if self.Email_entry == " " and self.Password_entry == " ":
            self.login_pop_up = QMessageBox.critical(None, "Login", "Login is unsuccesfull plzz Enter")
        else:
            self.mysql()
            q = "SELECT * FROM users WHERE email = %s and password = %s"
            self.curr.execute(q, (self.Email_entry.text(),self.Password_entry.text()))
            self.result = self.curr.fetchone()
            if self.result is None:
                self.login_up_pop_up = QMessageBox.critical(None,"Result", "Account not exist, Please Create Account!")
            else:    
                self.login_up_pop_up = QMessageBox.information(None, "Log in", "Login is succesfull")
                print(self.Email_entry.text())
                print(self.Password_entry.text())
                #self.backen_pymysql()
        
        
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
