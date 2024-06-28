from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout ,QMessageBox
import sys
from ui_forgetpasspg import Ui_MainWindow as ForgetPassPage
from ui_loginpg import Ui_MainWindow as LoginPage
from ui_resetpasspg import Ui_MainWindow as ResetPassPage
from ui_signuppg import Ui_MainWindow as SignupPage
import pymysql as psql
import re
import random
from twilio.rest import Client
import smtplib
from email.message import EmailMessage



class LoginWidget(QWidget):
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)
        self.ui = LoginPage()
        temp_mainwindow = QMainWindow()
        self.ui.setupUi(temp_mainwindow)
        central_widget = temp_mainwindow.centralWidget()
        layout = QVBoxLayout()
        layout.addWidget(central_widget)
        self.setLayout(layout)

class SignupWidget(QWidget):
    def __init__(self, parent=None):
        super(SignupWidget, self).__init__(parent)
        self.ui = SignupPage()
        temp_mainwindow = QMainWindow()
        self.ui.setupUi(temp_mainwindow)
        central_widget = temp_mainwindow.centralWidget()
        layout = QVBoxLayout()
        layout.addWidget(central_widget)
        self.setLayout(layout)

class ForgetPassWidget(QWidget):

    def __init__(self, parent=None):

        super(ForgetPassWidget, self).__init__(parent)

        self.ui = ForgetPassPage()

        temp_mainwindow = QMainWindow()

        self.ui.setupUi(temp_mainwindow)

        central_widget = temp_mainwindow.centralWidget()

        layout = QVBoxLayout()

        layout.addWidget(central_widget)

        self.setLayout(layout)
class ResetPassWidget(QWidget):
    def __init__(self, parent=None):
        super(ResetPassWidget, self).__init__(parent)
        self.ui = ResetPassPage()
        temp_mainwindow = QMainWindow()
        self.ui.setupUi(temp_mainwindow)
        central_widget = temp_mainwindow.centralWidget()
        layout = QVBoxLayout()
        layout.addWidget(central_widget)
        self.setLayout(layout)

