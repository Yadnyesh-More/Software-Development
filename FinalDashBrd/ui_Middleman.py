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
        self.dropshadowframe.setStyleSheet(u"QFrame#dropshadowframe{\n"
"background-color:rgb(35, 47, 49);\n"
"color:rgb(220,220,220);\n"
"border-radius:10px;\n"
"border: 1px solid rgb(0, 170, 0);\n"  # Add this line to set a white thin border
"}")
        self.dropshadowframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropshadowframe.setFrameShadow(QFrame.Shadow.Raised)
        self.label_title = QLabel(self.dropshadowframe)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(10, 89, 641, 71))
        font = QFont()
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color:rgb(0, 170, 0);")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_description = QLabel(self.dropshadowframe)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(10, 150, 641, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar = QProgressBar(self.dropshadowframe)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 270, 581, 21))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"background-color:rgb(251, 251, 251);\n"
"color:rgb(0, 0, 0);\n"
"border-style:none;\n"
"border-radius:10px;\n"
"text-align:center;\n"
"}\n"
"QProgressBar::chunk{\n"
"border-radius:10px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 169, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"};")
        self.progressBar.setValue(24)
        self.label_3 = QLabel(self.dropshadowframe)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 300, 641, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color:rgb(98,114,168);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.dropshadowframe)

        Progressbar.setCentralWidget(self.centralwidget)

        self.retranslateUi(Progressbar)

        QMetaObject.connectSlotsByName(Progressbar)
    # setupUi

    def retranslateUi(self, Progressbar):
        Progressbar.setWindowTitle(QCoreApplication.translate("Progressbar", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("Progressbar", u"<strong>M</strong>iddle <strong>M</strong>an", None))
        self.label_description.setText(QCoreApplication.translate("Progressbar", u"<strong>Ghar</strong> Lo <strong>Ghar</strong> Do", None))
        self.label_3.setText(QCoreApplication.translate("Progressbar", u"loading", None))
    # retranslateUi
