import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QPushButton

# Import the generated UI classes
from ui_forgetpasspg import Ui_MainWindow as ForgetPassPage
from ui_loginpg import Ui_MainWindow as LoginPage
from ui_resetpasspg import Ui_MainWindow as ResetPassPage
from ui_signuppg import Ui_MainWindow as SignupPage

class LoginWidget(QWidget):
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)
        self.ui = LoginPage()
        
        # Create a temporary QMainWindow
        temp_mainwindow = QMainWindow()
        self.ui.setupUi(temp_mainwindow)
        
        # Extract the central widget
        central_widget = temp_mainwindow.centralWidget()
        
        # Set the layout of the QWidget to that of the QMainWindow
        layout = QVBoxLayout()
        layout.addWidget(central_widget)
        self.setLayout(layout)

class SignupWidget(QWidget):
    def __init__(self, parent=None):
        super(SignupWidget, self).__init__(parent)
        self.ui = SignupPage()
        
        # Create a temporary QMainWindow
        temp_mainwindow = QMainWindow()
        self.ui.setupUi(temp_mainwindow)
        
        # Extract the central widget
        central_widget = temp_mainwindow.centralWidget()
        
        # Set the layout of the QWidget to that of the QMainWindow
        layout = QVBoxLayout()
        layout.addWidget(central_widget)
        self.setLayout(layout)

class ForgetPassWidget(QWidget):
    def __init__(self, parent=None):
        super(ForgetPassWidget, self).__init__(parent)
        self.ui = ForgetPassPage()
        
        # Create a temporary QMainWindow
        temp_mainwindow = QMainWindow()
        self.ui.setupUi(temp_mainwindow)
        
        # Extract the central widget
        central_widget = temp_mainwindow.centralWidget()
        
        # Set the layout of the QWidget to that of the QMainWindow
        layout = QVBoxLayout()
        layout.addWidget(central_widget)
        self.setLayout(layout)

class ResetPassWidget(QWidget):
    def __init__(self, parent=None):
        super(ResetPassWidget, self).__init__(parent)
        self.ui = ResetPassPage()
        
        # Create a temporary QMainWindow
        temp_mainwindow = QMainWindow()
        self.ui.setupUi(temp_mainwindow)
        
        
        # Extract the central widget
        central_widget = temp_mainwindow.centralWidget()
        
        # Set the layout of the QWidget to that of the QMainWindow
        layout = QVBoxLayout()
        layout.addWidget(central_widget)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # Make the window frameless
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        # Create instances of the widgets
        self.login_page_widget = LoginWidget()
        self.signup_page_widget = SignupWidget()
        self.forget_pass_page_widget = ForgetPassWidget()
        self.reset_pass_page_widget = ResetPassWidget()

        # Add widgets to the stacked widget
        self.central_widget.addWidget(self.login_page_widget)
        self.central_widget.addWidget(self.signup_page_widget)
        self.central_widget.addWidget(self.forget_pass_page_widget)
        self.central_widget.addWidget(self.reset_pass_page_widget)

        self.central_widget.setCurrentWidget(self.reset_pass_page_widget)  # Start with the login page

        # Connect buttons to switch pages
        self.login_page_widget.ui.signupbutton.clicked.connect(self.show_signup_page)
        self.signup_page_widget.ui.backbutton.clicked.connect(self.show_login_page)
        self.login_page_widget.ui.forgetpassbutton.clicked.connect(self.show_forget_pass_page)  # Corrected here
        self.forget_pass_page_widget.ui.backbutton.clicked.connect(self.show_login_page)
        self.reset_pass_page_widget.ui.backbutton.clicked.connect(self.show_login_page)
        self.forget_pass_page_widget.ui.pushButton.clicked.connect(self.show_reset_pass_page)

        # Add a close button to the frameless window
        close_button = QPushButton('X', self)
        close_button.setStyleSheet('background-color: red; color: white; font-weight: bold;')
        close_button.setFixedSize(30, 30)
        close_button.move(self.width() - 40, 10)
        close_button.clicked.connect(self.close)

    def show_login_page(self):
        self.central_widget.setCurrentWidget(self.login_page_widget)

    def show_signup_page(self):
        self.central_widget.setCurrentWidget(self.signup_page_widget)

    def show_forget_pass_page(self):
        self.central_widget.setCurrentWidget(self.forget_pass_page_widget)

    def show_reset_pass_page(self):
        self.central_widget.setCurrentWidget(self.reset_pass_page_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
