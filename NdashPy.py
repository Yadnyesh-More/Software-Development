from email.mime.application import MIMEApplication
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QPropertyAnimation)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextEdit, QToolBox,
    QVBoxLayout, QWidget,QSlider,QMessageBox,QGraphicsOpacityEffect,QVBoxLayout,QHBoxLayout,QGroupBox,QFileDialog)
import time
import urllib.request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import make_msgid
import os 
from functools import partial
import json
import ressanket_rc



class Ui_MainWindow(object):
    # After coding 
    def __init__(self):
        
        self.filter_frame_visible = False
        self.filter_frame = None
        self.logout_frame_visible = False
        self.logout_frame = None
        self.feedback_frame_visible = False
        self.feedback_frame = None
        self.notification_frame_visible = False
        self.notification_frame = None
        self.scratch_frame_visible = False
        self.scratch_frame = None
        self.owner_frame_visible = False
        self.owner_frame = None
        self.refer_and_frame = None
        self.refer_and_frame_visible = False
        self.my_rewards_frame = None
        self.my_rewards_frame_visible = False
        self.my_scratches_frame = None
        self.my_scratches_frame_visible = False
        self.no_scratches_frame = None
        self.no_scratches_frame_visible = False
        self.get_an_visible = False
        self.get_an_info_frame = None
        self.rates = 0
        self.add_dis = 0
        self.sub_dis = 0 
        self.subtracting = 0
        self.MMcash = 3000
        self.str_value = 0
        self.scratches_zmt = 0
        self.scratches_ama = 0
        self.scratches_pizu = 0 
        self.scratches_flp = 0
        self.scratches_myn = 0
        self.scratches_domi = 0
        self.intevlu = True
        self.blackic = QIcon()
        self.blackic.addFile(u':/sanket/images/starblank.png', QSize(), QIcon.Normal, QIcon.Off)
        self.goldic = QIcon()
        self.goldic.addFile(u":/sanket/images/starfill.png", QSize(), QIcon.Normal, QIcon.Off)
        self.values1 = [24.98, 26.37, 34.31, 40, 41.1, 43.5, 75.22, 78, 86, 1.1, 1.2, 1.33]  # Duplicate property 43.5L
        self.values2 = [33.52, 40.14, 40.66, 44.67, 59.21, 62.7, 66, 66.2, 78.5, 1.2, 1.25, 1.45, 1.86, 1.81, 1.55, 1.72, 1.96, 2.2]  # Duplicate property 66L
        self.values3 = [98.19, 1.08, 1.69, 1.89, 1.96, 3.16, 3.32, 4.5, 4.14]
        self.valuesoth = [41.87, 47.90, 1.66, 2.96, 8.9]
        self.values = self.values1  # Initial values
        self.value_map = {i: value for i, value in enumerate(self.values)}
        self.item_text = None # BHk types 
        self.actual_value = 0 # Price in BHk type
        self.cmb_city = None
        self.user_local_area_vl = None
        self.viaemail_body= None
        self.viaemail_subject = None
        self.viawp = None
        self.Scratch1 = None 
        self.amount_map = {}
        pass


    def clck_more_info(self,property_detail):
        if not self.get_an_visible :
                self.get_an_info_frame = QFrame(self.mainmenu)
                self.get_an_info_frame.setObjectName(u"self.get_an_info_frame")
                self.get_an_info_frame.setGeometry(290,150,700, 400)
                self.get_an_info_frame.setMinimumSize(QSize(700, 400))
                self.get_an_info_frame.setMaximumSize(QSize(700, 400))
                self.frame = QFrame(self.get_an_info_frame)
                self.frame.setObjectName(u"frame")
                self.frame.setGeometry(QRect(0, 0, 700, 400))
                font = QFont()
                font.setFamilies([u"Sitka Banner Semibold"])
                self.frame.setFont(font)
                self.frame.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
                "border:3px solid rgb(18, 140, 126);\n"
                "border-radius:10px;")
                self.frame.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame.setFrameShadow(QFrame.Shadow.Raised)
                self.label_6 = QLabel(self.frame)
                self.label_6.setObjectName(u"label_6")
                self.label_6.setGeometry(QRect(371, 52, 261, 61))
                font1 = QFont()
                font1.setPointSize(16)
                self.label_6.setFont(font1)
                self.label_6.setStyleSheet(u"border:none;\n"
                "color:white")
                self.user_nm = QLineEdit(self.frame)
                self.user_nm.setObjectName(u"user_nm")
                self.user_nm.setGeometry(QRect(371, 167, 291, 31))
                font2 = QFont()
                font2.setPointSize(11)
                self.user_nm.setFont(font2)
                self.user_nm.setStyleSheet(u"QLineEdit{\n"
                "border:none;\n"
                "background-color:white;\n"
                "border-radius:0px;\n"
                "}\n"
                "QLineEdit:hover{\n"
                "border-bottom:2px solid rgb(18, 140, 126);\n"
                "}")
                self.user_nm.setCursorPosition(0)
                self.info_username = QLabel(self.frame)
                self.info_username.setObjectName(u"info_username")
                self.info_username.setGeometry(QRect(371, 146, 101, 18))
                font3 = QFont()
                font3.setPointSize(10)
                self.info_username.setFont(font3)
                self.info_username.setStyleSheet(u"border:none;\n"
                "color:rgb(18, 140, 126);")
                self.info_contact = QLabel(self.frame)
                self.info_contact.setObjectName(u"info_contact")
                self.info_contact.setGeometry(QRect(370, 224, 101, 18))
                self.info_contact.setFont(font3)
                self.info_contact.setStyleSheet(u"border:none;\n"
                "color:rgb(18, 140, 126);")
                self.cntct_num = QLineEdit(self.frame)
                self.cntct_num.setObjectName(u"cntct_num")
                self.cntct_num.setGeometry(QRect(371, 245, 291, 31))
                font4 = QFont()
                font4.setPointSize(11)
                font4.setBold(False)
                self.cntct_num.setFont(font4)
                self.cntct_num.setStyleSheet(u"QLineEdit{\n"
                "border:none;\n"
                "background-color:white;\n"
                "border-radius:0px;\n"
                "}\n"
                "QLineEdit:hover{\n"
                "border-bottom:2px solid rgb(18, 140, 126);\n"
                "}")
                self.cntct_num.setMaxLength(10)
                self.cntct_num.setCursorPosition(0)
                self.snd_email_img = QPushButton(self.frame)
                self.snd_email_img.setObjectName(u"snd_email_img")
                self.snd_email_img.setGeometry(QRect(433, 319, 170, 31))
                font5 = QFont()
                font5.setPointSize(12)
                self.snd_email_img.setFont(font5)
                self.snd_email_img.setStyleSheet(u"QPushButton\n"
                "{\n"
                "background-color:rgb(18, 140, 126);\n"
                "border:none;\n"
                "border-radius:10px;\n"
                "}\n"
                "QPushButton:hover\n"
                "{\n"
                "border:1px solid rgb(18, 140, 126);\n"
                "background-color:rgb(35, 47, 49);\n"
                "	color: rgb(255, 255, 255);\n"
                "}")
                self.snd_email_img.setCheckable(True)
                self.info_close = QPushButton(self.frame)
                self.info_close.setObjectName(u"info_close")
                self.info_close.setGeometry(QRect(674, 4, 20, 20))
                font6 = QFont()
                font6.setPointSize(13)
                self.info_close.setFont(font6)
                self.info_close.setStyleSheet(u"border:none; color:white;")
                self.info_close.setCheckable(True)
                self.frame_2 = QFrame(self.frame)
                self.frame_2.setObjectName(u"frame_2")
                self.frame_2.setGeometry(QRect(10, 10, 351, 371))
                self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

                self.retranslateUi(self.get_an_info_frame)
                self.label_6.setText(QCoreApplication.translate("self.get_an_info_frame", u"<html><head/><body><p>Get personalized assistance <br/>from our experts for <span style=\" font-weight:700; color:#128c7e;\">FREE</span></p></body></html>", None))
                self.user_nm.setText("")
                self.user_nm.setPlaceholderText("")
                self.info_username.setText(QCoreApplication.translate("self.get_an_info_frame", u"User Name", None))
                self.info_contact.setText(QCoreApplication.translate("self.get_an_info_frame", u"Phone Number", None))
                self.cntct_num.setText("")
                self.cntct_num.setPlaceholderText("")
                self.snd_email_img.setText(QCoreApplication.translate("self.get_an_info_frame", u"Connect", None))
                self.info_close.setText(QCoreApplication.translate("self.get_an_info_frame", u"x", None))
                self.info_close.toggled.connect(self.get_an_info_frame.close)
                self.snd_email_img.clicked.connect(lambda : self.get_an_email(property_detail))
                self.get_an_info_frame.show()
                self.get_an_visible = True
                
        else:
                self.get_an_info_frame.hide()
                self.get_an_visible =False
        pass


    def get_an_email(self,property_detail):
        print(self.pushButton_2.isChecked(),self.pushButton_3.isChecked(),property_detail)
        file_path = '.vscode/property_details.json'
        target_id = property_detail

        try:
        # Read the JSON file
                with open(file_path, 'r') as file:
                        properties = json.load(file)

                # Find the property with the given ID
                property_info = next((prop for prop in properties if prop["id"] == target_id), None)

                if property_info:
                        # Extract details
                        prop_id = property_info.get("id", "ID not available")
                        propname = property_info.get("propname", "Property name not available")
                        price = property_info.get("price", {})
                        address = property_info.get("address", "Address not available")
                        status = property_info.get("status", "Status not available")
                        bathrooms = property_info.get("bathrooms", {})
                        amenities = property_info.get("amenities", [])
                        interior = property_info.get("interior_details", "Interior details not available")
                        exterior = property_info.get("exterior_details", "Exterior details not available")
                        location_hi = property_info.get("location_highlights", "Location highlights not available")
                        property_typ = property_info.get("property_type", "Property type not available")
                        img_pth = property_info.get("image_path", [])
                        pdf_pth = property_info.get("pdf_path", "Pdf path is not available")

                        # Collect price details
                        price_details = ", ".join([f"{bhk_type}: {bhk_price}" for bhk_type, bhk_price in price.items()])

                        # Collect bathroom details
                        bathroom_details = ", ".join([f"{bhk_type}: {num_bathrooms}" for bhk_type, num_bathrooms in bathrooms.items()])

                        image_paths = img_pth

                        # Print details for debugging
                        print(f"ID: {prop_id}")
                        print(f"Property Name: {propname}")
                        print(f"Address: {address}")
                        print(f"Status: {status}")
                        print(f"Property Type: {property_typ}")
                        print(f"Interior Details: {interior}")
                        print(f"Exterior Details: {exterior}")
                        print(f"Location Highlights: {location_hi}")
                        print(f"Price Details: {price_details}")
                        print(f"Bathroom Details: {bathroom_details}")
                        print(f"Amenities: {', '.join(amenities) if amenities else 'None'}")
                        print(f"Pdf Path : {pdf_pth}")
                        print(f"Image Paths  {image_paths}")

                else:
                        print(f"Property with ID {target_id} not found.")

        except FileNotFoundError:
                print(f"The file at {file_path} does not exist.")
        except json.JSONDecodeError:
                print("Error decoding JSON from the file.")

        # Define email details
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # Correct SMTP port for TLS
        sender_email = 'middleman3701@gmail.com'  # Your email
        sender_password = 'wtkh syvj zptd elfa'  # Your email password or app password
        receiver_email = 'middleman3701@gmail.com'  # Replace with actual receiver email
        subject = "Exclusive Property Details"

        # Define HTML message
        message = f"""<!DOCTYPE html>
        <html lang="en">
        <head>        
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Property Details Email</title>
        <style>
                body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                }}
                .container {{
                margin: 0 auto;
                padding: 20px;
                max-width: 600px;
                border: 1px solid #ddd;
                border-radius: 10px;
                }}
                .header {{
                text-align: center;
                padding: 10px 0;
                border-bottom: 1px solid #ddd;
                }}
                .content {{
                margin: 20px 0;
                }}
                .content p {{
                margin: 10px 0;
                }}
                .images {{
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 40px;
                margin: 20px 0;
                }}
                .images img {{
                max-width: 100%;
                height: auto;
                border-radius: 10px;
                margin: 0 10px; 
                }}
                .footer {{
                text-align: center;
                padding: 10px 0;
                border-top: 1px solid #ddd;
                margin-top: 20px;
                }}
        </style>
        </head>
        <body>
        <div class="container">
                <div class="header">
                <h2>Exclusive Property Details – {address}</h2>
                </div>
                <div class="content">
                <p>Dear [Recipient's Name],</p>
                <p>I hope this email finds you well. I am pleased to share with you the details of an exceptional property that may perfectly suit your needs. Below are the key highlights and specifications of the property:</p>
                <p><strong>Property Address:</strong><br>{address}</p>
                <p><strong>Property Type:</strong><br>{property_typ}</p>
                <p><strong>Price:</strong><br>{price_details}</p>
                <p><strong>Key Features:</strong></p>
                <ul>
                        <li><strong>Bathrooms:</strong> {bathroom_details}</li>
                        <li><strong>Amenities:</strong> {', '.join(amenities) if amenities else 'None'}</li>
                        <li><strong>Status:</strong> {status}</li>
                </ul>
                <p><strong>Interior Details:</strong><br>{interior}</p>
                <p><strong>Exterior Details:</strong><br>{exterior}</p>
                <p><strong>Location Highlights:</strong><br>{location_hi}</p>

                <!-- Image section -->
                <div class="images">
                        {' '.join(f'<img src="cid:image{i+1}" alt="Property Image {i+1}">' for i in range(len(image_paths)))}
                </div>

                <p>For more information or to schedule a viewing, please do not hesitate to contact me at 8097667158 or reply to this email.</p>
                <p>Thank you for considering this property. I look forward to assisting you with any questions or to arrange a visit at your convenience.</p>
                </div>
                <div class="footer">
                <p>Best regards,</p>
                <p>[Your Name]<br>[Your Title/Position]<br>[Your Contact Information]<br>MiddleMan<br>Shaydri Nagar, Temi Pada Road, Mulund (E), Pin Code - 400078, near Ayyappa Mandir<br>middleman3701@gmail.com<br>8097667158</p>
                </div>
        </div>
        </body>
        </html>
        """

        # Prepare the email
        msg = MIMEMultipart('related')
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Attach the HTML message to the MIME message
        msg.attach(MIMEText(message, 'html'))

        # Attach images
        for i, image_path in enumerate(image_paths):
                if os.path.exists(image_path):
                        with open(image_path, 'rb') as img:
                                mime_image = MIMEImage(img.read())
                                cid = make_msgid(domain='example.com')
                                mime_image.add_header('Content-ID', f'<image{i + 1}>')
                                mime_image.add_header('Content-Disposition', 'inline')
                                msg.attach(mime_image)
                else:
                        print(f"Image file not found: {image_path}")

        # Attach PDF
        if os.path.exists(pdf_pth):
                with open(pdf_pth, 'rb') as pdf:
                        mime_pdf = MIMEApplication(pdf.read(), _subtype="pdf")
                        mime_pdf.add_header('Content-Disposition', 'attachment')
                        msg.attach(mime_pdf)
        else:
                print(f"PDF file not found: {pdf_pth}")

        try:
            # Connect to SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Start TLS encryption
            # Login to SMTP server
            server.login(sender_email, sender_password)
            # Send email
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email. Error: {str(e)}")
        finally:
            # Close the connection
            server.quit()
        pass

    def noscratches_win_frame(self):

        if self.my_rewards_frame:
                self.my_rewards_frame.close()
                self.my_rewards_frame.hide()
                
                if not self.no_scratches_frame_visible:
                        self.no_scratches_frame = QFrame(self.frame_17)    
                        self.no_scratches_frame.setGeometry(925,70,400, 593)
                        self.no_scratches_frame.resize(400, 593)
                        self.no_scratches_frame.setMinimumSize(QSize(400, 593))
                        self.no_scratches_frame.setMaximumSize(QSize(400, 593))
                        self.frame_81 = QFrame(self.no_scratches_frame)
                        self.frame_81.setObjectName(u"frame_81")
                        self.frame_81.setGeometry(QRect(0, 0, 400, 591))
                        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
                        sizePolicy.setHorizontalStretch(0)
                        sizePolicy.setVerticalStretch(0)
                        sizePolicy.setHeightForWidth(self.frame_81.sizePolicy().hasHeightForWidth())
                        self.frame_81.setSizePolicy(sizePolicy)
                        self.frame_81.setMinimumSize(QSize(400, 591))
                        self.frame_81.setMaximumSize(QSize(400, 591))
                        font = QFont()
                        font.setPointSize(13)
                        self.frame_81.setFont(font)
                        self.frame_81.setStyleSheet(u"background-color:rgb(35, 47, 49);\n"
                "border:3px solid rgb(18, 140, 126);\n"
                "border-radius:10px;")
                        self.frame_81.setFrameShape(QFrame.Shape.Panel)
                        self.frame_81.setFrameShadow(QFrame.Shadow.Raised)
                        self.line_14 = QFrame(self.frame_81)
                        self.line_14.setObjectName(u"line_14")
                        self.line_14.setGeometry(QRect(-20, 69, 431, 3))
                        self.line_14.setMinimumSize(QSize(0, 3))
                        self.line_14.setMaximumSize(QSize(16777215, 3))
                        self.line_14.setStyleSheet(u"border:none;\n"
                "background-color:rgb(18, 140, 126);\n"
                "border-radius:0px;")
                        self.line_14.setFrameShape(QFrame.Shape.HLine)
                        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)
                        self.label_182 = QLabel(self.frame_81)
                        self.label_182.setObjectName(u"label_182")
                        self.label_182.setGeometry(QRect(90, 13, 231, 41))
                        font1 = QFont()
                        font1.setPointSize(20)
                        font1.setBold(True)
                        self.label_182.setFont(font1)
                        self.label_182.setStyleSheet(u"color:white; border:none;")
                        self.label = QLabel(self.frame_81)
                        self.label.setObjectName(u"label")
                        self.label.setGeometry(QRect(80, 150, 241, 181))
                        self.label.setStyleSheet(u"border:none;")
                        self.label.setPixmap(QPixmap(u":/sanket/images/scratchcard.png"))
                        self.label.setScaledContents(True)
                        self.label_2 = QLabel(self.frame_81)
                        self.label_2.setObjectName(u"label_2")
                        self.label_2.setGeometry(QRect(60, 360, 291, 91))
                        font2 = QFont()
                        font2.setPointSize(16)
                        self.label_2.setFont(font2)
                        self.label_2.setStyleSheet(u"color:white; border:none;")
                        self.label_182.setText(QCoreApplication.translate("self.my_scratches_frame", u"My Coupon Cards", None))
                        self.label.setText("")
                        self.label_2.setText(QCoreApplication.translate("self.my_scratches_frame", u"No Scratch Cards are \n"
                                " availabel", None))
                        self.no_scratches_frame.show()
                        self.no_scratches_frame_visible = True
                else:
                    self.no_scratches_frame.hide()
                    self.no_scratches_frame_visible = False          
                
        else:
                pass
        
    def myscratches_win_frame(self):
        if not self.my_scratches_frame_visible:
                self.my_scratches_frame = QFrame(self.frame_17)
                self.my_scratches_frame.setObjectName(u"self.my_scratches_frame")
                self.my_scratches_frame.setGeometry(925,70,400, 593)
                self.my_scratches_frame.resize(400, 593)
                self.my_scratches_frame.setMinimumSize(QSize(400, 593))
                self.my_scratches_frame.setMaximumSize(QSize(400, 593))
                self.frame_81 = QFrame(self.my_scratches_frame)
                self.frame_81.setObjectName(u"frame_81")
                self.frame_81.setGeometry(QRect(0, 0, 400, 591))
                sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.frame_81.sizePolicy().hasHeightForWidth())
                self.frame_81.setSizePolicy(sizePolicy)
                self.frame_81.setMinimumSize(QSize(400, 591))
                self.frame_81.setMaximumSize(QSize(400, 591))
                self.frame_81.setStyleSheet(u"background-color:rgb(35, 47, 49);\n"
        "border:3px solid rgb(18, 140, 126);\n"
        "border-radius:10px;")
                self.frame_81.setFrameShape(QFrame.Shape.Panel)
                self.frame_81.setFrameShadow(QFrame.Shadow.Raised)
                self.line_14 = QFrame(self.frame_81)
                self.line_14.setObjectName(u"line_14")
                self.line_14.setGeometry(QRect(-20, 69, 431, 3))
                self.line_14.setMinimumSize(QSize(0, 3))
                self.line_14.setMaximumSize(QSize(16777215, 3))
                self.line_14.setStyleSheet(u"border:none;\n"
        "background-color:rgb(18, 140, 126);\n"
        "border-radius:0px;")
                self.line_14.setFrameShape(QFrame.Shape.HLine)
                self.line_14.setFrameShadow(QFrame.Shadow.Sunken)
                self.label_182 = QLabel(self.frame_81)
                self.label_182.setObjectName(u"label_182")
                self.label_182.setGeometry(QRect(90, 13, 231, 41))
                font = QFont()
                font.setPointSize(20)
                font.setBold(True)
                self.label_182.setFont(font)
                self.label_182.setStyleSheet(u"color:white; border:none;")
                self.layoutWidget = QWidget(self.frame_81)
                self.layoutWidget.setObjectName(u"layoutWidget")
                self.layoutWidget.setGeometry(QRect(11, 89, 377, 488))
                self.gridLayout = QGridLayout(self.layoutWidget)
                self.gridLayout.setObjectName(u"gridLayout")
                self.gridLayout.setHorizontalSpacing(15)
                self.gridLayout.setVerticalSpacing(18)
                self.gridLayout.setContentsMargins(0, 0, 0, 0)
                self.amazon_frame = QFrame(self.layoutWidget)
                self.amazon_frame.setObjectName(u"amazon_frame")
                self.amazon_frame.setMinimumSize(QSize(180, 150))
                self.amazon_frame.setMaximumSize(QSize(180, 150))
                self.amazon_frame.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
        "border-radius:10px;")
                self.amazon_frame.setFrameShape(QFrame.Shape.StyledPanel)
                self.amazon_frame.setFrameShadow(QFrame.Shadow.Raised)
                self.frame_26 = QFrame(self.amazon_frame)
                self.frame_26.setObjectName(u"frame_26")
                self.frame_26.setGeometry(QRect(0, -3, 201, 121))
                self.frame_26.setStyleSheet(u"")
                self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
                self.label_52 = QLabel(self.frame_26)
                self.label_52.setObjectName(u"label_52")
                self.label_52.setGeometry(QRect(-52, -25, 281, 171))
                self.label_52.setPixmap(QPixmap(r"images/Ama.png"))
                self.label_52.setScaledContents(True)
                self.layoutWidget_2 = QWidget(self.amazon_frame)
                self.layoutWidget_2.setObjectName(u"layoutWidget_2")
                self.layoutWidget_2.setGeometry(QRect(11, 168, 182, 52))
                self.verticalLayout_40 = QVBoxLayout(self.layoutWidget_2)
                self.verticalLayout_40.setSpacing(0)
                self.verticalLayout_40.setObjectName(u"verticalLayout_40")
                self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
                self.label_147 = QLabel(self.layoutWidget_2)
                self.label_147.setObjectName(u"label_147")
                font1 = QFont()
                font1.setPointSize(12)
                font1.setBold(True)
                self.label_147.setFont(font1)
                self.label_147.setStyleSheet(u"color: rgb(7, 94, 84);")

                self.verticalLayout_40.addWidget(self.label_147)

                self.label_148 = QLabel(self.layoutWidget_2)
                self.label_148.setObjectName(u"label_148")
                self.label_148.setStyleSheet(u"color: rgb(255, 255, 255);")

                self.verticalLayout_40.addWidget(self.label_148)

                self.amazon_refer = QLabel(self.amazon_frame)
                self.amazon_refer.setObjectName(u"amazon_refer")
                self.amazon_refer.setGeometry(QRect(25, 124, 128, 21))

                self.gridLayout.addWidget(self.amazon_frame, 0, 0, 1, 1)

                self.dominos_frame = QFrame(self.layoutWidget)
                self.dominos_frame.setObjectName(u"dominos_frame")
                self.dominos_frame.setMinimumSize(QSize(180, 150))
                self.dominos_frame.setMaximumSize(QSize(180, 150))
                self.dominos_frame.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
        "border-radius:10px;")
                self.dominos_frame.setFrameShape(QFrame.Shape.StyledPanel)
                self.dominos_frame.setFrameShadow(QFrame.Shadow.Raised)
                self.frame_28 = QFrame(self.dominos_frame)
                self.frame_28.setObjectName(u"frame_28")
                self.frame_28.setGeometry(QRect(0, -3, 201, 120))
                self.frame_28.setStyleSheet(u"")
                self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
                self.label_149 = QLabel(self.frame_28)
                self.label_149.setObjectName(u"label_149")
                self.label_149.setGeometry(QRect(-12, -9, 201, 141))
                self.label_149.setPixmap(QPixmap(u"Dominos.png"))
                self.label_149.setScaledContents(True)
                self.layoutWidget_3 = QWidget(self.dominos_frame)
                self.layoutWidget_3.setObjectName(u"layoutWidget_3")
                self.layoutWidget_3.setGeometry(QRect(11, 168, 182, 52))
                self.verticalLayout_41 = QVBoxLayout(self.layoutWidget_3)
                self.verticalLayout_41.setSpacing(0)
                self.verticalLayout_41.setObjectName(u"verticalLayout_41")
                self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
                self.label_150 = QLabel(self.layoutWidget_3)
                self.label_150.setObjectName(u"label_150")
                self.label_150.setFont(font1)
                self.label_150.setStyleSheet(u"color: rgb(7, 94, 84);")

                self.verticalLayout_41.addWidget(self.label_150)

                self.label_151 = QLabel(self.layoutWidget_3)
                self.label_151.setObjectName(u"label_151")
                self.label_151.setStyleSheet(u"color: rgb(255, 255, 255);")

                self.verticalLayout_41.addWidget(self.label_151)

                self.dominos_refer = QLabel(self.dominos_frame)
                self.dominos_refer.setObjectName(u"dominos_refer")
                self.dominos_refer.setGeometry(QRect(25, 122, 123, 21))

                self.gridLayout.addWidget(self.dominos_frame, 0, 1, 1, 1)

                self.flipkart_frame = QFrame(self.layoutWidget)
                self.flipkart_frame.setObjectName(u"flipkart_frame")
                self.flipkart_frame.setMinimumSize(QSize(180, 150))
                self.flipkart_frame.setMaximumSize(QSize(180, 150))
                self.flipkart_frame.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
        "border-radius:10px;")
                self.flipkart_frame.setFrameShape(QFrame.Shape.StyledPanel)
                self.flipkart_frame.setFrameShadow(QFrame.Shadow.Raised)
                self.frame_32 = QFrame(self.flipkart_frame)
                self.frame_32.setObjectName(u"frame_32")
                self.frame_32.setGeometry(QRect(0, -3, 201, 121))
                self.frame_32.setStyleSheet(u"")
                self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
                self.label_155 = QLabel(self.frame_32)
                self.label_155.setObjectName(u"label_155")
                self.label_155.setGeometry(QRect(-10, -10, 201, 141))
                self.label_155.setPixmap(QPixmap(u"flipkart.png"))
                self.label_155.setScaledContents(True)
                self.layoutWidget_5 = QWidget(self.flipkart_frame)
                self.layoutWidget_5.setObjectName(u"layoutWidget_5")
                self.layoutWidget_5.setGeometry(QRect(11, 168, 182, 52))
                self.verticalLayout_43 = QVBoxLayout(self.layoutWidget_5)
                self.verticalLayout_43.setSpacing(0)
                self.verticalLayout_43.setObjectName(u"verticalLayout_43")
                self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
                self.label_153 = QLabel(self.layoutWidget_5)
                self.label_153.setObjectName(u"label_153")
                self.label_153.setFont(font1)
                self.label_153.setStyleSheet(u"color: rgb(7, 94, 84);")

                self.verticalLayout_43.addWidget(self.label_153)

                self.label_154 = QLabel(self.layoutWidget_5)
                self.label_154.setObjectName(u"label_154")
                self.label_154.setStyleSheet(u"color: rgb(255, 255, 255);")

                self.verticalLayout_43.addWidget(self.label_154)

                self.flipkart_refer = QLabel(self.flipkart_frame)
                self.flipkart_refer.setObjectName(u"flipkart_refer")
                self.flipkart_refer.setGeometry(QRect(25, 123, 124, 21))

                self.gridLayout.addWidget(self.flipkart_frame, 1, 0, 1, 1)

                self.myntra_frame = QFrame(self.layoutWidget)
                self.myntra_frame.setObjectName(u"myntra_frame")
                self.myntra_frame.setMinimumSize(QSize(180, 150))
                self.myntra_frame.setMaximumSize(QSize(180, 150))
                self.myntra_frame.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
        "border-radius:10px;")
                self.myntra_frame.setFrameShape(QFrame.Shape.StyledPanel)
                self.myntra_frame.setFrameShadow(QFrame.Shadow.Raised)
                self.frame_34 = QFrame(self.myntra_frame)
                self.frame_34.setObjectName(u"frame_34")
                self.frame_34.setGeometry(QRect(0, -3, 201, 121))
                self.frame_34.setStyleSheet(u"")
                self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
                self.label_158 = QLabel(self.frame_34)
                self.label_158.setObjectName(u"label_158")
                self.label_158.setGeometry(QRect(-10, -10, 196, 134))
                self.label_158.setPixmap(QPixmap(u"Myntra1.png"))
                self.label_158.setScaledContents(True)
                self.layoutWidget_6 = QWidget(self.myntra_frame)
                self.layoutWidget_6.setObjectName(u"layoutWidget_6")
                self.layoutWidget_6.setGeometry(QRect(11, 168, 182, 52))
                self.verticalLayout_44 = QVBoxLayout(self.layoutWidget_6)
                self.verticalLayout_44.setSpacing(0)
                self.verticalLayout_44.setObjectName(u"verticalLayout_44")
                self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
                self.label_156 = QLabel(self.layoutWidget_6)
                self.label_156.setObjectName(u"label_156")
                self.label_156.setFont(font1)
                self.label_156.setStyleSheet(u"color: rgb(7, 94, 84);")

                self.verticalLayout_44.addWidget(self.label_156)

                self.label_157 = QLabel(self.layoutWidget_6)
                self.label_157.setObjectName(u"label_157")
                self.label_157.setStyleSheet(u"color: rgb(255, 255, 255);")

                self.verticalLayout_44.addWidget(self.label_157)

                self.myntra_refer = QLabel(self.myntra_frame)
                self.myntra_refer.setObjectName(u"myntra_refer")
                self.myntra_refer.setGeometry(QRect(23, 123, 131, 21))

                self.gridLayout.addWidget(self.myntra_frame, 1, 1, 1, 1)

                self.pizzahu_frame = QFrame(self.layoutWidget)
                self.pizzahu_frame.setObjectName(u"pizzahu_frame")
                self.pizzahu_frame.setMinimumSize(QSize(180, 150))
                self.pizzahu_frame.setMaximumSize(QSize(180, 150))
                self.pizzahu_frame.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
        "border-radius:10px;")
                self.pizzahu_frame.setFrameShape(QFrame.Shape.StyledPanel)
                self.pizzahu_frame.setFrameShadow(QFrame.Shadow.Raised)
                self.frame_31 = QFrame(self.pizzahu_frame)
                self.frame_31.setObjectName(u"frame_31")
                self.frame_31.setGeometry(QRect(0, -3, 201, 121))
                self.frame_31.setStyleSheet(u"")
                self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
                self.label_152 = QLabel(self.frame_31)
                self.label_152.setObjectName(u"label_152")
                self.label_152.setGeometry(QRect(-10, 0, 201, 124))
                self.label_152.setPixmap(QPixmap(u"PizzaHut.png"))
                self.label_152.setScaledContents(True)
                self.layoutWidget_4 = QWidget(self.pizzahu_frame)
                self.layoutWidget_4.setObjectName(u"layoutWidget_4")
                self.layoutWidget_4.setGeometry(QRect(11, 168, 182, 52))
                self.verticalLayout_42 = QVBoxLayout(self.layoutWidget_4)
                self.verticalLayout_42.setSpacing(0)
                self.verticalLayout_42.setObjectName(u"verticalLayout_42")
                self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
                self.label_164 = QLabel(self.layoutWidget_4)
                self.label_164.setObjectName(u"label_164")
                self.label_164.setFont(font1)
                self.label_164.setStyleSheet(u"color: rgb(7, 94, 84);")

                self.verticalLayout_42.addWidget(self.label_164)

                self.label_165 = QLabel(self.layoutWidget_4)
                self.label_165.setObjectName(u"label_165")
                self.label_165.setStyleSheet(u"color: rgb(255, 255, 255);")

                self.verticalLayout_42.addWidget(self.label_165)

                self.pizzahu_refer = QLabel(self.pizzahu_frame)
                self.pizzahu_refer.setObjectName(u"pizzahu_refer")
                self.pizzahu_refer.setGeometry(QRect(24, 123, 144, 21))

                self.gridLayout.addWidget(self.pizzahu_frame, 2, 0, 1, 1)

                self.zomato_frame = QFrame(self.layoutWidget)
                self.zomato_frame.setObjectName(u"zomato_frame")
                self.zomato_frame.setMinimumSize(QSize(180, 150))
                self.zomato_frame.setMaximumSize(QSize(180, 150))
                self.zomato_frame.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
        "border-radius:10px;")
                self.zomato_frame.setFrameShape(QFrame.Shape.StyledPanel)
                self.zomato_frame.setFrameShadow(QFrame.Shadow.Raised)
                self.frame_36 = QFrame(self.zomato_frame)
                self.frame_36.setObjectName(u"frame_36")
                self.frame_36.setGeometry(QRect(0, -3, 201, 121))
                self.frame_36.setStyleSheet(u"")
                self.frame_36.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
                self.label_161 = QLabel(self.frame_36)
                self.label_161.setObjectName(u"label_161")
                self.label_161.setGeometry(QRect(-10, 0, 201, 126))
                self.label_161.setPixmap(QPixmap(r'images/Zomato.jpg'))
                self.label_161.setScaledContents(True)
                self.layoutWidget_7 = QWidget(self.zomato_frame)
                self.layoutWidget_7.setObjectName(u"layoutWidget_7")
                self.layoutWidget_7.setGeometry(QRect(11, 168, 182, 52))
                self.verticalLayout_45 = QVBoxLayout(self.layoutWidget_7)
                self.verticalLayout_45.setSpacing(0)
                self.verticalLayout_45.setObjectName(u"verticalLayout_45")
                self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
                self.label_166 = QLabel(self.layoutWidget_7)
                self.label_166.setObjectName(u"label_166")
                self.label_166.setFont(font1)
                self.label_166.setStyleSheet(u"color: rgb(7, 94, 84);")

                self.verticalLayout_45.addWidget(self.label_166)

                self.label_167 = QLabel(self.layoutWidget_7)
                self.label_167.setObjectName(u"label_167")
                self.label_167.setStyleSheet(u"color: rgb(255, 255, 255);")

                self.verticalLayout_45.addWidget(self.label_167)

                self.zomato_refer = QLabel(self.zomato_frame)
                self.zomato_refer.setObjectName(u"zomato_refer")
                self.zomato_refer.setGeometry(QRect(16, 123, 144, 21))

                self.gridLayout.addWidget(self.zomato_frame, 2, 1, 1, 1)
                self.label_182.setText(QCoreApplication.translate("Frame", u"My Coupon Cards", None))
                self.label_52.setText("")
                self.label_147.setText(QCoreApplication.translate("Frame", u"Amazon", None))
                self.label_148.setText(QCoreApplication.translate("Frame", u"A Gift Voucher for every wishlist", None))
                self.amazon_refer.setText(QCoreApplication.translate("Frame", u"Code ( 20% ): Am1250", None))
                self.label_149.setText("")
                self.label_150.setText(QCoreApplication.translate("Frame", u"Amazon", None))
                self.label_151.setText(QCoreApplication.translate("Frame", u"A Gift Voucher for every wishlist", None))
                self.dominos_refer.setText(QCoreApplication.translate("Frame", u"Code ( 10% ): DP2024", None))
                self.label_155.setText("")
                self.label_153.setText(QCoreApplication.translate("Frame", u"Amazon", None))
                self.label_154.setText(QCoreApplication.translate("Frame", u"A Gift Voucher for every wishlist", None))
                self.flipkart_refer.setText(QCoreApplication.translate("Frame", u"Code ( 20% ): FP14GC", None))
                self.label_158.setText("")
                self.label_156.setText(QCoreApplication.translate("Frame", u"Amazon", None))
                self.label_157.setText(QCoreApplication.translate("Frame", u"A Gift Voucher for every wishlist", None))
                self.myntra_refer.setText(QCoreApplication.translate("Frame", u"Code ( 30% ): MSale50", None))
                self.label_152.setText("")
                self.label_164.setText(QCoreApplication.translate("Frame", u"Amazon", None))
                self.label_165.setText(QCoreApplication.translate("Frame", u"A Gift Voucher for every wishlist", None))
                self.pizzahu_refer.setText(QCoreApplication.translate("Frame", u"Code ( 10% ): PHUT15", None))
                self.label_161.setText("")
                self.label_166.setText(QCoreApplication.translate("Frame", u"Amazon", None))
                self.label_167.setText(QCoreApplication.translate("Frame", u"A Gift Voucher for every wishlist", None))
                self.zomato_refer.setText(QCoreApplication.translate("Frame", u"Code ( 10% ): ZOMATO19", None))
                self.my_scratches_frame.show()
                self.amazon_frame.hide()
                self.flipkart_frame.hide()
                self.pizzahu_frame.hide()
                self.myntra_frame.hide()
                self.dominos_frame.hide()
                self.zomato_frame.hide()
                
                if self.scratches_ama== 1:
                        self.amazon_frame.show()
                if self.scratches_domi== 2:
                        self.amazon_frame.show()
                if self.scratches_pizu== 3:
                        self.amazon_frame.show()
                if self.scratches_flp== 4:
                        self.amazon_frame.show()
                if self.scratches_myn== 5:
                        self.amazon_frame.show()
                if self.scratches_zmt== 6:
                        self.amazon_frame.show()
                
        else:
                self.my_scratches_frame.hide()
                self.my_rewards_frame_visible = False
        
    def myreward_win_frame(self):
        # self.my_scratches_frame.hide()
        # self.no_scratches_frame.hide()
        
        if not self.my_rewards_frame_visible:
                self.my_rewards_frame = QFrame(self.frame_17)
                self.my_rewards_frame.setGeometry(925,70,400, 593)
                self.my_rewards_frame.setObjectName(u"self.my_rewards_frame")
                self.my_rewards_frame.resize(400, 593)
                self.frame_81 = QFrame(self.my_rewards_frame)
                self.frame_81.setObjectName(u"frame_81")
                self.frame_81.setGeometry(QRect(0, 0, 400, 591))
                sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.frame_81.sizePolicy().hasHeightForWidth())
                self.frame_81.setSizePolicy(sizePolicy)
                self.frame_81.setMinimumSize(QSize(400, 591))
                self.frame_81.setMaximumSize(QSize(400, 591))
                self.frame_81.setStyleSheet(u"background-color:rgb(35, 47, 49);\n"
        "border:3px solid rgb(18, 140, 126);\n"
        "border-radius:10px;")
                self.frame_81.setFrameShape(QFrame.Shape.Panel)
                self.frame_81.setFrameShadow(QFrame.Shadow.Raised)
                self.line_14 = QFrame(self.frame_81)
                self.line_14.setObjectName(u"line_14")
                self.line_14.setGeometry(QRect(-20, 80, 431, 3))
                self.line_14.setMinimumSize(QSize(0, 3))
                self.line_14.setMaximumSize(QSize(16777215, 3))
                self.line_14.setStyleSheet(u"border:none;\n"
        "background-color:rgb(18, 140, 126);\n"
        "border-radius:0px;")
                self.line_14.setFrameShape(QFrame.Shape.HLine)
                self.line_14.setFrameShadow(QFrame.Shadow.Sunken)
                self.label_182 = QLabel(self.frame_81)
                self.label_182.setObjectName(u"label_182")
                self.label_182.setGeometry(QRect(120, 20, 161, 41))
                font = QFont()
                font.setPointSize(20)
                font.setBold(True)
                self.label_182.setFont(font)
                self.label_182.setStyleSheet(u"color:white; border:none;")
                self.frame = QFrame(self.frame_81)
                self.frame.setObjectName(u"frame")
                self.frame.setGeometry(QRect(10, 210, 381, 91))
                self.frame.setStyleSheet(u"background-color:rgb(7, 94, 84);\n"
        "border-radius:10px;\n"
        "border:none;")
                self.frame.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame.setFrameShadow(QFrame.Shadow.Raised)
                self.label_3 = QLabel(self.frame)
                self.label_3.setObjectName(u"label_3")
                self.label_3.setGeometry(QRect(523, 3, 16, 20))
                font1 = QFont()
                font1.setPointSize(13)
                self.label_3.setFont(font1)
                self.label_3.setStyleSheet(u"border:none;")
                self.pushButton = QPushButton(self.frame)
                self.pushButton.setObjectName(u"pushButton")
                self.pushButton.setGeometry(QRect(440, 60, 81, 31))
                font2 = QFont()
                font2.setPointSize(10)
                font2.setBold(True)
                font2.setUnderline(True)
                self.pushButton.setFont(font2)
                self.pushButton.setStyleSheet(u"border:none;\n"
        "color:rgb(35, 47, 49);")
                self.layoutWidget = QWidget(self.frame)
                self.layoutWidget.setObjectName(u"layoutWidget")
                self.layoutWidget.setGeometry(QRect(22, 4, 389, 88))
                self.horizontalLayout = QHBoxLayout(self.layoutWidget)
                self.horizontalLayout.setSpacing(15)
                self.horizontalLayout.setObjectName(u"horizontalLayout")
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.label = QLabel(self.layoutWidget)
                self.label.setObjectName(u"label")
                self.label.setMinimumSize(QSize(65, 60))
                self.label.setMaximumSize(QSize(65, 60))
                self.label.setStyleSheet(u"border:none;")
                self.label.setPixmap(QPixmap(u"../../Shivam/Downloads/wallet.png"))
                self.label.setScaledContents(True)

                self.horizontalLayout.addWidget(self.label)

                self.verticalLayout = QVBoxLayout()
                self.verticalLayout.setSpacing(0)
                self.verticalLayout.setObjectName(u"verticalLayout")
                self.label_2 = QLabel(self.layoutWidget)
                self.label_2.setObjectName(u"label_2")
                font3 = QFont()
                font3.setPointSize(18)
                font3.setBold(True)
                self.label_2.setFont(font3)
                self.label_2.setStyleSheet(u"color:white;")

                self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignBottom)

                self.label_13 = QLabel(self.layoutWidget)
                self.label_13.setObjectName(u"label_13")
                font4 = QFont()
                font4.setPointSize(10)
                self.label_13.setFont(font4)
                self.label_13.setStyleSheet(u"color:rgb(229, 229, 229);")

                self.verticalLayout.addWidget(self.label_13, 0, Qt.AlignmentFlag.AlignTop)


                self.horizontalLayout.addLayout(self.verticalLayout)

                self.frame_2 = QFrame(self.frame_81)
                self.frame_2.setObjectName(u"frame_2")
                self.frame_2.setGeometry(QRect(10, 100, 381, 91))
                self.frame_2.setStyleSheet(u"background-color:rgb(7, 94, 84);\n"
        "border-radius:10px;\n"
        "border:none;")
                self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
                self.my_rewars_login = QLabel(self.frame_2)
                self.my_rewars_login.setObjectName(u"my_rewars_login")
                self.my_rewars_login.setGeometry(QRect(523, 3, 16, 20))
                self.my_rewars_login.setFont(font1)
                self.my_rewars_login.setStyleSheet(u"border:none;")
                self.pushButton_2 = QPushButton(self.frame_2)
                self.pushButton_2.setObjectName(u"pushButton_2")
                self.pushButton_2.setGeometry(QRect(440, 60, 81, 31))
                self.pushButton_2.setFont(font2)
                self.pushButton_2.setStyleSheet(u"border:none;\n"
        "color:rgb(35, 47, 49);")
                self.layoutWidget_2 = QWidget(self.frame_2)
                self.layoutWidget_2.setObjectName(u"layoutWidget_2")
                self.layoutWidget_2.setGeometry(QRect(22, 4, 352, 88))
                self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_2)
                self.horizontalLayout_2.setSpacing(15)
                self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
                self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.label_6 = QLabel(self.layoutWidget_2)
                self.label_6.setObjectName(u"label_6")
                self.label_6.setMinimumSize(QSize(65, 60))
                self.label_6.setMaximumSize(QSize(65, 60))
                self.label_6.setStyleSheet(u"border:none;")
                self.label_6.setPixmap(QPixmap(u"../../Shivam/Downloads/wallet.png"))
                self.label_6.setScaledContents(True)

                self.horizontalLayout_2.addWidget(self.label_6)

                self.verticalLayout_2 = QVBoxLayout()
                self.verticalLayout_2.setSpacing(0)
                self.verticalLayout_2.setObjectName(u"verticalLayout_2")
                self.label_7 = QLabel(self.layoutWidget_2)
                self.label_7.setObjectName(u"label_7")
                self.label_7.setFont(font3)
                self.label_7.setStyleSheet(u"color:white;")

                self.verticalLayout_2.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignBottom)

                self.label_8 = QLabel(self.layoutWidget_2)
                self.label_8.setObjectName(u"label_8")
                self.label_8.setFont(font4)
                self.label_8.setStyleSheet(u"color:rgb(229, 229, 229);")

                self.verticalLayout_2.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignTop)


                self.horizontalLayout_2.addLayout(self.verticalLayout_2)

                self.frame_3 = QFrame(self.frame_81)
                self.frame_3.setObjectName(u"frame_3")
                self.frame_3.setGeometry(QRect(10, 320, 381, 91))
                self.frame_3.setStyleSheet(u"background-color:rgb(7, 94, 84);\n"
        "border-radius:10px;\n"
        "border:none;")
                self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
                self.my_rewars_welc = QLabel(self.frame_3)
                self.my_rewars_welc.setObjectName(u"my_rewars_welc")
                self.my_rewars_welc.setGeometry(QRect(523, 3, 16, 20))
                self.my_rewars_welc.setFont(font1)
                self.my_rewars_welc.setStyleSheet(u"border:none;")
                self.pushButton_3 = QPushButton(self.frame_3)
                self.pushButton_3.setObjectName(u"pushButton_3")
                self.pushButton_3.setGeometry(QRect(440, 60, 81, 31))
                self.pushButton_3.setFont(font2)
                self.pushButton_3.setStyleSheet(u"border:none;\n"
        "color:rgb(35, 47, 49);")
                self.layoutWidget_3 = QWidget(self.frame_3)
                self.layoutWidget_3.setObjectName(u"layoutWidget_3")
                self.layoutWidget_3.setGeometry(QRect(22, 4, 372, 88))
                self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_3)
                self.horizontalLayout_3.setSpacing(15)
                self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
                self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.label_10 = QLabel(self.layoutWidget_3)
                self.label_10.setObjectName(u"label_10")
                self.label_10.setMinimumSize(QSize(65, 60))
                self.label_10.setMaximumSize(QSize(65, 60))
                self.label_10.setStyleSheet(u"border:none;")
                self.label_10.setPixmap(QPixmap(u"../../Shivam/Downloads/wallet.png"))
                self.label_10.setScaledContents(True)

                self.horizontalLayout_3.addWidget(self.label_10)

                self.verticalLayout_3 = QVBoxLayout()
                self.verticalLayout_3.setSpacing(0)
                self.verticalLayout_3.setObjectName(u"verticalLayout_3")
                self.label_11 = QLabel(self.layoutWidget_3)
                self.label_11.setObjectName(u"label_11")
                self.label_11.setFont(font3)
                self.label_11.setStyleSheet(u"color:white;")

                self.verticalLayout_3.addWidget(self.label_11, 0, Qt.AlignmentFlag.AlignBottom)

                self.label_12 = QLabel(self.layoutWidget_3)
                self.label_12.setObjectName(u"label_12")
                self.label_12.setFont(font4)
                self.label_12.setStyleSheet(u"color:rgb(229, 229, 229);")

                self.verticalLayout_3.addWidget(self.label_12, 0, Qt.AlignmentFlag.AlignTop)
                self.my_rewards_frame.show()
                self.label_182.setText(QCoreApplication.translate("self.my_scratches_frame", u"My Rewards", None))
                self.label_3.setText(QCoreApplication.translate("self.my_scratches_frame", u"x", None))
                self.pushButton.setText(QCoreApplication.translate("self.my_scratches_frame", u"View", None))
                self.label.setText("")
                self.label_2.setText(QCoreApplication.translate("self.my_scratches_frame", u"MM Rewards", None))
                self.label_13.setText(QCoreApplication.translate("self.my_scratches_frame", u"for successful Login                                 +1000", None))
                self.my_rewars_login.setText(QCoreApplication.translate("self.my_scratches_frame", u"x", None))
                self.pushButton_2.setText(QCoreApplication.translate("self.my_scratches_frame", u"View", None))
                self.label_6.setText("")
                self.label_7.setText(QCoreApplication.translate("self.my_scratches_frame", u"MM Rewards", None))
                self.label_8.setText(QCoreApplication.translate("self.my_scratches_frame", u"Welcome Bonus                                       +2000", None))
                self.my_rewars_welc.setText(QCoreApplication.translate("self.my_scratches_frame", u"x", None))
                self.pushButton_3.setText(QCoreApplication.translate("self.my_scratches_frame", u"View", None))
                self.label_10.setText("")
                self.label_11.setText(QCoreApplication.translate("self.my_scratches_frame", u"MM Rewards", None))
                self.label_12.setText(QCoreApplication.translate("self.my_scratches_frame", u"First AC Service                                       +2000", None))

                self.horizontalLayout_3.addLayout(self.verticalLayout_3)
                self.frame_3.hide()  # Remaining to add condion  ----wait
                self.my_rewards_frame.show()
                # print(self.my_rewards_frame_visible)
                self.my_rewards_frame_visible = True
                
        else:
                self.my_rewards_frame.hide()
                self.my_rewards_frame_visible = False
                pass
        
    def refer_win_frame(self):
        if not self.refer_and_frame_visible:
                self.refer_and_frame = QFrame(self.mainmenu)
                self.refer_and_frame.setObjectName(u"self.refer_and_frame")
                self.refer_and_frame.setGeometry(350,170,500, 400)
                self.refer_and_frame.resize(500, 400)
                self.refer_and_frame.setMinimumSize(QSize(500, 400))
                self.refer_and_frame.setMaximumSize(QSize(500, 400))
                font = QFont()
                font.setPointSize(6)
                self.refer_and_frame.setFont(font)
                self.refer_and_frame.setStyleSheet(u"background-color:rgb(35, 47, 49);\n"
        "border:3px solid rgb(7, 94, 84);\n"
        "border-radius:10px;\n"
        "")
                self.refer_uploadimage_entry = QLineEdit(self.refer_and_frame)
                self.refer_uploadimage_entry.setObjectName(u"refer_uploadimage_entry")
                self.refer_uploadimage_entry.setGeometry(QRect(130, 253, 231, 41))
                self.refer_uploadimage_entry.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
        "border:none;")
                self.refer_uploadimage_entry.setReadOnly(True)
                self.refer_upload_button = QPushButton(self.refer_and_frame)
                self.refer_upload_button.setObjectName(u"refer_upload_button")
                self.refer_upload_button.setGeometry(QRect(296, 255, 63, 36))
                self.refer_upload_button.setStyleSheet(u"QPushButton\n"
        "{background-color: rgb(198, 198, 198);\n"
        "border:1px solid black;\n"
        "}\n"
        "\n"
        "QPushButton:hover\n"
        "{\n"
        "background-color:rgb(255, 255, 255);\n"
        "border:1px solid rgb(187, 187, 187);\n"
        "}\n"
        "")
                self.refer_Combobox_city = QComboBox(self.refer_and_frame)
                self.refer_Combobox_city.addItem("")
                self.refer_Combobox_city.addItem("")
                self.refer_Combobox_city.addItem("")
                self.refer_Combobox_city.addItem("")
                self.refer_Combobox_city.addItem("")
                self.refer_Combobox_city.setObjectName(u"refer_Combobox_city")
                self.refer_Combobox_city.setGeometry(QRect(80, 154, 341, 41))
                font1 = QFont()
                font1.setPointSize(9)
                self.refer_Combobox_city.setFont(font1)
                self.refer_Combobox_city.setStyleSheet(u"background-color: rgb(255, 255, 255); border:none;")
                self.refer_Combobox_city.setEditable(True)
                self.refer_Information = QLabel(self.refer_and_frame)
                self.refer_Information.setObjectName(u"refer_Information")
                self.refer_Information.setGeometry(QRect(50, 90, 401, 41))
                font2 = QFont()
                font2.setPointSize(12)
                self.refer_Information.setFont(font2)
                self.refer_Information.setStyleSheet(u"color:rgb(37, 211, 102); border:none;")
                self.refer_note = QLabel(self.refer_and_frame)
                self.refer_note.setObjectName(u"refer_note")
                self.refer_note.setGeometry(QRect(83, 200, 321, 31))
                font3 = QFont()
                font3.setPointSize(10)
                self.refer_note.setFont(font3)
                self.refer_note.setStyleSheet(u"color: rgb(198, 198, 198);\n"
        "border:none;")
                self.line = QFrame(self.refer_and_frame)
                self.line.setObjectName(u"line")
                self.line.setGeometry(QRect(0, 75, 501, 2))
                self.line.setMinimumSize(QSize(0, 2))
                self.line.setMaximumSize(QSize(16777215, 2))
                self.line.setStyleSheet(u"background-color: rgb(7, 94, 84);\n"
        "border:none;")
                self.line.setFrameShape(QFrame.Shape.HLine)
                self.line.setFrameShadow(QFrame.Shadow.Sunken)
                self.refer_Heading = QLabel(self.refer_and_frame)
                self.refer_Heading.setObjectName(u"refer_Heading")
                self.refer_Heading.setGeometry(QRect(52, 21, 391, 41))
                font4 = QFont()
                font4.setFamilies([u"Engravers MT"])
                font4.setPointSize(30)
                self.refer_Heading.setFont(font4)
                self.refer_Heading.setStyleSheet(u"color: rgb(255, 255, 255); border:none;")
                self.refer_close = QPushButton(self.refer_and_frame)
                self.refer_close.setObjectName(u"refer_close")
                self.refer_close.setGeometry(QRect(458, 4, 31, 15))
                font5 = QFont()
                font5.setPointSize(9)
                font5.setUnderline(True)
                self.refer_close.setFont(font5)
                self.refer_close.setCursor(QCursor(Qt.ClosedHandCursor))
                self.refer_close.setStyleSheet(u"border:none;\n"
        "color:rgb(198, 198, 198);")
                self.refer_close.setCheckable(True)
                self.refer_close.setAutoExclusive(False)
                self.refer_submit_earn = QPushButton(self.refer_and_frame)
                self.refer_submit_earn.setObjectName(u"refer_submit_earn")
                self.refer_submit_earn.setGeometry(QRect(165, 354, 170, 25))
                self.refer_submit_earn.setFont(font3)
                self.refer_submit_earn.setStyleSheet(u"QPushButton\n"
        "{background-color: rgb(37, 211, 102);\n"
        "border-radius:10px;\n"
        "border:none;\n"
        "}\n"
        "\n"
        "QPushButton:hover\n"
        "{\n"
        "	background-color: rgb(35, 47, 49);\n"
        "	border:1px solid rgb(37, 211, 102);\n"
        "	color:white;\n"
        "}")
                self.image_label = QLabel(self.refer_and_frame)
                pixmap = QPixmap(r"C:\Users\sanke\Downloads\image(2).png")
                self.image_label.setPixmap(pixmap)
                self.image_label.setGeometry(QRect(140, 300, 31, 31))
                self.image_label.setStyleSheet("border:none;")
                self.image_label = QLabel(self.refer_and_frame) 
                pixmap = QPixmap(r"C:\Users\sanke\Downloads\image(1).png")                
                scaled_pixmap = pixmap.scaled(31, 31, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.image_label.setPixmap(scaled_pixmap)
                self.image_label.setGeometry(QRect(140, 300, 31, 31))
                self.image_label.setStyleSheet("border:none;")  
                self.image_name_label = QLabel(self.refer_and_frame)
                self.image_name_label.setGeometry(QRect(180, 310, 90, 17))
                font5 = QFont()
                font5.setPointSize(9)
                self.image_name_label.setFont(font5)
                self.image_name_label.setText("imagename.png")
                self.image_name_label.setStyleSheet(u"color: rgb(198, 198, 198);\n"
        "border:none;")  
                self.image_name_label.show()
                self.image_name_label.hide()
                self.image_label.hide()
                self.refer_close.toggled.connect(self.refer_and_frame.close)
                self.refer_submit_earn.setCheckable(True)
                self.refer_uploadimage_entry.setPlaceholderText(QCoreApplication.translate("self.scratch_frame", u"Upload an Image", None))
                self.refer_upload_button.setText(QCoreApplication.translate("self.scratch_frame", u"Upload", None))
                self.refer_Combobox_city.setItemText(0, QCoreApplication.translate("self.scratch_frame", u"Mumbai", None))
                self.refer_Combobox_city.setItemText(1, QCoreApplication.translate("self.scratch_frame", u"Pune", None))
                self.refer_Combobox_city.setItemText(2, QCoreApplication.translate("self.scratch_frame", u"New Mumbai", None))
                self.refer_Combobox_city.setItemText(3, QCoreApplication.translate("self.scratch_frame", u"Kalyan", None))
                self.refer_Combobox_city.setItemText(4, QCoreApplication.translate("self.scratch_frame", u"Thane", None))

                self.refer_Combobox_city.setCurrentText(QCoreApplication.translate("self.scratch_frame", u"Mumbai", None))
                self.refer_Combobox_city.setPlaceholderText("")
                self.refer_Information.setText(QCoreApplication.translate("self.scratch_frame", u"Upload a picture of TO-LET board outside any house and \n"
        "                   Get \u20b9120 in your Paytm UPI Wallet", None))
                self.refer_note.setText(QCoreApplication.translate("self.scratch_frame", u"* Please enter locality to ensure faster response\n"
        "   from us", None))
                self.refer_Heading.setText(QCoreApplication.translate("self.scratch_frame", u"Refer & Earn", None))
                self.refer_close.setText(QCoreApplication.translate("self.scratch_frame", u"close", None))
                self.refer_submit_earn.setText(QCoreApplication.translate("self.scratch_frame", u"Submit", None))
        # retranslateUi
                self.refer_submit_earn.clicked.connect(self.confirm_uplo_image)
                self.refer_upload_button.clicked.connect(self.img_uplod)
                self.refer_and_frame.show()
                self.refer_and_frame_visible = True
        else:
            self.refer_and_frame.hide()
            self.refer_and_frame_visible= False
            pass
    
    def confirm_own_detail(self):
        print(self.contact_number.text(),self.select_city_lab.text(),self.select_prop_type.text(),self.tell_us_more.text())
        self.label_2.hide()
        self.label_3.hide()
        pixmap = QPixmap(u':/sanket/images/congratulation.png')                
        scaled_pixmap = pixmap.scaled(201, 201, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.label_2.setPixmap(scaled_pixmap)
        self.label_2.setGeometry(150,100,201,201)
        self.label_2.setStyleSheet("border:none;")  
        self.label_3.setGeometry(50,350,411,51)
        font = QFont()
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255,255,255);\n"
        "border:none;")
        self.label_3.setText("Congratulations! You have received \n 500 MM in cash")
        self.label_2.show()
        self.label_3.show()
        self.own_button.hide()
        self.lineEdit.hide()
        # self.refer_Heading.hide()
        self.owner_frm.hide()
        # self.refer_close.hide()
        self.contact_number.hide()
        self.select_city_lab.hide()
        self.select_prop_type.hide()
        self.tell_us_more.hide()
        self.MMcash += 500
        self.label_131.setText(QCoreApplication.translate("MainWindow", str(self.MMcash) +  " MM cash will expire in ", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", str(self.MMcash) + " MMcash", None))

        
    def confirm_uplo_image(self):
        self.MMcash += 2000
        self.label_131.setText(QCoreApplication.translate("MainWindow", str(self.MMcash) +  " MM cash will expire in ", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", str(self.MMcash) + " MMcash", None))
        selected_text = self.refer_Combobox_city.currentText()
        print(selected_text,self.image_name_label.text())
        self.refer_upload_button.hide()
        self.refer_Combobox_city.hide()
        self.refer_Information.hide()
        self.refer_note.hide()
        self.refer_uploadimage_entry.hide()
        self.refer_uploadimage_entry.hide()
        self.refer_submit_earn.hide()
        self.image_name_label.hide()
        self.image_label.hide()
        pixmap = QPixmap(u':/sanket/images/congratulation.png')                
        scaled_pixmap = pixmap.scaled(201, 201, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setGeometry(150,60,201,201)
        self.image_label.setStyleSheet("border:none;")  
        self.image_name_label.setGeometry(60,270,411,51)
        font = QFont()
        font.setPointSize(17)
        self.image_name_label.setFont(font)
        self.image_name_label.setStyleSheet(u"color: rgb(255,255,255);\n"
        "border:none;")
        self.image_name_label.setText("Congratulations! You have received 2000 MM in cash")
        self.image_label.show()
        self.image_name_label.show()
        self.refer_Heading.hide()
        self.line.hide()
        
        
    def img_uplod(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg)")
        file_dialog.setViewMode(QFileDialog.List)
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            image_name = os.path.basename(file_path)
            self.image_name_label.setText(image_name)
            self.image_name_label.show()
            self.image_label.show()
        else:
            print("The path is not selected")
            
        
        pass    
    def owner_win_frame(self):
        if not self.owner_frame_visible:
            self.owner_frame = QFrame(self.mainmenu)
            self.owner_frame.setObjectName(u"self.owner_frame")
            self.owner_frame.setGeometry(290,150,505, 521)
            self.owner_frame.resize(505, 521)
            self.owner_frame.setMinimumSize(QSize(505, 521))
            self.owner_frame.setMaximumSize(QSize(505, 521))
            self.owner_frame.setStyleSheet(u"background-color:rgb(35, 47, 49);\n"
    "border:2px solid rgb(7, 94, 84);\n"
    "border-radius:10px;")
            self.line = QFrame(self.owner_frame)
            self.line.setObjectName(u"line")
            self.line.setGeometry(QRect(2, 80, 501, 2))
            self.line.setMinimumSize(QSize(0, 2))
            self.line.setMaximumSize(QSize(16777215, 2))
            self.line.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            self.line.setFrameShape(QFrame.Shape.HLine)
            self.line.setFrameShadow(QFrame.Shadow.Sunken)
            self.label_2 = QLabel(self.owner_frame)
            self.label_2.setObjectName(u"label_2")
            self.label_2.setGeometry(QRect(39, 101, 431, 21))
            font = QFont()
            font.setPointSize(10)
            self.label_2.setFont(font)
            self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
    "border:none;")
            self.label_3 = QLabel(self.owner_frame)
            self.label_3.setObjectName(u"label_3")
            self.label_3.setGeometry(QRect(41, 125, 421, 31))
            self.label_3.setStyleSheet(u"color:rgb(37, 211, 102);\n"
    "border:none;")
            self.own_button = QPushButton(self.owner_frame)
            self.own_button.setObjectName(u"pushButton")
            self.own_button.setGeometry(QRect(170, 463, 161, 31))
            self.own_button.setStyleSheet(u"QPushButton\n"
    "{background-color: rgb(37, 211, 102);\n"
    "border-radius:10px;\n"
    "border:none;\n"
    "}\n"
    "\n"
    "QPushButton:hover\n"
    "{\n"
    "	background-color: rgb(35, 47, 49);\n"
    "	border:1px solid rgb(37, 211, 102);\n"
    "	color:white;\n"
    "}")
            self.refer_Heading = QLabel(self.owner_frame)
            self.refer_Heading.setObjectName(u"refer_Heading")
            self.refer_Heading.setGeometry(QRect(60, 24, 391, 41))
            font1 = QFont()
            font1.setFamilies([u"Engravers MT"])
            font1.setPointSize(30)
            self.refer_Heading.setFont(font1)
            self.refer_Heading.setStyleSheet(u"color: rgb(255, 255, 255);\n"
    "border:none;")
            self.refer_close = QPushButton(self.owner_frame)
            self.refer_close.setObjectName(u"refer_close")
            self.refer_close.setGeometry(QRect(464, 5, 31, 15))
            font2 = QFont()
            font2.setPointSize(9)
            font2.setUnderline(True)
            self.refer_close.setFont(font2)
            self.refer_close.setCursor(QCursor(Qt.ClosedHandCursor))
            self.refer_close.setStyleSheet(u"border:none;\n"
    "color:rgb(198, 198, 198);")
            self.refer_close.setCheckable(True)
            self.refer_close.setAutoRepeat(False)
            self.refer_close.setAutoExclusive(True)
            self.contact_number = QLineEdit(self.owner_frame)
            self.contact_number.setObjectName(u"contact_number")
            self.contact_number.setGeometry(QRect(51, 229, 400, 35))
            self.contact_number.setMinimumSize(QSize(0, 35))
            self.contact_number.setBaseSize(QSize(0, 35))
            self.contact_number.setStyleSheet(u"QLineEdit\n"
    "{background-color: rgb(255, 255, 255);\n"
    "border:none;\n"
    "border-radius:none;\n"
    "}\n"
    "\n"
    "QLineEdit:hover\n"
    "{\n"
    "border-bottom:2px solid rgb(18, 140, 126);\n"
    "}")
            self.owner_frm = QLineEdit(self.owner_frame) # type: ignore
            self.owner_frm.setObjectName(u"owner_frm")
            self.owner_frm.setGeometry(QRect(51, 286, 400, 35))
            self.owner_frm.setMinimumSize(QSize(0, 35))
            self.owner_frm.setBaseSize(QSize(0, 35))
            self.owner_frm.setStyleSheet(u"QLineEdit\n"
    "{background-color: rgb(255, 255, 255);\n"
    "border:none;\n"
    "border-radius:none;\n"
    "}\n"
    "\n"
    "QLineEdit:hover\n"
    "{\n"
    "border-bottom:2px solid rgb(18, 140, 126);\n"
    "}")
            self.select_city_lab = QLineEdit(self.owner_frame)
            self.select_city_lab.setObjectName(u"select_city_lab")
            self.select_city_lab.setGeometry(QRect(51, 172, 400, 35))
            self.select_city_lab.setMinimumSize(QSize(0, 35))
            self.select_city_lab.setBaseSize(QSize(0, 35))
            self.select_city_lab.setStyleSheet(u"QLineEdit\n"
    "{background-color: rgb(255, 255, 255);\n"
    "border:none;\n"
    "border-radius:none;\n"
    "}\n"
    "\n"
    "QLineEdit:hover\n"
    "{\n"
    "border-bottom:2px solid rgb(18, 140, 126);\n"
    "}")
            self.select_prop_type = QLineEdit(self.owner_frame)
            self.select_prop_type.setObjectName(u"select_prop_type")
            self.select_prop_type.setGeometry(QRect(51, 343, 400, 35))
            self.select_prop_type.setMinimumSize(QSize(0, 35))
            self.select_prop_type.setBaseSize(QSize(0, 35))
            self.select_prop_type.setStyleSheet(u"QLineEdit\n"
    "{background-color: rgb(255, 255, 255);\n"
    "border:none;\n"
    "border-radius:none;\n"
    "}\n"
    "\n"
    "QLineEdit:hover\n"
    "{\n"
    "border-bottom:2px solid rgb(18, 140, 126);\n"
    "}")
            self.tell_us_more = QLineEdit(self.owner_frame)
            self.tell_us_more.setObjectName(u"tell_us_more")
            self.tell_us_more.setGeometry(QRect(51, 400, 400, 35))
            self.tell_us_more.setMinimumSize(QSize(0, 35))
            self.tell_us_more.setBaseSize(QSize(0, 35))
            self.tell_us_more.setStyleSheet(u"QLineEdit\n"
                "{background-color: rgb(255, 255, 255);\n"
                "border:none;\n"
                "border-radius:none;\n"
                "}\n"
                "\n"
                "QLineEdit:hover\n"
                "{\n"
                "border-bottom:2px solid rgb(18, 140, 126);\n"
                "}")
            self.label_2.setText(QCoreApplication.translate("self.scratch_frame", u"Provide Owner Contact & Get up to 2000MM cash in your account directly", None))
            self.label_3.setText(QCoreApplication.translate("self.scratch_frame", u"Please enter correct owner's name & phone to ensure faster response from us.", None))
            self.own_button.setText(QCoreApplication.translate("self.scratch_frame", u"Send Details", None))
            self.refer_Heading.setText(QCoreApplication.translate("self.scratch_frame", u"Refer & Earn", None))
            self.refer_close.setText(QCoreApplication.translate("self.scratch_frame", u"close", None))
            self.contact_number.setPlaceholderText(QCoreApplication.translate("self.scratch_frame", u"Owner contact number ", None))
            self.owner_frm.setPlaceholderText(QCoreApplication.translate("self.scratch_frame", u"Owner Name", None))
            self.select_city_lab.setPlaceholderText(QCoreApplication.translate("self.scratch_frame", u"Select City", None))
            self.select_prop_type.setPlaceholderText(QCoreApplication.translate("self.scratch_frame", u"Select property type", None))
            self.tell_us_more.setPlaceholderText(QCoreApplication.translate("self.scratch_frame", u"Tell us more ", None))
            self.refer_close.toggled.connect(self.owner_frame.close)
            self.own_button.clicked.connect(self.confirm_own_detail)
            self.owner_frame.show()
            self.owner_frame_visible = True
        else:
             self.owner_frame.hide()
             self.owner_frame_visible = False
        

    def addme(self):
        self.add_dis += 10
        if self.add_dis < 10 or self.add_dis > 100:
            self.add_dis = 10
            self.lineEdit.setText(str(10))
        else:
            self.lineEdit.setText(str(self.add_dis))
        self.update_need_to_pay(self.add_dis)
        
                
    def subme(self):
        self.subtracting = int(self.lineEdit.text()) - 10
        if self.subtracting < 10 or self.subtracting > 100:
            self.subtracting = 10
            self.lineEdit.setText(str(10))
        else:
            self.lineEdit.setText(str(self.subtracting))
        self.update_need_to_pay(self.subtracting)
        
    def update_need_to_pay(self, value):
        # Mapping of discounts to amounts
                self.amount_map = {
                10: "1100",
                15: "1150",
                20: "1200",
                30: "1300",
                40: "1400",
                50: "1500",
                60: "1600",
                70: "1700",
                80: "1800",
                90: "4000",
                100: "10000"
                }
                self.need_to_pay.setText(self.amount_map.get(value, "Error"))        
                self.str_value = value

                
    def image_show_code(self,image_path):
        image_name = os.path.basename(image_path)
        print(int(self.need_to_pay.text()))
        print(image_name)
        if image_name == "Ama.png":
                self.amazonbutton.setEnabled(False)
                self.scratches_ama = 1
                pass
        elif image_name == "Dominos_by_scratch.png":
                self.Dominosbutton.setEnabled(False)
                self.scratches_domi = 2


                pass
        elif image_name == "PizzaHut.png":
                self.PizzaHutbutton.setEnabled(False)
                self.scratches_pizu = 3


                pass
        elif image_name == "flipkart_by_scratch.png":
                self.FlipkartButton.setEnabled(False)
                self.scratches_flp = 4
             
                pass
        elif image_name == "Myntra1_by_scratch.png":
                self.Myntrabutton.setEnabled(False)
                self.scratches_myn = 5

                pass
        elif image_name == "Zomato_by_scratch.jpg":
                self.zomatobutton.setEnabled(False)
                self.scratches_zmt = 6

                pass
        else:
                print("No one scratch car are selected ")
                pass
        temp_mm = int(self.need_to_pay.text())
        if  temp_mm == 0 or temp_mm == None:
                print("You can't")
        elif temp_mm <= self.MMcash:
                self.MMcash -= temp_mm
                print("You can",self.MMcash)
                self.label_16.hide()
                self.pushButton_9.setEnabled(False)
                self.layout = QVBoxLayout()
                self.frame.setLayout(self.layout)

                self.layout.addWidget(self.label)
                pixmap = QPixmap(image_path)  # Replace with your image path
                self.label.setPixmap(pixmap)
                self.label.setGeometry(QRect(50, 50, pixmap.width(), pixmap.height()))

                self.opacity_effect = QGraphicsOpacityEffect()
                self.label.setGraphicsEffect(self.opacity_effect)

                self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
                self.animation.setDuration(3000)
                self.animation.setStartValue(1.0)
                self.animation.setEndValue(0.0)
                # movie.start()
                self.animation.start()
                # self.no_scratches_frame.deleteLater()
                self.label_131.setText(QCoreApplication.translate("MainWindow", str(self.MMcash) +  " MM cash will expire in ", None))
                self.pushButton_14.setText(QCoreApplication.translate("MainWindow", str(self.MMcash) + " MMcash", None))
                self.pushButton_12.clicked.disconnect(self.noscratches_win_frame)
                self.pushButton_12.clicked.connect(self.myscratches_win_frame)

                

                
        else:
                print("You can't")
        # print(self.amount_map.get(self.str_value))
        # if self.MMcash >= 
        

    def scratch_payment_chng(self):
            
        
        pass

    def scratch_win_which(self,Scracth1):
        print(Scracth1)
        if Scracth1 == 1:
                head_label = "Amazon"
                image_path = r":/sanket/images/Ama.png"
                refer_code = "Am1250"
        elif Scracth1 == 2:
                head_label = "Dominos"
                image_path = r":/sanket/images/Dominos_by_scratch.png"
                refer_code = "DP2024"
                
        elif Scracth1 == 3:
                head_label = "Pizza Hut"
                image_path = r":/sanket/images/PizzaHut.png"
                refer_code = "PHHUT15"
                
        elif Scracth1 == 4:
                head_label = "Flipkart"
                image_path = r":/sanket/images/flipkart_by_scratch.png"
                refer_code = "FP14c"
                
        elif Scracth1 == 5:
                head_label = "Myntra"
                image_path = r":/sanket/images/Myntra1_by_scratch.png"
                refer_code = "MSale150"
                
        elif Scracth1 == 6:
                head_label = "Zomato"
                image_path = u':/sanket/images/Zomato_by_scratch.jpg' 
                refer_code = "ZOMATO19"
        else:
            print("Something wrong ")
            
        self.scratch_win_frame(head_label,image_path,refer_code)
        
    def scratch_win_frame(self,head_label,image_path,refer_code):
        if not self.scratch_frame_visible:
            self.scratch_frame = QFrame(self.mainmenu)
            self.scratch_frame.setObjectName(u"self.scratch_frame")
            self.scratch_frame.setGeometry(220,150,690, 420)
            self.scratch_frame.resize(690, 420)
            self.scratch_frame.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
    "border:3px solid rgb(18, 140, 126);\n"
    "border-radius:10px;")
            self.frame = QFrame(self.scratch_frame)
            self.frame.setObjectName(u"frame")
            self.frame.setGeometry(QRect(30, 60, 331, 231))
            self.frame.setStyleSheet(u"\n"
    "background-color:white;")
            self.frame.setFrameShape(QFrame.Shape.StyledPanel)
            self.frame.setFrameShadow(QFrame.Shadow.Raised)
            
            self.label_15 = QLabel(self.frame)
            self.label_15.setObjectName(u"label_15")
            self.label_15.setGeometry(QRect(130, 100, 95, 31))
            font = QFont()
            font.setPointSize(14)
            font.setBold(True)
            self.label.setFont(font)
            fontre = QFont()
            fontre.setPointSize(12)
            fontre.setBold(True)
            self.label_15.setStyleSheet(u"border:none;")
            self.label_15.setFont(fontre)
            self.label_16 = QLabel(self.frame)
            self.label_16.setObjectName(u"label_16")
            self.label_16.setGeometry(QRect(20, 20, 291, 181))
            self.label_16.setStyleSheet(u"border:none;")
            self.frame_2 = QFrame(self.scratch_frame)
            self.frame_2.setObjectName(u"frame_2")
            self.frame_2.setGeometry(QRect(419, 41, 261, 141))
            self.frame_2.setStyleSheet(u"border:1px solid white;\n"
    "border-radius:0px;\n"
    "")
            self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
            self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
            self.label = QLabel(self.frame_2)
            self.label.setObjectName(u"label")
            self.label.setGeometry(QRect(22, 15, 131, 21))
            font = QFont()
            font.setPointSize(14)
            font.setBold(True)
            self.label.setFont(font)
            self.label.setStyleSheet(u"border:none; color:white;")
            self.button_10_per = QPushButton(self.frame_2)
            self.button_10_per.setObjectName(u"button_10_per")
            self.button_10_per.setGeometry(QRect(12, 55, 75, 24))
            self.button_10_per.setStyleSheet(u"background-color: rgb(37, 211, 102);\n"
    "border-radius:10px;\n"
    "border:none;")
            self.button_25_per = QPushButton(self.frame_2)
            self.button_25_per.setObjectName(u"button_25_per")
            self.button_25_per.setGeometry(QRect(92, 55, 75, 24))
            self.button_25_per.setStyleSheet(u"background-color: rgb(37, 211, 102);\n"
    "border-radius:10px;\n"
    "border:none;")
            self.button_50_per = QPushButton(self.frame_2)
            self.button_50_per.setObjectName(u"button_50_per")
            self.button_50_per.setGeometry(QRect(12, 95, 75, 24))
            self.button_50_per.setStyleSheet(u"background-color: rgb(37, 211, 102);\n"
    "border-radius:10px;\n"
    "border:none;")
            self.button_60_per = QPushButton(self.frame_2)
            self.button_60_per.setObjectName(u"button_60_per")
            self.button_60_per.setGeometry(QRect(92, 95, 75, 24))
            self.button_60_per.setStyleSheet(u"background-color: rgb(37, 211, 102);\n"
    "border-radius:10px;\n"
    "border:none;")
            self.button_40_per = QPushButton(self.frame_2)
            self.button_40_per.setObjectName(u"button_40_per")
            self.button_40_per.setGeometry(QRect(172, 55, 75, 24))
            self.button_40_per.setStyleSheet(u"background-color: rgb(37, 211, 102);\n"
    "border-radius:10px;\n"
    "border:none;")
            self.button_80_per = QPushButton(self.frame_2)
            self.button_80_per.setObjectName(u"button_80_per")
            self.button_80_per.setGeometry(QRect(172, 95, 75, 24))
            self.button_80_per.setStyleSheet(u"background-color: rgb(37, 211, 102);\n"
    "border-radius:10px;\n"
    "border:none;")
            self.layoutWidget = QWidget(self.frame_2)
            self.layoutWidget.setObjectName(u"layoutWidget")
            self.layoutWidget.setGeometry(QRect(161, 8, 94, 33))
            self.horizontalLayout = QHBoxLayout(self.layoutWidget)
            self.horizontalLayout.setObjectName(u"horizontalLayout")
            self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.pushButton_sub_per = QPushButton(self.layoutWidget)
            self.pushButton_sub_per.setObjectName(u"pushButton_sub_per")
            font1 = QFont()
            font1.setPointSize(17)
            self.pushButton_sub_per.setFont(font1)
            self.pushButton_sub_per.setStyleSheet(u"border:none;")

            self.horizontalLayout.addWidget(self.pushButton_sub_per)

            self.lineEdit = QLineEdit(self.layoutWidget)
            self.lineEdit.setObjectName(u"lineEdit")
            self.lineEdit.setStyleSheet(u"background:none;\n"
    "border:none;")
            self.lineEdit.setInputMethodHints(Qt.InputMethodHint.ImhDate)

            self.horizontalLayout.addWidget(self.lineEdit)

            self.pushbutton_add_per = QPushButton(self.layoutWidget)
            self.pushbutton_add_per.setObjectName(u"pushbutton_add_per")
            self.pushbutton_add_per.setFont(font1)
            self.pushbutton_add_per.setStyleSheet(u"border:none;")

            self.horizontalLayout.addWidget(self.pushbutton_add_per)

            self.label_2 = QLabel(self.scratch_frame)
            self.label_2.setObjectName(u"label_2")
            self.label_2.setGeometry(QRect(430, 190, 131, 21))
            self.label_2.setStyleSheet(u"border:none; color:white;")
            self.label_3 = QLabel(self.scratch_frame)
            self.label_3.setObjectName(u"label_3")
            self.label_3.setGeometry(QRect(430, 226, 81, 16))
            self.label_3.setStyleSheet(u"border:none; color:white;")
            self.line = QFrame(self.scratch_frame)
            self.line.setObjectName(u"line")
            self.line.setGeometry(QRect(430, 240, 241, 16))
            self.line.setStyleSheet(u"border:none; color:white;")
            self.line.setFrameShape(QFrame.Shape.HLine)
            self.line.setFrameShadow(QFrame.Shadow.Sunken)
            self.need_to_pay = QLabel(self.scratch_frame)
            self.need_to_pay.setObjectName(u"need_to_pay")
            self.need_to_pay.setGeometry(QRect(623, 226, 31, 16))
            self.need_to_pay.setStyleSheet(u"border:none; color:white;")
            self.label_5 = QLabel(self.scratch_frame)
            self.label_5.setObjectName(u"label_5")
            self.label_5.setGeometry(QRect(430, 250, 51, 16))
            self.label_5.setStyleSheet(u"border:none; color:white;")
            self.need_to_pay = QLabel(self.scratch_frame)
            self.need_to_pay.setObjectName(u"need_to_pay")
            self.need_to_pay.setGeometry(QRect(623, 250, 31, 16))
            self.need_to_pay.setStyleSheet(u"border:none; color:white;")
            self.line_2 = QFrame(self.scratch_frame)
            self.line_2.setObjectName(u"line_2")
            self.line_2.setGeometry(QRect(0, 320, 690, 2))
            self.line_2.setMinimumSize(QSize(0, 2))
            self.line_2.setMaximumSize(QSize(16777215, 2))
            self.line_2.setStyleSheet(u"border:none; color:white;\n"
    "background-color: rgb(18, 140, 126);")
            self.line_2.setFrameShape(QFrame.Shape.HLine)
            self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
            self.pushButton_9 = QPushButton(self.scratch_frame)
            self.pushButton_9.setObjectName(u"pushButton_9")
            self.pushButton_9.setGeometry(QRect(430, 280, 221, 31))
            self.pushButton_9.setStyleSheet(u"background-color: rgb(37, 211, 102);\n"
    "border-radius:10px; border:none;")
            self.label_7 = QLabel(self.scratch_frame)
            self.label_7.setObjectName(u"label_7")
            self.label_7.setGeometry(QRect(34, 6, 71, 16))
            self.label_7.setStyleSheet(u"border:none; color:white;")
            self.label_8 = QLabel(self.scratch_frame)
            self.label_8.setObjectName(u"label_8")
            self.label_8.setGeometry(QRect(19, 5, 15, 15))
            font2 = QFont()
            font2.setPointSize(12)
            self.label_8.setFont(font2)
            self.label_8.setStyleSheet(u"border:none; color:white;")
            self.label_9 = QLabel(self.scratch_frame)
            self.label_9.setObjectName(u"label_9")
            self.label_9.setGeometry(QRect(110, 6, 44, 16))
            self.label_9.setStyleSheet(u"border:none; color:white;")
            self.line_4 = QFrame(self.scratch_frame)
            self.line_4.setObjectName(u"line_4")
            self.line_4.setGeometry(QRect(0, 27, 690, 2))
            self.line_4.setMinimumSize(QSize(0, 2))
            self.line_4.setMaximumSize(QSize(16777215, 2))
            self.line_4.setStyleSheet(u"border:none;\n"
    "background-color: rgb(16, 127, 115);")
            self.line_4.setFrameShape(QFrame.Shape.HLine)
            self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
            self.label_10 = QLabel(self.scratch_frame)
            self.label_10.setObjectName(u"label_10")
            self.label_10.setGeometry(QRect(20, 330, 71, 21))
            font3 = QFont()
            font3.setBold(True)
            font3.setUnderline(True)
            self.label_10.setFont(font3)
            self.label_10.setStyleSheet(u"border:none; color:white;")
            self.label_11 = QLabel(self.scratch_frame)
            self.label_11.setObjectName(u"label_11")
            self.label_11.setGeometry(QRect(100, 330, 83, 21))
            self.label_11.setStyleSheet(u"border:none; color:white;")
            self.label_12 = QLabel(self.scratch_frame)
            self.label_12.setObjectName(u"label_12")
            self.label_12.setGeometry(QRect(200, 330, 101, 21))
            self.label_12.setStyleSheet(u"border:none; color:white;")
            self.label_13 = QLabel(self.scratch_frame)
            self.label_13.setObjectName(u"label_13")
            self.label_13.setGeometry(QRect(310, 330, 111, 21))
            self.label_13.setStyleSheet(u"border:none; color:white;")
            self.label_14 = QLabel(self.scratch_frame)
            self.label_14.setObjectName(u"label_14")
            self.label_14.setGeometry(QRect(20, 350, 641, 61))
            self.label_14.setStyleSheet(u"border:none; color:rgb(198, 198, 198);")
            self.refer_close = QPushButton(self.scratch_frame)
            self.refer_close.setObjectName(u"refer_close")
            self.refer_close.setGeometry(QRect(647, 7, 31, 15))
            self.label_16.setPixmap(QPixmap(image_path))
            font4 = QFont()
            font4.setPointSize(9)
            font4.setUnderline(True)
            self.refer_close.setFont(font4)
            self.refer_close.setCursor(QCursor(Qt.ClosedHandCursor))
            self.refer_close.setStyleSheet(u"border:none;\n"
    "color:rgb(198, 198, 198);")
            self.refer_close.setCheckable(True)
            self.refer_close.setAutoRepeat(False)
            self.refer_close.setAutoExclusive(True)
            self.label_15.setText(refer_code)
            self.label_16.setText("")
            self.label.setText(QCoreApplication.translate("self.my_rewards_frame", u"Card Discount", None))
            self.button_10_per.setText(QCoreApplication.translate("self.my_rewards_frame", u"10%", None))
            self.button_25_per.setText(QCoreApplication.translate("self.my_rewards_frame", u"25%", None))
            self.button_50_per.setText(QCoreApplication.translate("self.my_rewards_frame", u"50%", None))
            self.button_60_per.setText(QCoreApplication.translate("self.my_rewards_frame", u"60%", None))
            self.button_40_per.setText(QCoreApplication.translate("self.my_rewards_frame", u"40%", None))
            self.button_80_per.setText(QCoreApplication.translate("self.my_rewards_frame", u"80%", None))
            self.pushButton_sub_per.setText(QCoreApplication.translate("self.my_rewards_frame", u"-", None))
            self.pushbutton_add_per.setText(QCoreApplication.translate("self.my_rewards_frame", u"+", None))
            self.label_2.setText(QCoreApplication.translate("self.my_rewards_frame", u"Payment Sumaary", None))
            self.label_3.setText(QCoreApplication.translate("self.my_rewards_frame", u"Total Amount ", None))
            self.need_to_pay.setText(QCoreApplication.translate("self.my_rewards_frame", u"0", None))
            self.label_5.setText(QCoreApplication.translate("self.my_rewards_frame", u"To Pay", None))
            self.need_to_pay.setText(QCoreApplication.translate("self.my_rewards_frame", u"0", None))
            self.pushButton_9.setText(QCoreApplication.translate("self.my_rewards_frame", u"Checkout", None))
            self.label_7.setText(QCoreApplication.translate("self.my_rewards_frame", u"E-Gift Cards", None))
            self.label_8.setText(QCoreApplication.translate("self.my_rewards_frame", u"<", None))
            self.label_9.setText(head_label)
            self.label_10.setText(QCoreApplication.translate("self.my_rewards_frame", u"Description", None))
            self.label_11.setText(QCoreApplication.translate("self.my_rewards_frame", u"How to redeem", None))
            self.label_12.setText(QCoreApplication.translate("self.my_rewards_frame", u"How to Instruction", None))
            self.label_13.setText(QCoreApplication.translate("self.my_rewards_frame", u"Term and Condition", None))
            self.label_14.setText(QCoreApplication.translate("self.my_rewards_frame", u"Discover convenience with the Amazon Pay Gift Card from GyFTR. Seamlessly add it to your Amazon Pay balance and\n"
    "use it for vouchers, groceries via Amazon Fresh, and mobile recharges. Shop across 10 Cr+ products on Amazon.in and\n"
    "30,000+ apps, including Zomato, Myntra, Pizza Hut, and Flipkart.", None))
            self.refer_close.setText(QCoreApplication.translate("self.my_rewards_frame", u"close", None))
            self.refer_close.toggled.connect(self.scratch_frame.close)
            self.pushbutton_add_per.clicked.connect(self.addme)
            self.pushButton_sub_per.clicked.connect(self.subme)
            self.button_10_per.clicked.connect(lambda : self.lineEdit.setText(str(10)))
            self.button_25_per.clicked.connect(lambda : self.lineEdit.setText(str(25)))
            self.button_50_per.clicked.connect(lambda : self.lineEdit.setText(str(50)))
            self.button_60_per.clicked.connect(lambda : self.lineEdit.setText(str(60)))
            self.button_40_per.clicked.connect(lambda : self.lineEdit.setText(str(40)))
            self.button_80_per.clicked.connect(lambda : self.lineEdit.setText(str(80)))
            self.lineEdit.setReadOnly(True)

            # Payment changing
            self.button_10_per.clicked.connect(lambda : self.need_to_pay.setText(str(1000)))
            self.button_25_per.clicked.connect(lambda : self.need_to_pay.setText(str(1250)))
            self.button_50_per.clicked.connect(lambda : self.need_to_pay.setText(str(1500)))
            self.button_60_per.clicked.connect(lambda : self.need_to_pay.setText(str(1650)))
            self.button_40_per.clicked.connect(lambda : self.need_to_pay.setText(str(1450)))
            self.button_80_per.clicked.connect(lambda : self.need_to_pay.setText(str(2000)))
            self.refer_close.toggled.connect(self.scratch_frame.close)
            self.pushButton_9.clicked.connect(lambda: self.image_show_code(image_path) )
            self.scratch_frame.show()
            self.scratch_frame_visible = True
        else:
            self.scratch_frame.hide()
            self.scratch_frame_visible  = False   
        
    def gmail_code(self):
        receiver_email = "sanketangane2006@gmail.com"  # Replace with actual receiver email
        subject = self.viaemail_subject
        
        # Define your HTML message
        message = f"""<html>
                        <body>
                            <p>Hi The Middle Man Team</p>
                            <p>I hope this message finds you well. I am excited to share with you an exceptional opportunity to own/rent a beautiful [property type] in the heart of [location]. This property offers the perfect blend of comfort, luxury, and convenience.</p>
                            <p>I am writing to share some content/information that I believe would be valuable for The Middle Man application:</p>
                            
                            <p>{self.viaemail_body}</p>
                            
                            <p>Thank you for your time and consideration.</p>
                            <p>Best regards,</p>
                            <p>middleman3701@gmail.com<br>
                            9097667158<br>
                            {receiver_email}</p>
                        </body>
                    </html>"""

        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # Correct SMTP port for TLS
        sender_email = 'middleman3701@gmail.com'  # Your email
        sender_password = "wtkh syvj zptd elfa"  # Your email password or app password

        msg = MIMEMultipart('related')
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Attach the HTML message to the MIME message
        msg.attach(MIMEText(message, 'html'))

        try:
            # Connect to SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Start TLS encryption
            # Login to SMTP server
            server.login(sender_email, sender_password)
            # Send email
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email. Error: {str(e)}")
        finally:
            # Close the connection
            server.quit()
            
    def contact_us_wp(self):
        pass

    def contact_us_email(self):
        self.viawp = self.plainTextEdit.toPlainText()
        self.viaemail_body = self.plainTextEdit_2.toPlainText()
        self.viaemail_subject = self.lineEdit.text()
        email_subject_length = len(self.viaemail_subject)
        email_body_length = len(self.viaemail_subject)
        print(self.viaemail_body, email_body_length)
        if self.viaemail_subject == None or self.viaemail_body == None:
                self.label_4.setText("Please fill all the fields")
        else:
            if email_body_length >= 40 and email_subject_length >= 10 :
                self.gmail_code()
            else:
                print(self.viawp,self.viaemail_body,self.viaemail_subject)
        
    def fetch_city_price_type(self): # This are the search Button after clicking the search button this will fetch Value
        self.user_local_area_vl = self.lineEdit_3.text()
        self.frame_39.hide()
        self.frame_40.hide()
        self.frame_41.hide()
        self.frame_42.hide()
        self.frame_43.hide()
        self.frame_44.hide()
        self.frame_45.hide()
        self.frame_46.hide()
        if self.user_local_area_vl == "Sukhwani Nysa":
                # self.frame_39.show()
                self.frame_46.show()
                # self.frame_44.show()
      
        
        print(f"User City: {self.cmb_city}, Price: {self.actual_value}, Item Text: {self.item_text}, User Local Area: {self.user_local_area_vl}")
       
        pass

    def see_type(self, index): # This are the Selecting the bhk type 
        self.item_text = self.filter_comboBox.itemText(index)
        if self.item_text == " 1 BHK":
            self.values = self.values1
            print("For 1BHK",self.values)
        elif self.item_text == "  2 BHK":
            self.values = self.values2
            print("For 2BHK",self.values)
        elif self.item_text == "  3 BHK":
            self.values = self.values3
            print("For 3BHK",self.values)
        elif self.item_text ==  "  Others...":
            self.values = self.valuesoth
            print("For otBHK",self.values)
        else:
            self.values = []  # Handle unexpected case

        self.value_map = {i: value for i, value in enumerate(self.values)}
        self.horizontalSlider.setMaximum(len(self.values) - 1)


        print(self.value_map)
        print(self.item_text)

    def call_me(self, slider_value): # SlideBar
        self.actual_value = self.value_map.get(slider_value, 0)
        number_str = str(self.actual_value)  # Convert the number to a string
        digits_before_decimal = len(number_str.split('.')[0])
        
        if self.actual_value == None:
            print("Plz first Bhk type")
            
        else:
            if digits_before_decimal == 1:
                print(f"Slider value changed to {self.actual_value} Cr")
                self.label_3.setText(f"{self.actual_value}"+"Cr")
            else:
                print(f"Slider value changed to {self.actual_value} L")
                self.label_3.setText(f"{self.actual_value}"+"L")
            

    def internet_checker(self): # After clicking the owner details this will be going to call the check_internet function 
        print("I am in own_frame")
        self.intevlu = self.check_internet()
        if self.intevlu:
             print("Internet is smoothly running")
        else:
            self.frame_2.show()
            print("Internet issue")
            
        
        
    def check_internet(self): # Checking the internet connection
        print(" i am in the checkk internet")
        try:
            urllib.request.urlopen('http://google.com', timeout=5)
            return True
        except urllib.error.URLError:
            return False

    def feed_submit(self): # After Submit the feedback this will be shown
        print("hello")
        print(self.rates)
        
        if self.rates == 0 or self.rates == None:
                print("Empty feedback")
        else:       
                # self.feedback_submit.setEnabled(False)
                # self.feedback_heading.hide()
                self.feedback_heading2.hide()
                self.feedback_submit.hide()
                self.feedback_star1.hide()
                self.feedback_star2.hide()
                self.feedback_star3.hide()
                self.feedback_star4.hide()
                self.feedback_star5.hide()
                
                # self.feedback_frame.deleteLater()
                time.sleep(1)
                self.feedback_close = QPushButton(self.feedback_frame)
                self.feedback_close.setObjectName(u"feedback_close")
                self.feedback_close.setGeometry(QRect(662, -1, 31, 20))
                font3 = QFont()
                font3.setPointSize(9)
                font3.setUnderline(True)
                self.feedback_close.setFont(font3)
                self.feedback_close.setStyleSheet(u"border:none;\n"
        "color:rgb(74, 74, 74);")
                self.feedback_close.setText("close")
                self.feedback_close.setCheckable(True)
                self.feedback_close.setAutoExclusive(False)
                # self.feedback_image = QLabel(self.feedback_frame)
                # self.feedback_image.setGeometry(QRect(150, 30, 381, 291))
                # self.feedback_image.setStyleSheet(u"border:none;")
                self.feedback_image.setPixmap(QPixmap(r":/sanket/images/feedsubmit.png"))
                self.feedback_heading.setText("Thank you for feedback...")
                self.feedback_heading.move(150,350)
                # self.feedback_image.setScaledContents(True)
                # self.feedback_image.setText("Hello")
                
                # self.feedback_close.clicked.connect(lambda : self.feedback_submit_frame.hide())
                # self.feedback_submit_frame.show()
    def frt_opn(self): # First feed str
        print("hello")
        current_icon1 = self.feedback_star1.icon()
        # print(current_icon1.cacheKey(),self.blackic.cacheKey(),self.goldic.cacheKey())
        if current_icon1.cacheKey() != self.blackic.cacheKey():
              print("i am in if")
              self.feedback_star1.setIcon(self.blackic)
              self.feedback_star2.setIcon(self.blackic)
              self.feedback_star3.setIcon(self.blackic)
              self.feedback_star4.setIcon(self.blackic)
              self.feedback_star5.setIcon(self.blackic)
        

        else:
              self.rates = 1
              self.feedback_star1.setIcon(self.goldic)
              

    def snd_opn(self): # Second feed str
        current_icon2 = self.feedback_star2.icon()
        if current_icon2.cacheKey() != self.blackic.cacheKey():
              self.feedback_star2.setIcon(self.blackic)
              self.feedback_star3.setIcon(self.blackic)
              self.feedback_star4.setIcon(self.blackic)
              self.feedback_star5.setIcon(self.blackic)
        else:
                self.rates = 2
                self.feedback_star1.setIcon(self.goldic)
                self.feedback_star2.setIcon(self.goldic)
                
       

    def thr_opn(self): # Third feed str
        current_icon3 = self.feedback_star3.icon()
        if current_icon3.cacheKey() != self.blackic.cacheKey():
              self.feedback_star3.setIcon(self.blackic)
              self.feedback_star4.setIcon(self.blackic)
              self.feedback_star5.setIcon(self.blackic)
        else:
              self.rates = 3
              self.feedback_star1.setIcon(self.goldic)
              self.feedback_star2.setIcon(self.goldic)
              self.feedback_star3.setIcon(self.goldic)
      

    def for_opn(self): # Fourth Feed star
        current_icon4 = self.feedback_star4.icon()
        if current_icon4.cacheKey() != self.blackic.cacheKey():
            self.feedback_star4.setIcon(self.blackic)
            self.feedback_star5.setIcon(self.blackic)
        else:
              self.rates = 4
              self.feedback_star1.setIcon(self.goldic)
              self.feedback_star2.setIcon(self.goldic)
              self.feedback_star3.setIcon(self.goldic)
              self.feedback_star4.setIcon(self.goldic)
        

    def zrt_opn(self): # Fifth feed Star
        current_icon5 = self.feedback_star5.icon()
        if current_icon5.cacheKey() != self.blackic.cacheKey():
            self.feedback_star5.setIcon(self.blackic)
            
        else:
              self.rates = 5
              self.feedback_star1.setIcon(self.goldic)
              self.feedback_star2.setIcon(self.goldic)
              self.feedback_star3.setIcon(self.goldic)
              self.feedback_star4.setIcon(self.goldic)
              self.feedback_star5.setIcon(self.goldic)
              
        
    def tim(self):
            print(self.rates)
        
    def notification_win_frame(self): # Notification
            if not self.notification_frame_visible:
                self.notification_frame = QFrame(self.mainmenu)
                self.notification_frame.setObjectName(u"self.notification_frame")
                self.notification_frame.resize(587, 404)
                self.notification_frame.setGeometry(300,140,587,404)
                self.notification_frame.setMinimumSize(QSize(587, 404))
                self.notification_frame.setMaximumSize(QSize(587, 404))
                self.notification_frame.setStyleSheet(u"background-color:rgb(35, 47, 49);\n"
        "border:3px solid rgb(18, 140, 126);")
                self.frame = QFrame(self.notification_frame)
                self.frame.setObjectName(u"frame")
                self.frame.setGeometry(QRect(24, 90, 541, 91))
                self.frame.setStyleSheet(u"background-color:rgb(7, 94, 84);\n"
        "border-radius:10px;\n"
        "border:none;")
                self.frame.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame.setFrameShadow(QFrame.Shadow.Raised)
                self.label_3 = QLabel(self.frame)
                self.label_3.setObjectName(u"label_3")
                self.label_3.setGeometry(QRect(523, 3, 16, 20))
                font = QFont()
                font.setPointSize(13)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet(u"border:none;")
                self.pushButton = QPushButton(self.frame)
                self.pushButton.setObjectName(u"pushButton")
                self.pushButton.setGeometry(QRect(440, 60, 81, 31))
                font1 = QFont()
                font1.setPointSize(10)
                font1.setBold(True)
                font1.setUnderline(True)
                self.pushButton.setFont(font1)
                self.pushButton.setStyleSheet(u"border:none;\n"
        "color:rgb(35, 47, 49);")
                self.layoutWidget = QWidget(self.frame)
                self.layoutWidget.setObjectName(u"layoutWidget")
                self.layoutWidget.setGeometry(QRect(22, 7, 328, 84))
                self.horizontalLayout = QHBoxLayout(self.layoutWidget)
                self.horizontalLayout.setSpacing(15)
                self.horizontalLayout.setObjectName(u"horizontalLayout")
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.label = QLabel(self.layoutWidget)
                self.label.setObjectName(u"label")
                self.label.setMinimumSize(QSize(65, 60))
                self.label.setMaximumSize(QSize(65, 60))
                self.label.setPixmap(QPixmap(u"notification.png"))
                self.label.setScaledContents(True)

                self.horizontalLayout.addWidget(self.label)

                self.verticalLayout = QVBoxLayout()
                self.verticalLayout.setSpacing(0)
                self.verticalLayout.setObjectName(u"verticalLayout")
                self.label_2 = QLabel(self.layoutWidget)
                self.label_2.setObjectName(u"label_2")
                font2 = QFont()
                font2.setPointSize(18)
                font2.setBold(True)
                self.label_2.setFont(font2)
                self.label_2.setStyleSheet(u"color:white;")

                self.verticalLayout.addWidget(self.label_2)

                self.label_4 = QLabel(self.layoutWidget)
                self.label_4.setObjectName(u"label_4")
                font3 = QFont()
                font3.setPointSize(10)
                self.label_4.setFont(font3)
                self.label_4.setStyleSheet(u"color:rgb(229, 229, 229);")

                self.verticalLayout.addWidget(self.label_4)


                self.horizontalLayout.addLayout(self.verticalLayout)

                self.frame_2 = QFrame(self.notification_frame)
                self.frame_2.setObjectName(u"frame_2")
                self.frame_2.setGeometry(QRect(24, 200, 541, 91))
                self.frame_2.setMinimumSize(QSize(541, 91))
                self.frame_2.setMaximumSize(QSize(541, 91))
                self.frame_2.setStyleSheet(u"background-color:rgb(7, 94, 84);\n"
        "border-radius:10px;\n"
        "border:none;")
                self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
                self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
                self.label_5 = QLabel(self.frame_2)
                self.label_5.setObjectName(u"label_5")
                self.label_5.setGeometry(QRect(10, 10, 91, 81))
                self.label_5.setPixmap(QPixmap(u"../../../../../Users/sanke/Downloads/no-wifi.png"))
                self.label_5.setScaledContents(True)
                self.label_7 = QLabel(self.frame_2)
                self.label_7.setObjectName(u"label_7")
                self.label_7.setGeometry(QRect(523, 6, 20, 21))
                self.label_7.setFont(font)
                self.label_7.setStyleSheet(u"border:none;")
                self.pushButton_2 = QPushButton(self.frame_2)
                self.pushButton_2.setObjectName(u"pushButton_2")
                self.pushButton_2.setGeometry(QRect(440, 60, 81, 31))
                self.pushButton_2.setFont(font1)
                self.pushButton_2.setStyleSheet(u"border:none;\n"
        "color:rgb(35, 47, 49);")
                self.layoutWidget1 = QWidget(self.frame_2)
                self.layoutWidget1.setObjectName(u"layoutWidget1")
                self.layoutWidget1.setGeometry(QRect(20, 9, 316, 84))
                self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
                self.horizontalLayout_2.setSpacing(15)
                self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
                self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.label_6 = QLabel(self.layoutWidget1)
                self.label_6.setObjectName(u"label_6")
                self.label_6.setMinimumSize(QSize(65, 60))
                self.label_6.setMaximumSize(QSize(65, 60))
                self.label_6.setPixmap(QPixmap(u"../../../../../Users/Shivam/Downloads/no-wifi.png"))
                self.label_6.setScaledContents(True)

                self.horizontalLayout_2.addWidget(self.label_6)

                self.verticalLayout_2 = QVBoxLayout()
                self.verticalLayout_2.setSpacing(0)
                self.verticalLayout_2.setObjectName(u"verticalLayout_2")
                self.label_8 = QLabel(self.layoutWidget1)
                self.label_8.setObjectName(u"label_8")
                self.label_8.setFont(font2)
                self.label_8.setStyleSheet(u"color:white;")

                self.verticalLayout_2.addWidget(self.label_8)

                self.label_10 = QLabel(self.layoutWidget1)
                self.label_10.setObjectName(u"label_10")
                self.label_10.setFont(font3)
                self.label_10.setStyleSheet(u"color:rgb(229, 229, 229);")

                self.verticalLayout_2.addWidget(self.label_10)


                self.horizontalLayout_2.addLayout(self.verticalLayout_2)

                self.label_9 = QLabel(self.notification_frame)
                self.label_9.setObjectName(u"label_9")
                self.label_9.setGeometry(QRect(210, 8, 171, 51))
                font4 = QFont()
                font4.setPointSize(20)
                font4.setBold(True)
                self.label_9.setFont(font4)
                self.label_9.setStyleSheet(u"color:rgb(213, 213, 213);\n"
        "border:none;")
                self.line = QFrame(self.notification_frame)
                self.line.setObjectName(u"line")
                self.line.setGeometry(QRect(-10, 63, 600, 2))
                self.line.setFrameShape(QFrame.Shape.HLine)
                self.line.setFrameShadow(QFrame.Shadow.Sunken)
                self.label_3.setText("x")
                self.pushButton.setText("View")
                self.label.setText("")
                self.label_2.setText("New Notification")
                self.label_4.setText("New Property is added you can just click\n"
        "the button to visit")
                self.label_5.setText("")
                self.label_7.setText("x")
                self.pushButton_2.setText("Hide")
                self.label_6.setText("")
                self.label_8.setText("New Notification")
                self.label_10.setText("Please check your internet connection\n"
        "")
                self.label_9.setText("Notifications")
                if self.intevlu:
                    self.frame_2.hide()
                else:
                    self.frame_2.show()
                self.notification_frame.show()
                self.notification_frame_visible = True
            else:
                
                self.notification_frame.hide()
                self.notification_frame_visible = False
                
    def feedback_win_frame(self): # Feddback 
            self.stackedWidget_3.setCurrentIndex(18)
            if not self.feedback_frame_visible:
                    self.feedback_frame = QFrame(self.mainmenu)
                    self.feedback_frame.resize(700, 500)
                    self.feedback_frame.setGeometry(250,150,700, 500)
                    self.feedback_frame.setMinimumSize(QSize(700, 500))
                    self.feedback_frame.setMaximumSize(QSize(700, 500))
                    self.feedback_frame.setStyleSheet(u"background-color:rgb(18, 140, 126);\n"
            "border-radius:10px;\n"
            "border:1px solid rgb(0, 170, 0);")
                    self.feedback_heading = QLabel(self.feedback_frame)
                    self.feedback_heading.setObjectName(u"feedback_heading")
                    self.feedback_heading.setGeometry(QRect(125, 310, 451, 51))
                    font = QFont()
                    font.setFamilies([u"Sitka Display Semibold"])
                    font.setPointSize(28)
                    font.setItalic(False)
                    font.setUnderline(False)
                    self.feedback_heading.setFont(font)
                    self.feedback_heading.setStyleSheet(u"color: rgb(255, 255, 255); border:none;")
                    self.feedback_heading2 = QLabel(self.feedback_frame)
                    self.feedback_heading2.setObjectName(u"feedback_heading2")
                    self.feedback_heading2.setGeometry(QRect(150, 360, 401, 20))
                    font1 = QFont()
                    font1.setPointSize(13)
                    self.feedback_heading2.setFont(font1)
                    self.feedback_heading2.setStyleSheet(u"color:rgb(211, 211, 211);\n"
            "border:none;")
                    self.feedback_image = QLabel(self.feedback_frame)
                    self.feedback_image.setObjectName(u"feedback_image")
                    self.feedback_image.setGeometry(QRect(150, 30, 381, 291))
                    self.feedback_image.setStyleSheet(u"border:none;")
                #     self.feedback_image.setPixmap(QPixmap(r":/sanket/images/feedsubmit.png"))
                    self.feedback_image.setScaledContents(True)
                    self.feedback_submit = QPushButton(self.feedback_frame)
                    self.feedback_submit.setObjectName(u"feedback_submit")
                    self.feedback_submit.setGeometry(QRect(260, 460, 170, 25))
                    font2 = QFont()
                    font2.setPointSize(10)
                    self.feedback_submit.setFont(font2)
                    self.feedback_submit.setStyleSheet(u"QPushButton\n"
            "{\n"
            "background-color:rgb(204, 204, 204);\n"
            "border:1px solid black;\n"
            "border-radius:10px;\n"
            "color:black;\n"
            "}\n"
            "QPushButton:hover\n"
            "{\n"
            "border:1px solid white;\n"
            "background-color:rgb(18, 140, 126);\n"
            "	color: rgb(255, 255, 255);\n"
            "}")
                    self.feedback_submit.setCheckable(True)
                    self.feedback_close = QPushButton(self.feedback_frame)
                    self.feedback_close.setObjectName(u"feedback_close")
                    self.feedback_close.setGeometry(QRect(662, -1, 31, 20))
                    font3 = QFont()
                    font3.setPointSize(9)
                    font3.setUnderline(True)
                    self.feedback_close.setFont(font3)
                    self.feedback_close.setStyleSheet(u"border:none;\n"
            "color:rgb(74, 74, 74);")
                    self.feedback_close.setCheckable(True)
                    self.feedback_close.setAutoExclusive(False)
                    self.feedback_star1 = QPushButton(self.feedback_frame)
                    self.feedback_star1.setObjectName(u"feedback_star1")
                    self.feedback_star1.setGeometry(QRect(210, 400, 41, 41))
                    self.feedback_star1.setStyleSheet(u"border:none; background:none;")
                    icon = QIcon()
                    icon.addFile(u":sanket/images/starblank.png", QSize(), QIcon.Normal, QIcon.Off)
                    self.feedback_star1.setIcon(icon)
                    self.feedback_star1.setIconSize(QSize(50, 50))
                    self.feedback_star4 = QPushButton(self.feedback_frame)
                    self.feedback_star4.setObjectName(u"feedback_star4")
                    self.feedback_star4.setGeometry(QRect(390, 400, 41, 41))
                    self.feedback_star4.setStyleSheet(u"border:none; background:none;")
                    self.feedback_star4.setIcon(icon)
                    self.feedback_star4.setIconSize(QSize(50, 50))
                    self.feedback_star2 = QPushButton(self.feedback_frame)
                    self.feedback_star2.setObjectName(u"feedback_star2")
                    self.feedback_star2.setGeometry(QRect(270, 400, 41, 41))
                    self.feedback_star2.setStyleSheet(u"border:none; background:none;")
                    self.feedback_star2.setIcon(icon)
                    self.feedback_star2.setIconSize(QSize(50, 50))
                    self.feedback_star5 = QPushButton(self.feedback_frame)
                    self.feedback_star5.setObjectName(u"feedback_star5")
                    self.feedback_star5.setGeometry(QRect(450, 400, 41, 41))
                    self.feedback_star5.setStyleSheet(u"border:none; background:none;")
                    self.feedback_star5.setIcon(icon)
                    self.feedback_star5.setIconSize(QSize(50, 50))
                    self.feedback_star3 = QPushButton(self.feedback_frame)
                    self.feedback_star3.setObjectName(u"feedback_star3")
                    self.feedback_star3.setGeometry(QRect(330, 400, 41, 41))
                    self.feedback_star3.setStyleSheet(u"border:none; background:none;")
                    self.feedback_star3.setIcon(icon)
                    self.feedback_star3.setIconSize(QSize(50, 50))
                    self.feedback_heading.setText("Enjoying MiddleMan Services?")
                    self.feedback_heading2.setText("We'd love your feedback so that we serve you better")
                    self.feedback_image.setText("")
                    self.feedback_submit.setText("Submit")
                    self.feedback_close.setText("close")
                    self.feedback_star1.setText("")
                    self.feedback_star4.setText("")
                    self.feedback_star2.setText("")
                    self.feedback_star5.setText("")
                    self.feedback_star3.setText("")
                    self.feedback_star1.clicked.connect(self.frt_opn)
                    self.feedback_star2.clicked.connect(self.snd_opn)
                    self.feedback_star3.clicked.connect(self.thr_opn)
                    self.feedback_star4.clicked.connect(self.for_opn)
                    self.feedback_star5.clicked.connect(self.zrt_opn)
                    self.feedback_submit.clicked.connect(self.feed_submit)
                    self.feedback_close.clicked.connect(lambda : self.feedback_frame.hide())
                    self.feedback_frame.show()
                    self.feedback_frame_visible=True
            else:
                    self.feedback_frame.hide()
                    self.feedback_frame_visible = False
                
    def logout_win_frame(self): # Logout frame
            if not self.logout_frame_visible:
                     self.logout_frame = QFrame(self.mainmenu)
                     self.logout_frame.setGeometry(1100,60,250,250) # Logout frame geometry and move
                #      self.logout_frame.move()
                     self.logout_frame.setObjectName(u"frame")
                     font = QFont()
                     font.setPointSize(11)
                     font.setBold(True)
                     self.logout_frame.setFont(font)
                     self.logout_frame.setStyleSheet(u"QFrame{\n"
                        "background-color: rgb(35, 47, 49);\n"
                        "border:2px solid rgb(18, 140, 126);\n"
                        "border-radius:20px;\n"
                        "}")
                     self.logout_frame.setFrameShape(QFrame.Shape.StyledPanel)
                     self.logout_frame.setFrameShadow(QFrame.Shadow.Raised)
                     self.label = QLabel(self.logout_frame)
                     self.label.setObjectName(u"label")
                     self.label.setGeometry(QRect(61, 10, 131, 31))
                     font1 = QFont()
                     font1.setPointSize(15)
                     self.label.setFont(font1)
                     self.label.setStyleSheet(u"QLabel{\n"
                      "	color: rgb(255, 255, 255);\n"
                      "border:none;\n"
                      "}")
                     self.lineEdit = QLineEdit(self.logout_frame)
                     self.lineEdit.setObjectName(u"lineEdit")
                     self.lineEdit.setGeometry(QRect(30, 76, 191, 20))
                     self.lineEdit.setFont(font)
                     self.lineEdit.setStyleSheet(u"QLineEdit{\n"
             "background-color: rgb(255, 255, 255);\n"
             "border-bottom:3px solid rgb(0, 170, 0);\n"
             "}\n"
             "\n"
             "")
                     self.lineEdit.setReadOnly(True)
                     self.email_heading_3 = QLabel(self.logout_frame)
                     self.email_heading_3.setObjectName(u"email_heading_3")
                     self.email_heading_3.setGeometry(QRect(32, 55, 61, 16))
                     self.email_heading_3.setStyleSheet(u"color:rgb(18, 140, 126);\n"
             "border:none;\n"
             "")
                     self.loginbutton_2 = QPushButton(self.logout_frame)
                     self.loginbutton_2.setObjectName(u"loginbutton_2")
                     self.loginbutton_2.setGeometry(QRect(79, 216, 91, 21))
                     font2 = QFont()
                     font2.setPointSize(10)
                     font2.setBold(True)
                     self.loginbutton_2.setFont(font2)
                     self.loginbutton_2.setStyleSheet(u"QPushButton\n"
             "{\n"
             "background-color:rgb(18, 140, 126);\n"
             "border-radius:10px;\n"
             "}\n"
             "QPushButton:hover\n"
             "{\n"
             "border:1px solid rgb(18, 140, 126);\n"
             "background-color:rgb(35, 47, 49);\n"
             "	color: rgb(255, 255, 255);\n"
             "}")
                     self.loginbutton_2.setIconSize(QSize(15, 15))
                     self.loginbutton_2.setCheckable(True)
                     self.lineEdit_2 = QLineEdit(self.logout_frame)
                     self.lineEdit_2.setObjectName(u"lineEdit_2")
                     self.lineEdit_2.setGeometry(QRect(30, 124, 191, 20))
                     self.lineEdit_2.setFont(font)
                     self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
             "background-color: rgb(255, 255, 255);\n"
             "border-bottom:3px solid rgb(0, 170, 0);\n"
             "}\n"
             "\n"
             "")
                     self.lineEdit_2.setReadOnly(True)
                     self.email_heading_4 = QLabel(self.logout_frame)
                     self.email_heading_4.setObjectName(u"email_heading_4")
                     self.email_heading_4.setGeometry(QRect(32, 103, 61, 16))
                     self.email_heading_4.setStyleSheet(u"color:rgb(18, 140, 126);\n"
             "border:none;\n"
             "")
                     self.email_heading_5 = QLabel(self.logout_frame)
                     self.email_heading_5.setObjectName(u"email_heading_5")
                     self.email_heading_5.setGeometry(QRect(33, 148, 61, 16))
                     self.email_heading_5.setStyleSheet(u"color:rgb(18, 140, 126);\n"
             "border:none;\n"
             "")
                     self.lineEdit_3 = QLineEdit(self.logout_frame)
                     self.lineEdit_3.setObjectName(u"lineEdit_3")
                     self.lineEdit_3.setGeometry(QRect(31, 169, 191, 20))
                     self.lineEdit_3.setFont(font)
                     self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
                        "background-color: rgb(255, 255, 255);\n"
                        "border-bottom:3px solid rgb(0, 170, 0);\n"
                        "}\n"
                        "\n"
                        "")
                     #Label text
                     self.label.setText("PROFILE INFO")
                     self.email_heading_3.setText("Login as")
                     self.loginbutton_2.setText(" Log Out")
                     self.email_heading_4.setText("Login Date")
                     self.email_heading_5.setText("Login Time")
                     self.lineEdit_3.setReadOnly(True)
                     self.loginbutton_2.clicked.connect(lambda : MainWindow.close())
                     self.logout_frame.show()
                     self.logout_frame_visible = True
            else:
                    self.logout_frame.hide()
                    self.logout_frame_visible = None
                    
    def filter_win_frame(self): # Filter frame
        if not self.filter_frame_visible :
                self.filter_frame = QFrame(self.mainmenu)
                self.filter_frame.setGeometry(200,70,300,250)
                self.filter_frame.setObjectName("filter_frame")
                self.filter_frame.resize(300, 250)
                self.filter_frame.setMinimumSize(QSize(300, 250))
                self.filter_frame.setMaximumSize(QSize(300, 250))
                self.filter_frame.setStyleSheet(u"background-color:rgb(35, 47, 49);\n"
        "border:2px solid rgb(7, 94, 84);\n"
        "border-radius:10px")
                self.filter_comboBox = QComboBox(self.filter_frame)
                self.filter_comboBox.addItem("")
                self.filter_comboBox.addItem("")
                self.filter_comboBox.addItem("")
                self.filter_comboBox.addItem("")
                self.filter_comboBox.setObjectName(u"comboBox")
                self.filter_comboBox.setGeometry(QRect(25, 40, 251, 31))
                self.filter_comboBox.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
        "border:none;\n"
        "")
                self.horizontalSlider = QSlider(self.filter_frame)
                self.horizontalSlider.setObjectName(u"horizontalSlider")
                self.horizontalSlider.setGeometry(QRect(30, 130, 251, 21))
                self.horizontalSlider.setStyleSheet(u"border:none;")
                self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
                self.label_2 = QLabel(self.filter_frame)
                self.label_2.setObjectName(u"label_2")
                self.label_2.setGeometry(QRect(84, 100, 131, 16))
                font = QFont()
                font.setPointSize(8)
                font.setBold(False)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet(u"color:rgb(18, 140, 126); \n"
        "border:none;")
                self.label = QLabel(self.filter_frame)
                self.label.setObjectName(u"label")
                self.label.setGeometry(QRect(70, 170, 111, 31))
                font1 = QFont()
                font1.setPointSize(11)
                self.label.setFont(font1)
                self.label.setStyleSheet(u"border:none;\n"
        "color: rgb(18, 140, 126);")
                self.label_3 = QLabel(self.filter_frame)
                self.label_3.setObjectName(u"label_3")
                self.label_3.setGeometry(QRect(190, 170, 55, 31))
                font2 = QFont()
                font2.setPointSize(14)
                self.label_3.setFont(font2)
                self.label_3.setStyleSheet(u"border:none; color:white;")
                self.filter_comboBox.setItemText(0, " 1 BHK")
                self.filter_comboBox.setItemText(1,"  2 BHK")
                self.filter_comboBox.setItemText(2,  "  3 BHK")
                self.filter_comboBox.setItemText(3,  "  Others...")
                self.filter_comboBox.setPlaceholderText( "  Select one from above...")
                self.filter_comboBox.currentIndexChanged.connect(self.see_type)
                self.label_2.setText( "Price range as per selected BHK :")
                self.label.setText( "Selected Price :")
                self.label_3.setText( "0.0")
                self.horizontalSlider.valueChanged.connect(self.call_me)
                self.filter_frame.show()
                self.filter_frame_visible =True
        else:
                self.filter_frame.hide()
                self.filter_frame_visible = False
        
        # This all done by me sanket 
        
     # It's shivam part    
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1524, 682)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setMinimumSize(QSize(160, 0))
        self.icon_name_widget.setMaximumSize(QSize(160, 16777215))
        self.icon_name_widget.setAutoFillBackground(False)
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(35, 47, 49);\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"      color:white;\n"
"text-align:left;\n"
"height:35px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:rgb(236, 219, 186);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(139, 139, 139);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        self.verticalLayout_39 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_39.setSpacing(25)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 15)
        self.widget_7 = QWidget(self.icon_name_widget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 55))
        self.widget_7.setMaximumSize(QSize(16777215, 55))
        self.widget_7.setStyleSheet(u"\n"
"background-color: rgb(7, 94, 84);\n"
"")
        self.layoutWidget = QWidget(self.widget_7)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(-2, 2, 151, 52))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_39 = QPushButton(self.layoutWidget)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setMinimumSize(QSize(50, 50))
        self.pushButton_39.setMaximumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(u"PropImages/newMMprofile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_39.setIcon(icon)
        self.pushButton_39.setIconSize(QSize(40, 40))
        self.pushButton_39.setCheckable(True)
        self.pushButton_39.setAutoExclusive(True)

        self.horizontalLayout_7.addWidget(self.pushButton_39)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_7.addWidget(self.label_6)


        self.verticalLayout_39.addWidget(self.widget_7, 0, Qt.AlignmentFlag.AlignTop)

        self.toolBox = QToolBox(self.icon_name_widget)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(140, 410))
        self.toolBox.setMaximumSize(QSize(140, 410))
        self.toolBox.setBaseSize(QSize(140, 0))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.toolBox.setFont(font1)
        self.toolBox.setStyleSheet(u"QToolBox:tab{\n"
"	background-color:rgb(7, 94, 84);\n"
"	color:rgb(255, 255, 255);\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"}")
        self.toolBox.setLineWidth(1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 140, 160))
        self.layoutWidget1 = QWidget(self.page)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 160, 121))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(15, 0, 0, 0)
        self.Dashboard_2 = QPushButton(self.layoutWidget1)
        self.Dashboard_2.setObjectName(u"Dashboard_2")
        font2 = QFont()
        font2.setPointSize(11)
        self.Dashboard_2.setFont(font2)
        self.Dashboard_2.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../Shivam/Downloads/location.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_2.setIcon(icon1)
        self.Dashboard_2.setIconSize(QSize(25, 25))
        self.Dashboard_2.setCheckable(True)
        self.Dashboard_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Dashboard_2)

        self.Profile_2 = QPushButton(self.layoutWidget1)
        self.Profile_2.setObjectName(u"Profile_2")
        self.Profile_2.setFont(font2)
        self.Profile_2.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        self.Profile_2.setIcon(icon1)
        self.Profile_2.setIconSize(QSize(25, 25))
        self.Profile_2.setCheckable(True)
        self.Profile_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Profile_2)

        self.Messages_2 = QPushButton(self.layoutWidget1)
        self.Messages_2.setObjectName(u"Messages_2")
        self.Messages_2.setFont(font2)
        self.Messages_2.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        self.Messages_2.setIcon(icon1)
        self.Messages_2.setIconSize(QSize(25, 25))
        self.Messages_2.setCheckable(True)
        self.Messages_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Messages_2)

        icon2 = QIcon()
        icon2.addFile(u"PropImages/newhomeicom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page, icon2, u"New Project")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 140, 160))
        self.layoutWidget2 = QWidget(self.page_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(-3, 0, 142, 161))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Messages_3 = QPushButton(self.layoutWidget2)
        self.Messages_3.setObjectName(u"Messages_3")
        self.Messages_3.setFont(font2)
        self.Messages_3.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../../Shivam/Downloads/washing-removebg-preview (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.Messages_3.setIcon(icon3)
        self.Messages_3.setIconSize(QSize(25, 25))
        self.Messages_3.setCheckable(True)
        self.Messages_3.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.Messages_3)

        self.Dashboard_3 = QPushButton(self.layoutWidget2)
        self.Dashboard_3.setObjectName(u"Dashboard_3")
        self.Dashboard_3.setFont(font2)
        self.Dashboard_3.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../../Shivam/Downloads/paint-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_3.setIcon(icon4)
        self.Dashboard_3.setIconSize(QSize(25, 25))
        self.Dashboard_3.setCheckable(True)
        self.Dashboard_3.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.Dashboard_3)

        self.Profile_3 = QPushButton(self.layoutWidget2)
        self.Profile_3.setObjectName(u"Profile_3")
        self.Profile_3.setFont(font2)
        self.Profile_3.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../../Shivam/Downloads/svg-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Profile_3.setIcon(icon5)
        self.Profile_3.setIconSize(QSize(25, 25))
        self.Profile_3.setCheckable(True)
        self.Profile_3.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.Profile_3)

        self.Dashboard_5 = QPushButton(self.layoutWidget2)
        self.Dashboard_5.setObjectName(u"Dashboard_5")
        self.Dashboard_5.setFont(font2)
        self.Dashboard_5.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../../Shivam/Downloads/construction-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_5.setIcon(icon6)
        self.Dashboard_5.setIconSize(QSize(25, 25))
        self.Dashboard_5.setCheckable(True)
        self.Dashboard_5.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.Dashboard_5)

        icon7 = QIcon()
        icon7.addFile(u"../../Shivam/Downloads/ervice.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_2, icon7, u"Other Services")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 140, 160))
        self.layoutWidget_2 = QWidget(self.page_3)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(-10, 0, 182, 3107))
        self.verticalLayout_21 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(15, 0, 0, 0)
        self.Dashboard_4 = QPushButton(self.layoutWidget_2)
        self.Dashboard_4.setObjectName(u"Dashboard_4")
        self.Dashboard_4.setFont(font2)
        self.Dashboard_4.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"../../Shivam/Downloads/note-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_4.setIcon(icon8)
        self.Dashboard_4.setIconSize(QSize(25, 25))
        self.Dashboard_4.setCheckable(True)
        self.Dashboard_4.setAutoExclusive(True)

        self.verticalLayout_21.addWidget(self.Dashboard_4)

        self.Profile_4 = QPushButton(self.layoutWidget_2)
        self.Profile_4.setObjectName(u"Profile_4")
        self.Profile_4.setFont(font2)
        self.Profile_4.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"../../Shivam/Downloads/tenant.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Profile_4.setIcon(icon9)
        self.Profile_4.setIconSize(QSize(25, 25))
        self.Profile_4.setCheckable(True)
        self.Profile_4.setAutoExclusive(True)

        self.verticalLayout_21.addWidget(self.Profile_4)

        self.frame_3 = QFrame(self.layoutWidget_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 3000))
        self.frame_3.setStyleSheet(u"")

        self.verticalLayout_21.addWidget(self.frame_3)

        icon10 = QIcon()
        icon10.addFile(u"../../Shivam/Downloads/ervice (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_3, icon10, u"Agreements")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 140, 160))
        self.Dashboard_6 = QPushButton(self.page_4)
        self.Dashboard_6.setObjectName(u"Dashboard_6")
        self.Dashboard_6.setGeometry(QRect(10, 0, 141, 33))
        self.Dashboard_6.setFont(font2)
        self.Dashboard_6.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        self.Dashboard_6.setIconSize(QSize(25, 25))
        self.Dashboard_6.setCheckable(True)
        self.Dashboard_6.setAutoExclusive(True)
        self.Dashboard_8 = QPushButton(self.page_4)
        self.Dashboard_8.setObjectName(u"Dashboard_8")
        self.Dashboard_8.setGeometry(QRect(9, 43, 141, 33))
        self.Dashboard_8.setFont(font2)
        self.Dashboard_8.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        self.Dashboard_8.setIconSize(QSize(25, 25))
        self.Dashboard_8.setCheckable(True)
        self.Dashboard_8.setAutoExclusive(True)
        icon11 = QIcon()
        icon11.addFile(u"../../Shivam/Downloads/ervice (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_4, icon11, u"Click and Earn")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 140, 160))
        self.layoutWidget_3 = QWidget(self.page_5)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(-4, -7, 160, 121))
        self.verticalLayout_22 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(15, 0, 0, 0)
        self.Dashboard_7 = QPushButton(self.layoutWidget_3)
        self.Dashboard_7.setObjectName(u"Dashboard_7")
        self.Dashboard_7.setFont(font2)
        self.Dashboard_7.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"../../Shivam/Downloads/rating-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_7.setIcon(icon12)
        self.Dashboard_7.setIconSize(QSize(25, 25))
        self.Dashboard_7.setCheckable(True)
        self.Dashboard_7.setAutoExclusive(True)

        self.verticalLayout_22.addWidget(self.Dashboard_7)

        self.Profile_5 = QPushButton(self.layoutWidget_3)
        self.Profile_5.setObjectName(u"Profile_5")
        self.Profile_5.setFont(font2)
        self.Profile_5.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u"../../Shivam/Downloads/phone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Profile_5.setIcon(icon13)
        self.Profile_5.setIconSize(QSize(30, 30))
        self.Profile_5.setCheckable(True)
        self.Profile_5.setAutoExclusive(True)

        self.verticalLayout_22.addWidget(self.Profile_5)

        self.Messages_5 = QPushButton(self.layoutWidget_3)
        self.Messages_5.setObjectName(u"Messages_5")
        self.Messages_5.setFont(font2)
        self.Messages_5.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"background-color:rgb(30, 81, 40);\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:;\n"
"	color: rgb(0, 111, 0);\n"
"color:white;\n"
"font-weight:bold;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"../../Shivam/Downloads/round.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Messages_5.setIcon(icon14)
        self.Messages_5.setIconSize(QSize(25, 25))
        self.Messages_5.setCheckable(True)
        self.Messages_5.setAutoExclusive(True)

        self.verticalLayout_22.addWidget(self.Messages_5)

        icon15 = QIcon()
        icon15.addFile(u"../../Shivam/Downloads/Untitled design (8).png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_5, icon15, u" Others")

        self.verticalLayout_39.addWidget(self.toolBox, 0, Qt.AlignmentFlag.AlignRight)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer)

        self.pushButton_11 = QPushButton(self.icon_name_widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"border:none;")
        icon16 = QIcon()
        icon16.addFile(u"../../Shivam/Downloads/notification-bell.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon16)
        self.pushButton_11.setIconSize(QSize(30, 30))

        self.verticalLayout_39.addWidget(self.pushButton_11, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout.addWidget(self.icon_name_widget)

        self.mainmenu = QWidget(self.centralwidget)
        self.mainmenu.setObjectName(u"mainmenu")
        self.mainmenu.setAutoFillBackground(False)
        self.mainmenu.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.verticalLayout = QVBoxLayout(self.mainmenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.mainmenu)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 55))
        self.widget_3.setStyleSheet(u"background-color: rgb(7, 94, 84);")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.Menu = QPushButton(self.widget_3)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setStyleSheet(u"border:none;")
        icon17 = QIcon()
        icon17.addFile(u"PropImages/DASHHH.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu.setIcon(icon17)
        self.Menu.setIconSize(QSize(30, 30))
        self.Menu.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.Menu)

        self.horizontalSpacer = QSpacerItem(250, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 25))
        self.pushButton.setMaximumSize(QSize(90, 25))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(7, 94, 84);\n"
"")
        icon18 = QIcon()
        icon18.addFile(u"../../Shivam/Downloads/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon18)
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.pushButton)

        self.comboBox = QComboBox(self.widget_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(150, 25))
        self.comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"boder-radius:125px;\n"
"}")
        self.comboBox.setEditable(False)

        self.horizontalLayout_9.addWidget(self.comboBox)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, -1, -1, -1)
        self.lineEdit_3 = QLineEdit(self.widget_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(300, 25))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_10.addWidget(self.lineEdit_3)

        self.pushButton_32 = QPushButton(self.widget_3)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        icon19 = QIcon()
        icon19.addFile(u"../Sidebar/slidemenubar/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_32.setIcon(icon19)

        self.horizontalLayout_10.addWidget(self.pushButton_32)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)

        self.horizontalSpacer_6 = QSpacerItem(188, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.label_129 = QLabel(self.widget_3)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMinimumSize(QSize(40, 20))
        self.label_129.setMaximumSize(QSize(40, 20))
        self.label_129.setStyleSheet(u"background-color:rgb(37, 211, 102);\n"
"border:1px solid rgb(7, 94, 84);\n"
"color:rgb(70, 70, 70);\n"
"border-radius:10px;")
        self.label_129.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_129)

        self.pushButton_6 = QPushButton(self.widget_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(30, 30))
        self.pushButton_6.setMaximumSize(QSize(30, 30))
        self.pushButton_6.setStyleSheet(u"border:none;\n"
"")
        icon20 = QIcon()
        icon20.addFile(u"../../Shivam/Downloads/Coffe-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon20)
        self.pushButton_6.setIconSize(QSize(30, 30))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.pushButton_6)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.pushButton_33 = QPushButton(self.widget_3)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setStyleSheet(u"border:none;\n"
"")
        icon21 = QIcon()
        icon21.addFile(u"../Sidebar/slidemenubar/profile_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_33.setIcon(icon21)
        self.pushButton_33.setIconSize(QSize(25, 25))
        self.pushButton_33.setCheckable(True)
        self.pushButton_33.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.pushButton_33)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)


        self.verticalLayout.addWidget(self.widget_3)

        self.stackedWidget_3 = QStackedWidget(self.mainmenu)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setMaximumSize(QSize(16770, 16770))
        self.stackedWidget_3.setStyleSheet(u"background-color: rgb(35, 47, 49);")
        self.dashboardpage = QWidget()
        self.dashboardpage.setObjectName(u"dashboardpage")
        self.verticalLayout_17 = QVBoxLayout(self.dashboardpage)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.dashboardpage)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_19 = QVBoxLayout(self.widget_6)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_6 = QScrollArea(self.widget_6)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(7, 94, 84);\n"
" }")
        self.scrollArea_6.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 98, 2000))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 2000))
        self.frame_6.setStyleSheet(u"")
        self.horizontalLayout_13 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_6)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 2000))
        self.frame_30.setStyleSheet(u"")
        self.verticalLayout_37 = QVBoxLayout(self.frame_30)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setContentsMargins(50, 35, -1, 60)
        self.frame_34 = QFrame(self.frame_30)
        self.frame_34.setObjectName(u"frame_34")
        font3 = QFont()
        font3.setFamilies([u"Sitka Banner Semibold"])
        self.frame_34.setFont(font3)
        self.frame_34.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.label_222 = QLabel(self.frame_34)
        self.label_222.setObjectName(u"label_222")
        self.label_222.setGeometry(QRect(13, 10, 171, 33))
        font4 = QFont()
        font4.setFamilies([u"Sitka Subheading"])
        font4.setPointSize(25)
        self.label_222.setFont(font4)
        self.label_222.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_223 = QLabel(self.frame_34)
        self.label_223.setObjectName(u"label_223")
        self.label_223.setGeometry(QRect(16, 49, 16, 16))
        self.label_223.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_224 = QLabel(self.frame_34)
        self.label_224.setObjectName(u"label_224")
        self.label_224.setGeometry(QRect(35, 49, 81, 16))
        self.label_224.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_21 = QPushButton(self.frame_34)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_21.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_225 = QLabel(self.frame_34)
        self.label_225.setObjectName(u"label_225")
        self.label_225.setGeometry(QRect(294, 10, 182, 31))
        font5 = QFont()
        font5.setPointSize(17)
        self.label_225.setFont(font5)
        self.label_225.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_226 = QLabel(self.frame_34)
        self.label_226.setObjectName(u"label_226")
        self.label_226.setGeometry(QRect(461, 17, 91, 20))
        self.label_226.setFont(font2)
        self.label_226.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_227 = QLabel(self.frame_34)
        self.label_227.setObjectName(u"label_227")
        self.label_227.setGeometry(QRect(354, 44, 141, 20))
        self.label_227.setFont(font2)
        self.label_227.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_228 = QLabel(self.frame_34)
        self.label_228.setObjectName(u"label_228")
        self.label_228.setGeometry(QRect(10, 99, 291, 269))
        self.label_228.setStyleSheet(u"border-radius:5px;")
        self.label_228.setPixmap(QPixmap(u"PropImages/Thane/Thane-DostiHeron/Thane-4.1Elev.jpg"))
        self.label_228.setScaledContents(True)
        self.line_58 = QFrame(self.frame_34)
        self.line_58.setObjectName(u"line_58")
        self.line_58.setGeometry(QRect(307, 99, 16, 269))
        self.line_58.setFrameShape(QFrame.Shape.VLine)
        self.line_58.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_229 = QLabel(self.frame_34)
        self.label_229.setObjectName(u"label_229")
        self.label_229.setGeometry(QRect(377, 99, 175, 44))
        font6 = QFont()
        font6.setPointSize(12)
        self.label_229.setFont(font6)
        self.label_229.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_59 = QFrame(self.frame_34)
        self.line_59.setObjectName(u"line_59")
        self.line_59.setGeometry(QRect(316, 185, 274, 16))
        self.line_59.setFrameShape(QFrame.Shape.HLine)
        self.line_59.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_230 = QLabel(self.frame_34)
        self.label_230.setObjectName(u"label_230")
        self.label_230.setGeometry(QRect(377, 194, 120, 44))
        self.label_230.setFont(font6)
        self.label_230.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_231 = QLabel(self.frame_34)
        self.label_231.setObjectName(u"label_231")
        self.label_231.setGeometry(QRect(377, 290, 152, 66))
        self.label_231.setFont(font6)
        self.label_231.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_232 = QLabel(self.frame_34)
        self.label_232.setObjectName(u"label_232")
        self.label_232.setGeometry(QRect(10, 75, 241, 18))
        font7 = QFont()
        font7.setPointSize(10)
        self.label_232.setFont(font7)
        self.label_232.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_60 = QFrame(self.frame_34)
        self.line_60.setObjectName(u"line_60")
        self.line_60.setGeometry(QRect(316, 279, 274, 16))
        self.line_60.setFrameShape(QFrame.Shape.HLine)
        self.line_60.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.frame_34, 1, 1, 1, 1)

        self.frame_38 = QFrame(self.frame_30)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFont(font3)
        self.frame_38.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_38.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)
        self.label_266 = QLabel(self.frame_38)
        self.label_266.setObjectName(u"label_266")
        self.label_266.setGeometry(QRect(13, 10, 161, 33))
        self.label_266.setFont(font4)
        self.label_266.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_267 = QLabel(self.frame_38)
        self.label_267.setObjectName(u"label_267")
        self.label_267.setGeometry(QRect(16, 49, 16, 16))
        self.label_267.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_268 = QLabel(self.frame_38)
        self.label_268.setObjectName(u"label_268")
        self.label_268.setGeometry(QRect(35, 49, 111, 16))
        self.label_268.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_25 = QPushButton(self.frame_38)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_25.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_269 = QLabel(self.frame_38)
        self.label_269.setObjectName(u"label_269")
        self.label_269.setGeometry(QRect(285, 10, 191, 31))
        self.label_269.setFont(font5)
        self.label_269.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_270 = QLabel(self.frame_38)
        self.label_270.setObjectName(u"label_270")
        self.label_270.setGeometry(QRect(477, 17, 91, 20))
        self.label_270.setFont(font2)
        self.label_270.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_271 = QLabel(self.frame_38)
        self.label_271.setObjectName(u"label_271")
        self.label_271.setGeometry(QRect(354, 44, 151, 20))
        self.label_271.setFont(font2)
        self.label_271.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_272 = QLabel(self.frame_38)
        self.label_272.setObjectName(u"label_272")
        self.label_272.setGeometry(QRect(10, 99, 291, 269))
        self.label_272.setStyleSheet(u"border-radius:5px;")
        self.label_272.setPixmap(QPixmap(u"../../Shivam/Downloads/WhatsApp Image 2024-06-26 at 19.16.15_a6f43295.jpg"))
        self.label_272.setScaledContents(True)
        self.line_70 = QFrame(self.frame_38)
        self.line_70.setObjectName(u"line_70")
        self.line_70.setGeometry(QRect(307, 99, 16, 269))
        self.line_70.setFrameShape(QFrame.Shape.VLine)
        self.line_70.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_273 = QLabel(self.frame_38)
        self.label_273.setObjectName(u"label_273")
        self.label_273.setGeometry(QRect(377, 99, 175, 44))
        self.label_273.setFont(font6)
        self.label_273.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_71 = QFrame(self.frame_38)
        self.line_71.setObjectName(u"line_71")
        self.line_71.setGeometry(QRect(316, 185, 274, 16))
        self.line_71.setFrameShape(QFrame.Shape.HLine)
        self.line_71.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_274 = QLabel(self.frame_38)
        self.label_274.setObjectName(u"label_274")
        self.label_274.setGeometry(QRect(377, 194, 120, 44))
        self.label_274.setFont(font6)
        self.label_274.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_275 = QLabel(self.frame_38)
        self.label_275.setObjectName(u"label_275")
        self.label_275.setGeometry(QRect(377, 290, 152, 66))
        self.label_275.setFont(font6)
        self.label_275.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_276 = QLabel(self.frame_38)
        self.label_276.setObjectName(u"label_276")
        self.label_276.setGeometry(QRect(10, 75, 410, 18))
        self.label_276.setFont(font7)
        self.label_276.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_72 = QFrame(self.frame_38)
        self.line_72.setObjectName(u"line_72")
        self.line_72.setGeometry(QRect(316, 279, 274, 16))
        self.line_72.setFrameShape(QFrame.Shape.HLine)
        self.line_72.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.frame_38, 3, 1, 1, 1)

        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFont(font3)
        self.frame_33.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.label_211 = QLabel(self.frame_33)
        self.label_211.setObjectName(u"label_211")
        self.label_211.setGeometry(QRect(13, 10, 261, 33))
        self.label_211.setFont(font4)
        self.label_211.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_212 = QLabel(self.frame_33)
        self.label_212.setObjectName(u"label_212")
        self.label_212.setGeometry(QRect(16, 49, 16, 16))
        self.label_212.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_213 = QLabel(self.frame_33)
        self.label_213.setObjectName(u"label_213")
        self.label_213.setGeometry(QRect(35, 49, 71, 16))
        self.label_213.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_20 = QPushButton(self.frame_33)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_20.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_214 = QLabel(self.frame_33)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setGeometry(QRect(298, 10, 231, 31))
        font8 = QFont()
        font8.setPointSize(16)
        self.label_214.setFont(font8)
        self.label_214.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_215 = QLabel(self.frame_33)
        self.label_215.setObjectName(u"label_215")
        self.label_215.setGeometry(QRect(477, 17, 75, 20))
        self.label_215.setFont(font2)
        self.label_215.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_216 = QLabel(self.frame_33)
        self.label_216.setObjectName(u"label_216")
        self.label_216.setGeometry(QRect(354, 44, 151, 20))
        self.label_216.setFont(font2)
        self.label_216.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_217 = QLabel(self.frame_33)
        self.label_217.setObjectName(u"label_217")
        self.label_217.setGeometry(QRect(10, 99, 291, 269))
        self.label_217.setStyleSheet(u"border-radius:5px;")
        self.label_217.setPixmap(QPixmap(u"PropImages/Thane/Thane-ShivlayaHeights/Thane-3.jpg"))
        self.label_217.setScaledContents(True)
        self.line_55 = QFrame(self.frame_33)
        self.line_55.setObjectName(u"line_55")
        self.line_55.setGeometry(QRect(307, 99, 16, 269))
        self.line_55.setFrameShape(QFrame.Shape.VLine)
        self.line_55.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_218 = QLabel(self.frame_33)
        self.label_218.setObjectName(u"label_218")
        self.label_218.setGeometry(QRect(377, 99, 175, 44))
        self.label_218.setFont(font6)
        self.label_218.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_56 = QFrame(self.frame_33)
        self.line_56.setObjectName(u"line_56")
        self.line_56.setGeometry(QRect(316, 185, 274, 16))
        self.line_56.setFrameShape(QFrame.Shape.HLine)
        self.line_56.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_219 = QLabel(self.frame_33)
        self.label_219.setObjectName(u"label_219")
        self.label_219.setGeometry(QRect(377, 194, 120, 44))
        self.label_219.setFont(font6)
        self.label_219.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_220 = QLabel(self.frame_33)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setGeometry(QRect(377, 290, 152, 66))
        self.label_220.setFont(font6)
        self.label_220.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_221 = QLabel(self.frame_33)
        self.label_221.setObjectName(u"label_221")
        self.label_221.setGeometry(QRect(10, 75, 421, 18))
        self.label_221.setFont(font7)
        self.label_221.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_57 = QFrame(self.frame_33)
        self.line_57.setObjectName(u"line_57")
        self.line_57.setGeometry(QRect(316, 279, 274, 16))
        self.line_57.setFrameShape(QFrame.Shape.HLine)
        self.line_57.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.frame_33, 1, 0, 1, 1)

        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFont(font3)
        self.frame_32.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.label_200 = QLabel(self.frame_32)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setGeometry(QRect(13, 10, 181, 33))
        self.label_200.setFont(font4)
        self.label_200.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_201 = QLabel(self.frame_32)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setGeometry(QRect(16, 49, 16, 16))
        self.label_201.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_202 = QLabel(self.frame_32)
        self.label_202.setObjectName(u"label_202")
        self.label_202.setGeometry(QRect(35, 49, 81, 16))
        self.label_202.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_19 = QPushButton(self.frame_32)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_19.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_203 = QLabel(self.frame_32)
        self.label_203.setObjectName(u"label_203")
        self.label_203.setGeometry(QRect(300, 10, 182, 31))
        self.label_203.setFont(font5)
        self.label_203.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_204 = QLabel(self.frame_32)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setGeometry(QRect(467, 17, 91, 20))
        self.label_204.setFont(font2)
        self.label_204.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_205 = QLabel(self.frame_32)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setGeometry(QRect(354, 44, 151, 20))
        self.label_205.setFont(font2)
        self.label_205.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.line_52 = QFrame(self.frame_32)
        self.line_52.setObjectName(u"line_52")
        self.line_52.setGeometry(QRect(307, 99, 16, 269))
        self.line_52.setFrameShape(QFrame.Shape.VLine)
        self.line_52.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_207 = QLabel(self.frame_32)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setGeometry(QRect(377, 99, 175, 44))
        self.label_207.setFont(font6)
        self.label_207.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_53 = QFrame(self.frame_32)
        self.line_53.setObjectName(u"line_53")
        self.line_53.setGeometry(QRect(316, 185, 274, 16))
        self.line_53.setFrameShape(QFrame.Shape.HLine)
        self.line_53.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_208 = QLabel(self.frame_32)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setGeometry(QRect(377, 194, 120, 44))
        self.label_208.setFont(font6)
        self.label_208.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_209 = QLabel(self.frame_32)
        self.label_209.setObjectName(u"label_209")
        self.label_209.setGeometry(QRect(377, 289, 152, 66))
        self.label_209.setFont(font6)
        self.label_209.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_210 = QLabel(self.frame_32)
        self.label_210.setObjectName(u"label_210")
        self.label_210.setGeometry(QRect(10, 75, 191, 18))
        self.label_210.setFont(font7)
        self.label_210.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_54 = QFrame(self.frame_32)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setGeometry(QRect(316, 279, 274, 16))
        self.line_54.setFrameShape(QFrame.Shape.HLine)
        self.line_54.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_206 = QLabel(self.frame_32)
        self.label_206.setObjectName(u"label_206")
        self.label_206.setGeometry(QRect(10, 99, 291, 269))
        self.label_206.setStyleSheet(u"border-radius:5px;")
        self.label_206.setPixmap(QPixmap(u"PropImages/Thane/Thane-AsharMerac/Thane-2.1.Elevtion.jpg"))
        self.label_206.setScaledContents(True)

        self.gridLayout_3.addWidget(self.frame_32, 0, 1, 1, 1)

        self.frame_35 = QFrame(self.frame_30)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFont(font3)
        self.frame_35.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_35.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.label_233 = QLabel(self.frame_35)
        self.label_233.setObjectName(u"label_233")
        self.label_233.setGeometry(QRect(13, 10, 231, 33))
        self.label_233.setFont(font4)
        self.label_233.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_234 = QLabel(self.frame_35)
        self.label_234.setObjectName(u"label_234")
        self.label_234.setGeometry(QRect(16, 49, 16, 16))
        self.label_234.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_235 = QLabel(self.frame_35)
        self.label_235.setObjectName(u"label_235")
        self.label_235.setGeometry(QRect(35, 49, 90, 16))
        self.label_235.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_22 = QPushButton(self.frame_35)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_22.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_236 = QLabel(self.frame_35)
        self.label_236.setObjectName(u"label_236")
        self.label_236.setGeometry(QRect(298, 10, 182, 31))
        self.label_236.setFont(font5)
        self.label_236.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_237 = QLabel(self.frame_35)
        self.label_237.setObjectName(u"label_237")
        self.label_237.setGeometry(QRect(471, 17, 81, 20))
        self.label_237.setFont(font2)
        self.label_237.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_238 = QLabel(self.frame_35)
        self.label_238.setObjectName(u"label_238")
        self.label_238.setGeometry(QRect(354, 44, 151, 20))
        self.label_238.setFont(font2)
        self.label_238.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_239 = QLabel(self.frame_35)
        self.label_239.setObjectName(u"label_239")
        self.label_239.setGeometry(QRect(10, 99, 291, 269))
        self.label_239.setStyleSheet(u"border-radius:5px;")
        self.label_239.setPixmap(QPixmap(u"PropImages/Thane/Thane-ParijasHorizon/Thane-5.jpg"))
        self.label_239.setScaledContents(True)
        self.line_61 = QFrame(self.frame_35)
        self.line_61.setObjectName(u"line_61")
        self.line_61.setGeometry(QRect(307, 99, 16, 269))
        self.line_61.setFrameShape(QFrame.Shape.VLine)
        self.line_61.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_240 = QLabel(self.frame_35)
        self.label_240.setObjectName(u"label_240")
        self.label_240.setGeometry(QRect(377, 99, 175, 44))
        self.label_240.setFont(font6)
        self.label_240.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_62 = QFrame(self.frame_35)
        self.line_62.setObjectName(u"line_62")
        self.line_62.setGeometry(QRect(316, 185, 274, 16))
        self.line_62.setFrameShape(QFrame.Shape.HLine)
        self.line_62.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_241 = QLabel(self.frame_35)
        self.label_241.setObjectName(u"label_241")
        self.label_241.setGeometry(QRect(377, 194, 120, 44))
        self.label_241.setFont(font6)
        self.label_241.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_242 = QLabel(self.frame_35)
        self.label_242.setObjectName(u"label_242")
        self.label_242.setGeometry(QRect(377, 290, 152, 66))
        self.label_242.setFont(font6)
        self.label_242.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_243 = QLabel(self.frame_35)
        self.label_243.setObjectName(u"label_243")
        self.label_243.setGeometry(QRect(10, 75, 281, 18))
        self.label_243.setFont(font7)
        self.label_243.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_63 = QFrame(self.frame_35)
        self.line_63.setObjectName(u"line_63")
        self.line_63.setGeometry(QRect(316, 279, 274, 16))
        self.line_63.setFrameShape(QFrame.Shape.HLine)
        self.line_63.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.frame_35, 2, 0, 1, 1)

        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFont(font3)
        self.frame_31.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.label_189 = QLabel(self.frame_31)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setGeometry(QRect(13, 10, 161, 33))
        self.label_189.setFont(font4)
        self.label_189.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_190 = QLabel(self.frame_31)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setGeometry(QRect(16, 49, 16, 16))
        self.label_190.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_191 = QLabel(self.frame_31)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setGeometry(QRect(35, 49, 81, 16))
        self.label_191.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_18 = QPushButton(self.frame_31)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_18.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_192 = QLabel(self.frame_31)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setGeometry(QRect(287, 10, 191, 31))
        self.label_192.setFont(font5)
        self.label_192.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_193 = QLabel(self.frame_31)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setGeometry(QRect(477, 17, 75, 20))
        self.label_193.setFont(font2)
        self.label_193.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_194 = QLabel(self.frame_31)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setGeometry(QRect(354, 44, 151, 20))
        self.label_194.setFont(font2)
        self.label_194.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_195 = QLabel(self.frame_31)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setGeometry(QRect(10, 99, 291, 269))
        self.label_195.setStyleSheet(u"border-radius:5px;")
        self.label_195.setPixmap(QPixmap(u"PropImages/Thane/Thane-Balkum.Thane.west/Thane-1.jpg"))
        self.label_195.setScaledContents(True)
        self.line_49 = QFrame(self.frame_31)
        self.line_49.setObjectName(u"line_49")
        self.line_49.setGeometry(QRect(307, 99, 16, 269))
        self.line_49.setFrameShape(QFrame.Shape.VLine)
        self.line_49.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_196 = QLabel(self.frame_31)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setGeometry(QRect(377, 99, 175, 44))
        self.label_196.setFont(font6)
        self.label_196.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_50 = QFrame(self.frame_31)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setGeometry(QRect(316, 185, 274, 16))
        self.line_50.setFrameShape(QFrame.Shape.HLine)
        self.line_50.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_197 = QLabel(self.frame_31)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setGeometry(QRect(377, 194, 120, 44))
        self.label_197.setFont(font6)
        self.label_197.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_198 = QLabel(self.frame_31)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setGeometry(QRect(377, 290, 152, 66))
        self.label_198.setFont(font6)
        self.label_198.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_199 = QLabel(self.frame_31)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setGeometry(QRect(10, 75, 410, 18))
        self.label_199.setFont(font7)
        self.label_199.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_51 = QFrame(self.frame_31)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setGeometry(QRect(316, 279, 274, 16))
        self.line_51.setFrameShape(QFrame.Shape.HLine)
        self.line_51.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.frame_31, 0, 0, 1, 1)

        self.frame_37 = QFrame(self.frame_30)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFont(font3)
        self.frame_37.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_37.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.label_255 = QLabel(self.frame_37)
        self.label_255.setObjectName(u"label_255")
        self.label_255.setGeometry(QRect(13, 10, 181, 33))
        self.label_255.setFont(font4)
        self.label_255.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_256 = QLabel(self.frame_37)
        self.label_256.setObjectName(u"label_256")
        self.label_256.setGeometry(QRect(16, 49, 16, 16))
        self.label_256.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_257 = QLabel(self.frame_37)
        self.label_257.setObjectName(u"label_257")
        self.label_257.setGeometry(QRect(35, 49, 81, 16))
        self.label_257.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_24 = QPushButton(self.frame_37)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_24.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_258 = QLabel(self.frame_37)
        self.label_258.setObjectName(u"label_258")
        self.label_258.setGeometry(QRect(298, 10, 182, 31))
        self.label_258.setFont(font5)
        self.label_258.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_259 = QLabel(self.frame_37)
        self.label_259.setObjectName(u"label_259")
        self.label_259.setGeometry(QRect(472, 17, 75, 20))
        self.label_259.setFont(font2)
        self.label_259.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_260 = QLabel(self.frame_37)
        self.label_260.setObjectName(u"label_260")
        self.label_260.setGeometry(QRect(354, 44, 151, 20))
        self.label_260.setFont(font2)
        self.label_260.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_261 = QLabel(self.frame_37)
        self.label_261.setObjectName(u"label_261")
        self.label_261.setGeometry(QRect(10, 99, 291, 269))
        self.label_261.setStyleSheet(u"border-radius:5px;")
        self.label_261.setPixmap(QPixmap(u"PropImages/WhatsApp Image 2024-07-05 at 20.11.02_1a624b3c.jpg"))
        self.label_261.setScaledContents(True)
        self.line_67 = QFrame(self.frame_37)
        self.line_67.setObjectName(u"line_67")
        self.line_67.setGeometry(QRect(307, 99, 16, 269))
        self.line_67.setFrameShape(QFrame.Shape.VLine)
        self.line_67.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_262 = QLabel(self.frame_37)
        self.label_262.setObjectName(u"label_262")
        self.label_262.setGeometry(QRect(377, 99, 175, 44))
        self.label_262.setFont(font6)
        self.label_262.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_68 = QFrame(self.frame_37)
        self.line_68.setObjectName(u"line_68")
        self.line_68.setGeometry(QRect(316, 185, 274, 16))
        self.line_68.setFrameShape(QFrame.Shape.HLine)
        self.line_68.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_263 = QLabel(self.frame_37)
        self.label_263.setObjectName(u"label_263")
        self.label_263.setGeometry(QRect(377, 194, 120, 44))
        self.label_263.setFont(font6)
        self.label_263.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_264 = QLabel(self.frame_37)
        self.label_264.setObjectName(u"label_264")
        self.label_264.setGeometry(QRect(377, 290, 152, 66))
        self.label_264.setFont(font6)
        self.label_264.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_265 = QLabel(self.frame_37)
        self.label_265.setObjectName(u"label_265")
        self.label_265.setGeometry(QRect(10, 75, 421, 18))
        self.label_265.setFont(font7)
        self.label_265.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_69 = QFrame(self.frame_37)
        self.line_69.setObjectName(u"line_69")
        self.line_69.setGeometry(QRect(316, 279, 274, 16))
        self.line_69.setFrameShape(QFrame.Shape.HLine)
        self.line_69.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.frame_37, 3, 0, 1, 1)

        self.frame_36 = QFrame(self.frame_30)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFont(font3)
        self.frame_36.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_36.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
        self.label_244 = QLabel(self.frame_36)
        self.label_244.setObjectName(u"label_244")
        self.label_244.setGeometry(QRect(13, 10, 231, 33))
        self.label_244.setFont(font4)
        self.label_244.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_245 = QLabel(self.frame_36)
        self.label_245.setObjectName(u"label_245")
        self.label_245.setGeometry(QRect(16, 49, 16, 16))
        self.label_245.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_246 = QLabel(self.frame_36)
        self.label_246.setObjectName(u"label_246")
        self.label_246.setGeometry(QRect(35, 49, 71, 16))
        self.label_246.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_23 = QPushButton(self.frame_36)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_23.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_247 = QLabel(self.frame_36)
        self.label_247.setObjectName(u"label_247")
        self.label_247.setGeometry(QRect(280, 10, 201, 31))
        self.label_247.setFont(font5)
        self.label_247.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_248 = QLabel(self.frame_36)
        self.label_248.setObjectName(u"label_248")
        self.label_248.setGeometry(QRect(484, 17, 75, 20))
        self.label_248.setFont(font2)
        self.label_248.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_249 = QLabel(self.frame_36)
        self.label_249.setObjectName(u"label_249")
        self.label_249.setGeometry(QRect(354, 44, 151, 20))
        self.label_249.setFont(font2)
        self.label_249.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_250 = QLabel(self.frame_36)
        self.label_250.setObjectName(u"label_250")
        self.label_250.setGeometry(QRect(10, 99, 291, 269))
        self.label_250.setStyleSheet(u"border-radius:5px;")
        self.label_250.setPixmap(QPixmap(u"PropImages/WhatsApp Image 2024-07-05 at 20.01.08_33b1ab10.jpg"))
        self.label_250.setScaledContents(True)
        self.line_64 = QFrame(self.frame_36)
        self.line_64.setObjectName(u"line_64")
        self.line_64.setGeometry(QRect(307, 99, 16, 269))
        self.line_64.setFrameShape(QFrame.Shape.VLine)
        self.line_64.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_251 = QLabel(self.frame_36)
        self.label_251.setObjectName(u"label_251")
        self.label_251.setGeometry(QRect(377, 99, 175, 44))
        self.label_251.setFont(font6)
        self.label_251.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_65 = QFrame(self.frame_36)
        self.line_65.setObjectName(u"line_65")
        self.line_65.setGeometry(QRect(316, 185, 274, 16))
        self.line_65.setFrameShape(QFrame.Shape.HLine)
        self.line_65.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_252 = QLabel(self.frame_36)
        self.label_252.setObjectName(u"label_252")
        self.label_252.setGeometry(QRect(377, 194, 120, 44))
        self.label_252.setFont(font6)
        self.label_252.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_253 = QLabel(self.frame_36)
        self.label_253.setObjectName(u"label_253")
        self.label_253.setGeometry(QRect(377, 292, 152, 66))
        self.label_253.setFont(font6)
        self.label_253.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_254 = QLabel(self.frame_36)
        self.label_254.setObjectName(u"label_254")
        self.label_254.setGeometry(QRect(10, 75, 410, 18))
        self.label_254.setFont(font7)
        self.label_254.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_66 = QFrame(self.frame_36)
        self.line_66.setObjectName(u"line_66")
        self.line_66.setGeometry(QRect(316, 279, 274, 16))
        self.line_66.setFrameShape(QFrame.Shape.HLine)
        self.line_66.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.frame_36, 2, 1, 1, 1)


        self.verticalLayout_37.addLayout(self.gridLayout_3)


        self.horizontalLayout_13.addWidget(self.frame_30)


        self.verticalLayout_18.addWidget(self.frame_6)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_19.addWidget(self.scrollArea_6)


        self.verticalLayout_17.addWidget(self.widget_6)

        self.stackedWidget_3.addWidget(self.dashboardpage)
        self.meassagespage = QWidget()
        self.meassagespage.setObjectName(u"meassagespage")
        self.verticalLayout_2 = QVBoxLayout(self.meassagespage)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.meassagespage)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_7 = QScrollArea(self.widget)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(7, 94, 84);\n"
" }")
        self.scrollArea_7.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 119, 2000))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 2000))
        self.frame_7.setStyleSheet(u"")
        self.horizontalLayout_14 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(50)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(50, 35, -1, 60)
        self.frame_46 = QFrame(self.frame_7)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFont(font3)
        self.frame_46.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_46.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Shadow.Raised)
        self.label_354 = QLabel(self.frame_46)
        self.label_354.setObjectName(u"label_354")
        self.label_354.setGeometry(QRect(13, 10, 221, 33))
        self.label_354.setFont(font4)
        self.label_354.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_355 = QLabel(self.frame_46)
        self.label_355.setObjectName(u"label_355")
        self.label_355.setGeometry(QRect(16, 49, 16, 16))
        self.label_355.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_356 = QLabel(self.frame_46)
        self.label_356.setObjectName(u"label_356")
        self.label_356.setGeometry(QRect(35, 49, 190, 16))
        self.label_356.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_35 = QPushButton(self.frame_46)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_35.setStyleSheet(u"QPushButton\n"
"{color:white;\n"
"	background-color: rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_357 = QLabel(self.frame_46)
        self.label_357.setObjectName(u"label_357")
        self.label_357.setGeometry(QRect(301, 10, 191, 31))
        self.label_357.setFont(font8)
        self.label_357.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_358 = QLabel(self.frame_46)
        self.label_358.setObjectName(u"label_358")
        self.label_358.setGeometry(QRect(482, 17, 75, 20))
        self.label_358.setFont(font2)
        self.label_358.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_359 = QLabel(self.frame_46)
        self.label_359.setObjectName(u"label_359")
        self.label_359.setGeometry(QRect(354, 44, 151, 20))
        self.label_359.setFont(font2)
        self.label_359.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_360 = QLabel(self.frame_46)
        self.label_360.setObjectName(u"label_360")
        self.label_360.setGeometry(QRect(10, 99, 291, 269))
        self.label_360.setStyleSheet(u"border-radius:5px;")
        self.label_360.setPixmap(QPixmap(u"../../Shivam/Downloads/WhatsApp Image 2024-06-26 at 19.16.15_a6f43295.jpg"))
        self.label_360.setScaledContents(True)
        self.line_94 = QFrame(self.frame_46)
        self.line_94.setObjectName(u"line_94")
        self.line_94.setGeometry(QRect(307, 99, 16, 269))
        self.line_94.setFrameShape(QFrame.Shape.VLine)
        self.line_94.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_361 = QLabel(self.frame_46)
        self.label_361.setObjectName(u"label_361")
        self.label_361.setGeometry(QRect(377, 99, 175, 44))
        self.label_361.setFont(font6)
        self.label_361.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_95 = QFrame(self.frame_46)
        self.line_95.setObjectName(u"line_95")
        self.line_95.setGeometry(QRect(316, 185, 274, 16))
        self.line_95.setFrameShape(QFrame.Shape.HLine)
        self.line_95.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_362 = QLabel(self.frame_46)
        self.label_362.setObjectName(u"label_362")
        self.label_362.setGeometry(QRect(377, 194, 120, 44))
        self.label_362.setFont(font6)
        self.label_362.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_363 = QLabel(self.frame_46)
        self.label_363.setObjectName(u"label_363")
        self.label_363.setGeometry(QRect(377, 290, 152, 66))
        self.label_363.setFont(font6)
        self.label_363.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_364 = QLabel(self.frame_46)
        self.label_364.setObjectName(u"label_364")
        self.label_364.setGeometry(QRect(10, 75, 181, 18))
        self.label_364.setFont(font7)
        self.label_364.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_96 = QFrame(self.frame_46)
        self.line_96.setObjectName(u"line_96")
        self.line_96.setGeometry(QRect(316, 279, 274, 16))
        self.line_96.setFrameShape(QFrame.Shape.HLine)
        self.line_96.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.frame_46, 3, 1, 1, 1)

        self.frame_39 = QFrame(self.frame_7)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFont(font3)
        self.frame_39.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_39.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Shadow.Raised)
        self.label_277 = QLabel(self.frame_39)
        self.label_277.setObjectName(u"label_277")
        self.label_277.setGeometry(QRect(13, 10, 231, 33))
        self.label_277.setFont(font4)
        self.label_277.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_278 = QLabel(self.frame_39)
        self.label_278.setObjectName(u"label_278")
        self.label_278.setGeometry(QRect(16, 49, 16, 16))
        self.label_278.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_279 = QLabel(self.frame_39)
        self.label_279.setObjectName(u"label_279")
        self.label_279.setGeometry(QRect(35, 49, 81, 16))
        self.label_279.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_26 = QPushButton(self.frame_39)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_26.setStyleSheet(u"QPushButton\n"
"{color:white;\n"
"	background-color: rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_280 = QLabel(self.frame_39)
        self.label_280.setObjectName(u"label_280")
        self.label_280.setGeometry(QRect(298, 10, 182, 31))
        self.label_280.setFont(font5)
        self.label_280.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_281 = QLabel(self.frame_39)
        self.label_281.setObjectName(u"label_281")
        self.label_281.setGeometry(QRect(477, 17, 75, 20))
        self.label_281.setFont(font2)
        self.label_281.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_282 = QLabel(self.frame_39)
        self.label_282.setObjectName(u"label_282")
        self.label_282.setGeometry(QRect(354, 44, 151, 20))
        self.label_282.setFont(font2)
        self.label_282.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_283 = QLabel(self.frame_39)
        self.label_283.setObjectName(u"label_283")
        self.label_283.setGeometry(QRect(10, 99, 291, 269))
        self.label_283.setStyleSheet(u"border-radius:5px;")
        self.label_283.setPixmap(QPixmap(u"PropImages/fs.jpg"))
        self.label_283.setScaledContents(True)
        self.line_73 = QFrame(self.frame_39)
        self.line_73.setObjectName(u"line_73")
        self.line_73.setGeometry(QRect(307, 99, 16, 269))
        self.line_73.setFrameShape(QFrame.Shape.VLine)
        self.line_73.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_284 = QLabel(self.frame_39)
        self.label_284.setObjectName(u"label_284")
        self.label_284.setGeometry(QRect(377, 99, 175, 44))
        self.label_284.setFont(font6)
        self.label_284.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_74 = QFrame(self.frame_39)
        self.line_74.setObjectName(u"line_74")
        self.line_74.setGeometry(QRect(316, 185, 274, 16))
        self.line_74.setFrameShape(QFrame.Shape.HLine)
        self.line_74.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_285 = QLabel(self.frame_39)
        self.label_285.setObjectName(u"label_285")
        self.label_285.setGeometry(QRect(377, 194, 120, 44))
        self.label_285.setFont(font6)
        self.label_285.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_286 = QLabel(self.frame_39)
        self.label_286.setObjectName(u"label_286")
        self.label_286.setGeometry(QRect(377, 290, 152, 66))
        self.label_286.setFont(font6)
        self.label_286.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_287 = QLabel(self.frame_39)
        self.label_287.setObjectName(u"label_287")
        self.label_287.setGeometry(QRect(10, 72, 591, 18))
        self.label_287.setFont(font7)
        self.label_287.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_75 = QFrame(self.frame_39)
        self.line_75.setObjectName(u"line_75")
        self.line_75.setGeometry(QRect(316, 279, 274, 16))
        self.line_75.setFrameShape(QFrame.Shape.HLine)
        self.line_75.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.frame_39, 0, 0, 1, 1)

        self.frame_43 = QFrame(self.frame_7)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFont(font3)
        self.frame_43.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_43.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Shadow.Raised)
        self.label_321 = QLabel(self.frame_43)
        self.label_321.setObjectName(u"label_321")
        self.label_321.setGeometry(QRect(13, 10, 331, 33))
        font9 = QFont()
        font9.setFamilies([u"Sitka Subheading"])
        font9.setPointSize(23)
        self.label_321.setFont(font9)
        self.label_321.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_322 = QLabel(self.frame_43)
        self.label_322.setObjectName(u"label_322")
        self.label_322.setGeometry(QRect(16, 49, 16, 16))
        self.label_322.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_323 = QLabel(self.frame_43)
        self.label_323.setObjectName(u"label_323")
        self.label_323.setGeometry(QRect(35, 49, 101, 16))
        self.label_323.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_30 = QPushButton(self.frame_43)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_30.setStyleSheet(u"QPushButton\n"
"{color:white;\n"
"	background-color: rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_324 = QLabel(self.frame_43)
        self.label_324.setObjectName(u"label_324")
        self.label_324.setGeometry(QRect(330, 10, 171, 30))
        self.label_324.setFont(font8)
        self.label_324.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_325 = QLabel(self.frame_43)
        self.label_325.setObjectName(u"label_325")
        self.label_325.setGeometry(QRect(500, 17, 70, 20))
        self.label_325.setFont(font2)
        self.label_325.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_326 = QLabel(self.frame_43)
        self.label_326.setObjectName(u"label_326")
        self.label_326.setGeometry(QRect(354, 44, 151, 20))
        self.label_326.setFont(font2)
        self.label_326.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_327 = QLabel(self.frame_43)
        self.label_327.setObjectName(u"label_327")
        self.label_327.setGeometry(QRect(10, 99, 291, 269))
        self.label_327.setStyleSheet(u"border-radius:5px;")
        self.label_327.setPixmap(QPixmap(u"PropImages/namrata_prime_land-talegaon_dabhade_1-pune-namrata_group.jpg"))
        self.label_327.setScaledContents(True)
        self.line_85 = QFrame(self.frame_43)
        self.line_85.setObjectName(u"line_85")
        self.line_85.setGeometry(QRect(307, 99, 16, 269))
        self.line_85.setFrameShape(QFrame.Shape.VLine)
        self.line_85.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_328 = QLabel(self.frame_43)
        self.label_328.setObjectName(u"label_328")
        self.label_328.setGeometry(QRect(377, 99, 175, 44))
        self.label_328.setFont(font6)
        self.label_328.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_86 = QFrame(self.frame_43)
        self.line_86.setObjectName(u"line_86")
        self.line_86.setGeometry(QRect(316, 185, 274, 16))
        self.line_86.setFrameShape(QFrame.Shape.HLine)
        self.line_86.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_329 = QLabel(self.frame_43)
        self.label_329.setObjectName(u"label_329")
        self.label_329.setGeometry(QRect(377, 194, 120, 44))
        self.label_329.setFont(font6)
        self.label_329.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_330 = QLabel(self.frame_43)
        self.label_330.setObjectName(u"label_330")
        self.label_330.setGeometry(QRect(377, 288, 152, 66))
        self.label_330.setFont(font6)
        self.label_330.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_331 = QLabel(self.frame_43)
        self.label_331.setObjectName(u"label_331")
        self.label_331.setGeometry(QRect(10, 75, 410, 18))
        self.label_331.setFont(font7)
        self.label_331.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_87 = QFrame(self.frame_43)
        self.line_87.setObjectName(u"line_87")
        self.line_87.setGeometry(QRect(316, 279, 274, 16))
        self.line_87.setFrameShape(QFrame.Shape.HLine)
        self.line_87.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.frame_43, 2, 0, 1, 1)

        self.frame_44 = QFrame(self.frame_7)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFont(font3)
        self.frame_44.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_44.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Shadow.Raised)
        self.label_332 = QLabel(self.frame_44)
        self.label_332.setObjectName(u"label_332")
        self.label_332.setGeometry(QRect(13, 10, 171, 33))
        self.label_332.setFont(font4)
        self.label_332.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_333 = QLabel(self.frame_44)
        self.label_333.setObjectName(u"label_333")
        self.label_333.setGeometry(QRect(16, 49, 16, 16))
        self.label_333.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_334 = QLabel(self.frame_44)
        self.label_334.setObjectName(u"label_334")
        self.label_334.setGeometry(QRect(35, 49, 231, 16))
        self.label_334.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_31 = QPushButton(self.frame_44)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_31.setStyleSheet(u"QPushButton\n"
"{color:white;\n"
"	background-color: rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_335 = QLabel(self.frame_44)
        self.label_335.setObjectName(u"label_335")
        self.label_335.setGeometry(QRect(298, 10, 182, 31))
        self.label_335.setFont(font5)
        self.label_335.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_336 = QLabel(self.frame_44)
        self.label_336.setObjectName(u"label_336")
        self.label_336.setGeometry(QRect(477, 17, 75, 20))
        self.label_336.setFont(font2)
        self.label_336.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_337 = QLabel(self.frame_44)
        self.label_337.setObjectName(u"label_337")
        self.label_337.setGeometry(QRect(354, 44, 141, 20))
        self.label_337.setFont(font2)
        self.label_337.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_338 = QLabel(self.frame_44)
        self.label_338.setObjectName(u"label_338")
        self.label_338.setGeometry(QRect(10, 99, 291, 269))
        self.label_338.setPixmap(QPixmap(u"PropImages/fs-large.jpg"))
        self.label_338.setScaledContents(True)
        self.line_88 = QFrame(self.frame_44)
        self.line_88.setObjectName(u"line_88")
        self.line_88.setGeometry(QRect(307, 99, 16, 269))
        self.line_88.setFrameShape(QFrame.Shape.VLine)
        self.line_88.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_339 = QLabel(self.frame_44)
        self.label_339.setObjectName(u"label_339")
        self.label_339.setGeometry(QRect(377, 99, 175, 44))
        self.label_339.setFont(font6)
        self.label_339.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_89 = QFrame(self.frame_44)
        self.line_89.setObjectName(u"line_89")
        self.line_89.setGeometry(QRect(316, 185, 274, 16))
        self.line_89.setFrameShape(QFrame.Shape.HLine)
        self.line_89.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_340 = QLabel(self.frame_44)
        self.label_340.setObjectName(u"label_340")
        self.label_340.setGeometry(QRect(377, 194, 120, 44))
        self.label_340.setFont(font6)
        self.label_340.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_341 = QLabel(self.frame_44)
        self.label_341.setObjectName(u"label_341")
        self.label_341.setGeometry(QRect(377, 290, 161, 66))
        self.label_341.setFont(font6)
        self.label_341.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_342 = QLabel(self.frame_44)
        self.label_342.setObjectName(u"label_342")
        self.label_342.setGeometry(QRect(10, 75, 261, 18))
        self.label_342.setFont(font7)
        self.label_342.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_90 = QFrame(self.frame_44)
        self.line_90.setObjectName(u"line_90")
        self.line_90.setGeometry(QRect(316, 279, 274, 16))
        self.line_90.setFrameShape(QFrame.Shape.HLine)
        self.line_90.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.frame_44, 2, 1, 1, 1)

        self.frame_41 = QFrame(self.frame_7)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFont(font3)
        self.frame_41.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_41.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Shadow.Raised)
        self.label_299 = QLabel(self.frame_41)
        self.label_299.setObjectName(u"label_299")
        self.label_299.setGeometry(QRect(13, 10, 201, 33))
        self.label_299.setFont(font4)
        self.label_299.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_300 = QLabel(self.frame_41)
        self.label_300.setObjectName(u"label_300")
        self.label_300.setGeometry(QRect(16, 49, 16, 16))
        self.label_300.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_301 = QLabel(self.frame_41)
        self.label_301.setObjectName(u"label_301")
        self.label_301.setGeometry(QRect(35, 49, 91, 16))
        self.label_301.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_28 = QPushButton(self.frame_41)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_28.setStyleSheet(u"QPushButton\n"
"{color:white;\n"
"	background-color: rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_302 = QLabel(self.frame_41)
        self.label_302.setObjectName(u"label_302")
        self.label_302.setGeometry(QRect(282, 10, 191, 31))
        self.label_302.setFont(font5)
        self.label_302.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_303 = QLabel(self.frame_41)
        self.label_303.setObjectName(u"label_303")
        self.label_303.setGeometry(QRect(477, 17, 91, 20))
        self.label_303.setFont(font2)
        self.label_303.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_304 = QLabel(self.frame_41)
        self.label_304.setObjectName(u"label_304")
        self.label_304.setGeometry(QRect(354, 44, 151, 20))
        self.label_304.setFont(font2)
        self.label_304.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_305 = QLabel(self.frame_41)
        self.label_305.setObjectName(u"label_305")
        self.label_305.setGeometry(QRect(10, 99, 291, 269))
        self.label_305.setStyleSheet(u"border-radius:5px;")
        self.label_305.setPixmap(QPixmap(u"../../Shivam/Downloads/ivory_heights-charholi_budruk-pune-aakar_realties.jpg"))
        self.label_305.setScaledContents(True)
        self.line_79 = QFrame(self.frame_41)
        self.line_79.setObjectName(u"line_79")
        self.line_79.setGeometry(QRect(307, 99, 16, 269))
        self.line_79.setFrameShape(QFrame.Shape.VLine)
        self.line_79.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_306 = QLabel(self.frame_41)
        self.label_306.setObjectName(u"label_306")
        self.label_306.setGeometry(QRect(373, 99, 211, 44))
        self.label_306.setFont(font6)
        self.label_306.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_80 = QFrame(self.frame_41)
        self.line_80.setObjectName(u"line_80")
        self.line_80.setGeometry(QRect(316, 185, 274, 16))
        self.line_80.setFrameShape(QFrame.Shape.HLine)
        self.line_80.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_307 = QLabel(self.frame_41)
        self.label_307.setObjectName(u"label_307")
        self.label_307.setGeometry(QRect(377, 194, 120, 44))
        self.label_307.setFont(font6)
        self.label_307.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_308 = QLabel(self.frame_41)
        self.label_308.setObjectName(u"label_308")
        self.label_308.setGeometry(QRect(377, 290, 152, 66))
        self.label_308.setFont(font6)
        self.label_308.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_309 = QLabel(self.frame_41)
        self.label_309.setObjectName(u"label_309")
        self.label_309.setGeometry(QRect(10, 75, 371, 18))
        self.label_309.setFont(font7)
        self.label_309.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_81 = QFrame(self.frame_41)
        self.line_81.setObjectName(u"line_81")
        self.line_81.setGeometry(QRect(316, 279, 274, 16))
        self.line_81.setFrameShape(QFrame.Shape.HLine)
        self.line_81.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.frame_41, 1, 0, 1, 1)

        self.frame_42 = QFrame(self.frame_7)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFont(font3)
        self.frame_42.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_42.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Shadow.Raised)
        self.label_310 = QLabel(self.frame_42)
        self.label_310.setObjectName(u"label_310")
        self.label_310.setGeometry(QRect(13, 10, 271, 33))
        self.label_310.setFont(font4)
        self.label_310.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_311 = QLabel(self.frame_42)
        self.label_311.setObjectName(u"label_311")
        self.label_311.setGeometry(QRect(16, 49, 16, 16))
        self.label_311.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_312 = QLabel(self.frame_42)
        self.label_312.setObjectName(u"label_312")
        self.label_312.setGeometry(QRect(35, 49, 81, 16))
        self.label_312.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_29 = QPushButton(self.frame_42)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_29.setStyleSheet(u"QPushButton\n"
"{color:white;\n"
"	background-color: rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_313 = QLabel(self.frame_42)
        self.label_313.setObjectName(u"label_313")
        self.label_313.setGeometry(QRect(298, 10, 182, 31))
        self.label_313.setFont(font5)
        self.label_313.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_314 = QLabel(self.frame_42)
        self.label_314.setObjectName(u"label_314")
        self.label_314.setGeometry(QRect(477, 17, 91, 20))
        self.label_314.setFont(font2)
        self.label_314.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_315 = QLabel(self.frame_42)
        self.label_315.setObjectName(u"label_315")
        self.label_315.setGeometry(QRect(354, 44, 151, 20))
        self.label_315.setFont(font2)
        self.label_315.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_316 = QLabel(self.frame_42)
        self.label_316.setObjectName(u"label_316")
        self.label_316.setGeometry(QRect(10, 99, 291, 269))
        self.label_316.setStyleSheet(u"border-radius:5px;")
        self.label_316.setPixmap(QPixmap(u"PropImages/dosti_greenscapes-hadapsar-pune-dosti_realty.jpg"))
        self.label_316.setScaledContents(True)
        self.line_82 = QFrame(self.frame_42)
        self.line_82.setObjectName(u"line_82")
        self.line_82.setGeometry(QRect(307, 99, 16, 269))
        self.line_82.setFrameShape(QFrame.Shape.VLine)
        self.line_82.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_317 = QLabel(self.frame_42)
        self.label_317.setObjectName(u"label_317")
        self.label_317.setGeometry(QRect(377, 99, 175, 44))
        self.label_317.setFont(font6)
        self.label_317.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_83 = QFrame(self.frame_42)
        self.line_83.setObjectName(u"line_83")
        self.line_83.setGeometry(QRect(316, 185, 274, 16))
        self.line_83.setFrameShape(QFrame.Shape.HLine)
        self.line_83.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_318 = QLabel(self.frame_42)
        self.label_318.setObjectName(u"label_318")
        self.label_318.setGeometry(QRect(377, 194, 120, 44))
        self.label_318.setFont(font6)
        self.label_318.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_319 = QLabel(self.frame_42)
        self.label_319.setObjectName(u"label_319")
        self.label_319.setGeometry(QRect(377, 290, 152, 66))
        self.label_319.setFont(font6)
        self.label_319.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_320 = QLabel(self.frame_42)
        self.label_320.setObjectName(u"label_320")
        self.label_320.setGeometry(QRect(10, 75, 221, 18))
        self.label_320.setFont(font7)
        self.label_320.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_84 = QFrame(self.frame_42)
        self.line_84.setObjectName(u"line_84")
        self.line_84.setGeometry(QRect(316, 279, 274, 16))
        self.line_84.setFrameShape(QFrame.Shape.HLine)
        self.line_84.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.frame_42, 1, 1, 1, 1)

        self.frame_40 = QFrame(self.frame_7)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFont(font3)
        self.frame_40.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_40.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)
        self.label_288 = QLabel(self.frame_40)
        self.label_288.setObjectName(u"label_288")
        self.label_288.setGeometry(QRect(13, 10, 251, 33))
        self.label_288.setFont(font4)
        self.label_288.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_289 = QLabel(self.frame_40)
        self.label_289.setObjectName(u"label_289")
        self.label_289.setGeometry(QRect(16, 49, 16, 16))
        self.label_289.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_290 = QLabel(self.frame_40)
        self.label_290.setObjectName(u"label_290")
        self.label_290.setGeometry(QRect(35, 49, 101, 16))
        self.label_290.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_27 = QPushButton(self.frame_40)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_27.setStyleSheet(u"QPushButton\n"
"{color:white;\n"
"	background-color: rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_291 = QLabel(self.frame_40)
        self.label_291.setObjectName(u"label_291")
        self.label_291.setGeometry(QRect(310, 9, 171, 31))
        self.label_291.setFont(font8)
        self.label_291.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_292 = QLabel(self.frame_40)
        self.label_292.setObjectName(u"label_292")
        self.label_292.setGeometry(QRect(488, 15, 80, 20))
        self.label_292.setFont(font2)
        self.label_292.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_293 = QLabel(self.frame_40)
        self.label_293.setObjectName(u"label_293")
        self.label_293.setGeometry(QRect(354, 44, 151, 20))
        self.label_293.setFont(font2)
        self.label_293.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_294 = QLabel(self.frame_40)
        self.label_294.setObjectName(u"label_294")
        self.label_294.setGeometry(QRect(10, 99, 291, 269))
        self.label_294.setStyleSheet(u"border-radius:5px;")
        self.label_294.setPixmap(QPixmap(u"../../Shivam/Downloads/WhatsApp Image 2024-06-26 at 19.16.15_a6f43295.jpg"))
        self.label_294.setScaledContents(True)
        self.line_76 = QFrame(self.frame_40)
        self.line_76.setObjectName(u"line_76")
        self.line_76.setGeometry(QRect(307, 99, 16, 269))
        self.line_76.setFrameShape(QFrame.Shape.VLine)
        self.line_76.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_295 = QLabel(self.frame_40)
        self.label_295.setObjectName(u"label_295")
        self.label_295.setGeometry(QRect(377, 99, 175, 44))
        self.label_295.setFont(font6)
        self.label_295.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_77 = QFrame(self.frame_40)
        self.line_77.setObjectName(u"line_77")
        self.line_77.setGeometry(QRect(316, 185, 274, 16))
        self.line_77.setFrameShape(QFrame.Shape.HLine)
        self.line_77.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_296 = QLabel(self.frame_40)
        self.label_296.setObjectName(u"label_296")
        self.label_296.setGeometry(QRect(377, 194, 120, 44))
        self.label_296.setFont(font6)
        self.label_296.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_297 = QLabel(self.frame_40)
        self.label_297.setObjectName(u"label_297")
        self.label_297.setGeometry(QRect(377, 291, 152, 66))
        self.label_297.setFont(font6)
        self.label_297.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_298 = QLabel(self.frame_40)
        self.label_298.setObjectName(u"label_298")
        self.label_298.setGeometry(QRect(10, 72, 501, 18))
        self.label_298.setFont(font7)
        self.label_298.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_78 = QFrame(self.frame_40)
        self.line_78.setObjectName(u"line_78")
        self.line_78.setGeometry(QRect(316, 279, 274, 16))
        self.line_78.setFrameShape(QFrame.Shape.HLine)
        self.line_78.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.frame_40, 0, 1, 1, 1)

        self.frame_45 = QFrame(self.frame_7)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFont(font3)
        self.frame_45.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_45.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Shadow.Raised)
        self.label_343 = QLabel(self.frame_45)
        self.label_343.setObjectName(u"label_343")
        self.label_343.setGeometry(QRect(13, 10, 291, 33))
        self.label_343.setFont(font9)
        self.label_343.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_344 = QLabel(self.frame_45)
        self.label_344.setObjectName(u"label_344")
        self.label_344.setGeometry(QRect(16, 49, 16, 16))
        self.label_344.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_345 = QLabel(self.frame_45)
        self.label_345.setObjectName(u"label_345")
        self.label_345.setGeometry(QRect(35, 49, 71, 16))
        self.label_345.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_34 = QPushButton(self.frame_45)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_34.setStyleSheet(u"QPushButton\n"
"{color:white;\n"
"	background-color: rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_346 = QLabel(self.frame_45)
        self.label_346.setObjectName(u"label_346")
        self.label_346.setGeometry(QRect(312, 10, 161, 31))
        self.label_346.setFont(font8)
        self.label_346.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_347 = QLabel(self.frame_45)
        self.label_347.setObjectName(u"label_347")
        self.label_347.setGeometry(QRect(477, 17, 81, 20))
        self.label_347.setFont(font2)
        self.label_347.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_348 = QLabel(self.frame_45)
        self.label_348.setObjectName(u"label_348")
        self.label_348.setGeometry(QRect(354, 44, 151, 20))
        self.label_348.setFont(font2)
        self.label_348.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_349 = QLabel(self.frame_45)
        self.label_349.setObjectName(u"label_349")
        self.label_349.setGeometry(QRect(10, 99, 291, 269))
        self.label_349.setStyleSheet(u"border-radius:5px;")
        self.label_349.setPixmap(QPixmap(u"PropImages/shubharambh_clara-kiwale-pune-shubharambh_landmarks.jpg"))
        self.label_349.setScaledContents(True)
        self.line_91 = QFrame(self.frame_45)
        self.line_91.setObjectName(u"line_91")
        self.line_91.setGeometry(QRect(307, 99, 16, 269))
        self.line_91.setFrameShape(QFrame.Shape.VLine)
        self.line_91.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_350 = QLabel(self.frame_45)
        self.label_350.setObjectName(u"label_350")
        self.label_350.setGeometry(QRect(377, 99, 201, 44))
        self.label_350.setFont(font6)
        self.label_350.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_92 = QFrame(self.frame_45)
        self.line_92.setObjectName(u"line_92")
        self.line_92.setGeometry(QRect(316, 185, 274, 16))
        self.line_92.setFrameShape(QFrame.Shape.HLine)
        self.line_92.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_351 = QLabel(self.frame_45)
        self.label_351.setObjectName(u"label_351")
        self.label_351.setGeometry(QRect(377, 194, 120, 44))
        self.label_351.setFont(font6)
        self.label_351.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_352 = QLabel(self.frame_45)
        self.label_352.setObjectName(u"label_352")
        self.label_352.setGeometry(QRect(377, 290, 152, 66))
        self.label_352.setFont(font6)
        self.label_352.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_353 = QLabel(self.frame_45)
        self.label_353.setObjectName(u"label_353")
        self.label_353.setGeometry(QRect(10, 75, 491, 18))
        self.label_353.setFont(font7)
        self.label_353.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_93 = QFrame(self.frame_45)
        self.line_93.setObjectName(u"line_93")
        self.line_93.setGeometry(QRect(316, 279, 274, 16))
        self.line_93.setFrameShape(QFrame.Shape.HLine)
        self.line_93.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.frame_45, 3, 0, 1, 1)


        self.horizontalLayout_14.addLayout(self.gridLayout_4)


        self.verticalLayout_20.addWidget(self.frame_7)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_3.addWidget(self.scrollArea_7)


        self.verticalLayout_2.addWidget(self.widget)

        self.stackedWidget_3.addWidget(self.meassagespage)
        self.notificationspage = QWidget()
        self.notificationspage.setObjectName(u"notificationspage")
        self.verticalLayout_7 = QVBoxLayout(self.notificationspage)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.notificationspage)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_9 = QVBoxLayout(self.widget_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.widget_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(7, 94, 84);\n"
" }")
        self.scrollArea_2.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1350, 1350))
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(1350, 1350))
        self.scrollAreaWidgetContents_2.setMaximumSize(QSize(1350, 1350))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 3000))
        self.frame_2.setStyleSheet(u"")
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 20, 1331, 251))
        self.label_8.setPixmap(QPixmap(u"../../Shivam/Downloads/Get In Touch With Us (1).png"))
        self.label_8.setScaledContents(True)
        self.plainTextEdit_2 = QPlainTextEdit(self.frame_2)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(725, 371, 471, 371))
        font10 = QFont()
        font10.setPointSize(18)
        self.plainTextEdit_2.setFont(font10)
        self.plainTextEdit_2.setStyleSheet(u"border:2px solid rgb(7, 94, 84);\n"
"border-bottom-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"color:rgb(109, 115, 116);\n"
"placeholder {\n"
"  color:white;\n"
"  font-sixze:10px;\n"
"}")
        self.loginbutton_2 = QPushButton(self.frame_2)
        self.loginbutton_2.setObjectName(u"loginbutton_2")
        self.loginbutton_2.setGeometry(QRect(860, 760, 200, 30))
        self.loginbutton_2.setFont(font7)
        self.loginbutton_2.setStyleSheet(u"QPushButton\n"
"{\n"
"color:white;\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:15px;\n"
"border:none;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.loginbutton_2.setCheckable(True)
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(725, 331, 471, 31))
        self.lineEdit.setStyleSheet(u"border:2px solid rgb(7, 94, 84);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"color:white;\n"
"")
        self.plainTextEdit = QPlainTextEdit(self.frame_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(155, 331, 471, 411))
        self.plainTextEdit.setFont(font10)
        self.plainTextEdit.setStyleSheet(u"border:2px solid rgb(7, 94, 84);\n"
"border-radius:20px;\n"
"color:rgb(184, 184, 184);\n"
"placeholder {\n"
"  font-sixze:10px;\n"
"}")
        self.loginbutton = QPushButton(self.frame_2)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setGeometry(QRect(290, 760, 200, 30))
        self.loginbutton.setFont(font7)
        self.loginbutton.setStyleSheet(u"QPushButton\n"
"{\n"
"color:white;\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:15px;\n"
"border:none;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.loginbutton.setCheckable(True)
        self.label_57 = QLabel(self.frame_2)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(470, 830, 400, 400))
        self.label_110 = QLabel(self.frame_2)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setGeometry(QRect(60, 827, 1241, 21))
        font11 = QFont()
        font11.setPointSize(17)
        font11.setBold(True)
        self.label_110.setFont(font11)
        self.label_110.setStyleSheet(u"border:none;\n"
"color:rgb(165, 165, 165);")
        self.layoutWidget3 = QWidget(self.frame_2)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(60, 890, 1242, 402))
        self.horizontalLayout_15 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_15.setSpacing(20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.widget_15 = QWidget(self.layoutWidget3)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(400, 400))
        self.widget_15.setMaximumSize(QSize(400, 400))
        self.widget_15.setStyleSheet(u"border:1px solid rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"background-color: rgb(18, 140, 113);\n"
"")
        self.label_2 = QLabel(self.widget_15)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 361, 191))
        self.label_2.setPixmap(QPixmap(u"PropImages/Thane/Thane-AsharMerac/Thane-2.jpg"))
        self.label_2.setScaledContents(True)
        self.label_58 = QLabel(self.widget_15)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(50, 224, 301, 121))
        self.label_58.setStyleSheet(u"border:none;")
        self.label_59 = QLabel(self.widget_15)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(122, 361, 151, 21))
        self.label_59.setFont(font11)
        self.label_59.setStyleSheet(u"border:none;\n"
"color:rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.layoutWidget3)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(400, 400))
        self.widget_16.setMaximumSize(QSize(400, 400))
        self.widget_16.setStyleSheet(u"border:1px solid rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"background-color: rgb(18, 140, 113);\n"
"")
        self.label_60 = QLabel(self.widget_16)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(20, 20, 361, 191))
        self.label_60.setPixmap(QPixmap(u"PropImages/Mumbai/Mumbai-Ghatkopar.Rajshree/Mumbai-1.5.jpg"))
        self.label_60.setScaledContents(True)
        self.label_61 = QLabel(self.widget_16)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(60, 224, 271, 121))
        self.label_61.setStyleSheet(u"border:none;")
        self.label_106 = QLabel(self.widget_16)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setGeometry(QRect(47, 360, 301, 21))
        self.label_106.setFont(font11)
        self.label_106.setStyleSheet(u"border:none;\n"
"color:rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.layoutWidget3)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(400, 400))
        self.widget_17.setMaximumSize(QSize(400, 400))
        self.widget_17.setStyleSheet(u"border:1px solid rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"background-color: rgb(18, 140, 113);\n"
"")
        self.label_107 = QLabel(self.widget_17)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setGeometry(QRect(20, 20, 361, 191))
        self.label_107.setPixmap(QPixmap(u"PropImages/Mumbai/Mumbai-Ghatkopar.Rajshree/Mumbai-1.jpg"))
        self.label_107.setScaledContents(True)
        self.label_108 = QLabel(self.widget_17)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setGeometry(QRect(60, 224, 271, 121))
        self.label_108.setStyleSheet(u"border:none;")
        self.label_109 = QLabel(self.widget_17)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setGeometry(QRect(90, 361, 211, 21))
        self.label_109.setFont(font11)
        self.label_109.setStyleSheet(u"border:none;\n"
"color:rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.widget_17)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_9.addWidget(self.scrollArea_2)


        self.verticalLayout_7.addWidget(self.widget_2)

        self.stackedWidget_3.addWidget(self.notificationspage)
        self.settingpage = QWidget()
        self.settingpage.setObjectName(u"settingpage")
        self.horizontalLayout_18 = QHBoxLayout(self.settingpage)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.widget_18 = QWidget(self.settingpage)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(1300, 0))
        self.verticalLayout_41 = QVBoxLayout(self.widget_18)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_15 = QScrollArea(self.widget_18)
        self.scrollArea_15.setObjectName(u"scrollArea_15")
        self.scrollArea_15.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(7, 94, 84);\n"
" }")
        self.scrollArea_15.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_15.setWidgetResizable(True)
        self.scrollAreaWidgetContents_15 = QWidget()
        self.scrollAreaWidgetContents_15.setObjectName(u"scrollAreaWidgetContents_15")
        self.scrollAreaWidgetContents_15.setGeometry(QRect(0, 0, 1350, 1500))
        self.scrollAreaWidgetContents_15.setMinimumSize(QSize(0, 1500))
        self.scrollAreaWidgetContents_15.setMaximumSize(QSize(16777215, 1500))
        self.verticalLayout_42 = QVBoxLayout(self.scrollAreaWidgetContents_15)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.scrollAreaWidgetContents_15)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(1350, 2000))
        self.frame_23.setMaximumSize(QSize(1350, 2000))
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.label_111 = QLabel(self.frame_23)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setGeometry(QRect(20, 20, 1331, 251))
        self.label_111.setPixmap(QPixmap(u"../../Shivam/Downloads/Get In Touch With Us (2).png"))
        self.label_111.setScaledContents(True)
        self.textEdit = QTextEdit(self.frame_23)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(40, 300, 1251, 681))
        self.textEdit.setStyleSheet(u"border:none;")
        self.label_112 = QLabel(self.frame_23)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setGeometry(QRect(-20, 990, 1571, 51))
        self.label_112.setFont(font10)
        self.label_112.setStyleSheet(u"color:white;")
        self.layoutWidget4 = QWidget(self.frame_23)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(24, 1070, 1311, 351))
        self.horizontalLayout_16 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_16.setSpacing(20)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_19 = QWidget(self.layoutWidget4)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setFont(font2)
        self.widget_19.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.label_113 = QLabel(self.widget_19)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setGeometry(QRect(30, 233, 251, 41))
        font12 = QFont()
        font12.setPointSize(24)
        font12.setBold(True)
        self.label_113.setFont(font12)
        self.textEdit_2 = QTextEdit(self.widget_19)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(40, 277, 231, 61))
        self.label_114 = QLabel(self.widget_19)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setGeometry(QRect(40, 0, 231, 231))
        self.label_114.setPixmap(QPixmap(u"../../Shivam/Downloads/Talk to us (1).png"))
        self.label_114.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.widget_19)

        self.widget_20 = QWidget(self.layoutWidget4)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.label_119 = QLabel(self.widget_20)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setGeometry(QRect(60, 233, 201, 41))
        self.label_119.setFont(font12)
        self.textEdit_5 = QTextEdit(self.widget_20)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(40, 274, 231, 61))
        self.label_120 = QLabel(self.widget_20)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setGeometry(QRect(50, 7, 211, 201))
        self.label_120.setPixmap(QPixmap(u"../../Shivam/Downloads/Talk to us (3).png"))
        self.label_120.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.widget_20)

        self.widget_21 = QWidget(self.layoutWidget4)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.label_121 = QLabel(self.widget_21)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setGeometry(QRect(20, 230, 271, 41))
        font13 = QFont()
        font13.setPointSize(20)
        font13.setBold(True)
        self.label_121.setFont(font13)
        self.textEdit_6 = QTextEdit(self.widget_21)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(40, 272, 231, 61))
        self.label_122 = QLabel(self.widget_21)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setGeometry(QRect(50, 10, 211, 201))
        self.label_122.setPixmap(QPixmap(u"../../Shivam/Downloads/Talk to us (4).png"))
        self.label_122.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.widget_21)

        self.widget_22 = QWidget(self.layoutWidget4)
        self.widget_22.setObjectName(u"widget_22")
        font14 = QFont()
        font14.setPointSize(9)
        self.widget_22.setFont(font14)
        self.widget_22.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.label_123 = QLabel(self.widget_22)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setGeometry(QRect(80, 220, 161, 31))
        self.label_123.setFont(font11)
        self.textEdit_7 = QTextEdit(self.widget_22)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setGeometry(QRect(50, 285, 231, 51))
        self.label_124 = QLabel(self.widget_22)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setGeometry(QRect(50, 10, 211, 201))
        self.label_124.setPixmap(QPixmap(u"../../Shivam/Downloads/Talk to us (5).png"))
        self.label_124.setScaledContents(True)
        self.label_125 = QLabel(self.widget_22)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setGeometry(QRect(80, 250, 161, 31))
        self.label_125.setFont(font11)

        self.horizontalLayout_16.addWidget(self.widget_22)


        self.verticalLayout_42.addWidget(self.frame_23)

        self.scrollArea_15.setWidget(self.scrollAreaWidgetContents_15)

        self.verticalLayout_41.addWidget(self.scrollArea_15)


        self.horizontalLayout_18.addWidget(self.widget_18)

        self.stackedWidget_3.addWidget(self.settingpage)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_10 = QVBoxLayout(self.page_9)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_14 = QScrollArea(self.page_9)
        self.scrollArea_14.setObjectName(u"scrollArea_14")
        self.scrollArea_14.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(7, 94, 84);\n"
" }")
        self.scrollArea_14.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_14.setWidgetResizable(True)
        self.scrollAreaWidgetContents_14 = QWidget()
        self.scrollAreaWidgetContents_14.setObjectName(u"scrollAreaWidgetContents_14")
        self.scrollAreaWidgetContents_14.setGeometry(QRect(0, 0, 98, 1800))
        self.scrollAreaWidgetContents_14.setMinimumSize(QSize(0, 1800))
        self.scrollAreaWidgetContents_14.setMaximumSize(QSize(16777215, 1800))
        self.verticalLayout_38 = QVBoxLayout(self.scrollAreaWidgetContents_14)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.scrollAreaWidgetContents_14)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 2000))
        self.frame_22.setStyleSheet(u"")
        self.horizontalLayout_17 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.frame_22)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(0, 2000))
        self.frame_47.setStyleSheet(u"")
        self.label_115 = QLabel(self.frame_47)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setGeometry(QRect(20, 20, 1321, 281))
        self.label_115.setPixmap(QPixmap(u"../../Shivam/Downloads/About Us (3).png"))
        self.label_115.setScaledContents(True)
        self.textEdit_3 = QTextEdit(self.frame_47)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(250, 380, 841, 91))
        self.textEdit_3.setStyleSheet(u"border:none;")
        self.loginbutton_3 = QPushButton(self.frame_47)
        self.loginbutton_3.setObjectName(u"loginbutton_3")
        self.loginbutton_3.setGeometry(QRect(699, 225, 170, 31))
        self.loginbutton_3.setFont(font7)
        self.loginbutton_3.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(115, 237, 240, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:10px;\n"
"color:rgb(7, 94, 84);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(201, 239, 240);\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(115, 237, 240, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color:rgb(7, 94, 84);\n"
"}0")
        self.loginbutton_3.setCheckable(True)
        self.label_116 = QLabel(self.frame_47)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setGeometry(QRect(20, 560, 1321, 281))
        self.label_116.setPixmap(QPixmap(u"../../Shivam/Downloads/About Us (2).png"))
        self.label_116.setScaledContents(True)
        self.loginbutton_4 = QPushButton(self.frame_47)
        self.loginbutton_4.setObjectName(u"loginbutton_4")
        self.loginbutton_4.setGeometry(QRect(107, 778, 170, 31))
        self.loginbutton_4.setFont(font7)
        self.loginbutton_4.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(115, 237, 240, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:10px;\n"
"color:rgb(7, 94, 84);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(201, 239, 240);\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(115, 237, 240, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color:rgb(7, 94, 84);\n"
"}0")
        self.loginbutton_4.setCheckable(True)
        self.toolBox_2 = QToolBox(self.frame_47)
        self.toolBox_2.setObjectName(u"toolBox_2")
        self.toolBox_2.setGeometry(QRect(350, 990, 701, 411))
        self.toolBox_2.setFont(font2)
        self.toolBox_2.setStyleSheet(u"QToolBox:tab{\n"
"	background-color:rgb(7, 94, 84);\n"
"	color:rgb(255, 255, 255);\n"
"padding-left:10px;\n"
"}")
        self.toolBox_2.setLineWidth(1)
        self.page_21 = QWidget()
        self.page_21.setObjectName(u"page_21")
        self.page_21.setGeometry(QRect(0, 0, 100, 30))
        self.plainTextEdit_3 = QPlainTextEdit(self.page_21)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(10, 0, 691, 251))
        self.plainTextEdit_3.setFont(font2)
        self.plainTextEdit_3.setStyleSheet(u"color:white;")
        self.plainTextEdit_3.setReadOnly(True)
        self.toolBox_2.addItem(self.page_21, u"I had submitted my listing, but it has been rejected. Why?                                                                      +")
        self.page_23 = QWidget()
        self.page_23.setObjectName(u"page_23")
        self.page_23.setGeometry(QRect(0, 0, 100, 30))
        self.plainTextEdit_4 = QPlainTextEdit(self.page_23)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setGeometry(QRect(10, 0, 691, 251))
        self.plainTextEdit_4.setFont(font2)
        self.plainTextEdit_4.setStyleSheet(u"color:white;")
        self.plainTextEdit_4.setReadOnly(True)
        self.toolBox_2.addItem(self.page_23, u"How will I get the reward money?                                                                                                             +")
        self.page_24 = QWidget()
        self.page_24.setObjectName(u"page_24")
        self.page_24.setGeometry(QRect(0, 0, 100, 30))
        self.plainTextEdit_5 = QPlainTextEdit(self.page_24)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setGeometry(QRect(10, 0, 691, 251))
        self.plainTextEdit_5.setFont(font2)
        self.plainTextEdit_5.setStyleSheet(u"color:white")
        self.plainTextEdit_5.setReadOnly(True)
        self.toolBox_2.addItem(self.page_24, u"Can I get the reward directly in my account?                                                                                            +")
        self.page_22 = QWidget()
        self.page_22.setObjectName(u"page_22")
        self.page_22.setGeometry(QRect(0, 0, 100, 30))
        self.plainTextEdit_6 = QPlainTextEdit(self.page_22)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setGeometry(QRect(10, 0, 691, 241))
        self.plainTextEdit_6.setFont(font2)
        self.plainTextEdit_6.setStyleSheet(u"color:white;")
        self.plainTextEdit_6.setReadOnly(True)
        self.toolBox_2.addItem(self.page_22, u"I have submitted my listing, but have not received the reward?                                                              +")
        self.label_117 = QLabel(self.frame_47)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setGeometry(QRect(360, 860, 701, 101))
        font15 = QFont()
        font15.setPointSize(25)
        self.label_117.setFont(font15)
        self.label_117.setStyleSheet(u"color:rgb(149, 149, 149);")
        self.layoutWidget5 = QWidget(self.frame_47)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(20, 1460, 1311, 251))
        self.horizontalLayout_19 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_19.setSpacing(30)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_23 = QWidget(self.layoutWidget5)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setFont(font14)
        self.widget_23.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.label_126 = QLabel(self.widget_23)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setGeometry(QRect(121, 38, 111, 31))
        self.label_126.setFont(font11)
        self.textEdit_8 = QTextEdit(self.widget_23)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setGeometry(QRect(62, 99, 491, 101))
        self.label_118 = QLabel(self.widget_23)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setGeometry(QRect(60, 40, 61, 51))
        self.label_118.setPixmap(QPixmap(u"../../Shivam/Downloads/kisspng-computer-icons-user-profile-avatar-job-icon-5b521c56afedc0.0537187115321078627206.png"))
        self.label_118.setScaledContents(True)
        self.layoutWidget6 = QWidget(self.widget_23)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(128, 68, 101, 17))
        self.horizontalLayout_20 = QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_20.setSpacing(2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_133 = QLabel(self.layoutWidget6)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setMinimumSize(QSize(15, 15))
        self.label_133.setMaximumSize(QSize(15, 15))
        self.label_133.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_133.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.label_133)

        self.label_138 = QLabel(self.layoutWidget6)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setMinimumSize(QSize(15, 15))
        self.label_138.setMaximumSize(QSize(15, 15))
        self.label_138.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_138.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.label_138)

        self.label_139 = QLabel(self.layoutWidget6)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setMinimumSize(QSize(15, 15))
        self.label_139.setMaximumSize(QSize(15, 15))
        self.label_139.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_139.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.label_139)

        self.label_140 = QLabel(self.layoutWidget6)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setMinimumSize(QSize(15, 15))
        self.label_140.setMaximumSize(QSize(15, 15))
        self.label_140.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_140.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.label_140)

        self.label_141 = QLabel(self.layoutWidget6)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setMinimumSize(QSize(15, 15))
        self.label_141.setMaximumSize(QSize(15, 15))
        self.label_141.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_141.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.label_141)


        self.horizontalLayout_19.addWidget(self.widget_23)

        self.widget_24 = QWidget(self.layoutWidget5)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setFont(font14)
        self.widget_24.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.label_127 = QLabel(self.widget_24)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setGeometry(QRect(117, 37, 171, 31))
        self.label_127.setFont(font11)
        self.textEdit_9 = QTextEdit(self.widget_24)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setGeometry(QRect(54, 99, 491, 101))
        self.label_128 = QLabel(self.widget_24)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setGeometry(QRect(50, 40, 61, 51))
        self.label_128.setPixmap(QPixmap(u"../../Shivam/Downloads/kisspng-computer-icons-user-profile-avatar-job-icon-5b521c56afedc0.0537187115321078627206.png"))
        self.label_128.setScaledContents(True)
        self.layoutWidget_4 = QWidget(self.widget_24)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(121, 68, 101, 17))
        self.horizontalLayout_21 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_21.setSpacing(2)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_134 = QLabel(self.layoutWidget_4)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setMinimumSize(QSize(15, 15))
        self.label_134.setMaximumSize(QSize(15, 15))
        self.label_134.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_134.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.label_134)

        self.label_142 = QLabel(self.layoutWidget_4)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setMinimumSize(QSize(15, 15))
        self.label_142.setMaximumSize(QSize(15, 15))
        self.label_142.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_142.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.label_142)

        self.label_143 = QLabel(self.layoutWidget_4)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setMinimumSize(QSize(15, 15))
        self.label_143.setMaximumSize(QSize(15, 15))
        self.label_143.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_143.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.label_143)

        self.label_144 = QLabel(self.layoutWidget_4)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setMinimumSize(QSize(15, 15))
        self.label_144.setMaximumSize(QSize(15, 15))
        self.label_144.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_144.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.label_144)

        self.label_145 = QLabel(self.layoutWidget_4)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setMinimumSize(QSize(15, 15))
        self.label_145.setMaximumSize(QSize(15, 15))
        self.label_145.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_145.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.label_145)


        self.horizontalLayout_19.addWidget(self.widget_24)


        self.horizontalLayout_17.addWidget(self.frame_47)


        self.verticalLayout_38.addWidget(self.frame_22)

        self.scrollArea_14.setWidget(self.scrollAreaWidgetContents_14)

        self.verticalLayout_10.addWidget(self.scrollArea_14)

        self.stackedWidget_3.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.horizontalLayout_5 = QHBoxLayout(self.page_10)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.page_10)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_27 = QVBoxLayout(self.widget_10)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_9 = QScrollArea(self.widget_10)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        self.scrollArea_9.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(7, 94, 84);\n"
" }")
        self.scrollArea_9.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 98, 1650))
        self.scrollAreaWidgetContents_9.setMinimumSize(QSize(0, 1650))
        self.scrollAreaWidgetContents_9.setMaximumSize(QSize(16777215, 1650))
        self.verticalLayout_28 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 3000))
        self.frame_17.setStyleSheet(u"")
        self.label_130 = QLabel(self.frame_17)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setGeometry(QRect(37, 110, 151, 16))
        self.label_130.setStyleSheet(u"color:rgb(18, 140, 126);")
        self.frame_24 = QFrame(self.frame_17)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(34, 20, 831, 41))
        self.frame_24.setStyleSheet(u"background-color: rgb(18, 140, 126);")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.label_131 = QLabel(self.frame_24)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setGeometry(QRect(48, 10, 191, 21))
        self.label_131.setFont(font2)
        self.label_131.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_132 = QLabel(self.frame_24)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setGeometry(QRect(240, 10, 86, 21))
        self.label_132.setFont(font2)
        self.label_132.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_135 = QLabel(self.frame_24)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setGeometry(QRect(21, 10, 21, 21))
        self.label_135.setPixmap(QPixmap(u"PropImages/Coffe-removebg-preview.png"))
        self.label_135.setScaledContents(True)
        self.pushButton_12 = QPushButton(self.frame_24)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(609, 8, 100, 25))
        self.pushButton_12.setFont(font7)
        self.pushButton_12.setStyleSheet(u"background-color: rgb(37, 211, 102);\n"
"color:rgb(26, 26, 26);\n"
"border-radius:5px;")
        self.pushButton_13 = QPushButton(self.frame_24)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(720, 8, 100, 25))
        self.pushButton_13.setFont(font7)
        self.pushButton_13.setStyleSheet(u"background-color: rgb(37, 211, 102);\n"
"color:rgb(26, 26, 26);\n"
"border-radius:5px;")
        self.pushButton_14 = QPushButton(self.frame_24)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(480, 8, 120, 25))
        self.pushButton_14.setFont(font7)
        self.pushButton_14.setStyleSheet(u"background-color: rgb(37, 211, 102);\n"
"color:rgb(26, 26, 26);\n"
"border-radius:5px;")
        icon22 = QIcon()
        icon22.addFile(u"PropImages/Coffe-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon22)
        self.pushButton_14.setIconSize(QSize(20, 20))
        self.label_136 = QLabel(self.frame_17)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setGeometry(QRect(761, 107, 101, 16))
        self.label_136.setStyleSheet(u"color:rgb(18, 140, 126);")
        self.label_137 = QLabel(self.frame_17)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setGeometry(QRect(37, 70, 111, 31))
        self.label_137.setFont(font6)
        self.label_137.setStyleSheet(u"color:rgb(18, 140, 126);")
        self.label_146 = QLabel(self.frame_17)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setGeometry(QRect(782, 78, 81, 16))
        self.label_146.setStyleSheet(u"color:rgb(18, 140, 126);")
        self.pushButton_15 = QPushButton(self.frame_17)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(741, 77, 41, 21))
        self.pushButton_15.setFont(font14)
        self.pushButton_15.setStyleSheet(u"border:none;")
        icon23 = QIcon()
        icon23.addFile(u"PropImages/BBShivam/BBShivam9-7-24work/Scracth.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon23)
        self.pushButton_15.setIconSize(QSize(25, 25))
        self.line_13 = QFrame(self.frame_17)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setGeometry(QRect(731, 62, 20, 71))
        self.line_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_13.setFrameShape(QFrame.Shape.VLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)
        self.pushButton_16 = QPushButton(self.frame_17)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(174, 100, 91, 31))
        self.pushButton_16.setFont(font7)
        self.pushButton_16.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"color:rgb(35, 47, 49);\n"
"border-radius:10px;")
        self.pushButton_16.setIcon(icon22)
        self.pushButton_16.setIconSize(QSize(25, 25))
        self.layoutWidget7 = QWidget(self.frame_17)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(20, 160, 872, 452))
        self.gridLayout_2 = QGridLayout(self.layoutWidget7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(30)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.layoutWidget7)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(280, 210))
        self.frame_25.setMaximumSize(QSize(280, 210))
        self.frame_25.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(0, -3, 331, 171))
        self.frame_26.setStyleSheet(u"")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.label_52 = QLabel(self.frame_26)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(-70, -35, 411, 231))
        self.label_52.setPixmap(QPixmap(u"PropImages/BBShivam/BBShivam9-7-24work/Ama.png"))
        self.label_52.setScaledContents(True)
        self.layoutWidget8 = QWidget(self.frame_25)
        self.layoutWidget8.setObjectName(u"layoutWidget8")
        self.layoutWidget8.setGeometry(QRect(11, 168, 171, 40))
        self.verticalLayout_40 = QVBoxLayout(self.layoutWidget8)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_147 = QLabel(self.layoutWidget8)
        self.label_147.setObjectName(u"label_147")
        font16 = QFont()
        font16.setPointSize(12)
        font16.setBold(True)
        self.label_147.setFont(font16)
        self.label_147.setStyleSheet(u"color: rgb(7, 94, 84);")

        self.verticalLayout_40.addWidget(self.label_147)

        self.label_148 = QLabel(self.layoutWidget8)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_40.addWidget(self.label_148)

        self.amazonbutton = QPushButton(self.frame_25)
        self.amazonbutton.setObjectName(u"amazonbutton")
        self.amazonbutton.setGeometry(QRect(-2, 0, 281, 211))
        self.amazonbutton.setStyleSheet(u"border:none;\n"
"background-color:none;")
        self.amazonbutton.setCheckable(True)
        self.amazonbutton.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.frame_25, 0, 0, 1, 1)

        self.frame_27 = QFrame(self.layoutWidget7)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(280, 210))
        self.frame_27.setMaximumSize(QSize(280, 210))
        self.frame_27.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(0, -3, 331, 171))
        self.frame_28.setStyleSheet(u"")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.label_149 = QLabel(self.frame_28)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setGeometry(QRect(-10, -30, 301, 201))
        self.label_149.setPixmap(QPixmap(u"PropImages/BBShivam/BBShivam9-7-24work/Dominos.png"))
        self.label_149.setScaledContents(True)
        self.layoutWidget_5 = QWidget(self.frame_27)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(11, 168, 171, 40))
        self.verticalLayout_43 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_150 = QLabel(self.layoutWidget_5)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setFont(font16)
        self.label_150.setStyleSheet(u"color: rgb(7, 94, 84);")

        self.verticalLayout_43.addWidget(self.label_150)

        self.label_151 = QLabel(self.layoutWidget_5)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_43.addWidget(self.label_151)

        self.Dominosbutton = QPushButton(self.frame_27)
        self.Dominosbutton.setObjectName(u"Dominosbutton")
        self.Dominosbutton.setGeometry(QRect(-1, 0, 281, 211))
        self.Dominosbutton.setStyleSheet(u"border:none;\n"
"background-color:none;")
        self.Dominosbutton.setCheckable(True)
        self.Dominosbutton.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.frame_27, 0, 1, 1, 1)

        self.frame_29 = QFrame(self.layoutWidget7)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(280, 210))
        self.frame_29.setMaximumSize(QSize(280, 210))
        self.frame_29.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_48 = QFrame(self.frame_29)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setGeometry(QRect(0, -3, 331, 171))
        self.frame_48.setStyleSheet(u"")
        self.frame_48.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Shadow.Raised)
        self.label_152 = QLabel(self.frame_48)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setGeometry(QRect(-10, -10, 301, 181))
        self.label_152.setPixmap(QPixmap(u"PropImages/BBShivam/BBShivam9-7-24work/PizzaHut.png"))
        self.label_152.setScaledContents(True)
        self.layoutWidget_6 = QWidget(self.frame_29)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(11, 168, 171, 40))
        self.verticalLayout_44 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_153 = QLabel(self.layoutWidget_6)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setFont(font16)
        self.label_153.setStyleSheet(u"color: rgb(7, 94, 84);")

        self.verticalLayout_44.addWidget(self.label_153)

        self.label_154 = QLabel(self.layoutWidget_6)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_44.addWidget(self.label_154)

        self.PizzaHutbutton = QPushButton(self.frame_29)
        self.PizzaHutbutton.setObjectName(u"PizzaHutbutton")
        self.PizzaHutbutton.setGeometry(QRect(1, 0, 281, 211))
        self.PizzaHutbutton.setStyleSheet(u"border:none;\n"
"background-color:none;")
        self.PizzaHutbutton.setCheckable(True)
        self.PizzaHutbutton.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.frame_29, 0, 2, 1, 1)

        self.frame_49 = QFrame(self.layoutWidget7)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(280, 210))
        self.frame_49.setMaximumSize(QSize(280, 210))
        self.frame_49.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.frame_49.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_50 = QFrame(self.frame_49)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setGeometry(QRect(0, -3, 331, 171))
        self.frame_50.setStyleSheet(u"")
        self.frame_50.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Shadow.Raised)
        self.label_155 = QLabel(self.frame_50)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setGeometry(QRect(-16, -5, 315, 171))
        self.label_155.setPixmap(QPixmap(u"PropImages/BBShivam/BBShivam9-7-24work/flipkart.png"))
        self.label_155.setScaledContents(True)
        self.layoutWidget_7 = QWidget(self.frame_49)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(11, 168, 171, 40))
        self.verticalLayout_45 = QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_156 = QLabel(self.layoutWidget_7)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setFont(font16)
        self.label_156.setStyleSheet(u"color: rgb(7, 94, 84);")

        self.verticalLayout_45.addWidget(self.label_156)

        self.label_157 = QLabel(self.layoutWidget_7)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_45.addWidget(self.label_157)

        self.FlipkartButton = QPushButton(self.frame_49)
        self.FlipkartButton.setObjectName(u"FlipkartButton")
        self.FlipkartButton.setGeometry(QRect(0, 0, 281, 211))
        self.FlipkartButton.setStyleSheet(u"border:none;\n"
"background-color:none;")
        self.FlipkartButton.setCheckable(True)
        self.FlipkartButton.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.frame_49, 1, 0, 1, 1)

        self.frame_51 = QFrame(self.layoutWidget7)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(280, 210))
        self.frame_51.setMaximumSize(QSize(280, 210))
        self.frame_51.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.frame_51.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_52 = QFrame(self.frame_51)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setGeometry(QRect(0, -3, 331, 171))
        self.frame_52.setStyleSheet(u"")
        self.frame_52.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Shadow.Raised)
        self.label_158 = QLabel(self.frame_52)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setGeometry(QRect(-10, -5, 301, 171))
        self.label_158.setPixmap(QPixmap(u"PropImages/BBShivam/BBShivam9-7-24work/Myntra1.png"))
        self.label_158.setScaledContents(True)
        self.layoutWidget_8 = QWidget(self.frame_51)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(11, 168, 171, 40))
        self.verticalLayout_46 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_159 = QLabel(self.layoutWidget_8)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setFont(font16)
        self.label_159.setStyleSheet(u"color: rgb(7, 94, 84);")

        self.verticalLayout_46.addWidget(self.label_159)

        self.label_160 = QLabel(self.layoutWidget_8)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_46.addWidget(self.label_160)

        self.Myntrabutton = QPushButton(self.frame_51)
        self.Myntrabutton.setObjectName(u"Myntrabutton")
        self.Myntrabutton.setGeometry(QRect(0, 0, 281, 211))
        self.Myntrabutton.setStyleSheet(u"border:none;\n"
"background-color:none;")
        self.Myntrabutton.setCheckable(True)
        self.Myntrabutton.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.frame_51, 1, 1, 1, 1)

        self.frame_53 = QFrame(self.layoutWidget7)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(280, 210))
        self.frame_53.setMaximumSize(QSize(280, 210))
        self.frame_53.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.frame_53.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_54 = QFrame(self.frame_53)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setGeometry(QRect(0, -5, 331, 168))
        self.frame_54.setStyleSheet(u"")
        self.frame_54.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Shadow.Raised)
        self.label_161 = QLabel(self.frame_54)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setGeometry(QRect(-10, -4, 301, 181))
        self.label_161.setPixmap(QPixmap(u"PropImages/BBShivam/BBShivam9-7-24work/Zomato.jpg"))
        self.label_161.setScaledContents(True)
        self.layoutWidget_9 = QWidget(self.frame_53)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(11, 168, 171, 40))
        self.verticalLayout_47 = QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_162 = QLabel(self.layoutWidget_9)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setFont(font16)
        self.label_162.setStyleSheet(u"color: rgb(7, 94, 84);")

        self.verticalLayout_47.addWidget(self.label_162)

        self.label_163 = QLabel(self.layoutWidget_9)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_47.addWidget(self.label_163)

        self.zomatobutton = QPushButton(self.frame_53)
        self.zomatobutton.setObjectName(u"zomatobutton")
        self.zomatobutton.setGeometry(QRect(0, 0, 281, 211))
        self.zomatobutton.setStyleSheet(u"border:none;\n"
"background-color:none;")
        self.zomatobutton.setCheckable(True)
        self.zomatobutton.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.frame_53, 1, 2, 1, 1)

        self.label_164 = QLabel(self.frame_17)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setGeometry(QRect(275, 663, 361, 31))
        font17 = QFont()
        font17.setPointSize(15)
        self.label_164.setFont(font17)
        self.label_164.setStyleSheet(u"color:rgb(165, 165, 165);")
        self.frame_55 = QFrame(self.frame_17)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setGeometry(QRect(23, 750, 425, 400))
        self.frame_55.setMinimumSize(QSize(425, 400))
        self.frame_55.setMaximumSize(QSize(425, 400))
        self.frame_55.setStyleSheet(u"background-color: rgb(18, 140, 126);")
        self.frame_55.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Shadow.Raised)
        self.label_168 = QLabel(self.frame_55)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setGeometry(QRect(120, 160, 281, 291))
        self.label_168.setStyleSheet(u"border:none;")
        self.label_168.setPixmap(QPixmap(u"../../Shivam/Downloads/Times-When-You-Definitely-Need-a-Professional-Plumber-removebg-preview.png"))
        self.label_168.setScaledContents(True)
        self.label_166 = QLabel(self.frame_55)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setGeometry(QRect(30, 54, 291, 91))
        font18 = QFont()
        font18.setPointSize(25)
        font18.setBold(True)
        self.label_166.setFont(font18)
        self.label_166.setStyleSheet(u"color: rgb(7, 94, 84);")
        self.layoutWidget9 = QWidget(self.frame_55)
        self.layoutWidget9.setObjectName(u"layoutWidget9")
        self.layoutWidget9.setGeometry(QRect(30, 25, 121, 27))
        self.horizontalLayout_22 = QHBoxLayout(self.layoutWidget9)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_165 = QLabel(self.layoutWidget9)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setMinimumSize(QSize(25, 25))
        self.label_165.setMaximumSize(QSize(25, 25))
        self.label_165.setFont(font2)
        self.label_165.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_165.setPixmap(QPixmap(u"PropImages/Coffe-removebg-preview.png"))
        self.label_165.setScaledContents(True)

        self.horizontalLayout_22.addWidget(self.label_165)

        self.label_167 = QLabel(self.layoutWidget9)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setFont(font7)
        self.label_167.setStyleSheet(u"color:rgb(202, 202, 202);")

        self.horizontalLayout_22.addWidget(self.label_167)

        self.label_166.raise_()
        self.layoutWidget5.raise_()
        self.label_168.raise_()
        self.frame_56 = QFrame(self.frame_17)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setGeometry(QRect(463, 750, 425, 400))
        self.frame_56.setMinimumSize(QSize(425, 400))
        self.frame_56.setMaximumSize(QSize(425, 400))
        self.frame_56.setStyleSheet(u"background-color: rgb(18, 140, 126);")
        self.frame_56.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Shadow.Raised)
        self.label_169 = QLabel(self.frame_56)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setGeometry(QRect(10, 153, 511, 291))
        self.label_169.setStyleSheet(u"border:none;")
        self.label_169.setPixmap(QPixmap(u"../../Shivam/Downloads/carpentor-removebg-preview.png"))
        self.label_169.setScaledContents(True)
        self.label_170 = QLabel(self.frame_56)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setGeometry(QRect(30, 54, 291, 91))
        self.label_170.setFont(font18)
        self.label_170.setStyleSheet(u"color: rgb(7, 94, 84);")
        self.layoutWidget_10 = QWidget(self.frame_56)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.layoutWidget_10.setGeometry(QRect(30, 25, 121, 27))
        self.horizontalLayout_23 = QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_171 = QLabel(self.layoutWidget_10)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setMinimumSize(QSize(25, 25))
        self.label_171.setMaximumSize(QSize(25, 25))
        self.label_171.setFont(font2)
        self.label_171.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_171.setPixmap(QPixmap(u"PropImages/Coffe-removebg-preview.png"))
        self.label_171.setScaledContents(True)

        self.horizontalLayout_23.addWidget(self.label_171)

        self.label_172 = QLabel(self.layoutWidget_10)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setFont(font7)
        self.label_172.setStyleSheet(u"color:rgb(202, 202, 202);")

        self.horizontalLayout_23.addWidget(self.label_172)

        self.frame_57 = QFrame(self.frame_17)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setGeometry(QRect(463, 1167, 425, 400))
        self.frame_57.setMinimumSize(QSize(425, 400))
        self.frame_57.setMaximumSize(QSize(425, 400))
        self.frame_57.setStyleSheet(u"background-color: rgb(18, 140, 126);")
        self.frame_57.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Shadow.Raised)
        self.label_174 = QLabel(self.frame_57)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setGeometry(QRect(30, 54, 291, 91))
        self.label_174.setFont(font18)
        self.label_174.setStyleSheet(u"color: rgb(7, 94, 84);")
        self.layoutWidget_11 = QWidget(self.frame_57)
        self.layoutWidget_11.setObjectName(u"layoutWidget_11")
        self.layoutWidget_11.setGeometry(QRect(30, 25, 121, 27))
        self.horizontalLayout_24 = QHBoxLayout(self.layoutWidget_11)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_175 = QLabel(self.layoutWidget_11)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setMinimumSize(QSize(25, 25))
        self.label_175.setMaximumSize(QSize(25, 25))
        self.label_175.setFont(font2)
        self.label_175.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_175.setPixmap(QPixmap(u"PropImages/Coffe-removebg-preview.png"))
        self.label_175.setScaledContents(True)

        self.horizontalLayout_24.addWidget(self.label_175)

        self.label_176 = QLabel(self.layoutWidget_11)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setFont(font7)
        self.label_176.setStyleSheet(u"color:rgb(202, 202, 202);")

        self.horizontalLayout_24.addWidget(self.label_176)

        self.label_173 = QLabel(self.frame_57)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setGeometry(QRect(70, 150, 341, 271))
        self.label_173.setPixmap(QPixmap(u"../../Shivam/Downloads/ACServices-removebg-preview.png"))
        self.label_173.setScaledContents(True)
        self.frame_58 = QFrame(self.frame_17)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setGeometry(QRect(23, 1167, 425, 400))
        self.frame_58.setMinimumSize(QSize(425, 400))
        self.frame_58.setMaximumSize(QSize(425, 400))
        self.frame_58.setStyleSheet(u"background-color: rgb(18, 140, 126);")
        self.frame_58.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Shadow.Raised)
        self.label_178 = QLabel(self.frame_58)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setGeometry(QRect(30, 54, 281, 91))
        self.label_178.setFont(font18)
        self.label_178.setStyleSheet(u"color: rgb(7, 94, 84);")
        self.layoutWidget_12 = QWidget(self.frame_58)
        self.layoutWidget_12.setObjectName(u"layoutWidget_12")
        self.layoutWidget_12.setGeometry(QRect(30, 25, 121, 27))
        self.horizontalLayout_25 = QHBoxLayout(self.layoutWidget_12)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_179 = QLabel(self.layoutWidget_12)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setMinimumSize(QSize(25, 25))
        self.label_179.setMaximumSize(QSize(25, 25))
        self.label_179.setFont(font2)
        self.label_179.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_179.setPixmap(QPixmap(u"PropImages/Coffe-removebg-preview.png"))
        self.label_179.setScaledContents(True)

        self.horizontalLayout_25.addWidget(self.label_179)

        self.label_180 = QLabel(self.layoutWidget_12)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setFont(font7)
        self.label_180.setStyleSheet(u"color:rgb(202, 202, 202);")

        self.horizontalLayout_25.addWidget(self.label_180)

        self.label_177 = QLabel(self.frame_58)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setGeometry(QRect(70, 142, 311, 451))
        self.label_177.setPixmap(QPixmap(u"PropImages/pngtree-crouched-woman-painting-wall-renewal-png-image_10034990.png"))
        self.label_177.setScaledContents(True)

        self.verticalLayout_28.addWidget(self.frame_17)

        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_27.addWidget(self.scrollArea_9)


        self.horizontalLayout_5.addWidget(self.widget_10)

        self.stackedWidget_3.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.horizontalLayout_6 = QHBoxLayout(self.page_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.page_11)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_29 = QVBoxLayout(self.widget_11)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_10 = QScrollArea(self.widget_11)
        self.scrollArea_10.setObjectName(u"scrollArea_10")
        self.scrollArea_10.setMinimumSize(QSize(0, 500))
        self.scrollArea_10.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(7, 94, 84);\n"
" }")
        self.scrollArea_10.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 98, 700))
        self.scrollAreaWidgetContents_10.setMinimumSize(QSize(0, 700))
        self.scrollAreaWidgetContents_10.setMaximumSize(QSize(16777215, 700))
        self.verticalLayout_30 = QVBoxLayout(self.scrollAreaWidgetContents_10)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.scrollAreaWidgetContents_10)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 3000))
        self.frame_18.setStyleSheet(u"")
        self.widget_31 = QWidget(self.frame_18)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setGeometry(QRect(30, 20, 1321, 300))
        self.widget_31.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(18, 140, 126);")
        self.label_53 = QLabel(self.widget_31)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(610, 61, 641, 81))
        font19 = QFont()
        font19.setFamilies([u"Bell MT"])
        font19.setPointSize(50)
        self.label_53.setFont(font19)
        self.label_53.setStyleSheet(u"color:white;")
        self.label_181 = QLabel(self.widget_31)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setGeometry(QRect(90, -10, 431, 311))
        self.label_181.setPixmap(QPixmap(u"../../Shivam/Downloads/Coffe (7).png"))
        self.label_181.setScaledContents(True)
        self.label_182 = QLabel(self.widget_31)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setGeometry(QRect(530, 70, 61, 60))
        self.label_182.setPixmap(QPixmap(u"../../Shivam/Downloads/Coffe (9).png"))
        self.label_182.setScaledContents(True)
        self.label_183 = QLabel(self.widget_31)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setGeometry(QRect(620, 140, 531, 41))
        font20 = QFont()
        font20.setPointSize(14)
        self.label_183.setFont(font20)
        self.label_183.setStyleSheet(u"color: rgb(198, 198, 198);")

        self.verticalLayout_30.addWidget(self.frame_18)

        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)

        self.verticalLayout_29.addWidget(self.scrollArea_10)


        self.horizontalLayout_6.addWidget(self.widget_11)

        self.stackedWidget_3.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.horizontalLayout_8 = QHBoxLayout(self.page_12)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.page_12)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_31 = QVBoxLayout(self.widget_12)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_11 = QScrollArea(self.widget_12)
        self.scrollArea_11.setObjectName(u"scrollArea_11")
        self.scrollArea_11.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(7, 94, 84);\n"
" }")
        self.scrollArea_11.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 1346, 3000))
        font21 = QFont()
        font21.setFamilies([u"Segoe UI"])
        self.scrollAreaWidgetContents_11.setFont(font21)
        self.verticalLayout_32 = QVBoxLayout(self.scrollAreaWidgetContents_11)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.scrollAreaWidgetContents_11)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 3000))
        self.frame_19.setStyleSheet(u"")
        self.widget_35 = QWidget(self.frame_19)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setGeometry(QRect(30, 30, 1300, 300))
        self.widget_35.setStyleSheet(u"background-color: rgb(18, 140, 126);")
        self.label_54 = QLabel(self.widget_35)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(20, -140, 461, 451))
        self.label_54.setPixmap(QPixmap(u"../../Shivam/Downloads/Coffe (13).png"))
        self.label_54.setScaledContents(True)
        self.label_400 = QLabel(self.widget_35)
        self.label_400.setObjectName(u"label_400")
        self.label_400.setGeometry(QRect(540, 10, 741, 281))
        font22 = QFont()
        font22.setFamilies([u"Elephant"])
        font22.setPointSize(48)
        self.label_400.setFont(font22)
        self.label_400.setStyleSheet(u"color: rgb(226, 219, 249);")

        self.verticalLayout_32.addWidget(self.frame_19)

        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_11)

        self.verticalLayout_31.addWidget(self.scrollArea_11)


        self.horizontalLayout_8.addWidget(self.widget_12)

        self.stackedWidget_3.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.horizontalLayout_11 = QHBoxLayout(self.page_13)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.page_13)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_33 = QVBoxLayout(self.widget_13)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_12 = QScrollArea(self.widget_13)
        self.scrollArea_12.setObjectName(u"scrollArea_12")
        self.scrollArea_12.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(0, 170, 0);\n"
" }")
        self.scrollArea_12.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_12.setWidgetResizable(True)
        self.scrollAreaWidgetContents_12 = QWidget()
        self.scrollAreaWidgetContents_12.setObjectName(u"scrollAreaWidgetContents_12")
        self.scrollAreaWidgetContents_12.setGeometry(QRect(0, 0, 98, 3000))
        self.verticalLayout_34 = QVBoxLayout(self.scrollAreaWidgetContents_12)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.scrollAreaWidgetContents_12)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 3000))
        self.frame_20.setStyleSheet(u"")
        self.label_55 = QLabel(self.frame_20)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(470, 230, 49, 16))

        self.verticalLayout_34.addWidget(self.frame_20)

        self.scrollArea_12.setWidget(self.scrollAreaWidgetContents_12)

        self.verticalLayout_33.addWidget(self.scrollArea_12)


        self.horizontalLayout_11.addWidget(self.widget_13)

        self.stackedWidget_3.addWidget(self.page_13)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.horizontalLayout_12 = QHBoxLayout(self.page_14)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.page_14)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_35 = QVBoxLayout(self.widget_14)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_13 = QScrollArea(self.widget_14)
        self.scrollArea_13.setObjectName(u"scrollArea_13")
        self.scrollArea_13.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(0, 170, 0);\n"
" }")
        self.scrollArea_13.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_13.setWidgetResizable(True)
        self.scrollAreaWidgetContents_13 = QWidget()
        self.scrollAreaWidgetContents_13.setObjectName(u"scrollAreaWidgetContents_13")
        self.scrollAreaWidgetContents_13.setGeometry(QRect(0, 0, 98, 3000))
        self.verticalLayout_36 = QVBoxLayout(self.scrollAreaWidgetContents_13)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.scrollAreaWidgetContents_13)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 3000))
        self.frame_21.setStyleSheet(u"")
        self.label_56 = QLabel(self.frame_21)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(470, 230, 49, 16))

        self.verticalLayout_36.addWidget(self.frame_21)

        self.scrollArea_13.setWidget(self.scrollAreaWidgetContents_13)

        self.verticalLayout_35.addWidget(self.scrollArea_13)


        self.horizontalLayout_12.addWidget(self.widget_14)

        self.stackedWidget_3.addWidget(self.page_14)
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.stackedWidget_3.addWidget(self.page_15)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.stackedWidget_3.addWidget(self.page_16)
        self.page_17 = QWidget()
        self.page_17.setObjectName(u"page_17")
        self.stackedWidget_3.addWidget(self.page_17)
        self.page_18 = QWidget()
        self.page_18.setObjectName(u"page_18")
        self.stackedWidget_3.addWidget(self.page_18)
        self.page_19 = QWidget()
        self.page_19.setObjectName(u"page_19")
        self.stackedWidget_3.addWidget(self.page_19)
        self.page_20 = QWidget()
        self.page_20.setObjectName(u"page_20")
        self.stackedWidget_3.addWidget(self.page_20)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.horizontalLayout_2 = QHBoxLayout(self.page_6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.page_6)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_11 = QVBoxLayout(self.widget_4)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.widget_4)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(0, 170, 0);\n"
" }")
        self.scrollArea_3.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 98, 3000))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 3000))
        self.frame_14.setStyleSheet(u"")
        self.label_4 = QLabel(self.frame_14)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(470, 230, 49, 16))

        self.verticalLayout_12.addWidget(self.frame_14)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_11.addWidget(self.scrollArea_3)


        self.horizontalLayout_2.addWidget(self.widget_4)

        self.stackedWidget_3.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.horizontalLayout_3 = QHBoxLayout(self.page_7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.page_7)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_23 = QVBoxLayout(self.widget_8)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.widget_8)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(0, 170, 0);\n"
" }")
        self.scrollArea_4.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 98, 3000))
        self.verticalLayout_24 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 3000))
        self.frame_15.setStyleSheet(u"")
        self.label_7 = QLabel(self.frame_15)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(470, 230, 49, 16))

        self.verticalLayout_24.addWidget(self.frame_15)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_23.addWidget(self.scrollArea_4)


        self.horizontalLayout_3.addWidget(self.widget_8)

        self.stackedWidget_3.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.horizontalLayout_4 = QHBoxLayout(self.page_8)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.page_8)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_25 = QVBoxLayout(self.widget_9)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_8 = QScrollArea(self.widget_9)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(7, 94, 84);\n"
" }")
        self.scrollArea_8.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 98, 2800))
        self.scrollAreaWidgetContents_8.setMinimumSize(QSize(0, 2800))
        self.scrollAreaWidgetContents_8.setMaximumSize(QSize(16777215, 2800))
        self.verticalLayout_26 = QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.scrollAreaWidgetContents_8)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 3000))
        self.frame_16.setStyleSheet(u"color:white;")
        self.groupBox_Video = QGroupBox(self.frame_16)
        self.groupBox_Video.setObjectName(u"groupBox_Video")
        self.groupBox_Video.setGeometry(QRect(25, 25, 1300, 550))
        self.groupBox_Video.setStyleSheet(u"QGroupBox\n"
"{\n"
"	border:1px solid black;\n"
"}")
        self.widget_29 = QWidget(self.frame_16)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setGeometry(QRect(24, 640, 1300, 50))
        self.widget_29.setStyleSheet(u"background-color: rgb(7, 94, 84);")
        self.label_5 = QLabel(self.widget_29)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 10, 751, 31))
        font23 = QFont()
        font23.setFamilies([u"Lucida Bright"])
        font23.setPointSize(19)
        self.label_5.setFont(font23)
        self.label_5.setStyleSheet(u"color: rgb(198, 198, 198);")
        self.pushButton_40 = QPushButton(self.widget_29)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setGeometry(QRect(970, 10, 141, 31))
        self.pushButton_40.setFont(font7)
        self.pushButton_40.setStyleSheet(u"color:black;\n"
"background-color: rgb(37, 211, 102);\n"
"border-radius:5px;")
        self.label_51 = QLabel(self.frame_16)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(25, 1120, 1303, 41))
        font24 = QFont()
        font24.setPointSize(22)
        self.label_51.setFont(font24)
        self.label_51.setStyleSheet(u"color:white;")
        self.widget_30 = QWidget(self.frame_16)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setGeometry(QRect(28, 1220, 1300, 300))
        self.widget_30.setStyleSheet(u"background-color: rgb(18, 140, 126);")
        self.label_185 = QLabel(self.widget_30)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setGeometry(QRect(440, 20, 701, 141))
        font25 = QFont()
        font25.setPointSize(40)
        font25.setBold(True)
        self.label_185.setFont(font25)
        self.label_185.setStyleSheet(u"color:rgb(239, 238, 228);")
        self.pushButton_41 = QPushButton(self.widget_30)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setGeometry(QRect(446, 188, 141, 31))
        self.pushButton_41.setFont(font7)
        self.pushButton_41.setStyleSheet(u"QPushButton{\n"
"color:black;\n"
"background-color:rgb(239, 238, 228);\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(231, 246, 252);\n"
"border:1px solid rgb(7, 94, 84);\n"
"}")
        self.label_187 = QLabel(self.widget_30)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setGeometry(QRect(449, 230, 191, 16))
        font26 = QFont()
        font26.setPointSize(8)
        self.label_187.setFont(font26)
        self.label_365 = QLabel(self.widget_30)
        self.label_365.setObjectName(u"label_365")
        self.label_365.setGeometry(QRect(60, -10, 331, 311))
        self.label_365.setPixmap(QPixmap(u"../../Shivam/Downloads/Coffe (7).png"))
        self.label_365.setScaledContents(True)
        self.label_367 = QLabel(self.frame_16)
        self.label_367.setObjectName(u"label_367")
        self.label_367.setGeometry(QRect(26, 1570, 1299, 51))
        font27 = QFont()
        font27.setPointSize(26)
        self.label_367.setFont(font27)
        self.label_367.setStyleSheet(u"color:rgb(198, 198, 198);")
        self.layoutWidget10 = QWidget(self.frame_16)
        self.layoutWidget10.setObjectName(u"layoutWidget10")
        self.layoutWidget10.setGeometry(QRect(26, 750, 1301, 311))
        self.horizontalLayout_26 = QHBoxLayout(self.layoutWidget10)
        self.horizontalLayout_26.setSpacing(50)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.widget_25 = QWidget(self.layoutWidget10)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setFont(font2)
        self.widget_25.setStyleSheet(u"background-color:rgb(35, 47, 49);\n"
"border:2px solid rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.label_184 = QLabel(self.widget_25)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setGeometry(QRect(80, 200, 131, 81))
        self.label_184.setFont(font13)
        self.label_184.setStyleSheet(u"border:none;\n"
"color: rgb(198, 198, 198);")
        self.pushButton_17 = QPushButton(self.widget_25)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(48, 18, 191, 171))
        self.pushButton_17.setStyleSheet(u"border:none;")
        icon24 = QIcon()
        icon24.addFile(u"../../Shivam/Downloads/Coffe (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon24)
        self.pushButton_17.setIconSize(QSize(180, 180))
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setAutoExclusive(True)

        self.horizontalLayout_26.addWidget(self.widget_25)

        self.widget_26 = QWidget(self.layoutWidget10)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setFont(font2)
        self.widget_26.setStyleSheet(u"background-color:rgb(35, 47, 49);\n"
"border:2px solid rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.label_186 = QLabel(self.widget_26)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setGeometry(QRect(53, 200, 181, 81))
        self.label_186.setFont(font13)
        self.label_186.setStyleSheet(u"border:none;\n"
"color: rgb(198, 198, 198);")
        self.pushButton_36 = QPushButton(self.widget_26)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setGeometry(QRect(50, 20, 191, 171))
        self.pushButton_36.setStyleSheet(u"border:none;")
        icon25 = QIcon()
        icon25.addFile(u"../../Shivam/Downloads/Coffe (3).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_36.setIcon(icon25)
        self.pushButton_36.setIconSize(QSize(180, 180))
        self.pushButton_36.setCheckable(True)
        self.pushButton_36.setAutoExclusive(True)

        self.horizontalLayout_26.addWidget(self.widget_26)

        self.widget_27 = QWidget(self.layoutWidget10)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setFont(font2)
        self.widget_27.setStyleSheet(u"background-color:rgb(35, 47, 49);\n"
"border:2px solid rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.label_188 = QLabel(self.widget_27)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setGeometry(QRect(75, 200, 151, 81))
        self.label_188.setFont(font13)
        self.label_188.setStyleSheet(u"border:none;\n"
"color: rgb(198, 198, 198);")
        self.pushButton_37 = QPushButton(self.widget_27)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setGeometry(QRect(50, 20, 191, 171))
        self.pushButton_37.setStyleSheet(u"border:none;")
        icon26 = QIcon()
        icon26.addFile(u"../../Shivam/Downloads/Coffe (4).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_37.setIcon(icon26)
        self.pushButton_37.setIconSize(QSize(180, 180))
        self.pushButton_37.setCheckable(True)
        self.pushButton_37.setAutoExclusive(True)

        self.horizontalLayout_26.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.layoutWidget10)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setFont(font2)
        self.widget_28.setStyleSheet(u"background-color:rgb(35, 47, 49);\n"
"border:2px solid rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.label_366 = QLabel(self.widget_28)
        self.label_366.setObjectName(u"label_366")
        self.label_366.setGeometry(QRect(80, 200, 121, 81))
        self.label_366.setFont(font13)
        self.label_366.setStyleSheet(u"border:none;\n"
"color: rgb(198, 198, 198);")
        self.pushButton_38 = QPushButton(self.widget_28)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setGeometry(QRect(48, 20, 191, 171))
        self.pushButton_38.setStyleSheet(u"border:none;")
        icon27 = QIcon()
        icon27.addFile(u"../../Shivam/Downloads/Coffe (5).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_38.setIcon(icon27)
        self.pushButton_38.setIconSize(QSize(200, 200))
        self.pushButton_38.setCheckable(True)
        self.pushButton_38.setAutoExclusive(True)

        self.horizontalLayout_26.addWidget(self.widget_28)

        self.layoutWidget11 = QWidget(self.frame_16)
        self.layoutWidget11.setObjectName(u"layoutWidget11")
        self.layoutWidget11.setGeometry(QRect(120, 1670, 1127, 272))
        self.horizontalLayout_27 = QHBoxLayout(self.layoutWidget11)
        self.horizontalLayout_27.setSpacing(100)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setSpacing(15)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_368 = QLabel(self.layoutWidget11)
        self.label_368.setObjectName(u"label_368")
        self.label_368.setMinimumSize(QSize(181, 181))
        self.label_368.setMaximumSize(QSize(181, 181))
        self.label_368.setFont(font12)
        self.label_368.setStyleSheet(u"color:rgb(198, 198, 198);\n"
"border:5px solid rgb(18, 140, 126);\n"
"border-radius:90px;;")

        self.verticalLayout_48.addWidget(self.label_368)

        self.label_372 = QLabel(self.layoutWidget11)
        self.label_372.setObjectName(u"label_372")
        font28 = QFont()
        font28.setPointSize(19)
        font28.setBold(True)
        self.label_372.setFont(font28)
        self.label_372.setStyleSheet(u"color:rgb(198, 198, 198);")

        self.verticalLayout_48.addWidget(self.label_372)


        self.horizontalLayout_27.addLayout(self.verticalLayout_48)

        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setSpacing(15)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_370 = QLabel(self.layoutWidget11)
        self.label_370.setObjectName(u"label_370")
        self.label_370.setMinimumSize(QSize(181, 181))
        self.label_370.setMaximumSize(QSize(181, 181))
        self.label_370.setFont(font12)
        self.label_370.setStyleSheet(u"color:rgb(198, 198, 198);\n"
"border:5px solid rgb(18, 140, 126);\n"
"border-radius:90px;;")

        self.verticalLayout_50.addWidget(self.label_370, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_374 = QLabel(self.layoutWidget11)
        self.label_374.setObjectName(u"label_374")
        self.label_374.setFont(font28)
        self.label_374.setStyleSheet(u"color:rgb(198, 198, 198);")

        self.verticalLayout_50.addWidget(self.label_374, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_27.addLayout(self.verticalLayout_50)

        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setSpacing(15)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_369 = QLabel(self.layoutWidget11)
        self.label_369.setObjectName(u"label_369")
        self.label_369.setMinimumSize(QSize(181, 181))
        self.label_369.setMaximumSize(QSize(181, 181))
        self.label_369.setFont(font12)
        self.label_369.setStyleSheet(u"color:rgb(198, 198, 198);\n"
"border:5px solid rgb(18, 140, 126);\n"
"border-radius:90px;;")

        self.verticalLayout_49.addWidget(self.label_369, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_373 = QLabel(self.layoutWidget11)
        self.label_373.setObjectName(u"label_373")
        font29 = QFont()
        font29.setPointSize(18)
        font29.setBold(True)
        self.label_373.setFont(font29)
        self.label_373.setStyleSheet(u"color:rgb(198, 198, 198);")

        self.verticalLayout_49.addWidget(self.label_373, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_27.addLayout(self.verticalLayout_49)

        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setSpacing(15)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.label_371 = QLabel(self.layoutWidget11)
        self.label_371.setObjectName(u"label_371")
        self.label_371.setMinimumSize(QSize(181, 181))
        self.label_371.setMaximumSize(QSize(181, 181))
        self.label_371.setFont(font12)
        self.label_371.setStyleSheet(u"color:rgb(198, 198, 198);\n"
"border:5px solid rgb(18, 140, 126);\n"
"border-radius:90px;;")

        self.verticalLayout_51.addWidget(self.label_371, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_375 = QLabel(self.layoutWidget11)
        self.label_375.setObjectName(u"label_375")
        self.label_375.setFont(font28)
        self.label_375.setStyleSheet(u"color:rgb(198, 198, 198);")

        self.verticalLayout_51.addWidget(self.label_375, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_27.addLayout(self.verticalLayout_51)

        self.widget_32 = QWidget(self.frame_16)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setGeometry(QRect(27, 2010, 1300, 400))
        self.widget_32.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.label_376 = QLabel(self.widget_32)
        self.label_376.setObjectName(u"label_376")
        self.label_376.setGeometry(QRect(30, 30, 350, 350))
        self.label_376.setPixmap(QPixmap(u"../../Shivam/Downloads/Coffe (12).png"))
        self.label_376.setScaledContents(True)
        self.label_377 = QLabel(self.widget_32)
        self.label_377.setObjectName(u"label_377")
        self.label_377.setGeometry(QRect(130, 120, 151, 161))
        self.label_377.setStyleSheet(u"border:none;")
        self.label_377.setPixmap(QPixmap(u"../../Shivam/Downloads/Black White Minimalist SImple Monogram Typography Logo (11).png"))
        self.label_377.setScaledContents(True)
        self.label_378 = QLabel(self.widget_32)
        self.label_378.setObjectName(u"label_378")
        self.label_378.setGeometry(QRect(420, 40, 701, 171))
        font30 = QFont()
        font30.setFamilies([u"Bell MT"])
        font30.setPointSize(55)
        self.label_378.setFont(font30)
        self.label_379 = QLabel(self.widget_32)
        self.label_379.setObjectName(u"label_379")
        self.label_379.setGeometry(QRect(420, 260, 201, 31))
        font31 = QFont()
        font31.setFamilies([u"Segoe UI"])
        font31.setPointSize(17)
        self.label_379.setFont(font31)
        self.label_379.setStyleSheet(u"color: rgb(198, 198, 198);")
        self.label_380 = QLabel(self.widget_32)
        self.label_380.setObjectName(u"label_380")
        self.label_380.setGeometry(QRect(420, 215, 321, 31))
        self.label_380.setFont(font17)
        self.line_14 = QFrame(self.widget_32)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setGeometry(QRect(350, 0, 16, 401))
        self.line_14.setFrameShape(QFrame.Shape.VLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)
        self.layoutWidget_13 = QWidget(self.widget_32)
        self.layoutWidget_13.setObjectName(u"layoutWidget_13")
        self.layoutWidget_13.setGeometry(QRect(420, 320, 177, 32))
        self.horizontalLayout_29 = QHBoxLayout(self.layoutWidget_13)
        self.horizontalLayout_29.setSpacing(10)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_385 = QLabel(self.layoutWidget_13)
        self.label_385.setObjectName(u"label_385")
        self.label_385.setMinimumSize(QSize(30, 30))
        self.label_385.setMaximumSize(QSize(30, 30))
        self.label_385.setPixmap(QPixmap(u"../../Shivam/Downloads/app-store.png"))
        self.label_385.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.label_385)

        self.label_386 = QLabel(self.layoutWidget_13)
        self.label_386.setObjectName(u"label_386")
        self.label_386.setFont(font2)

        self.horizontalLayout_29.addWidget(self.label_386)

        self.layoutWidget12 = QWidget(self.widget_32)
        self.layoutWidget12.setObjectName(u"layoutWidget12")
        self.layoutWidget12.setGeometry(QRect(720, 320, 165, 32))
        self.horizontalLayout_28 = QHBoxLayout(self.layoutWidget12)
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_384 = QLabel(self.layoutWidget12)
        self.label_384.setObjectName(u"label_384")
        self.label_384.setMinimumSize(QSize(30, 30))
        self.label_384.setMaximumSize(QSize(30, 30))
        self.label_384.setPixmap(QPixmap(u"../../Shivam/Downloads/playstore.png"))
        self.label_384.setScaledContents(True)

        self.horizontalLayout_28.addWidget(self.label_384)

        self.label_383 = QLabel(self.layoutWidget12)
        self.label_383.setObjectName(u"label_383")
        self.label_383.setFont(font2)

        self.horizontalLayout_28.addWidget(self.label_383)

        self.widget_33 = QWidget(self.frame_16)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setGeometry(QRect(26, 2490, 640, 249))
        self.widget_33.setFont(font14)
        self.widget_33.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.label_381 = QLabel(self.widget_33)
        self.label_381.setObjectName(u"label_381")
        self.label_381.setGeometry(QRect(121, 38, 111, 31))
        self.label_381.setFont(font11)
        self.textEdit_10 = QTextEdit(self.widget_33)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setGeometry(QRect(62, 99, 491, 101))
        self.label_382 = QLabel(self.widget_33)
        self.label_382.setObjectName(u"label_382")
        self.label_382.setGeometry(QRect(60, 40, 61, 51))
        self.label_382.setPixmap(QPixmap(u"../../Shivam/Downloads/kisspng-computer-icons-user-profile-avatar-job-icon-5b521c56afedc0.0537187115321078627206.png"))
        self.label_382.setScaledContents(True)
        self.layoutWidget_14 = QWidget(self.widget_33)
        self.layoutWidget_14.setObjectName(u"layoutWidget_14")
        self.layoutWidget_14.setGeometry(QRect(128, 68, 101, 17))
        self.horizontalLayout_30 = QHBoxLayout(self.layoutWidget_14)
        self.horizontalLayout_30.setSpacing(2)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_387 = QLabel(self.layoutWidget_14)
        self.label_387.setObjectName(u"label_387")
        self.label_387.setMinimumSize(QSize(15, 15))
        self.label_387.setMaximumSize(QSize(15, 15))
        self.label_387.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_387.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.label_387)

        self.label_388 = QLabel(self.layoutWidget_14)
        self.label_388.setObjectName(u"label_388")
        self.label_388.setMinimumSize(QSize(15, 15))
        self.label_388.setMaximumSize(QSize(15, 15))
        self.label_388.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_388.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.label_388)

        self.label_389 = QLabel(self.layoutWidget_14)
        self.label_389.setObjectName(u"label_389")
        self.label_389.setMinimumSize(QSize(15, 15))
        self.label_389.setMaximumSize(QSize(15, 15))
        self.label_389.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_389.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.label_389)

        self.label_390 = QLabel(self.layoutWidget_14)
        self.label_390.setObjectName(u"label_390")
        self.label_390.setMinimumSize(QSize(15, 15))
        self.label_390.setMaximumSize(QSize(15, 15))
        self.label_390.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_390.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.label_390)

        self.label_391 = QLabel(self.layoutWidget_14)
        self.label_391.setObjectName(u"label_391")
        self.label_391.setMinimumSize(QSize(15, 15))
        self.label_391.setMaximumSize(QSize(15, 15))
        self.label_391.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_391.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.label_391)

        self.widget_34 = QWidget(self.frame_16)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setGeometry(QRect(690, 2490, 639, 249))
        self.widget_34.setFont(font14)
        self.widget_34.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.label_392 = QLabel(self.widget_34)
        self.label_392.setObjectName(u"label_392")
        self.label_392.setGeometry(QRect(117, 37, 171, 31))
        self.label_392.setFont(font11)
        self.textEdit_11 = QTextEdit(self.widget_34)
        self.textEdit_11.setObjectName(u"textEdit_11")
        self.textEdit_11.setGeometry(QRect(54, 99, 491, 101))
        self.label_393 = QLabel(self.widget_34)
        self.label_393.setObjectName(u"label_393")
        self.label_393.setGeometry(QRect(50, 40, 61, 51))
        self.label_393.setPixmap(QPixmap(u"../../Shivam/Downloads/kisspng-computer-icons-user-profile-avatar-job-icon-5b521c56afedc0.0537187115321078627206.png"))
        self.label_393.setScaledContents(True)
        self.layoutWidget_15 = QWidget(self.widget_34)
        self.layoutWidget_15.setObjectName(u"layoutWidget_15")
        self.layoutWidget_15.setGeometry(QRect(121, 68, 101, 17))
        self.horizontalLayout_31 = QHBoxLayout(self.layoutWidget_15)
        self.horizontalLayout_31.setSpacing(2)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_394 = QLabel(self.layoutWidget_15)
        self.label_394.setObjectName(u"label_394")
        self.label_394.setMinimumSize(QSize(15, 15))
        self.label_394.setMaximumSize(QSize(15, 15))
        self.label_394.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_394.setScaledContents(True)

        self.horizontalLayout_31.addWidget(self.label_394)

        self.label_395 = QLabel(self.layoutWidget_15)
        self.label_395.setObjectName(u"label_395")
        self.label_395.setMinimumSize(QSize(15, 15))
        self.label_395.setMaximumSize(QSize(15, 15))
        self.label_395.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_395.setScaledContents(True)

        self.horizontalLayout_31.addWidget(self.label_395)

        self.label_396 = QLabel(self.layoutWidget_15)
        self.label_396.setObjectName(u"label_396")
        self.label_396.setMinimumSize(QSize(15, 15))
        self.label_396.setMaximumSize(QSize(15, 15))
        self.label_396.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_396.setScaledContents(True)

        self.horizontalLayout_31.addWidget(self.label_396)

        self.label_397 = QLabel(self.layoutWidget_15)
        self.label_397.setObjectName(u"label_397")
        self.label_397.setMinimumSize(QSize(15, 15))
        self.label_397.setMaximumSize(QSize(15, 15))
        self.label_397.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_397.setScaledContents(True)

        self.horizontalLayout_31.addWidget(self.label_397)

        self.label_398 = QLabel(self.layoutWidget_15)
        self.label_398.setObjectName(u"label_398")
        self.label_398.setMinimumSize(QSize(15, 15))
        self.label_398.setMaximumSize(QSize(15, 15))
        self.label_398.setPixmap(QPixmap(u"PropImages/db31640ff5ae3623bdd2fcd616d6c24a.png"))
        self.label_398.setScaledContents(True)

        self.horizontalLayout_31.addWidget(self.label_398)

        self.label_399 = QLabel(self.frame_16)
        self.label_399.setObjectName(u"label_399")
        self.label_399.setGeometry(QRect(542, 2423, 270, 51))
        font32 = QFont()
        font32.setFamilies([u"Segoe UI Variable Display Light"])
        font32.setPointSize(19)
        self.label_399.setFont(font32)
        self.label_399.setStyleSheet(u"color:rgb(198, 198, 198);")

        self.verticalLayout_26.addWidget(self.frame_16)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_25.addWidget(self.scrollArea_8)


        self.horizontalLayout_4.addWidget(self.widget_9)

        self.stackedWidget_3.addWidget(self.page_8)
        self.profilepage = QWidget()
        self.profilepage.setObjectName(u"profilepage")
        self.verticalLayout_14 = QVBoxLayout(self.profilepage)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.profilepage)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_16 = QVBoxLayout(self.widget_5)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_5 = QScrollArea(self.widget_5)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(7, 94, 84);\n"
" }")
        self.scrollArea_5.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 98, 2000))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 2000))
        self.frame_5.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(50, 35, -1, 60)
        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFont(font3)
        self.frame.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(13, 10, 147, 33))
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(16, 49, 16, 16))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(35, 49, 52, 16))
        self.label_9.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_2.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(298, 10, 182, 31))
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(477, 17, 75, 20))
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(354, 44, 151, 20))
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 99, 291, 269))
        self.label_13.setStyleSheet(u"border-radius:5px;")
        self.label_13.setPixmap(QPixmap(u"../../Shivam/Downloads/WhatsApp Image 2024-06-26 at 19.16.15_a6f43295.jpg"))
        self.label_13.setScaledContents(True)
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(307, 99, 16, 269))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(377, 99, 175, 44))
        self.label_14.setFont(font6)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(316, 185, 274, 16))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(377, 194, 120, 44))
        self.label_15.setFont(font6)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(377, 288, 152, 66))
        self.label_16.setFont(font6)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 75, 410, 18))
        self.label_17.setFont(font7)
        self.label_17.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(316, 279, 274, 16))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFont(font3)
        self.frame_4.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(13, 10, 180, 33))
        self.label_18.setFont(font4)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(16, 49, 16, 16))
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_20 = QLabel(self.frame_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(35, 49, 150, 16))
        self.label_20.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_3.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_21 = QLabel(self.frame_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(298, 10, 182, 31))
        self.label_21.setFont(font5)
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_22 = QLabel(self.frame_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(477, 17, 95, 20))
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_23 = QLabel(self.frame_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(354, 44, 151, 20))
        self.label_23.setFont(font2)
        self.label_23.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_24 = QLabel(self.frame_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 99, 291, 269))
        self.label_24.setStyleSheet(u"border-radius:5px;")
        self.label_24.setPixmap(QPixmap(u"PropImages/Mumbai/Mumbai-Malad.PratapLibertyOne/Mumbai-2.jpg"))
        self.label_24.setScaledContents(True)
        self.line_4 = QFrame(self.frame_4)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(307, 99, 16, 269))
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_25 = QLabel(self.frame_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(377, 99, 175, 44))
        self.label_25.setFont(font6)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_5 = QFrame(self.frame_4)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(316, 185, 274, 16))
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_26 = QLabel(self.frame_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(377, 194, 120, 44))
        self.label_26.setFont(font6)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_27 = QLabel(self.frame_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(377, 290, 152, 66))
        self.label_27.setFont(font6)
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_28 = QLabel(self.frame_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 75, 550, 18))
        self.label_28.setFont(font7)
        self.label_28.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_6 = QFrame(self.frame_4)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(316, 279, 274, 16))
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.frame_4, 0, 1, 1, 1)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFont(font3)
        self.frame_8.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.label_29 = QLabel(self.frame_8)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(13, 10, 147, 33))
        self.label_29.setFont(font4)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_30 = QLabel(self.frame_8)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(16, 49, 16, 16))
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_31 = QLabel(self.frame_8)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(35, 49, 100, 16))
        self.label_31.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_4 = QPushButton(self.frame_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_4.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_32 = QLabel(self.frame_8)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(298, 10, 182, 31))
        self.label_32.setFont(font5)
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_33 = QLabel(self.frame_8)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(477, 17, 75, 20))
        self.label_33.setFont(font2)
        self.label_33.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_34 = QLabel(self.frame_8)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(354, 44, 151, 20))
        self.label_34.setFont(font2)
        self.label_34.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_35 = QLabel(self.frame_8)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(10, 99, 291, 269))
        self.label_35.setStyleSheet(u"border-radius:5px;")
        self.label_35.setPixmap(QPixmap(u"PropImages/Mumbai/Mumbai-Andheri.Tathastu/Mumbai-4.1.jpg"))
        self.label_35.setScaledContents(True)
        self.line_7 = QFrame(self.frame_8)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(307, 99, 16, 269))
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_36 = QLabel(self.frame_8)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(377, 99, 175, 44))
        self.label_36.setFont(font6)
        self.label_36.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_8 = QFrame(self.frame_8)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(316, 185, 274, 16))
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_37 = QLabel(self.frame_8)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(377, 194, 120, 44))
        self.label_37.setFont(font6)
        self.label_37.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_38 = QLabel(self.frame_8)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(373, 290, 152, 66))
        self.label_38.setFont(font6)
        self.label_38.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_39 = QLabel(self.frame_8)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(10, 75, 500, 18))
        self.label_39.setFont(font7)
        self.label_39.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_9 = QFrame(self.frame_8)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(316, 279, 274, 16))
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.frame_8, 1, 0, 1, 1)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFont(font3)
        self.frame_9.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.label_40 = QLabel(self.frame_9)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(13, 10, 220, 33))
        self.label_40.setFont(font4)
        self.label_40.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_41 = QLabel(self.frame_9)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(16, 49, 16, 16))
        self.label_41.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_42 = QLabel(self.frame_9)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(35, 49, 200, 16))
        self.label_42.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_5 = QPushButton(self.frame_9)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_5.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_43 = QLabel(self.frame_9)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(283, 10, 191, 31))
        self.label_43.setFont(font5)
        self.label_43.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_44 = QLabel(self.frame_9)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(477, 17, 75, 20))
        self.label_44.setFont(font2)
        self.label_44.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_45 = QLabel(self.frame_9)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(354, 44, 151, 20))
        self.label_45.setFont(font2)
        self.label_45.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_46 = QLabel(self.frame_9)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(10, 99, 291, 269))
        self.label_46.setStyleSheet(u"border-radius:5px;")
        self.label_46.setPixmap(QPixmap(u"PropImages/Mumbai/Mumbai-Boriwali.VKLALHariPhasI/Mumbai - 5.jpg"))
        self.label_46.setScaledContents(True)
        self.line_10 = QFrame(self.frame_9)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(307, 99, 16, 269))
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_47 = QLabel(self.frame_9)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(377, 99, 175, 44))
        self.label_47.setFont(font6)
        self.label_47.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_11 = QFrame(self.frame_9)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(316, 185, 274, 16))
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_48 = QLabel(self.frame_9)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(377, 194, 120, 44))
        self.label_48.setFont(font6)
        self.label_48.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_49 = QLabel(self.frame_9)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(377, 290, 152, 66))
        self.label_49.setFont(font6)
        self.label_49.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_50 = QLabel(self.frame_9)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(10, 75, 421, 18))
        self.label_50.setFont(font7)
        self.label_50.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_12 = QFrame(self.frame_9)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setGeometry(QRect(316, 279, 274, 16))
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.frame_9, 1, 1, 1, 1)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFont(font3)
        self.frame_10.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.label_62 = QLabel(self.frame_10)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(13, 10, 241, 33))
        self.label_62.setFont(font4)
        self.label_62.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_63 = QLabel(self.frame_10)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(16, 49, 16, 16))
        self.label_63.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_64 = QLabel(self.frame_10)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(35, 49, 111, 16))
        self.label_64.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_7 = QPushButton(self.frame_10)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_7.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_65 = QLabel(self.frame_10)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(284, 10, 201, 31))
        self.label_65.setFont(font5)
        self.label_65.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_66 = QLabel(self.frame_10)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(477, 17, 75, 20))
        self.label_66.setFont(font2)
        self.label_66.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_67 = QLabel(self.frame_10)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(354, 44, 151, 20))
        self.label_67.setFont(font2)
        self.label_67.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_68 = QLabel(self.frame_10)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(10, 99, 291, 269))
        self.label_68.setStyleSheet(u"border-radius:5px;")
        self.label_68.setPixmap(QPixmap(u"PropImages/Mumbai/Mumbai-Ghatkopar.Rajshree/Mumbai-1.jpg"))
        self.label_68.setScaledContents(True)
        self.line_16 = QFrame(self.frame_10)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setGeometry(QRect(307, 99, 16, 269))
        self.line_16.setFrameShape(QFrame.Shape.VLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_69 = QLabel(self.frame_10)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(377, 99, 175, 44))
        self.label_69.setFont(font6)
        self.label_69.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_17 = QFrame(self.frame_10)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setGeometry(QRect(316, 185, 274, 16))
        self.line_17.setFrameShape(QFrame.Shape.HLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_70 = QLabel(self.frame_10)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(377, 194, 120, 44))
        self.label_70.setFont(font6)
        self.label_70.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_71 = QLabel(self.frame_10)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(377, 290, 152, 66))
        self.label_71.setFont(font6)
        self.label_71.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_72 = QLabel(self.frame_10)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(10, 75, 521, 18))
        self.label_72.setFont(font7)
        self.label_72.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_18 = QFrame(self.frame_10)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setGeometry(QRect(316, 279, 274, 16))
        self.line_18.setFrameShape(QFrame.Shape.HLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.frame_10, 2, 0, 1, 1)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFont(font3)
        self.frame_11.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.label_73 = QLabel(self.frame_11)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(13, 10, 161, 33))
        self.label_73.setFont(font4)
        self.label_73.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_74 = QLabel(self.frame_11)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(16, 49, 16, 16))
        self.label_74.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_75 = QLabel(self.frame_11)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(35, 49, 81, 16))
        self.label_75.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_8 = QPushButton(self.frame_11)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_8.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_76 = QLabel(self.frame_11)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(298, 10, 182, 31))
        self.label_76.setFont(font5)
        self.label_76.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_77 = QLabel(self.frame_11)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(477, 17, 75, 20))
        self.label_77.setFont(font2)
        self.label_77.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_78 = QLabel(self.frame_11)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(354, 44, 151, 20))
        self.label_78.setFont(font2)
        self.label_78.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_79 = QLabel(self.frame_11)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(10, 99, 291, 269))
        self.label_79.setStyleSheet(u"border-radius:5px;")
        self.label_79.setPixmap(QPixmap(u"PropImages/Mumbai/Mumbai-3-LowerParel.LodhaPark/Mumbai-3.1_1_11zon.jpg"))
        self.label_79.setScaledContents(True)
        self.line_19 = QFrame(self.frame_11)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setGeometry(QRect(307, 99, 16, 269))
        self.line_19.setFrameShape(QFrame.Shape.VLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_80 = QLabel(self.frame_11)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(377, 99, 175, 44))
        self.label_80.setFont(font6)
        self.label_80.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_20 = QFrame(self.frame_11)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setGeometry(QRect(316, 185, 274, 16))
        self.line_20.setFrameShape(QFrame.Shape.HLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_81 = QLabel(self.frame_11)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(377, 194, 120, 44))
        self.label_81.setFont(font6)
        self.label_81.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_82 = QLabel(self.frame_11)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(377, 290, 152, 66))
        self.label_82.setFont(font6)
        self.label_82.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_83 = QLabel(self.frame_11)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(10, 75, 471, 18))
        self.label_83.setFont(font7)
        self.label_83.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_21 = QFrame(self.frame_11)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setGeometry(QRect(316, 279, 274, 16))
        self.line_21.setFrameShape(QFrame.Shape.HLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.frame_11, 2, 1, 1, 1)

        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFont(font3)
        self.frame_12.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.label_84 = QLabel(self.frame_12)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(13, 10, 181, 33))
        self.label_84.setFont(font4)
        self.label_84.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_85 = QLabel(self.frame_12)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(16, 49, 16, 16))
        self.label_85.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_86 = QLabel(self.frame_12)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(35, 49, 81, 16))
        self.label_86.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_9 = QPushButton(self.frame_12)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_9.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_87 = QLabel(self.frame_12)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(285, 10, 191, 31))
        self.label_87.setFont(font5)
        self.label_87.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_88 = QLabel(self.frame_12)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(477, 17, 75, 20))
        self.label_88.setFont(font2)
        self.label_88.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_89 = QLabel(self.frame_12)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(354, 44, 151, 20))
        self.label_89.setFont(font2)
        self.label_89.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_90 = QLabel(self.frame_12)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setGeometry(QRect(10, 99, 291, 269))
        self.label_90.setStyleSheet(u"border-radius:5px;")
        self.label_90.setPixmap(QPixmap(u"PropImages/WhatsApp Image 2024-07-05 at 17.29.33_eac17ca7.jpg"))
        self.label_90.setScaledContents(True)
        self.line_22 = QFrame(self.frame_12)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setGeometry(QRect(307, 99, 16, 269))
        self.line_22.setFrameShape(QFrame.Shape.VLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_91 = QLabel(self.frame_12)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(377, 99, 175, 44))
        self.label_91.setFont(font6)
        self.label_91.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_23 = QFrame(self.frame_12)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setGeometry(QRect(316, 185, 274, 16))
        self.line_23.setFrameShape(QFrame.Shape.HLine)
        self.line_23.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_92 = QLabel(self.frame_12)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setGeometry(QRect(377, 194, 120, 44))
        self.label_92.setFont(font6)
        self.label_92.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_93 = QLabel(self.frame_12)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setGeometry(QRect(377, 290, 152, 66))
        self.label_93.setFont(font6)
        self.label_93.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_94 = QLabel(self.frame_12)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setGeometry(QRect(10, 75, 501, 18))
        self.label_94.setFont(font7)
        self.label_94.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_24 = QFrame(self.frame_12)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setGeometry(QRect(316, 279, 274, 16))
        self.line_24.setFrameShape(QFrame.Shape.HLine)
        self.line_24.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.frame_12, 3, 0, 1, 1)

        self.frame_13 = QFrame(self.frame_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFont(font3)
        self.frame_13.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.label_95 = QLabel(self.frame_13)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setGeometry(QRect(13, 10, 231, 33))
        self.label_95.setFont(font4)
        self.label_95.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_96 = QLabel(self.frame_13)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setGeometry(QRect(16, 49, 16, 16))
        self.label_96.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_97 = QLabel(self.frame_13)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(35, 49, 101, 16))
        self.label_97.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_10 = QPushButton(self.frame_13)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_10.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(7, 94, 84);\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border:1px solid rgb(7, 94, 84);\n"
"background-color:rgb(35, 47, 49);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_98 = QLabel(self.frame_13)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setGeometry(QRect(294, 10, 182, 31))
        self.label_98.setFont(font5)
        self.label_98.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_99 = QLabel(self.frame_13)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(467, 17, 91, 20))
        self.label_99.setFont(font2)
        self.label_99.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_100 = QLabel(self.frame_13)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setGeometry(QRect(354, 44, 151, 20))
        self.label_100.setFont(font2)
        self.label_100.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_101 = QLabel(self.frame_13)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setGeometry(QRect(10, 99, 291, 269))
        self.label_101.setStyleSheet(u"border-radius:5px;")
        self.label_101.setPixmap(QPixmap(u"../../Shivam/Downloads/WhatsApp Image 2024-06-26 at 19.16.15_a6f43295.jpg"))
        self.label_101.setScaledContents(True)
        self.line_25 = QFrame(self.frame_13)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setGeometry(QRect(307, 99, 16, 269))
        self.line_25.setFrameShape(QFrame.Shape.VLine)
        self.line_25.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_102 = QLabel(self.frame_13)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setGeometry(QRect(377, 99, 175, 44))
        self.label_102.setFont(font6)
        self.label_102.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_26 = QFrame(self.frame_13)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setGeometry(QRect(316, 185, 274, 16))
        self.line_26.setFrameShape(QFrame.Shape.HLine)
        self.line_26.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_103 = QLabel(self.frame_13)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setGeometry(QRect(377, 194, 120, 44))
        self.label_103.setFont(font6)
        self.label_103.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_104 = QLabel(self.frame_13)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setGeometry(QRect(377, 290, 152, 66))
        self.label_104.setFont(font6)
        self.label_104.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_105 = QLabel(self.frame_13)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setGeometry(QRect(10, 75, 410, 18))
        self.label_105.setFont(font7)
        self.label_105.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_27 = QFrame(self.frame_13)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setGeometry(QRect(316, 279, 274, 16))
        self.line_27.setFrameShape(QFrame.Shape.HLine)
        self.line_27.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.frame_13, 3, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout_15.addWidget(self.frame_5)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_16.addWidget(self.scrollArea_5)


        self.verticalLayout_14.addWidget(self.widget_5)

        self.stackedWidget_3.addWidget(self.profilepage)

        self.verticalLayout.addWidget(self.stackedWidget_3)


        self.horizontalLayout.addWidget(self.mainmenu)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        
        self.Menu.toggled.connect(self.icon_name_widget.setHidden)
        # Lineedit mode
        # self.linedit.
        # self.lineEdit.setReadOnly(True)
        
# ----------------------
        self.pushButton_33.clicked.connect(self.logout_win_frame)
        self.pushButton.clicked.connect(self.filter_win_frame)
        self.Dashboard_7.clicked.connect(self.feedback_win_frame)
        self.pushButton_11.clicked.connect(self.notification_win_frame)
        self.pushButton_11.clicked.connect(self.internet_checker) # Internet checker 
        
        self.loginbutton_3.clicked.connect(self.owner_win_frame) 
        # self.comboBox.currentIndexChanged.connect(self.fetch_city)  # If belo lambda will not work then is for backend
        self.comboBox.currentIndexChanged.connect(lambda index: setattr(self, 'cmb_city', self.comboBox.itemText(index)))
        self.pushButton_32.clicked.connect(self.fetch_city_price_type) # Search Button fetching the values 
        self.loginbutton.clicked.connect(self.contact_us_wp) 
        self.loginbutton_2.clicked.connect(self.contact_us_email)
#------ # Scratch framess
        self.amazonbutton.clicked.connect(lambda : self.scratch_win_which(1))
        self.Dominosbutton.clicked.connect(lambda : self.scratch_win_which(2))
        self.PizzaHutbutton.clicked.connect(lambda : self.scratch_win_which(3))
        self.FlipkartButton.clicked.connect(lambda : self.scratch_win_which(4))
        self.Myntrabutton.clicked.connect(lambda : self.scratch_win_which(5))
        self.zomatobutton.clicked.connect(lambda : self.scratch_win_which(6))
        
        self.loginbutton_4.clicked.connect(self.refer_win_frame)
        self.pushButton_13.clicked.connect(self.myreward_win_frame)
        self.pushButton_12.clicked.connect(self.noscratches_win_frame)
        self.pushButton_6.clicked.connect(self.clck_more_info)
        
        # List of buttons for Mumbai
        mumbai_buttons = [
        (self.pushButton_2, "M1"), 
        (self.pushButton_3, "M2"), 
        (self.pushButton_4, "M3"), 
        (self.pushButton_5, "M4"), 
        (self.pushButton_7, "M5"), 
        (self.pushButton_8, "M6"), 
        (self.pushButton_9, "M7"), 
        (self.pushButton_10, "M8")
        ]

        # List of buttons for Pune
        pune_buttons = [
        (self.pushButton_26, "P1"), 
        (self.pushButton_27, "P2"), 
        (self.pushButton_28, "P3"), 
        (self.pushButton_29, "P4"), 
        (self.pushButton_30, "P5"), 
        (self.pushButton_31, "P6"), 
        (self.pushButton_34, "P7"), 
        (self.pushButton_35, "P8")
        ]

        # List of buttons for Thane
        thane_buttons = [
        (self.pushButton_18, "T1"), 
        (self.pushButton_19, "T2"), 
        (self.pushButton_20, "T3"), 
        (self.pushButton_21, "T4"), 
        (self.pushButton_22, "T5"), 
        (self.pushButton_23, "T6"), 
        (self.pushButton_24, "T7"), 
        (self.pushButton_25, "T8")
        ]

        # Combine all buttons into a single list
        all_buttons = mumbai_buttons + pune_buttons + thane_buttons

        # Connect each button to the get_an_email method with an additional argument
        for button, property_detail in all_buttons:
                button.clicked.connect(partial(self.clck_more_info, property_detail))
                
                
                
                
                
        
        self.myreward_win_frame() # This frame are alrdy showing through the scratch and win frame
        
        
       
       
        # Stackwidgets Calling 
        self.toolBox.setCurrentIndex(3)
        self.toolBox.layout().setSpacing(22)
        self.comboBox.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(18)
        self.toolBox_2.setCurrentIndex(0)
        
        self.toolBox_2.layout().setSpacing(10)
        self.Profile_2.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(0))
        self.Messages_2.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(1))
        self.Profile_5.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(2))
        self.Messages_5.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(3))
        self.pushButton_40.clicked.connect(lambda : self.stackedWidget_3.setCurrentIndex(4))
        self.Dashboard_6.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(4))
        self.Dashboard_8.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(5))
        self.pushButton_39.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(18))
        self.pushButton_41.clicked.connect(lambda : self.stackedWidget_3.setCurrentIndex(19))
        self.Dashboard_2.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(19))
        
        
        
#-----------------------------------

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_39.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<strong>M</strong>iddle <strong>M</strong>an", None))
        self.Dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Mumbai", None))
        self.Profile_2.setText(QCoreApplication.translate("MainWindow", u"Thane", None))
        self.Messages_2.setText(QCoreApplication.translate("MainWindow", u"Pune", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"New Project", None))
        self.Messages_3.setText(QCoreApplication.translate("MainWindow", u"Plumbing", None))
        self.Dashboard_3.setText(QCoreApplication.translate("MainWindow", u"Interior Design", None))
        self.Profile_3.setText(QCoreApplication.translate("MainWindow", u"Ac Services", None))
        self.Dashboard_5.setText(QCoreApplication.translate("MainWindow", u"Carpentry", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Other Services", None))
        self.Dashboard_4.setText(QCoreApplication.translate("MainWindow", u"Rent Reciept", None))
        self.Profile_4.setText(QCoreApplication.translate("MainWindow", u"Tenant Verif..", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"Agreements", None))
        self.Dashboard_6.setText(QCoreApplication.translate("MainWindow", u"Click Here...", None))
        self.Dashboard_8.setText(QCoreApplication.translate("MainWindow", u"Scratch and Earn", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"Click and Earn", None))
        self.Dashboard_7.setText(QCoreApplication.translate("MainWindow", u" Feedback", None))
        self.Profile_5.setText(QCoreApplication.translate("MainWindow", u"Contact Us", None))
        self.Messages_5.setText(QCoreApplication.translate("MainWindow", u"About Us", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u" Others", None))
        self.pushButton_11.setText("")
        self.Menu.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"   Filter", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Mumbai", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Thane", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Pune", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Mumbai", None))
        self.pushButton_32.setText("")
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"  new", None))
        self.pushButton_6.setText("")
        self.pushButton_33.setText("")
        self.label_222.setText(QCoreApplication.translate("MainWindow", u"Dosti Heron", None))
        self.label_223.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_224.setText(QCoreApplication.translate("MainWindow", u"DOSTI REALTY", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_225.setText(QCoreApplication.translate("MainWindow", u"\u20b945.0 L - 1.1 Cr | ", None))
        self.label_226.setText(QCoreApplication.translate("MainWindow", u"\u20b915.63 K/sq.ft", None))
        self.label_227.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b923.83 K", None))
        self.label_228.setText("")
        self.label_229.setText(QCoreApplication.translate("MainWindow", u"Studio, 1, 2 BHK Apartments\n"
"Configurations", None))
        self.label_230.setText(QCoreApplication.translate("MainWindow", u"Dec, 2027\n"
"Possession Starts", None))
        self.label_231.setText(QCoreApplication.translate("MainWindow", u"288 sq.ft. - 604 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_232.setText(QCoreApplication.translate("MainWindow", u"Dosti Heron, Balkum, Thane West, Thane", None))
        self.label_266.setText(QCoreApplication.translate("MainWindow", u"Lakescape", None))
        self.label_267.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_268.setText(QCoreApplication.translate("MainWindow", u"HOMEBAZAAR.COM", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_269.setText(QCoreApplication.translate("MainWindow", u"\u20b91.54 Cr - 1.96 Cr | ", None))
        self.label_270.setText(QCoreApplication.translate("MainWindow", u"\u20b921.26 K/sq.ft", None))
        self.label_271.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b971.99 K", None))
        self.label_272.setText("")
        self.label_273.setText(QCoreApplication.translate("MainWindow", u"2, 3 BHK Apartments\n"
"Configurations", None))
        self.label_274.setText(QCoreApplication.translate("MainWindow", u"Dec, 2028\n"
"Possession Starts", None))
        self.label_275.setText(QCoreApplication.translate("MainWindow", u"680 sq.ft. - 925 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_276.setText(QCoreApplication.translate("MainWindow", u"G B Road, Kavesar Village, Thane West, Ghodbunder Road, Thane", None))
        self.label_211.setText(QCoreApplication.translate("MainWindow", u"Shivalaya Heights", None))
        self.label_212.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_213.setText(QCoreApplication.translate("MainWindow", u"RUDIS INFRA", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_214.setText(QCoreApplication.translate("MainWindow", u"\u20b936.99 L - 64.78 L |", None))
        self.label_215.setText(QCoreApplication.translate("MainWindow", u"\u20b934 K/sq.ftl", None))
        self.label_216.setText(QCoreApplication.translate("MainWindow", u"Emi start at  19.59 K", None))
        self.label_217.setText("")
        self.label_218.setText(QCoreApplication.translate("MainWindow", u"1, 2 BHK Apartments\n"
"Configurations", None))
        self.label_219.setText(QCoreApplication.translate("MainWindow", u"Dec, 2027\n"
"Possession Starts", None))
        self.label_220.setText(QCoreApplication.translate("MainWindow", u"418 sq.ft. - 732 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_221.setText(QCoreApplication.translate("MainWindow", u"153, Hissa No-1/1/ & Hissa No-2, Shilphata, Beyond Thane, Navi Mumbai", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"Ashar Merac", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"ASHAR GROUP", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"\u20b970 K - 1.69 Cr | ", None))
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"\u20b920.18 K/sq.ft", None))
        self.label_205.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b938.72 K", None))
        self.label_207.setText(QCoreApplication.translate("MainWindow", u"1, 2, 3 BHK Apartments\n"
"Configurations", None))
        self.label_208.setText(QCoreApplication.translate("MainWindow", u"Dec, 2028\n"
"Possession Starts", None))
        self.label_209.setText(QCoreApplication.translate("MainWindow", u"390 sq.ft. - 830 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"Ashar Merac, Thane(West), Thane", None))
        self.label_206.setText("")
        self.label_233.setText(QCoreApplication.translate("MainWindow", u"Parijas Horizon\n"
"", None))
        self.label_234.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_235.setText(QCoreApplication.translate("MainWindow", u"PARIJAS GROUP", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_236.setText(QCoreApplication.translate("MainWindow", u"\u20b945.3 L - 66.0 L | ", None))
        self.label_237.setText(QCoreApplication.translate("MainWindow", u"\u20b98.85 K/sq.ft", None))
        self.label_238.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b923..05 K", None))
        self.label_239.setText("")
        self.label_240.setText(QCoreApplication.translate("MainWindow", u"1, 2 BHK Apartments\n"
"Configurations", None))
        self.label_241.setText(QCoreApplication.translate("MainWindow", u"Jun, 2028\n"
"Possession Starts", None))
        self.label_242.setText(QCoreApplication.translate("MainWindow", u"484 sq.ft. - 757 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_243.setText(QCoreApplication.translate("MainWindow", u"Gandhare, Kalyan West, Beyond Thane, Thane", None))
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"Dosti Olive", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"DOSTI REALITY", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"\u20b91.25 Cr - 2.04 Cr | ", None))
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"\u20b934 K/sq.ft", None))
        self.label_194.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b962.86 K", None))
        self.label_195.setText("")
        self.label_196.setText(QCoreApplication.translate("MainWindow", u"2, 3 BHK Apartments\n"
"Configurations", None))
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"Sep, 2028\n"
"Possession Starts", None))
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"628 sq.ft. - 1022 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"Balkum, Thane West, Thane", None))
        self.label_255.setText(QCoreApplication.translate("MainWindow", u"Tulsi Ariana\n"
"", None))
        self.label_256.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_257.setText(QCoreApplication.translate("MainWindow", u"TULSI REALITY", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_258.setText(QCoreApplication.translate("MainWindow", u"\u20b990.0 L - 1.8 Cr | ", None))
        self.label_259.setText(QCoreApplication.translate("MainWindow", u"\u20b954 K/sq.ftl", None))
        self.label_260.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b945.68 K", None))
        self.label_261.setText("")
        self.label_262.setText(QCoreApplication.translate("MainWindow", u"2, 4 BHK Apartments\n"
"Configurations", None))
        self.label_263.setText(QCoreApplication.translate("MainWindow", u"Dec, 2024\n"
"Possession Starts", None))
        self.label_264.setText(QCoreApplication.translate("MainWindow", u"734 sq.ft. - 1449 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_265.setText(QCoreApplication.translate("MainWindow", u"Vasant Valley Road, Near Poddar International School, Kalyan West, Thane", None))
        self.label_244.setText(QCoreApplication.translate("MainWindow", u"Tisai Residency", None))
        self.label_245.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_246.setText(QCoreApplication.translate("MainWindow", u"SKY TOUCH", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_247.setText(QCoreApplication.translate("MainWindow", u"\u20b941.63 l - 63.23 Cr | ", None))
        self.label_248.setText(QCoreApplication.translate("MainWindow", u"\u20b96 K/sq.ft", None))
        self.label_249.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b921.76 K", None))
        self.label_250.setText("")
        self.label_251.setText(QCoreApplication.translate("MainWindow", u"1, 2 BHK Apartments\n"
"Configurations", None))
        self.label_252.setText(QCoreApplication.translate("MainWindow", u"Jun, 2027\n"
"Possession Starts", None))
        self.label_253.setText(QCoreApplication.translate("MainWindow", u"685 sq.ft. - 1050 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_254.setText(QCoreApplication.translate("MainWindow", u"Namdev Wadi, Behind Tisai Marriage Hall, Tisgaon, Kalyan (E ), Thane", None))
        self.label_354.setText(QCoreApplication.translate("MainWindow", u"Sukhwani Nysa", None))
        self.label_355.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_356.setText(QCoreApplication.translate("MainWindow", u"Ms Ravet, Pimpri Chinchwad, Pune", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_357.setText(QCoreApplication.translate("MainWindow", u"\u20b933.52 L - 56.32 L | ", None))
        self.label_358.setText(QCoreApplication.translate("MainWindow", u"\u20b934 K/sq.ftl", None))
        self.label_359.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b917.75 K", None))
        self.label_360.setText("")
        self.label_361.setText(QCoreApplication.translate("MainWindow", u"2 BHK Apartments\n"
"Configurations", None))
        self.label_362.setText(QCoreApplication.translate("MainWindow", u"Jun, 2024\n"
"Possession Starts", None))
        self.label_363.setText(QCoreApplication.translate("MainWindow", u"466 sq.ft. - 783 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_364.setText(QCoreApplication.translate("MainWindow", u"Ravet, Pimpri Chinchwad, Pune", None))
        self.label_277.setText(QCoreApplication.translate("MainWindow", u"Silver Gardenia", None))
        self.label_278.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_279.setText(QCoreApplication.translate("MainWindow", u"SILVER GROUP", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_280.setText(QCoreApplication.translate("MainWindow", u"\u20b960.0 L - 1.7 Cr | ", None))
        self.label_281.setText(QCoreApplication.translate("MainWindow", u"\u20b924 K/sq.ftl", None))
        self.label_282.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b935.23 K", None))
        self.label_283.setText("")
        self.label_284.setText(QCoreApplication.translate("MainWindow", u"2, 3, 4, 5 BHK Apartments\n"
"Configurations", None))
        self.label_285.setText(QCoreApplication.translate("MainWindow", u"Dec, 2025\n"
"Possession Starts", None))
        self.label_286.setText(QCoreApplication.translate("MainWindow", u"716 sq.ft. - 1655 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_287.setText(QCoreApplication.translate("MainWindow", u"Silver Gardenia, Dehu-Moshi Road, Opp. D-Mart, Borhadewadi, PCMC, Pimpri Chinchwad, Pune", None))
        self.label_321.setText(QCoreApplication.translate("MainWindow", u"Namrata Prime Land", None))
        self.label_322.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_323.setText(QCoreApplication.translate("MainWindow", u"NAMRATA GROUP", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_324.setText(QCoreApplication.translate("MainWindow", u"\u20b926.37 L - 44.5 L | ", None))
        self.label_325.setText(QCoreApplication.translate("MainWindow", u"\u20b97 K/sq.ftl", None))
        self.label_326.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b913.97 K", None))
        self.label_327.setText("")
        self.label_328.setText(QCoreApplication.translate("MainWindow", u"1, 2 BHK Apartments\n"
"Configurations", None))
        self.label_329.setText(QCoreApplication.translate("MainWindow", u"Sep, 2023\n"
"Possession Starts", None))
        self.label_330.setText(QCoreApplication.translate("MainWindow", u"429 sq.ft. - 636 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_331.setText(QCoreApplication.translate("MainWindow", u"Station Road, Dnyaneshwar Nagar, Talegaon Dabhade, Pune", None))
        self.label_332.setText(QCoreApplication.translate("MainWindow", u"The Nature", None))
        self.label_333.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_334.setText(QCoreApplication.translate("MainWindow", u"MAHARASHTRA HOUSING CORPORATION", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_335.setText(QCoreApplication.translate("MainWindow", u"\u20b91.86 Cr - 2.9 Cr | ", None))
        self.label_336.setText(QCoreApplication.translate("MainWindow", u"\u20b934 K/sq.ftl", None))
        self.label_337.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b992.34 K", None))
        self.label_338.setText("")
        self.label_339.setText(QCoreApplication.translate("MainWindow", u"2 BHK Apartments\n"
"Configurations", None))
        self.label_340.setText(QCoreApplication.translate("MainWindow", u"Dec, 2025\n"
"Possession Starts", None))
        self.label_341.setText(QCoreApplication.translate("MainWindow", u"1383 sq.ft. - 3000 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_342.setText(QCoreApplication.translate("MainWindow", u"The Nature, Mukaiwadi, Pirangut Road, Pune", None))
        self.label_299.setText(QCoreApplication.translate("MainWindow", u"Ivory Heights", None))
        self.label_300.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_301.setText(QCoreApplication.translate("MainWindow", u"AAKAR REALTIES", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_302.setText(QCoreApplication.translate("MainWindow", u"\u20b934.31 L - 52.05 L | ", None))
        self.label_303.setText(QCoreApplication.translate("MainWindow", u"\u20b911.75 K/sq.ft", None))
        self.label_304.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b918.7 K", None))
        self.label_305.setText("")
        self.label_306.setText(QCoreApplication.translate("MainWindow", u"1, 1.5, 2, 2.5 BHK Apartments\n"
"Configurations", None))
        self.label_307.setText(QCoreApplication.translate("MainWindow", u"Dec, 2027\n"
"Possession Starts", None))
        self.label_308.setText(QCoreApplication.translate("MainWindow", u"486 sq.ft. - 713 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_309.setText(QCoreApplication.translate("MainWindow", u"Survey No. 34/2, 34/3, 34/4 Chovisawadi, Charholi Budruk, Pune", None))
        self.label_310.setText(QCoreApplication.translate("MainWindow", u"Dosti Greenscapes", None))
        self.label_311.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_312.setText(QCoreApplication.translate("MainWindow", u"DOSTI REALTY", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_313.setText(QCoreApplication.translate("MainWindow", u"\u20b978.5 L - 1.66 Cr | ", None))
        self.label_314.setText(QCoreApplication.translate("MainWindow", u"\u20b911.75 K/sq.ftl", None))
        self.label_315.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b938.97 K", None))
        self.label_316.setText("")
        self.label_317.setText(QCoreApplication.translate("MainWindow", u"2, 3, 4 BHK Apartments\n"
"Configurations", None))
        self.label_318.setText(QCoreApplication.translate("MainWindow", u"Dec, 2027\n"
"Possession Starts", None))
        self.label_319.setText(QCoreApplication.translate("MainWindow", u"677 sq.ft. - 1395 sq.ft..\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_320.setText(QCoreApplication.translate("MainWindow", u"Dosti Greenscapes, Hadapsar, Pune", None))
        self.label_288.setText(QCoreApplication.translate("MainWindow", u"Namrata Eco City", None))
        self.label_289.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_290.setText(QCoreApplication.translate("MainWindow", u"NAMRATA GROUP", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_291.setText(QCoreApplication.translate("MainWindow", u"\u20b925.98 L - 40.66 L | ", None))
        self.label_292.setText(QCoreApplication.translate("MainWindow", u"\u20b94.27 K/sq.ft", None))
        self.label_293.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b913.76 K", None))
        self.label_294.setText("")
        self.label_295.setText(QCoreApplication.translate("MainWindow", u"1, 2 BHK Apartments\n"
"Configurations", None))
        self.label_296.setText(QCoreApplication.translate("MainWindow", u"Ready to Move\n"
"Possession Starts", None))
        self.label_297.setText(QCoreApplication.translate("MainWindow", u"647 sq.ft. - 952 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_298.setText(QCoreApplication.translate("MainWindow", u"S. No. 27/A/1/2B/5, Varale Road, Near New D.Y. Patil College, Talegaon Dabhade, Pune", None))
        self.label_343.setText(QCoreApplication.translate("MainWindow", u"Shubharambh Clara", None))
        self.label_344.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_345.setText(QCoreApplication.translate("MainWindow", u"URBAN NEST", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_346.setText(QCoreApplication.translate("MainWindow", u"\u20b92.2 Cr - 3.41 Cr | ", None))
        self.label_347.setText(QCoreApplication.translate("MainWindow", u"\u20b99.63 K/sq.ft", None))
        self.label_348.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b935.06 K", None))
        self.label_349.setText("")
        self.label_350.setText(QCoreApplication.translate("MainWindow", u"2, 3 BHK Apartments\n"
"Configurations", None))
        self.label_351.setText(QCoreApplication.translate("MainWindow", u"Dec, 2028\n"
"Possession Starts", None))
        self.label_352.setText(QCoreApplication.translate("MainWindow", u"687 sq.ft. - 1086 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_353.setText(QCoreApplication.translate("MainWindow", u"Plot No. 76/1/1, 76/1/2, 76/1/3 And 76/1/1/1/2/1/3 At Ravet, Pimpri Chinchwad, Pune", None))
        self.label_8.setText("")
        self.plainTextEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Share Anything to us.....", None))
        self.loginbutton_2.setText(QCoreApplication.translate("MainWindow", u"Via Email", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Subject", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Share Anything to us.....", None))
        self.loginbutton.setText(QCoreApplication.translate("MainWindow", u"Via Whatsaap", None))
        self.label_57.setText("")
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"------------------------------------------------------ Customer Review ----------------------------------------------------------", None))
        self.label_2.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#9eb4b7;\">MiddleMan made selling my property effortless. </span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#9eb4b7;\">Professional, knowledgeable, and effective  - they</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#9eb4b7;\">ensured a quick sale at a great price.</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#9eb4b7;\">Highly recommended!</span></p></body></html>", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"VIKAS DUBEY", None))
        self.label_60.setText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#9eb4b7;\">MiddleMan exceeded my expectations in every way.</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#9eb4b7;\">From their expert guidance to their seamless process,</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#9eb4b7;\">selling my property was a breeze. Their team was</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#9eb4b7;\">responsive, proactive, and dedicated.</span></p></body></html>", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"ABHINESH MAHINDRAKAR", None))
        self.label_107.setText("")
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#9eb4b7;\">MiddleMan made selling my property straightforward</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#9eb4b7;\">and successful. Their team was proactive, knowledgeable,</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#9eb4b7;\">and made the entire process stress-free.</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#9eb4b7;\">I couldn't be happier with the results!</span></p></body></html>", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"ATHARVA DEVKAR", None))
        self.label_111.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffffff;\">About Us</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font"
                        "-size:11pt; color:#ffffff;\">Welcome to The </span><span style=\" font-size:11pt; font-weight:700; color:#075e54;\">Middle Man</span><span style=\" font-size:11pt; color:#ffffff;\">!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffffff;\">At The</span><span style=\" font-size:11pt; color:#075e54;\"> </span><span style=\" font-size:11pt; font-weight:700; color:#075e54;\">Middle Man</span><span style=\" font-size:11pt; color:#ffffff;\">, we believe that finding your dream property should be an exciting and seamless experience. Whether you are buying or selling, our mission is to connect you with the right opportunities through a platform that prioritizes ease, efficiency, and trust.</span></p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffffff;\">Who We Are</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffffff;\">The </span><span style=\" font-size:11pt; font-weight:700; color:#075e54;\">Middle Man</span><span style=\" font-size:11pt; color:#ffffff;\"> is a pioneering property selling application designed to bridge the gap between buyers and sellers. Our team is a dynamic blend of real estate experts, tech enthusiasts, and customer service professionals dedicated to transforming the property market.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0"
                        "px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffffff;\">Our Vision</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffffff;\">We envision a world where property transactions are straightforward, transparent, and beneficial for all parties involved. By leveraging advanced technology and user-friendly design, we aim to make property dealings as smooth as possible.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -"
                        "qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffffff;\">What We Offer?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#075e54;\">1] Comprehensive Listings</span><span style=\" font-size:11pt; font-weight:700; color:#ffffff;\"> </span><span style=\" font-size:11pt; color:#ffffff;\">: Browse through a wide array of property listings that cater to diverse needs and preferences. Our platform features detailed information and high-quality images to help you make informed decisions.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight"
                        ":700; color:#075e54;\">2] Seamless Transactions</span><span style=\" font-size:11pt; font-weight:700; color:#ffffff;\"> </span><span style=\" font-size:11pt; color:#ffffff;\">: Enjoy a streamlined process from start to finish. Our application ensures that all necessary steps, from viewing to closing, are handled efficiently and securely.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#075e54;\">3] Expert Support</span><span style=\" font-size:11pt; font-weight:700; color:#ffffff;\"> </span><span style=\" font-size:11pt; color:#ffffff;\">: Our dedicated support team is here to assist you at every stage of your property journey. Whether you have questions about a listing or need help with the buying process, we are just a click away.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0"
                        "; text-indent:0px; font-size:11pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffffff;\">Why Choose The Middle Man?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#075e54;\">1] User-Friendly Interface</span><span style=\" font-size:11pt; font-weight:700; color:#ffffff;\"> </span><span style=\" font-size:11pt; color:#ffffff;\">: Our intuitive design makes it easy to navigate the platform and find exactly what you're looking for.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#075e54;\">2] Trusted Network</span><span style=\" font-size:11pt; font-weight:700; color:#ffffff;\"> </span><span style=\" font-size:11pt; color:#ffffff;\">: We partner with reputable agents and verified sellers to ensure that every listing on our platform is genuine and reliable.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#075e54;\">3] Innovative Solutions</span><span style=\" font-size:11pt; font-weight:700; color:#ffffff;\"> </span><span style=\" font-size:11pt; color:#ffffff;\">: We continuously update our features and tools to provide you with the best possible experience.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#ffffff;\"><br /></p>\n"
"<p sty"
                        "le=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffffff;\">At The </span><span style=\" font-size:11pt; font-weight:700; color:#075e54;\">Middle Man</span><span style=\" font-size:11pt; color:#ffffff;\">, your satisfaction is our top priority. We are committed to helping you find the perfect property or sell your existing one with confidence and ease. Join us today and take the first step towards your next great investment.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffffff;\">Thank you for choosing The </span><span style=\" font-size:11pt; font-weight:700; color:#075e54;\">Middle Man</span><"
                        "span style=\" font-size:11pt; color:#ffffff;\">!</span></p></body></html>", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"--------------------------------------------------o          Why Middle Man          o---------------------------------------------------------------", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"AVOID BROKERS", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700; color:#3f3f3f;\">We directly connect you to verified</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700; color:#3f3f3f;\">owners to save brokerage</span></p></body></html>", None))
        self.label_114.setText("")
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"FREE LISTING", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700; color:#3f3f3f;\">Easy listing process. Also</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700; color:#3f3f3f;\">using Whatsapp</span></p></body></html>", None))
        self.label_120.setText("")
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"RENTAL AGREEMENT", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700; color:#3f3f3f;\">Assistance in creating Rental</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700; color:#3f3f3f;\">Agreements and Paper Work</span></p></body></html>", None))
        self.label_122.setText("")
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Short List</p><p align=\"center\"><br/></p></body></html>", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700; color:#3f3f3f;\">Assistance in creating Rental</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700; color:#3f3f3f;\">Agreements and Paper Work</span></p></body></html>", None))
        self.label_124.setText("")
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Without Visit</p></body></html>", None))
        self.label_115.setText("")
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Click a Pic or Refer owner details to </span><span style=\" font-size:22pt; font-weight:700; color:#c9eff0;\">earn upto</span><span style=\" font-size:22pt; font-weight:700; color:#ffffff;\"> </span><span style=\" font-size:22pt; font-weight:700; color:#c9eff0;\">MM 2000</span><span style=\" font-size:22pt; color:#ffffff;\"> for</span></p>\n"
"<p align=\""
                        "center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">every property listing we publish.</span></p></body></html>", None))
        self.loginbutton_3.setText(QCoreApplication.translate("MainWindow", u"Enter Owner's Details", None))
        self.label_116.setText("")
        self.loginbutton_4.setText(QCoreApplication.translate("MainWindow", u"Upload Image", None))
        self.plainTextEdit_3.setPlainText(QCoreApplication.translate("MainWindow", u"\n"
"A Refer & Earn entry is not entitled to reward for the following reasons:\n"
"\n"
"1. The house of the Owner was already listed on NoBroker.in\n"
"\n"
"2. The house of the Owner has already been rented out.\n"
"\n"
"3. The contact provided by you belongs to a Broker.", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_21), QCoreApplication.translate("MainWindow", u"I had submitted my listing, but it has been rejected. Why?                                                                      +", None))
        self.plainTextEdit_4.setPlainText(QCoreApplication.translate("MainWindow", u"To redeem your reward money:\n"
"\n"
"1. Download NoBroker App from Apple Store / Play Store\n"
"\n"
"2. Open Click & Earn Page\n"
"\n"
"3. Go to My Rewards Page\n"
"\n"
"4. Set preferred payment mode, UPI for direct credit to account, Paytm if your registered number is linked to Paytm wallet.\n"
"\n"
"5. Transfer the Amount available to redeem.", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_23), QCoreApplication.translate("MainWindow", u"How will I get the reward money?                                                                                                             +", None))
        self.plainTextEdit_5.setPlainText(QCoreApplication.translate("MainWindow", u"\n"
"Yes, you can get the reward directly in your bank account, \n"
"by setting UPI as preferred payment mode.", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_24), QCoreApplication.translate("MainWindow", u"Can I get the reward directly in my account?                                                                                            +", None))
        self.plainTextEdit_6.setPlainText(QCoreApplication.translate("MainWindow", u"\n"
"Please bear with us for some time as we are verifying your claim.\n"
"\n"
"This will be reviewed and we will get back to you ASAP.", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_22), QCoreApplication.translate("MainWindow", u"I have submitted my listing, but have not received the reward?                                                              +", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"o----------- COMMON QUESTIONS -----------o", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Raj Dhuri</p></body></html>", None))
        self.textEdit_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">The NoBroker app is very useful. I have also earned money by using the Refer &amp; Earn option. I have also earned 21000 in last 30 days with the Refer &amp; Earn option. The NoBroker company customer care is excellent at handling their customers. So I am giving them a 5-star rating.</span></p></body></html>", None))
        self.label_118.setText("")
        self.label_133.setText("")
        self.label_138.setText("")
        self.label_139.setText("")
        self.label_140.setText("")
        self.label_141.setText("")
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Sanket Jinagare</p></body></html>", None))
        self.textEdit_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Wow! I am really amazed. Refer n Earn is awesome, I really earn by just clicking pictures of To-Let boards. Even many of my friends are also earning by this. The processing of leads is very fast and me and my friends are very happy. This is a great concept.</span></p></body></html>", None))
        self.label_128.setText("")
        self.label_134.setText("")
        self.label_142.setText("")
        self.label_143.setText("")
        self.label_144.setText("")
        self.label_145.setText("")
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"Get coupan via MMcash ", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", str(self.MMcash) +  " MM cash will expire in ", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"22 Aug 2024", None))
        self.label_135.setText("")
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Gift Cards", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"My rewards", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", str(self.MMcash) + " MMcash", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"0 Card Availabe >", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"Gift Vouchers", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"Scratches card ", None))
        self.pushButton_15.setText("")
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u" MMcash", None))
        self.label_52.setText("")
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"Amazon", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"A Gift Voucher for every wishlist", None))
        self.amazonbutton.setText("")
        self.label_149.setText("")
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Domino's Pizza", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"Flat 11.5% off", None))
        self.Dominosbutton.setText("")
        self.label_152.setText("")
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"Pizza Hut", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"Flat 6.5% off", None))
        self.PizzaHutbutton.setText("")
        self.label_155.setText("")
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Flipkart", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"Flat 15% off", None))
        self.FlipkartButton.setText("")
        self.label_158.setText("")
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"Myntra", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"A Gift Voucher for every wishlist", None))
        self.Myntrabutton.setText("")
        self.label_161.setText("")
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"Zomato", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"Zomato nahi Zomaaato", None))
        self.zomatobutton.setText("")
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"---------- Redeem your rewards ----------", None))
        self.label_168.setText("")
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"Upto 30% off on\n"
"Plumbing Services", None))
        self.label_165.setText("")
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"3000 MMCash", None))
        self.label_169.setText("")
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"Upto 20% off on\n"
"Carpentry Services", None))
        self.label_171.setText("")
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"3000 MMCash", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"Upto 10% off on\n"
"AC Services", None))
        self.label_175.setText("")
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"1500 MMCash", None))
        self.label_173.setText("")
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"Upto 15% off on\n"
"Interior Designing", None))
        self.label_179.setText("")
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"1000 MMCash", None))
        self.label_177.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"NO RESULT FOUND", None))
        self.label_181.setText("")
        self.label_182.setText("")
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"Try removing some filters nad change the locality to get results", None))
        self.label_54.setText("")
        self.label_400.setText(QCoreApplication.translate("MainWindow", u"ALL\n"
"AIR CONDITIONER\n"
"SERVICES", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Notify", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Notify", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Notify", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Notify", None))
        self.groupBox_Video.setTitle("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Do you know how to Click and Earn? Get Maximum <span style=\" font-weight:700; color:#ffffff;\">MM Cash</span></p></body></html>", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"Click here to Check", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"------------------------o          MiddleMan Business Assist Plan For Builders          o------------------------", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"Get in touch with us\n"
"to Sell or Rent Your Projects", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"Click here to Check", None))
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#dcdcdc;\">For Builder Enquiries: +91 8097667158</span></p></body></html>", None))
        self.label_365.setText("")
        self.label_367.setText(QCoreApplication.translate("MainWindow", u"--------------------------o          We Make A Difference          o--------------------------", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u" BUILDER\n"
"PROJECTS", None))
        self.pushButton_17.setText("")
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"       SALE\n"
"AGREEMENTS", None))
        self.pushButton_36.setText("")
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"   HOME\n"
"INTERIORS", None))
        self.pushButton_37.setText("")
        self.label_366.setText(QCoreApplication.translate("MainWindow", u"    OUR\n"
"SERVICES", None))
        self.pushButton_38.setText("")
        self.label_368.setText(QCoreApplication.translate("MainWindow", u" \u20b9130 Cr+", None))
        self.label_372.setText(QCoreApplication.translate("MainWindow", u"Brokerage Saved\n"
"      Monthly", None))
        self.label_370.setText(QCoreApplication.translate("MainWindow", u" \u20b92 Lakh+", None))
        self.label_374.setText(QCoreApplication.translate("MainWindow", u"New Listings\n"
"    Monthly", None))
        self.label_369.setText(QCoreApplication.translate("MainWindow", u"\u20b930 Lakh+", None))
        self.label_373.setText(QCoreApplication.translate("MainWindow", u"Customers Connected\n"
"         Monthly", None))
        self.label_371.setText(QCoreApplication.translate("MainWindow", u"\u20b950 Lakh+", None))
        self.label_375.setText(QCoreApplication.translate("MainWindow", u"Our Happy\n"
"Customers", None))
        self.label_376.setText("")
        self.label_377.setText("")
        self.label_378.setText(QCoreApplication.translate("MainWindow", u"FIND A NEW HOME\n"
"ON THE GO", None))
        self.label_379.setText(QCoreApplication.translate("MainWindow", u"Download Our App", None))
        self.label_380.setText(QCoreApplication.translate("MainWindow", u"Where convinence at you fingertips", None))
        self.label_385.setText("")
        self.label_386.setText(QCoreApplication.translate("MainWindow", u"Get it on AppleStore", None))
        self.label_384.setText("")
        self.label_383.setText(QCoreApplication.translate("MainWindow", u"Get it on PlayStore", None))
        self.label_381.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Raj Dhuri</p></body></html>", None))
        self.textEdit_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">The NoBroker app is very useful. I have also earned money by using the Refer &amp; Earn option. I have also earned 21000 in last 30 days with the Refer &amp; Earn option. The NoBroker company customer care is excellent at handling their customers. So I am giving them a 5-star rating.</span></p></body></html>", None))
        self.label_382.setText("")
        self.label_387.setText("")
        self.label_388.setText("")
        self.label_389.setText("")
        self.label_390.setText("")
        self.label_391.setText("")
        self.label_392.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Sanket Jinagare</p></body></html>", None))
        self.textEdit_11.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Wow! I am really amazed. Refer n Earn is awesome, I really earn by just clicking pictures of To-Let boards. Even many of my friends are also earning by this. The processing of leads is very fast and me and my friends are very happy. This is a great concept.</span></p></body></html>", None))
        self.label_393.setText("")
        self.label_394.setText("")
        self.label_395.setText("")
        self.label_396.setText("")
        self.label_397.setText("")
        self.label_398.setText("")
        self.label_399.setText(QCoreApplication.translate("MainWindow", u"------- Testimonials -------", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Courtyard", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Ms reality", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u20b92.2 Cr - 3.41 Cr | ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u20b934 K/sq.ft", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b91.09 Lacs", None))
        self.label_13.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"2, 2.5, 3 BHK Apartments\n"
"Configurations", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Mar, 2028\n"
"Possession Starts", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"648 sq.ft. - 1004 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Opp Kalina University, Kalina, Santacruz East, Western Suburbs, Mumbai", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Liberty One", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"DOWNTOWN LIFESPACES", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u20b91.3 Cr - 2.9 Cr | ", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u20b931.53 K/sq.ft", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b963.03 K", None))
        self.label_24.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"1,2 BHK Apartments\n"
"Configurations", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"June, 2026\n"
"Possession Starts", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"529 sq.ft. - 652 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Mamletdarwadi Main Rd, Malad, Navy Colony, Kanchpada, Malad West, Mumbai", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Tathastu", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"H abd D Projects", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u20b91.2 Cr - 3.16 Cr | ", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u20b930 K/sq.ft", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b959.72 K", None))
        self.label_35.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"1, 2, 3 BHK Apartments\n"
"Configurations", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"July, 2026\n"
"Possession Starts", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"401 sq.ft. - 1054 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Tathastu 22/A, Dawood Baug, Off J.P. Rd., Andheri West, Western Suburbs, Mumbai", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"VKLAL Phase I", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"VIKYALAL INVESTMENT COMPANY", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u20b975.22 L - 88.27 L | ", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u20b934 K/sq.ftl", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b934.34 K", None))
        self.label_46.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"1 BHK Apartments\n"
"Configurations", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Dec, 2025\n"
"Possession Starts", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"332 sq.ft. - 412 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Sant Gadge Maharaj Marg, Kajupada, Borivali, Western Suburbs, Mumbai", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Rajshree Eleven", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"RAJSHREE BUILDERS", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"\u20b92.12 Cr - 4.41 Cr | ", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"\u20b91.5 L/sq.ft", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b91.25 Lacs", None))
        self.label_68.setText("")
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"2, 3 BHK Apartments\n"
"Configurations", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Ready to Move\n"
"Possession Starts", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"638 sq.ft. - 1174 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Building No. 11, Behind Siddhivinayak Mandir, off. Hingwala Lane, Ghatkopar (E), Mumbai", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Lodha Park", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"LODHA GROUP", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"\u20b93.4 Cr - 4.41 Cr | ", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"\u20b934 K/sq.ftl", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b91.64 Lacs", None))
        self.label_79.setText("")
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"3, 4 BHK Apartments\n"
"Configurations", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Dec, 2019\n"
"Possession Starts", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"2016 sq.ft. - 2421 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Opposite Hard Rock Cafe, Pandurang Budhkar Marg, Worli, Lower Parel, Mumbai", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Green Stone", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"APLITE GROUP", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"\u20b91.72 Cr - 3.06 Cr | ", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"\u20b943 K/sq.ft", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b985.39 K", None))
        self.label_90.setText("")
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"1, 2 BHK Apartments\n"
"Configurations", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Dec, 2027\n"
"Possession Starts", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"400 sq.ft. - 741 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Ramabai Ambedkar Marg, Opposite Haj House, 3rd Floor, C Wing, Fort, Mumbai", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Lashkaria Pearl", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"LAKSHARIA PEARL", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"\u20b960.0 L - 91.0 L | ", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"\u20b925.8 K/sq.ft", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b942.70 K", None))
        self.label_101.setText("")
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"1 BHK Apartments\n"
"Configurations", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Nov, 2024\n"
"Possession Starts", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"333 sq.ft. - 351 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Lashkaria Pearl, Link Road, Near Gandhi School, Oshiwara, Mumbai", None))
    # retranslateUi


if __name__ == "__main__":
        import sys
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec())
        