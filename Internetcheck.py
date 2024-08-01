import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtCore import QUrl

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Internet Connection Monitor")
        self.setGeometry(100, 100, 400, 300)

        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # Create upper frame
        self.upper_frame = QFrame()
        self.upper_frame.setStyleSheet("background-color: red;")
        self.upper_frame.setFixedHeight(50)
        main_layout.addWidget(self.upper_frame)

        # Create content widget
        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: white;")
        main_layout.addWidget(content_widget)

        # Set up network manager and timer
        self.network_manager = QNetworkAccessManager()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_internet)
        self.timer.start(5000)  # Check every 5 seconds

        # Initial check
        self.check_internet()

    def check_internet(self):
        url = QUrl("https://www.google.com")
        request = QNetworkRequest(url)
        reply = self.network_manager.get(request)
        reply.finished.connect(self.handle_network_reply)

    def handle_network_reply(self):
        reply = self.sender()
        if reply.error() == QNetworkReply.NetworkError.NoError:
            self.upper_frame.hide()
        else:
            self.upper_frame.show()
        reply.deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())