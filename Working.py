from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout
import sys
from ui_forgetpasspg import Ui_MainWindow as ForgetPassPage
from ui_loginpg import Ui_MainWindow as LoginPage
from ui_resetpasspg import Ui_MainWindow as ResetPassPage
from ui_signuppg import Ui_MainWindow as SignupPage

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

        self.signup_page_widget.ui.backbutton.clicked.connect(self.show_login_page)

        self.login_page_widget.ui.forgetpassbutton.clicked.connect(self.show_forget_pass_page)

        self.forget_pass_page_widget.ui.backbutton.clicked.connect(self.show_login_page) # this are  moving to the reset page 
        
        self.reset_pass_page_widget.ui.backbutton.clicked.connect(self.show_forget_pass_page) # Newly addes by the sanki
        
        self.reset_pass_page_widget.ui.loginbutton.clicked.connect(self.show_login_page)
        
        self.signup_page_widget.ui.sig_up_close_bar.clicked.connect(self.window_closer)
        
        self.login_page_widget.ui.login_window_closer.clicked.connect(self.window_closer)
        
        self.login_page_widget.ui.loginbutton.clicked.connect(self.for_login) # This are calling the login function after clicking the login button

        self.signup_page_widget.ui.signupbutton.clicked.connect(self.show_login_page)
        
        self.signup_page_widget.ui.register_button.clicked.connect(self.for_signup) # This are calling the signup function after click the signup page

        layout = QVBoxLayout()

        layout.addWidget(self.central_widget)

        self.setLayout(layout)


    def show_login_page(self):

        self.central_widget.setCurrentWidget(self.login_page_widget)

        self.update_window_title("Login Page")


    def show_signup_page(self):

        self.central_widget.setCurrentWidget(self.signup_page_widget)

        self.update_window_title("Signup Page")


    def show_reset_pass_page(self):

        self.central_widget.setCurrentWidget(self.reset_pass_page_widget)

        self.update_window_title("Reset Password Page")
        


    def show_forget_pass_page(self):

        self.central_widget.setCurrentWidget(self.forget_pass_page_widget)

        self.update_window_title("Forget Password Page")


    def update_window_title(self, title):

        print(f"Switching to {title}")


    def window_closer(self):

        print("Verify button clicked, closing all windows.")

        self.closeAllWindows()  # Add this line
    def for_login(self): # after login button clicked this function run
        print("Login is succesfull")
        window.close()
        pass
    def for_signup(self): # After clicking the sign_up button this function runs
        print("Sign Up is Succesfull")
        print(self.signup_page_widget.ui.email_entry.text())
        
        pass

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