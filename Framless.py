import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
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

class MainWindow(QWidget):  # Changed to QWidget instead of QMainWindow
    def __init__(self):
        super(MainWindow, self).__init__()
        self.central_widget = QStackedWidget()

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

        # Set the layout of this QWidget
        layout = QVBoxLayout()
        layout.addWidget(self.central_widget)
        self.setLayout(layout)

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
    
    # Remove window frame and title bar (optional, if you want a frameless window)
    # app.setStyle("fusion")  # Optional: set Fusion style for consistent appearance
    window = MainWindow()
    window.setWindowFlags(Qt.FramelessWindowHint)  # Remove window frame
    window.setAttribute(Qt.WA_TranslucentBackground)
    window.show()
    
    sys.exit(app.exec())