class MainWindow(QWidget):

    def __init__(self):

        super(MainWindow, self).__init__()

        self.central_widget = QStackedWidget()


        self.login_page_widget = LoginWidget()

        self.signup_page_widget = SignupWidget()

        self.forget_pass_page_widget = ForgetPassWidget()

        self.reset_pass_page_widget = ResetPassWidget()  # Add this line


        self.central_widget.addWidget(self.login_page_widget)

        self.central_widget.addWidget(self.signup_page_widget)

        self.central_widget.addWidget(self.forget_pass_page_widget)

        self.central_widget.addWidget(self.reset_pass_page_widget)  # Add this line


        self.central_widget.setCurrentWidget(self.login_page_widget)


        self.forget_pass_page_widget.ui.loginbutton.clicked.connect(self.show_reset_pass_page)

        self.login_page_widget.ui.signupbutton.clicked.connect(self.show_signup_page)

        self.signup_page_widget.ui.backbutton.clicked.connect(self.login_page)

        self.login_page_widget.ui.forgetpassbutton.clicked.connect(self.show_forget_pass_page)

        self.forget_pass_page_widget.ui.backbutton.clicked.connect(self.login_page) # this are  moving to the reset page 
        
        self.reset_pass_page_widget.ui.backbutton.clicked.connect(self.show_forget_pass_page) # Newly addes by the sanki
        
        self.reset_pass_page_widget.ui.loginbutton.clicked.connect(self.show_login_page)
        
        self.signup_page_widget.ui.sig_up_close_bar.clicked.connect(self.window_closer)
        
        self.login_page_widget.ui.login_window_closer.clicked.connect(self.window_closer)
        
        self.login_page_widget.ui.loginbutton.clicked.connect(self.for_login) # This are calling the login function after clicking the login button

        self.signup_page_widget.ui.alrdy_button.clicked.connect(self.login_page) # done change
        
        self.signup_page_widget.ui.register_button.clicked.connect(self.for_signup) # This are calling the signup function after click the signup page

        layout = QVBoxLayout()

        layout.addWidget(self.central_widget)

        self.setLayout(layout)

    def mysql(self):
        self.a = psql.connect(host="localhost",port=3306,user="root",password="root",charset="utf8")
        self.curr = self.a.cursor()
        self.curr.execute("create database if not exists MIddleman")
        self.curr.execute("use MIddleman")

    def login_page(self):
        self.central_widget.setCurrentWidget(self.login_page_widget)

        self.update_window_title("Login Page")


    def show_login_page(self):
        password = self.reset_pass_page_widget.ui.email_entry.text()
        re_password = self.reset_pass_page_widget.ui.email_entry_2.text()
        print(password,re_password)
        if password == re_password:
            self.mysql()
            q = "update login set password = %s where email_id = %s"
            self.curr.execute(q,(re_password,self.login_email))
            self.a.commit()
            QMessageBox.information(None,"RESULT","Your Password Change Sucessfully !!! ")
            self.central_widget.setCurrentWidget(self.login_page_widget)

            self.update_window_title("Login Page")
        else:
            print("nahi rhe bhava nit bagh ")


    def show_signup_page(self):

        self.central_widget.setCurrentWidget(self.signup_page_widget)

        self.update_window_title("Signup Page")


    def show_reset_pass_page(self):
        self.phone = self.forget_pass_page_widget.ui.phone_entry.text() 
        self.otp_1 = self.forget_pass_page_widget.ui.otp_1.text()
        self.otp_2 = self.forget_pass_page_widget.ui.otp_2.text()
        self.otp_3 = self.forget_pass_page_widget.ui.otp_3.text()
        self.otp_4 = self.forget_pass_page_widget.ui.otp_4.text()

        print(self.forget_pass_page_widget.ui.phone_entry.text())
        if not self.phone :
            QMessageBox.warning(None,"Error","Enter Mobile No !!! ")
            #self.central_widget.setCurrentWidget(self.reset_pass_page_widget)

            #self.update_window_title("Reset Password Page")
        else:
            phone = "+91"+str(self.phone)
            #b = True
            global user_otp
            global send_otp
            if self.phone:
                Pat = re.compile("(0|91)?[6-9][0-9]{9}")
                pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

                if(re.fullmatch(Pat,str(self.phone))): 
                    account_sid = "ACbfc61c85346b4518d9d030c896509b26"
                    auth_token = "386a826cd361e4bdd5e5648fadbfb187"
                    print("Otp sent")
                    #b = False
                    #print(user_otp)
                    if self.otp_1 == '' and self.otp_2 == '' and self.otp_3 == '' and self.otp_4 == '':
                        print("hello")
                        send_otp = random.randint(1000,9999)
                        client = Client(account_sid,auth_token)
                        msg = client.messages.create(

                            body = f"Your OTP is {send_otp}",
                            from_= "+13613154011",
                            to = phone
                        )
                        print(send_otp)
                    else:
                        user_otp = self.otp_1+self.otp_2+self.otp_3+self.otp_4
                        print(str(user_otp))
                        if str(user_otp) == str(send_otp):
                            self.mysql()
                            q = "update login set phone_no = %s where email_id=%s "
                            self.curr.execute(q,(self.phone,self.login_email))
                            self.a.commit()
                            
                            self.central_widget.setCurrentWidget(self.reset_pass_page_widget)

                            self.update_window_title("Reset Password Page")

                        else:
                            print("Errorrrrrrrrrrrrrrrrrrrrrrr")
                #else:
                #    QMessageBox.warning(None,"Error","Enter Valid No !!! ")

                if (re.fullmatch(pattern,str(self.phone))):
                    print("sucess")
                    if self.otp_1 == '' and self.otp_2 == '' and self.otp_3 == '' and self.otp_4 == '':
                        print("hello")
                        send_otp = random.randint(1000,9999)
                        server = smtplib.SMTP("smtp.gmail.com",587)
                        server.starttls()

                        from_mail = "middleman3701@gmail.com"
                        server.login(from_mail, "wtkh syvj zptd elfa")
                        to_mail = self.phone

                        msg = EmailMessage()
                        msg['Subject'] = "OTP Verification"
                        msg['From'] = from_mail
                        msg['To'] = to_mail
                        msg.set_content(f"Your OTP is : {send_otp}")

                        server.send_message(msg)

                        print("Email Sent")
                        print(send_otp)
                    else:
                        user_otp = self.otp_1+self.otp_2+self.otp_3+self.otp_4
                        if str(user_otp) == str(send_otp):
                                self.mysql()
                                #q = "update login set phone_no = %s where email_id=%s "
                                #self.curr.execute(q,(self.phone,self.login_email))
                                #self.a.commit()
                                
                                self.central_widget.setCurrentWidget(self.reset_pass_page_widget)

                                self.update_window_title("Reset Password Page") 
                        else:
                                print("Errorrrrrrrrrrrrrrrrrrrrrrr")
                else:
                    print("error")

        


    def show_forget_pass_page(self):
        self.login_email = self.login_page_widget.ui.email_entry.text() 
        if self.login_email == "":
            QMessageBox.warning(None,"Error","please Enter Email !! ")
        else:
            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if(re.fullmatch(pattern, self.login_email)):
                self.mysql()
                q1 = "select * from login where Email_id = %s"
                self.curr.execute(q1,(self.login_email))
                self.result1 = self.curr.fetchone()
                if self.result1 is None :
                    QMessageBox.warning(None,"Error","Entered email is not register !! ")
                else:
                    self.central_widget.setCurrentWidget(self.forget_pass_page_widget)

                    self.update_window_title("Forget Password Page")
            else:
                QMessageBox.warning(None,"Error","please Enter Email in right format !!")


    def update_window_title(self, title):

        print(f"Switching to {title}")


    def window_closer(self):

        print("Verify button clicked, closing all windows.")

        self.closeAllWindows()  # Add this line

    def for_login(self): # after login button clicked this function run
        self.mysql()
        print("Login is succesfull")
        self.login_email = self.login_page_widget.ui.email_entry.text()
        self.login_pass = self.login_page_widget.ui.password_entry.text()
        print(self.login_page_widget.ui.email_entry.text())
        print(self.login_page_widget.ui.password_entry.text())
        if self.login_email == "" or self.login_pass == "":
            QMessageBox.warning(None,"Error","please Enter Text !! ")
        else:
            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if(re.fullmatch(pattern, self.login_email)):
                q1 = "select * from login where Email_id = %s and password = %s"
                self.curr.execute(q1,(self.login_email,self.login_pass))
                self.result1 = self.curr.fetchone()
                if self.result1 is None :
                    QMessageBox.warning(None,"Error","Entered email is not register !! ")
                else:
                    QMessageBox.information(None,"Result","Login sucessful ")
            else:
                QMessageBox.warning(None,"Error","please Enter Email in right format !!") 


        #window.close()
        

    def for_signup(self): # After clicking the sign_up button this function runs

        self.mysql()
        print("Sign Up is Succesfull")
        self.email = self.signup_page_widget.ui.email_entry.text()
        self.password = self.signup_page_widget.ui.password_entry.text()
        self.confirm_pass = self.signup_page_widget.ui.password_entry_2.text()
        print(self.signup_page_widget.ui.email_entry.text())
        print(self.signup_page_widget.ui.password_entry.text())
        print(self.signup_page_widget.ui.password_entry_2.text())
        self.curr.execute("create table if not exists login(Email_id varchar(30),password varchar(30),phone_no varchar(10))")
        
        if self.email == "" or self.password == "" or self.confirm_pass == "":
            QMessageBox.warning(None,"Error","please Enter Text !! ")
        else:
            q = "SELECT * FROM login WHERE email_id = %s"
            self.curr.execute(q, (self.email))
            self.result = self.curr.fetchone()
            if self.result is not None:
                QMessageBox.warning(None, "Result", "Account exists, Please Sign In!")
            else:
                if self.password == self.confirm_pass:
                    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                    if(re.fullmatch(pattern, self.email)):
                        #verify email
                        self.curr.execute("insert into login(Email_id,password) values(%s,%s)",(self.email,self.confirm_pass))
                        self.a.commit()
                        QMessageBox.information(None,"Result","Signup Succesfully , Please Login ")
                        self.central_widget.setCurrentWidget(self.login_page_widget)
                        self.update_window_title("Login Page")
                    else:
                        QMessageBox.warning(None,"Error","please Enter Email in right format !!") 
                else:
                    QMessageBox.warning(None,"Error","please Enter same password in both entry !!") 


    def closeAllWindows(self):

        for window in QApplication.topLevelWidgets():

            window.close()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()

    window.setWindowFlags(Qt.FramelessWindowHint)

    window.setAttribute(Qt.WA_TranslucentBackground)

    window.show()

    sys.exit(app.exec())

