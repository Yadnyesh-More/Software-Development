from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QSizePolicy, QWidget)

class Ui_Progressbar(object):
    def setupUi(self, Progressbar):
        if not Progressbar.objectName():
            Progressbar.setObjectName(u"Progressbar")
        Progressbar.resize(680, 400)
        self.centralwidget = QWidget(Progressbar)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropshadowframe = QFrame(self.centralwidget)
        self.dropshadowframe.setObjectName(u"dropshadowframe")
        self.dropshadowframe.setStyleSheet(u"QFrame{\n"
"background-color:rgb(35, 47, 49);\n"
"color:rgb(220,220,220);\n"
"border-radius:10px;\n"
"	border-color: rgb(255, 255, 255);\n"
"border:3px solid rgb(18, 140, 126);\n"
"}")
        self.dropshadowframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropshadowframe.setFrameShadow(QFrame.Shadow.Raised)
        self.head_label = QLabel(self.dropshadowframe)
        self.head_label.setObjectName(u"head_label")
        self.head_label.setGeometry(QRect(10, 89, 641, 71))
        font = QFont()
        font.setPointSize(40)
        self.head_label.setFont(font)
        self.head_label.setStyleSheet(u"color:rgb(18, 140, 126);\n"
"border:none;")
        self.head_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_description = QLabel(self.dropshadowframe)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(10, 150, 641, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color:rgb(165, 165, 165);\n"
"border:none;")
        self.label_description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar = QProgressBar(self.dropshadowframe)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 270, 581, 21))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color:rgb(251, 251, 251);\n"
"	color:rgb(0, 0, 0);\n"
"	border-style:none;\n"
"border-radius:10px;\n"
"text-align:center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius:10px;\n"
"	background-color:qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(18, 140, 126, 255), stop:1 rgba(255, 255, 255, 255));\n"
"};")
        self.progressBar.setValue(24)
        self.loading_label = QLabel(self.dropshadowframe)
        self.loading_label.setObjectName(u"loading_label")
        self.loading_label.setGeometry(QRect(12, 295, 641, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.loading_label.setFont(font2)
        self.loading_label.setStyleSheet(u"color:rgb(165, 165, 165);\n"
"border:none;")
        self.loading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.dropshadowframe)

        Progressbar.setCentralWidget(self.centralwidget)

        self.retranslateUi(Progressbar)

        QMetaObject.connectSlotsByName(Progressbar)
    # setupUi

    def retranslateUi(self, Progressbar):
        Progressbar.setWindowTitle(QCoreApplication.translate("Progressbar", u"MainWindow", None))
        self.head_label.setText(QCoreApplication.translate("Progressbar", u"<strong>M</strong>iddle <strong>M</strong>an", None))
        self.label_description.setText(QCoreApplication.translate("Progressbar", u"<strong>Ghar</strong> Lo <strong>Ghar</strong> Do", None))
        self.loading_label.setText(QCoreApplication.translate("Progressbar", u"loading...", None))
    # retranslateUi

