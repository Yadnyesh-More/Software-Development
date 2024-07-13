import sys
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.media_player = QMediaPlayer()

        video_widget = QVideoWidget()

        self.media_player.setVideoOutput(video_widget)

        self.media_player.errorOccurred.connect(self.handle_error)
        self.media_player.mediaStatusChanged.connect(self.handle_media_status_changed)

        layout = QVBoxLayout()
        layout.addWidget(video_widget)

        self.setLayout(layout)
        self.resize(1300, 400)  # Set the frame size to 1300x400


        self.media_player.setSource(QUrl.fromLocalFile(r"D:\MyFiles\nobroker\PropertyBBUI\Untitled video - Made with Clipchamp (4).mp4"))

        self.media_player.play()

    def handle_error(self, error):
        error_code = self.media_player.error()
        if error_code == QMediaPlayer.Error.ServiceMissing:
            print("Error: Service missing")
        elif error_code == QMediaPlayer.Error.FormatNotSupported:
            print("Error: Format not supported")
        elif error_code == QMediaPlayer.Error.NetworkError:
            print("Error: Network error")
        elif error_code == QMediaPlayer.Error.AccessDenied:
            print("Error: Access denied")
        elif error_code == QMediaPlayer.Error.MediaIsPlaylist:
            print("Error: Media is a playlist")
        else:
            print("Error: ", self.media_player.errorString())

    def handle_media_status_changed(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.media_player.setPosition(0)  # Reset the position to the beginning
            self.media_player.play()  # Restart playback

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())