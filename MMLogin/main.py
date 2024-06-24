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
        self.reset_pass_page_widget = ResetPassWidget()

        self.central_widget.addWidget(self.login_page_widget)
        self.central_widget.addWidget(self.signup_page_widget)
        self.central_widget.addWidget(self.forget_pass_page_widget)
        self.central_widget.addWidget(self.reset_pass_page_widget)

        self.central_widget.setCurrentWidget(self.login_page_widget)

        self.forget_pass_page_widget.ui.verify_pushbutton.clicked.connect(self.show_reset_pass_page)
        self.login_page_widget.ui.signupbutton.clicked.connect(self.show_signup_page)
        self.signup_page_widget.ui.backbutton.clicked.connect(self.show_login_page)
        self.login_page_widget.ui.forgetpassbutton.clicked.connect(self.show_forget_pass_page)
        self.forget_pass_page_widget.ui.backbutton.clicked.connect(self.show_login_page)
        self.reset_pass_page_widget.ui.backbutton.clicked.connect(self.show_login_page)

        layout = QVBoxLayout()
        layout.addWidget(self.central_widget)
        self.setLayout(layout)

    def show_login_page(self):
        print("Switching to Login Page")
        self.central_widget.setCurrentWidget(self.login_page_widget)
        self.update_window_title("Login Page")

    def show_signup_page(self):
        print("Switching to Signup Page")
        self.central_widget.setCurrentWidget(self.signup_page_widget)
        self.update_window_title("Signup Page")

    def show_reset_pass_page(self):
        pass
        # print("Verify button clicked, switching to Reset Password Page.")
        # self.central_widget.setCurrentWidget(self.reset_pass_page_widget)
        # self.update_window_title("Reset Password Page")
        # self.print_current_widget()

    def show_forget_pass_page(self):
        print("Switching to Forget Password Page")
        self.central_widget.setCurrentWidget(self.forget_pass_page_widget)
        self.update_window_title("Forget Password Page")

    def update_window_title(self, title):
        print(f"Switching to {title}")

    def print_current_widget(self):
        current_widget = self.central_widget.currentWidget()
        print(f"Current widget is: {type(current_widget).__name__}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowFlags(Qt.FramelessWindowHint)
    window.setAttribute(Qt.WA_TranslucentBackground)
    window.show()
    sys.exit(app.exec())
