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
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email import encoders
from email.utils import make_msgid,formataddr
import os 
from functools import partial
import json
import pymysql as psql
import datetime
from fillpdf import fillpdfs
import random
import string
import pyautogui as pg
import ressanket_rc
import resshivam_rc

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
        self.carpentry_frame = None
        self.carpentry_frame_visible = False
        self.rates = 0
        self.add_dis = 0
        self.sub_dis = 0 
        self.subtracting = 0
        self.MMcash = 3000
#-------------------------------BACKEND------------------------------------------------------
        self.mysql()
        self.curr.execute("create table if not exists refer_earn (Email_id varchar(30),City varchar(20),contact varchar(10),Name varchar(20),property_type varchar(30),tell_us_more varchar(90));")
        self.a.commit()
#--------------------------------------------------------------------------------------------  
        self.str_value = 0
        self.scratches_zmt = 0
        self.scratches_ama = 0
        self.scratches_pizu = 0 
        self.scratches_flp = 0
        self.scratches_myn = 0
        self.scratches_domi = 0
        self.scratch_avail = 0
        self.disco = True
        self.cmb_2 = None
        self.file_path = None
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
        self.frame_carpent_cnt = 0
        self.no_of_frm = []
#-------------------------------BACKEND------------------------------------------------------    
    def mysql(self):
        self.a = psql.connect(host='localhost',port=3306,user='root',password='root',charset="utf8",database='middleman')
        self.curr = self.a.cursor()
#--------------------------------------------------------------------------------------------
    def check_carpent(self):
        item = self.label_616.text()
        print(desc)
        price = 0
        desc = 0
        if item == "Channel":
               price = 119
               desc=  "Installation or replacement of one channel set"
               
        elif item == "Cupboard H":
                price = 149
                desc = "Installation or replacement "
        elif item == "Cupboard SD":
                price = 99
                desc = "Installation or replacement of one channel set"
        else:
                print("NOthing")    # Message box    
        print(price,desc)

    def check_plumbing(self):
        item = self.label_616.text()
        print(item)
        price = 0
        desc = 0
        if item == "Wash Basin":
               price = 409
               desc=  "Installation"
        elif item == "Blockage Removal":
                price = 149
                desc = "Remove the Blockage"
        elif item == "Blockage Removal":
                price = 149
                desc = "Remove the Blockage"
        elif item == "Leakage":
                price = 99
                desc = "Remove the Blockage"    
        else:
                print("NOthing")    # Message box    
        print(price,desc)   # frame_3
                
    def plumbing_frm(self, service_de):
            if service_de == 1:
                    self.label_616.setText("Wash Basin")
                    self.label_617.setText("₹ 409")
                    self.label_618.setText("Installation")
                    self.frame_77.show()
                    self.pushButton_79.clicked.connect(self.hide_frame_77)
                    self.frame_78.hide()
                    self.frame_79.hide()
            elif service_de == 2:
                    self.label_620.setText("Blockage Removal")
                    self.label_621.setText("₹ 149")
                    self.label_622.setText("Remove")
                    self.frame_78.show()
                    self.frame_78.setGeometry(10, 140, 380, 70)
                    self.pushButton_82.clicked.connect(self.hide_frame_78)
                    self.pushButton_83.clicked.connect(self.hide_frame_79)
            elif service_de == 3:
                #     self.frame_78.show()
                    self.frame_79.show()
                    self.label_624.setText("Leakage")
                    self.label_625.setText("₹ 99")
                    self.label_626.setText("Repair")
                    self.frame_78.setGeometry(10, 140, 380, 70)
                    self.frame_79.setGeometry(10, 220, 380, 70)
                    self.pushButton_84.clicked.connect(self.hide_frame_78)
                    self.pushButton_83.clicked.connect(self.hide_frame_79)
                    self.pushButton_86.clicked.connect(self.hide_frame_79)
            else:
                    print("Nothing selected")
                    
    def hide_frame_77(self):
        self.frame_77.hide()
        self.frame_78.setGeometry(10, 60, 380, 70)
        self.frame_79.setGeometry(10, 140, 380, 70)

    def hide_frame_78(self):
        self.frame_78.hide()
        if self.frame_77.isVisible():
                self.frame_79.setGeometry(10, 140, 380, 70)
        else: 
                self.frame_79.setGeometry(10, 60, 380, 70)

    def hide_frame_79(self):
        self.frame_79.hide()

    def carpentry_adding(self, service_de):
        if service_de == 1:
                self.label_629.setText("Channel")
                self.label_630.setText("₹ 119")
                self.label_631.setText("Installation or replacement of one channel set")
                self.label_631.setGeometry(5,20,40,60)

                self.frame_83.show()
                self.pushButton_84.clicked.connect(self.frm1)
                self.frame_84.hide()
                self.frame_85.hide()
        
        elif service_de == 2:
                self.label_633.setText("Cupboard H")
                self.label_635.setGeometry(5,20,40,60)
                self.label_634.setText("₹ 149")
                self.label_635.setText("Installation or replace")
                self.frame_83.show()
                self.frame_84.show()
                self.frame_85.hide()
                self.frame_84.setGeometry(10, 140, 380, 70)
                self.pushButton_84.clicked.connect(self.frm1)
                self.pushButton_85.clicked.connect(self.frm2)
        
        elif service_de == 3:
                self.label_637.setText("Cupboard SD")
                self.label_638.setText("₹ 99")
                self.label_639.setText("Installation or replacement of one handle")
                self.label_639.setGeometry(5,20,40,60)
                self.frame_83.show()
                self.frame_84.show()
                self.frame_85.show()
                self.frame_84.setGeometry(10, 140, 380, 70)
                self.frame_85.setGeometry(10, 220, 380, 70)
                self.pushButton_84.clicked.connect(self.frm1)
                self.pushButton_85.clicked.connect(self.frm2)
                self.pushButton_86.clicked.connect(self.frm3)
        
        else:
                print("Nothing selected")
                self.frame_83.hide()
                self.frame_84.hide()
                self.frame_85.hide()


    def frm1(self):
            self.frame_83.hide()
            self.frame_84.setGeometry(10, 60, 380, 70)
            self.frame_85.setGeometry(10, 140, 380, 70)

    def frm2(self):
            self.frame_84.hide()
            if self.frame_83.isVisible():
                    self.frame_85.setGeometry(10, 140, 380, 70)
            else:
                    self.frame_85.setGeometry(10, 60, 380, 70)

    def frm3(self):
            self.frame_85.hide()

    def add_ac_ser(self, index):
        ind = index
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_6.setEnabled(True)
        self.lineEdit_7.setEnabled(True)
        self.pushButton_43.clicked.connect(lambda :self.fetch_ac_user(ind))
        line_edits = [self.lineEdit_2, self.lineEdit_4, self.lineEdit_5, self.lineEdit_6, self.lineEdit_7]

        # Check if any QLineEdit is None
        for line_edit in line_edits:
                if line_edit is None:
                        print("One of the QLineEdit objects is None.")
                        return

        # Check if any QLineEdit is empty
        for line_edit in line_edits:
                if not line_edit.text().strip():
                        print("Please fill all the fields.")
                        return
        
        # If all checks pass and index is 0, print the data
    def fetch_ac_user(self, index):
        name = self.lineEdit_4.text()
        contact = self.lineEdit_2.text()
        email = self.lineEdit_6.text()
        address = self.lineEdit_7.text()
        pin = self.lineEdit_5.text()
        if index == 0:
                service_type = "Normal AC Service"
                desc1 = """1] Servicing of AC unit, cooling coil and drain tray"""
                desc2 = """2] 3X Cooling with Jet-Pump Technology"""
                desc3 = """3] Assured warranty of 30 days"""
                payble_amt = int(364)
        elif index == 1:
                service_type = "Essential AC Service"
                desc1 = """1] Servicing of AC unit, cooling coil and drain tray"""
                desc2 = """2] 3X Cooling with Jet-Pump Technology"""
                desc3 = """3] Assured warranty of 60 days"""
                payble_amt = int(900)
        elif index  == 2:
                service_type = "Premium AC Service"
                desc1 = """1] Servicing of AC unit, cooling coil and drain tray"""
                desc2 = """2] 3X Cooling with Jet-Pump Technology"""
                desc3 = """3] Assured warranty of 120 days"""
                payble_amt = int(1200)
        elif index == 3:
                service_type = "Essential AC Service"
                desc1 = """1] Servicing of AC unit, cooling coil and drain tray"""
                desc2 = """2] 3X Cooling with Jet-Pump Technology"""
                desc3 = """3] Assured warranty of 60 days"""
                payble_amt = int(1200)
        elif index  == 4:
                service_type = "AC Inspection"
                desc1 = """1] Pre-service, Post-service checks & Installation"""
                desc2 = """2] 30 days assured warranty on installation"""
                desc3 = """3] Additional spare part cost, gas charges, mason work not included"""
                payble_amt = int(653)
        elif index  == 5:
                service_type = "AC Uninstallation"
                desc1 = """1] Pre-service, Post-service checks & Un-installation of unit"""
                desc2 = """2] Warranty not applicable on un-installation"""
                desc3 = """3] Additional spare part cost, gas charges, mason work not included"""   
                payble_amt = int(398)
        else:
                print("Service is None")

        #BACKEND
        self.mysql()
        self.curr.execute("create table if not exists user_services(service_type varchar(50),name varchar(30),contact varchar(10),Email varchar(30),Address varchar(70),PIN int,Desc1 varchar(100),Desc2 varchar(100),Desc3 varchar(100),Final_Amount int);")
        
        q = "insert into user_services values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.curr.execute(q,(service_type,name,contact,email,address,pin,desc1,desc2,desc3,payble_amt))
        self.a.commit()
#-----------------------------------------BACKEND--TO--FILL--THE--PDF--INVOICE----------------------------------------------
        username_prefix = name[:3].upper()
        random_digits = ''.join(random.choices(string.digits, k=8))
        invoice_no = f"{username_prefix}-{random_digits}"
        print(invoice_no)
        
        form_fields = list(fillpdfs.get_form_fields('NEW AC.pdf').keys())

        invoice = invoice_no
        datee = datetime.datetime.today().strftime('%d-%m-%Y')
        name = name
        addr = f"{address} - {pin}" 
        description1 = desc1
        description2 = desc2
        description3 = desc3
        price = payble_amt

        data_dict2 = {
        form_fields[0] : invoice,
        form_fields[1] : datee,
        form_fields[2] : name,
        form_fields[3] : addr,
        form_fields[4] : description1,
        form_fields[5] : description2,
        form_fields[6] : description3,
        form_fields[7] : price
        }
        print(name)
        fillpdfs.write_fillable_pdf(input_pdf_path = 'NEW AC.pdf',output_pdf_path = f'{name}.pdf',data_dict = data_dict2)
        print("done") 
#---------------------------------------------------------------------------------------------------------------------------
        print(f"Service Type: {service_type}")
        print(f"User Name: {name}")
        print(f"Contact: {contact}")
        print(f"Email: {email}")
        print(f"Address: {address}")
        print(f"PIN: {pin}")
        print(f"desc1 : {desc1}")
        print(f"desc2 : {desc2}")
        print(f"desc3 : {desc3}")
        print(f"Payble ampunt {payble_amt}")
               
    def ac_service(self,index):
        pl = self.comboBox_2.itemText(index)
        if index in [0,1,2,3,4,5]:
                self.cmb_2 = index
                self.stackedWidget.setCurrentIndex(self.cmb_2)
                self.pushButton_42.setEnabled(True)
                self.pushButton_42.clicked.connect(self.add_ac_ser)
        elif self.cmb_2 == None:
                print("select The combobx")
                self.pushButton_42.setEnabled(False)
        else:
                self.pushButton_42.setEnabled(False)
        print(pl)

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
        receiver_email = 'yadnyeshmore@gmail.com'  # Replace with actual receiver email
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
                <p>MiddleMan<br>Shaydri Nagar, Temi Pada Road, Mulund (E), Pin Code - 400078, near Ayyappa Mandir<br>middleman3701@gmail.com<br>8097667158</p>
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
                self.label_149.setPixmap(QPixmap(r"images/Dominos.png"))
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
                self.label_155.setPixmap(QPixmap(r"images/flipkart.png"))
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
                self.label_158.setPixmap(QPixmap(r"images/Myntra1.png"))
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
                self.label_152.setPixmap(QPixmap(r"images/PizzaHut.png"))
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
                self.label_182.setText(QCoreApplication.translate("self.carpentry_frame", u"My Coupon Cards", None))
                self.label_52.setText("")
                self.label_147.setText(QCoreApplication.translate("self.carpentry_frame", u"Amazon", None))
                self.label_148.setText(QCoreApplication.translate("self.carpentry_frame", u"A Gift Voucher for every wishlist", None))
                self.amazon_refer.setText(QCoreApplication.translate("self.carpentry_frame", u"Code ( 20% ): Am1250", None))
                self.label_149.setText("")
                self.label_150.setText(QCoreApplication.translate("self.carpentry_frame", u"Amazon", None))
                self.label_151.setText(QCoreApplication.translate("self.carpentry_frame", u"A Gift Voucher for every wishlist", None))
                self.dominos_refer.setText(QCoreApplication.translate("self.carpentry_frame", u"Code ( 10% ): DP2024", None))
                self.label_155.setText("")
                self.label_153.setText(QCoreApplication.translate("self.carpentry_frame", u"Amazon", None))
                self.label_154.setText(QCoreApplication.translate("self.carpentry_frame", u"A Gift Voucher for every wishlist", None))
                self.flipkart_refer.setText(QCoreApplication.translate("self.carpentry_frame", u"Code ( 20% ): FP14GC", None))
                self.label_158.setText("")
                self.label_156.setText(QCoreApplication.translate("self.carpentry_frame", u"Amazon", None))
                self.label_157.setText(QCoreApplication.translate("self.carpentry_frame", u"A Gift Voucher for every wishlist", None))
                self.myntra_refer.setText(QCoreApplication.translate("self.carpentry_frame", u"Code ( 30% ): MSale50", None))
                self.label_152.setText("")
                self.label_164.setText(QCoreApplication.translate("self.carpentry_frame", u"Amazon", None))
                self.label_165.setText(QCoreApplication.translate("self.carpentry_frame", u"A Gift Voucher for every wishlist", None))
                self.pizzahu_refer.setText(QCoreApplication.translate("self.carpentry_frame", u"Code ( 10% ): PHUT15", None))
                self.label_161.setText("")
                self.label_166.setText(QCoreApplication.translate("self.carpentry_frame", u"Amazon", None))
                self.label_167.setText(QCoreApplication.translate("self.carpentry_frame", u"A Gift Voucher for every wishlist", None))
                self.zomato_refer.setText(QCoreApplication.translate("self.carpentry_frame", u"Code ( 10% ): ZOMATO19", None))
                self.my_scratches_frame.show()
                self.amazon_frame.hide()
                self.flipkart_frame.hide()
                self.pizzahu_frame.hide()
                self.myntra_frame.hide()
                self.dominos_frame.hide()
                self.zomato_frame.hide()
                
                print("The scrtach no is ",self.scratches_ama)
                if self.scratches_ama == 1:
                        self.amazon_frame.show()
                if self.scratches_domi== 2:
                        self.dominos_frame.show()
                if self.scratches_pizu== 3:
                        self.pizzahu_frame.show()
                if self.scratches_flp== 4:
                         self.flipkart_frame.show()
                if self.scratches_myn== 5:
                        self.myntra_frame.show()
                if self.scratches_zmt== 6:
                        self.zomato_frame.show()
                
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
#-------------------------------BACKEND------------------------------------------------------
        self.mysql()
        #self.curr.execute("create table if not exists refer_earn (Email_id varchar(30),City varchar(20),contact varchar(10),Name varchar(20),property_type varchar(30),tell_us_more varchar(90));")
        #FIXED EMAIL (yadnyeshmore@gmail.com)
        q = "update refer_earn set city = %s ,contact = %s,name = %s,property_type = %s,tell_us_more = %s where email_id = 'yadnyeshmore@gmail.com';"
        self.curr.execute(q,(self.select_city_lab.text(),self.contact_number.text(),self.owner_frm.text(),self.select_prop_type.text(),self.tell_us_more.text()))
        self.a.commit()
        print("done")
#----------------------------------------------------------------------------------------------
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
        #BACKEND
        print(self.MMcash)

        self.mysql()
        q = "update scratch_earn set MMcash = %s where email_id = 'yadnyeshmore@gmail.com';"
        self.curr.execute(q,self.MMcash)
        self.a.commit()

        self.label_131.setText(QCoreApplication.translate("MainWindow", str(self.MMcash) +  " MM cash will expire in ", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", str(self.MMcash) + " MMcash", None))

        
    def confirm_uplo_image(self):
#-------------------------------BACKEND----------------------------------------------------------------
        if self.image_name_label.text() != 'imagename.png':
                selected_text = self.refer_Combobox_city.currentText()
                print(selected_text,self.image_name_label.text(),self.MMcash)
                self.mysql()
                self.curr.execute("create table if not exists upload_image (email_id varchar(50),City varchar(50),Image_name varchar(60),MMcash int)")
                q = "update upload_image set city = %s ,Image_name = %s, MMcash = %s where email_id = 'yadnyeshmore@gmail.com';"
                self.curr.execute(q,(selected_text,self.image_name_label.text(),self.MMcash))
                self.a.commit()
#----------------------------------------------------------------------------------------------------------
                self.MMcash += 2000
                self.mysql()
                q = "update scratch_earn set MMcash = %s where email_id = 'yadnyeshmore@gmail.com';"
                self.curr.execute(q,self.MMcash)
                self.a.commit()
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
                self.email_to_midd(self.file_path) # If file path is none the show the messagebx
                self.line.hide()

        
    def email_to_midd(self, file_path):
        sender_email = "middleman3701@gmail.com"
        sender_name = "Your Name"
        recipient_email = "yadnyeshmore@gmail.com"
        subject = "Exclusive Property Details"
        body = """
        <!DOCTYPE html>
        <html>
        <head>
        <style>
                .container {
                font-family: Arial, sans-serif;
                margin: 20px;
                padding: 20px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: #f9f9f9;
                }
                .header {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 10px;
                }
                .content {
                margin-bottom: 20px;
                }
                .footer {
                font-size: 14px;
                color: #555;
                }
        </style>
        </head>
        <body>
        <div class="container">
                <div class="header">
                Hi,
                </div>
                <div class="content">
                I hope you're well. I have a high-quality image of a beautiful property in <strong>[Location]</strong> available for purchase. This image is perfect for your real estate marketing needs.
                </div>
                <div class="content">
                If you're interested, please reply to this email for more details.
                </div>
                <div class="footer">
                Best regards,<br>
                Your Name
                </div>
        </div>
        </body>
        </html>
        """
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # Correct SMTP port for TLS
        sender_password = 'wtkh syvj zptd elfa'  # Your email password or app password

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = formataddr((sender_name, sender_email))
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Add the email body
        msg.attach(MIMEText(body, 'plain'))

        # Add the image attachment
        try:
                with open(file_path, "rb") as attachment:
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(attachment.read())
                        
                        encoders.encode_base64(part)
                        part.add_header(
                        "Content-Disposition",
                        f"attachment; filename= {os.path.basename(file_path)}",
                        )
                        
                        msg.attach(part)
        except Exception as e:
                print(f"Failed to attach the file: {e}")
                return

        # Send the email
        try:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, recipient_email, msg.as_string())
                server.quit()
                print("Email sent successfully!")
        except Exception as e:
                print(f"Failed to send email: {e}")

        
    def img_uplod(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg)")
        file_dialog.setViewMode(QFileDialog.List)
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            self.file_path = file_path
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
                self.mysql()
                q = "update scratch_earn set card_scratch = 'Amazon' where email_id = 'yadnyeshmore@gmail.com';"
                self.curr.execute(q)
                self.a.commit()
                pass
        elif image_name == "Dominos_by_scratch.png":
                self.Dominosbutton.setEnabled(False)
                self.scratches_domi = 2
                self.mysql()
                q = "insert into scratch_earn(card_scratch) values ('Dominos');"
                self.curr.execute(q)
                self.a.commit()


                pass
        elif image_name == "PizzaHut.png":
                self.PizzaHutbutton.setEnabled(False)
                self.scratches_pizu = 3
                self.mysql()
                q = "insert into scratch_earn(card_scratch) values ('Pizza Hut');"
                self.curr.execute(q)
                self.a.commit()

                pass
        elif image_name == "flipkart_by_scratch.png":
                self.FlipkartButton.setEnabled(False)
                self.scratches_flp = 4
                self.mysql()
                q = "insert into scratch_earn(card_scratch) values ('flipkart');"
                self.curr.execute(q)
                self.a.commit()
                pass
        elif image_name == "Myntra1_by_scratch.png":
                self.Myntrabutton.setEnabled(False)
                self.scratches_myn = 5
                self.mysql()
                q = "insert into scratch_earn(card_scratch) values ('Myntra');"
                self.curr.execute(q)
                self.a.commit()
                pass
        elif image_name == "Zomato_by_scratch.jpg":
                self.zomatobutton.setEnabled(False)
                self.scratches_zmt = 6
                self.mysql()
                q = "insert into scratch_earn(card_scratch) values ('Zomato');"
                self.curr.execute(q)
                self.a.commit()
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

                self.mysql()
                q = "update scratch_earn set MMcash = %s where email_id = 'yadnyeshmore@gmail.com';"
                self.curr.execute(q,self.MMcash)
                self.a.commit()

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
                self.scratch_avail += 1 
                self.label_136.setText(QCoreApplication.translate("MainWindow", f"{self.scratch_avail}  Card Available >",None))
                
                if self.disco:
                        self.pushButton_12.clicked.disconnect(self.noscratches_win_frame)
                        self.disco = False
                
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
                image_path = r"images/Ama.png"
                refer_code = "Am1250"
        elif Scracth1 == 2:
                head_label = "Dominos"
                image_path = r"images/Dominos_by_scratch.png"
                refer_code = "DP2024"
                
        elif Scracth1 == 3:
                head_label = "Pizza Hut"
                image_path = r"images/PizzaHut.png"
                refer_code = "PHHUT15"
                
        elif Scracth1 == 4:
                head_label = "Flipkart"
                image_path = r"images/flipkart_by_scratch.png"
                refer_code = "FP14c"
                
        elif Scracth1 == 5:
                head_label = "Myntra"
                image_path = r"images/Myntra1_by_scratch.png"
                refer_code = "MSale150"
                
        elif Scracth1 == 6:
                head_label = "Zomato"
                image_path = r'images/Zomato_by_scratch.jpg' 
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
        receiver_email = "yadnyeshmore@gmail.com"  # Replace with actual receiver email
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
        self.viawp = self.plainTextEdit.toPlainText()
        print(self.viawp)
        
        pass

    def contact_us_email(self):
        self.viawp = self.plainTextEdit.toPlainText()
        print(self.viawp)
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
        
        
    def clr_all(self):
        for i in range(self.gridLayout.count()):
            widget = self.gridLayout.itemAt(i).widget()
            if widget is not None:
                widget.show()
                
        
    def check_word_in_text(self,add_id):
        file_path = '.vscode/Mumbai.json'
        prop_id = add_id
        use_inp = self.user_local_area_vl # Example word to search for
        print(use_inp)
        try:
        # Read the JSON file
                with open(file_path, 'r') as file:
                        properties = json.load(file)

                # Assuming the first dictionary in the list contains the data
                if isinstance(properties, list) and len(properties) > 0:
                        if add_id.startswith("M"):
                                property_data = properties[0]  # Get the first dictionary
                        elif add_id.startswith("T"):
                                property_data = properties[1]
                        elif add_id.startswith("P"):
                                property_data = properties[2]
                        else:
                                print("Nothing")

                        # Fetch the value for the given ID
                        property_value = property_data.get(prop_id, None)
                        print(property_value)

                        if property_value:
                        # Print the fetched value
                                print(f"Property Value: {property_value}")

                        # Check if the word is a substring of the property value
                        text_lower = property_value.lower()
                        word_lower = use_inp.lower()
                        print(text_lower , word_lower)
                        if word_lower in text_lower:
                                frames = [self.frame, self.frame_4, self.frame_9, self.frame_8, self.frame_10, self.frame_11, self.frame_12, self.frame_13]
    
                                # Hide all frames
                                for frame in frames:
                                        frame.hide()
                                                                                
                                
                                print(f"Property ID: {prop_id}")  # Debug: Check the value of prop_id
                                
                                if prop_id == "M1":
                                        
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M1")  # Debug: Indicate which frame should be shown
                                        self.frame.show()
                                elif prop_id == "M2":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_4.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M2")  # Debug: Indicate which frame should be shown
                                        self.frame_4.show()
                                elif prop_id == "M3":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        
                                        print("Showing frame for M3")  # Debug: Indicate which frame should be shown
                                        self.frame_8.setGeometry(QRect(24, 90, 541, 91))
                                        self.frame_8.show()
                                elif prop_id == "M4":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_9.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M4")  # Debug: Indicate which frame should be shown
                                        self.frame_9.show()
                                elif prop_id == "M5":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_10.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M5")  # Debug: Indicate which frame should be shown
                                        self.frame_10.show()
                                elif prop_id == "M6":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_11.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M6")  # Debug: Indicate which frame should be shown
                                        self.frame_11.show()
                                elif prop_id == "M7":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_12.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M7")  # Debug: Indicate which frame should be shown
                                        self.frame_12.show()
                                elif prop_id == "M8":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_13.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M8")  # Debug: Indicate which frame should be shown
                                        self.frame_13.show()
                                elif prop_id == "P1":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_39.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M2")  # Debug: Indicate which frame should be shown
                                        self.frame_39.show()
                                elif prop_id == "P2":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        
                                        print("Showing frame for M3")  # Debug: Indicate which frame should be shown
                                        self.frame_40.setGeometry(QRect(24, 90, 541, 91))
                                        self.frame_40.show()
                                elif prop_id == "P3":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_41.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M4")  # Debug: Indicate which frame should be shown
                                        self.frame_41.show()
                                elif prop_id == "P4":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_42.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M5")  # Debug: Indicate which frame should be shown
                                        self.frame_42.show()
                                elif prop_id == "P5":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_11.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M6")  # Debug: Indicate which frame should be shown
                                        self.frame_11.show()
                                elif prop_id == "P6":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_44.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M7")  # Debug: Indicate which frame should be shown
                                        self.frame_44.show()
                                elif prop_id == "P7":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_45.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M8")  # Debug: Indicate which frame should be shown
                                        self.frame_45.show()
                                elif prop_id == "P8":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_46.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M8")  # Debug: Indicate which frame should be shown
                                        self.frame_46.show()
                                elif prop_id == "T1":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_35.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M2")  # Debug: Indicate which frame should be shown
                                        self.frame_35.show()
                                elif prop_id == "T2":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()

                                        print("Showing frame for M3")  # Debug: Indicate which frame should be shown
                                        self.frame_32.setGeometry(QRect(24, 90, 541, 91))
                                        self.frame_32.show()
                                elif prop_id == "T3":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_33.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M4")  # Debug: Indicate which frame should be shown
                                        self.frame_33.show()
                                elif prop_id == "T4":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_31.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M5")  # Debug: Indicate which frame should be shown
                                        self.frame_31.show()
                                elif prop_id == "T5":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_35.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M6")  # Debug: Indicate which frame should be shown
                                        self.frame_35.show()
                                elif prop_id == "T6":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_37.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M7")  # Debug: Indicate which frame should be shown
                                        self.frame_37.show()
                                elif prop_id == "T7":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_36.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M8")  # Debug: Indicate which frame should be shown
                                        self.frame_36.show()
                                elif prop_id == "T8":
                                        for i in reversed(range(self.gridLayout.count())):
                                                widget = self.gridLayout.itemAt(i).widget()
                                                if widget is not None:
                                                        widget.hide()
                                        self.frame_38.setGeometry(QRect(24, 90, 541, 91))
                                        print("Showing frame for M8")  # Debug: Indicate which frame should be shown
                                        self.frame_38.show()
                                
                                else:
                                        print("Invalid Property ID, setting default index")  # Debug: Indicate invalid prop_id
                                        self.stackedWidget_3.setCurrentIndex(6)

                        else:
                                self.stackedWidget_3.setCurrentIndex(6)
                                print(f"'{use_inp}' is not a substring of the property value.")

                else:
                        self.stackedWidget_3.setCurrentIndex(6)
                        print("The JSON file is empty or not properly formatted.")

        except FileNotFoundError:
                print(f"The file at {file_path} does not exist.")
        except json.JSONDecodeError:
                print("Error decoding JSON from the file.")

    def fetch_city_price_type(self): # This are the search Button after clicking the search button this will fetch Value
        current_index = self.stackedWidget_3.currentIndex()
        print("current vindex is ",current_index)
        number_str = str(self.actual_value)
        digits_before_decimal = len(number_str.split('.')[0])
        self.user_local_area_vl = self.lineEdit_3.text()
        # print(f"User City: {self.cmb_city}, Price: {self.actual_value}, Item Text: {self.item_text}, User Local Area: {self.user_local_area_vl}")
        if digits_before_decimal == 1:
        #     print(f"Slider value changed to {self.actual_value} Cr")
            self.actual_value = str(self.actual_value) + ("Cr")
            print(self.actual_value)
        else:
            print(self.actual_value)
            self.actucal_value = str(self.actual_value) +  ("L")
            print("Aftere the lak ",self.actual_value)
            
        
        if current_index == 18:
                print(self.cmb_city)
                if self.cmb_city == "Thane" or self.cmb_city == "Pune" or self.cmb_city == "Mumbai":
                    print(f"User City: {self.cmb_city}, Price: {self.actual_value}, Item Text: {self.item_text}, User Local Area: {self.user_local_area_vl}")
                else:
                    print("Nothing selected in the Home combobox")
        elif current_index == 19:
                self.cmb_city = "Mumbai"
                if self.item_text == " 1 BHK" or self.item_text == "  2 BHK" or self.item_text == "  3 BHK" or self.item_text == "  Others...":
                        bh1 = {'1.33Cr': 'M2',
                        '1.2Cr': 'M4',
                        '75.22L': 'M5',
                        '86L': 'M8'}

                        bh2 = {
                        '1.2Cr': 'M1',
                        '1.81Cr': 'M4',
                        '2.2Cr': 'M6',
                        '1.72Cr': 'M7'
                        }

                        bh3 = {
                        '4.5Cr': 'M3',
                        '3.16Cr': 'M4',
                        '3.32Cr': 'M6',
                        '2.58Cr': 'M7'
                        }

                        bh4 = {
                        '2.96Cr': 'M6',
                        '8.9Cr': 'M3'
                        }
                        if self.actual_value in bh1:
                           verify1 = bh1.get(self.actual_value)
                           print("Condiotn checked",verify1)
                           self.check_word_in_text(verify1)
                        elif self.actual_value in bh2:
                           verify1 = bh2.get(self.actual_value)
                           print("Condiotn checked",verify1)
                           self.check_word_in_text(verify1)
                        elif  self.actual_value in bh3:
                           verify1 = bh3.get(self.actual_value)
                           print("Condiotn checked",verify1)
                           self.check_word_in_text(verify1)
                        elif  self.actual_value in bh4:
                           verify1 = bh4.get(self.actual_value)
                           print("Condiotn checked",verify1)
                           self.check_word_in_text(verify1)  
                        else:
                                print("Condiotn not checked")
                else:
                   print(f"User City: {self.cmb_city}, Price: {self.actual_value}, Item Text: {self.item_text}, User Local Area: {self.user_local_area_vl}")     
                   print("in else") 
                
                print(f"User City: {self.cmb_city}, Price: {self.actual_value}, Item Text: {self.item_text}, User Local Area: {self.user_local_area_vl}")
                
        elif current_index == 0:
                self.cmb_city = "Thane"
                if self.item_text == " 1 BHK" or self.item_text == "  2 BHK" or self.item_text == "  3 BHK" or self.item_text == "  Others...":
                        bh1 = {
                        '78L': 'T2',
                        '36.99L': 'T3',
                        '1.1Cr': 'T4',
                        '43.5L': 'T5',
                        '43.50L': 'T6',
                        '41.1L': 'T7'
                        }

                        bh2 = {
                        '1.25Cr': 'T1',
                        '1.19Cr': 'T2',
                        '59.21L': 'T3',
                        '1.96Cr': 'T4',
                        '66L': 'T5',
                        '67L': 'T6',
                        '62.7L': 'T7',
                        '1.4Cr': 'T8'
                        }

                        bh3 = {
                        '1.89Cr': 'T1',
                        '1.69Cr': 'T2',
                        '1.96Cr': 'T8'
                        }
                        if self.actual_value in bh1:
                           verify1 = bh1.get(self.actual_value)
                           print("Condiotn checked",verify1)
                           self.check_word_in_text(verify1)
                        elif self.actual_value in bh2:
                           verify1 = bh2.get(self.actual_value)
                           print("Condiotn checked",verify1)
                           self.check_word_in_text(verify1)
                        elif  self.actual_value in bh3:
                           verify1 = bh3.get(self.actual_value)
                           print("Condiotn checked",verify1)
                           self.check_word_in_text(verify1)
                        else:
                                print("Condiotn not checked")
                else:
                   print(f"User City: {self.cmb_city}, Price: {self.actual_value}, Item Text: {self.item_text}, User Local Area: {self.user_local_area_vl}")     
                   print("in else") 
                
                print(f"User City: {self.cmb_city}, Price: {self.actual_value}, Item Text: {self.item_text}, User Local Area: {self.user_local_area_vl}")
        elif current_index == 1:
                self.cmb_city = "Pune"
                if self.item_text == " 1 BHK" or self.item_text == "  2 BHK" or self.item_text == "  3 BHK" or self.item_text == "  Others...":
                        bh1 = {'24.98L':'P2','34.31L':'P3','26.37L':'P5'}
                        bh2 = {'60L':'P1','40.66L':'P2','44.67L':'P3','78.5L':'P4','40.14L':'P5','1.86Cr':'P6','66.21L':'P7','33.52L':'P8'}
                        bh3 = {'74L':'P1','1.08Cr':'P4','96.19L':'P7'}
                        bh4 = {'41.87L':'P3','47.90L':'P3','1.66Cr':'P4','1.32Cr':'P1'}
                        print('The actual values is : ')
                        
                        if self.actual_value in bh1:
                           verify1 = bh1.get(self.actual_value)
                           print("Condiotn checked",verify1)
                           self.check_word_in_text(verify1)
                        elif self.actual_value in bh2:
                           verify1 = bh2.get(self.actual_value)
                           print("Condiotn checked",verify1)
                           self.check_word_in_text(verify1)
                        elif  self.actual_value in bh3:
                           verify1 = bh3.get(self.actual_value)
                           print("Condiotn checked",verify1)
                           self.check_word_in_text(verify1)
                        elif  self.actual_value in bh4:
                           verify1 = bh4.get(self.actual_value)
                           print("Condiotn checked",verify1)
                           self.check_word_in_text(verify1)
                        else:
                                print("Condiotn not checked")
                else:
                   print(f"User City: {self.cmb_city}, Price: {self.actual_value}, Item Text: {self.item_text}, User Local Area: {self.user_local_area_vl}")     
                   print("in else") 
                
                print(f"User City: {self.cmb_city}, Price: {self.actual_value}, Item Text: {self.item_text}, User Local Area: {self.user_local_area_vl}")
        else:
                self.stackedWidget_3.setCurrentIndex(18)
                if self.cmb_city == "Thane" or self.cmb_city == "Pune" or self.cmb_city == "Mumbai":
                    print(f"User City: {self.cmb_city}, Price: {self.actual_value}, Item Text: {self.item_text}, User Local Area: {self.user_local_area_vl}")
                    bh1 = {'1.33Cr': 'M2',
                        '1.2Cr': 'M4',
                        '75.22L': 'M5',
                        '86L': 'M8','78L': 'T2',
                        '36.99L': 'T3',
                        '1.1Cr': 'T4',
                        '43.5L': 'T5',
                        '43.50L': 'T6',
                        '41.1L': 'T7','24.98L':'P2','34.31L':'P3','26.37L':'P5'}

                    bh2 = {
                        '1.2Cr': 'M1',
                        '1.81Cr': 'M4',
                        '2.2Cr': 'M6',
                        '1.72Cr': 'M7','1.25Cr': 'T1',
                        '1.19Cr': 'T2',
                        '59.21L': 'T3',
                        '1.96Cr': 'T4',
                        '66L': 'T5',
                        '67L': 'T6',
                        '62.7L': 'T7',
                        '1.4Cr': 'T8','60L':'P1','40.66L':'P2','44.67L':'P3','78.5L':'P4','40.14L':'P5','1.86Cr':'P6','66.21L':'P7','33.52L':'P8'
                        }

                    bh3 = {
                        '4.5Cr': 'M3',
                        '3.16Cr': 'M4',
                        '3.32Cr': 'M6',
                        '2.58Cr': 'M7','1.89Cr': 'T1',
                        '1.69Cr': 'T2',
                        '1.96Cr': 'T8','74L':'P1','1.08Cr':'P4','96.19L':'P7'
                        }

                    bh4 = {
                        '2.96Cr': 'M6',
                        '8.9Cr': 'M3','41.87L':'P3','47.90L':'P3','1.66Cr':'P4','1.32Cr':'P1'
                        }
                    if self.actual_value in bh1:
                           verify1 = bh1.get(self.actual_value)
                           print("Condiotn checked",verify1)
                           self.check_word_in_text(verify1)
                    elif self.actual_value in bh2:
                       verify1 = bh2.get(self.actual_value)
                       print("Condiotn checked",verify1)
                       self.check_word_in_text(verify1)
                    elif  self.actual_value in bh3:
                       verify1 = bh3.get(self.actual_value)
                       print("Condiotn checked",verify1)
                       self.check_word_in_text(verify1)
                    elif  self.actual_value in bh4:
                       verify1 = bh4.get(self.actual_value)
                       print("Condiotn checked",verify1)
                       self.check_word_in_text(verify1)
                    else:
                            print("Condiotn not checked")
                else:
                    print("Nothing selected in the combox of the another stacked")
       
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
            self.frame_3.show()
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
        self.mysql()
        self.curr.execute("create table if not exists feedback(Email_id varchar(50),stars int)")
        q = "insert into feedback values ('yadnyeshmore@gmail.com',%s)"
        self.curr.execute(q,self.rates)
        self.a.commit()
        
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
                self.label_3 = QPushButton(self.frame)
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
                self.label.setPixmap(QPixmap(u":/shivam/PropImages/notification.png"))
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
                self.label_6.setPixmap(QPixmap(u":/shivam/PropImages/no-wifi.png"))
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
                self.pushButton.clicked.connect(lambda : self.stackedWidget_3.setCurrentIndex(18))
                # self.pushButton.clicked.connect(self.notification_frame.close())
                self.label_3.setCheckable(True)
                self.label_3.clicked.connect(lambda : self.notification_frame.hide())

                if self.intevlu:
                    self.frame_3.hide()
                    self.frame_2.hide()
                else:
                    self.frame_3.show()
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
                    self.feedback_image.setPixmap(QPixmap(u":/shivam/PropImages//MUNECOHOME-removebg-preview.png"))
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
                     self.lineEdit.setText("yadnyeshmore@gmail.com")
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
             "")     #changes
                     self.curr.execute("SELECT * from login where email_id = 'yadnyeshmore@gmail.com' ;")
                     self.result = self.curr.fetchone()
                     self.current_date = self.result[3]
                     print(self.current_date)

                     self.lineEdit_2.setText(str(self.current_date))
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
                     self.current_time = self.result[4]
                     print(self.current_time)
                     self.lineEdit_3.setText(str(self.current_time))
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
        MainWindow.resize(1529, 795)
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
"")
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
        self.pushButton_39.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(7, 94, 84);\n"
"      color:white;\n"
"text-align:left;\n"
"height:35px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u":/sanket/images/prof_pic.png", QSize(), QIcon.Normal, QIcon.Off)
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

        self.pushButton_87 = QPushButton(self.icon_name_widget)
        self.pushButton_87.setObjectName(u"pushButton_87")
        self.pushButton_87.setMinimumSize(QSize(140, 30))
        self.pushButton_87.setMaximumSize(QSize(140, 30))
        font1 = QFont()
        font1.setPointSize(11)
        self.pushButton_87.setFont(font1)
        self.pushButton_87.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(7, 94, 84);\n"
"      color:white;\n"
"text-align:left;\n"
"height:35px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/shivam/PropImages/DASHHH.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_87.setIcon(icon1)
        self.pushButton_87.setCheckable(True)
        self.pushButton_87.setAutoExclusive(True)

        self.verticalLayout_39.addWidget(self.pushButton_87, 0, Qt.AlignmentFlag.AlignRight)

        self.toolBox = QToolBox(self.icon_name_widget)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(140, 410))
        self.toolBox.setMaximumSize(QSize(140, 410))
        self.toolBox.setBaseSize(QSize(140, 0))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.toolBox.setFont(font2)
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
        self.page.setGeometry(QRect(0, 0, 140, 210))
        self.layoutWidget1 = QWidget(self.page)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 160, 121))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(15, 0, 0, 0)
        self.Dashboard_2 = QPushButton(self.layoutWidget1)
        self.Dashboard_2.setObjectName(u"Dashboard_2")
        self.Dashboard_2.setFont(font1)
        self.Dashboard_2.setStyleSheet(u"QPushButton{\n"
"      color:white;\n"
"text-align:left;\n"
"height:35px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/shivam/PropImages/location.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_2.setIcon(icon2)
        self.Dashboard_2.setIconSize(QSize(25, 25))
        self.Dashboard_2.setCheckable(True)
        self.Dashboard_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Dashboard_2)

        self.Profile_2 = QPushButton(self.layoutWidget1)
        self.Profile_2.setObjectName(u"Profile_2")
        self.Profile_2.setFont(font1)
        self.Profile_2.setStyleSheet(u"QPushButton{\n"
"      color:white;\n"
"text-align:left;\n"
"height:35px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"\n"
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
        self.Profile_2.setIcon(icon2)
        self.Profile_2.setIconSize(QSize(25, 25))
        self.Profile_2.setCheckable(True)
        self.Profile_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Profile_2)

        self.Messages_2 = QPushButton(self.layoutWidget1)
        self.Messages_2.setObjectName(u"Messages_2")
        self.Messages_2.setFont(font1)
        self.Messages_2.setStyleSheet(u"QPushButton{\n"
"      color:white;\n"
"text-align:left;\n"
"height:35px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"\n"
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
        self.Messages_2.setIcon(icon2)
        self.Messages_2.setIconSize(QSize(25, 25))
        self.Messages_2.setCheckable(True)
        self.Messages_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.Messages_2)

        icon3 = QIcon()
        icon3.addFile(u"PropImages/newhomeicom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page, icon3, u"New Project")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 140, 210))
        self.layoutWidget2 = QWidget(self.page_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(-3, 0, 142, 161))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Messages_3 = QPushButton(self.layoutWidget2)
        self.Messages_3.setObjectName(u"Messages_3")
        self.Messages_3.setFont(font1)
        self.Messages_3.setStyleSheet(u"QPushButton{\n"
"      color:white;\n"
"text-align:left;\n"
"height:35px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"}\n"
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
        icon4.addFile(u":/shivam/PropImages/washing-removebg-preview (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.Messages_3.setIcon(icon4)
        self.Messages_3.setIconSize(QSize(25, 25))
        self.Messages_3.setCheckable(True)
        self.Messages_3.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.Messages_3)

        self.Dashboard_3 = QPushButton(self.layoutWidget2)
        self.Dashboard_3.setObjectName(u"Dashboard_3")
        self.Dashboard_3.setFont(font1)
        self.Dashboard_3.setStyleSheet(u"QPushButton{\n"
"      color:white;\n"
"text-align:left;\n"
"height:35px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"}\n"
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
        icon5.addFile(u":/shivam/PropImages/paint-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_3.setIcon(icon5)
        self.Dashboard_3.setIconSize(QSize(25, 25))
        self.Dashboard_3.setCheckable(True)
        self.Dashboard_3.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.Dashboard_3)

        self.Profile_3 = QPushButton(self.layoutWidget2)
        self.Profile_3.setObjectName(u"Profile_3")
        self.Profile_3.setFont(font1)
        self.Profile_3.setStyleSheet(u"QPushButton{\n"
"      color:white;\n"
"text-align:left;\n"
"height:35px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"}\n"
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
        icon6.addFile(u":/shivam/PropImages/svg-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Profile_3.setIcon(icon6)
        self.Profile_3.setIconSize(QSize(25, 25))
        self.Profile_3.setCheckable(True)
        self.Profile_3.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.Profile_3)

        self.Dashboard_5 = QPushButton(self.layoutWidget2)
        self.Dashboard_5.setObjectName(u"Dashboard_5")
        self.Dashboard_5.setFont(font1)
        self.Dashboard_5.setStyleSheet(u"QPushButton{\n"
"      color:white;\n"
"text-align:left;\n"
"height:35px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"}\n"
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
        icon7 = QIcon()
        icon7.addFile(u":/shivam/PropImages/construction-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_5.setIcon(icon7)
        self.Dashboard_5.setIconSize(QSize(25, 25))
        self.Dashboard_5.setCheckable(True)
        self.Dashboard_5.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.Dashboard_5)

        icon8 = QIcon()
        icon8.addFile(u"C:/Users/Shivam/Downloads/ervice.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_2, icon8, u"Other Services")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 140, 210))
        self.Dashboard_6 = QPushButton(self.page_4)
        self.Dashboard_6.setObjectName(u"Dashboard_6")
        self.Dashboard_6.setGeometry(QRect(10, 0, 141, 33))
        self.Dashboard_6.setFont(font1)
        self.Dashboard_6.setStyleSheet(u"QPushButton{\n"
"      color:white;\n"
"text-align:left;\n"
"height:35px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"}\n"
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
        self.Dashboard_8.setFont(font1)
        self.Dashboard_8.setStyleSheet(u"QPushButton{\n"
"      color:white;\n"
"text-align:left;\n"
"height:35px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"}\n"
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
        icon9 = QIcon()
        icon9.addFile(u"C:/Users/Shivam/Downloads/ervice (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_4, icon9, u"Click and Earn")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 140, 210))
        self.layoutWidget_3 = QWidget(self.page_5)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(-4, -7, 160, 121))
        self.verticalLayout_22 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(15, 0, 0, 0)
        self.Dashboard_7 = QPushButton(self.layoutWidget_3)
        self.Dashboard_7.setObjectName(u"Dashboard_7")
        self.Dashboard_7.setFont(font1)
        self.Dashboard_7.setStyleSheet(u"QPushButton{\n"
"      color:white;\n"
"text-align:left;\n"
"height:35px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"}\n"
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
        icon10 = QIcon()
        icon10.addFile(u":/shivam/PropImages/rating-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Dashboard_7.setIcon(icon10)
        self.Dashboard_7.setIconSize(QSize(25, 25))
        self.Dashboard_7.setCheckable(True)
        self.Dashboard_7.setAutoExclusive(True)

        self.verticalLayout_22.addWidget(self.Dashboard_7)

        self.Profile_5 = QPushButton(self.layoutWidget_3)
        self.Profile_5.setObjectName(u"Profile_5")
        self.Profile_5.setFont(font1)
        self.Profile_5.setStyleSheet(u"QPushButton{\n"
"      color:white;\n"
"text-align:left;\n"
"height:35px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"}\n"
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
        icon11 = QIcon()
        icon11.addFile(u":/shivam/PropImages/phone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Profile_5.setIcon(icon11)
        self.Profile_5.setIconSize(QSize(30, 30))
        self.Profile_5.setCheckable(True)
        self.Profile_5.setAutoExclusive(True)

        self.verticalLayout_22.addWidget(self.Profile_5)

        self.Messages_5 = QPushButton(self.layoutWidget_3)
        self.Messages_5.setObjectName(u"Messages_5")
        self.Messages_5.setFont(font1)
        self.Messages_5.setStyleSheet(u"QPushButton{\n"
"      color:white;\n"
"text-align:left;\n"
"height:35px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"}\n"
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
        icon12.addFile(u":/shivam/PropImages/round.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Messages_5.setIcon(icon12)
        self.Messages_5.setIconSize(QSize(25, 25))
        self.Messages_5.setCheckable(True)
        self.Messages_5.setAutoExclusive(True)

        self.verticalLayout_22.addWidget(self.Messages_5)

        icon13 = QIcon()
        icon13.addFile(u"C:/Users/Shivam/Downloads/Untitled design (8).png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_5, icon13, u" Others")

        self.verticalLayout_39.addWidget(self.toolBox, 0, Qt.AlignmentFlag.AlignRight)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer)

        self.pushButton_11 = QPushButton(self.icon_name_widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"\n"
"QPushButton{\n"
"border:none;\n"
"\n"
"\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/shivam/PropImages/notification-bell.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon14)
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
        self.Menu.setIcon(icon1)
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
        icon15 = QIcon()
        icon15.addFile(u":/shivam/PropImages/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon15)
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
        self.lineEdit_3.setClearButtonEnabled(True)

        self.horizontalLayout_10.addWidget(self.lineEdit_3)

        self.pushButton_32 = QPushButton(self.widget_3)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        icon16 = QIcon()
        icon16.addFile(u"../Sidebar/slidemenubar/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_32.setIcon(icon16)

        self.horizontalLayout_10.addWidget(self.pushButton_32)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)

        self.pushButton_77 = QPushButton(self.widget_3)
        self.pushButton_77.setObjectName(u"pushButton_77")
        self.pushButton_77.setBaseSize(QSize(10, 10))
        self.pushButton_77.setStyleSheet(u"border:none;")
        icon17 = QIcon()
        icon17.addFile(u":/shivam/PropImages/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_77.setIcon(icon17)
        self.pushButton_77.setIconSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.pushButton_77)

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
        icon18 = QIcon()
        icon18.addFile(u":/shivam/PropImages/Coffe-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon18)
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
        icon19 = QIcon()
        icon19.addFile(u":/sanket/images/profile_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_33.setIcon(icon19)
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
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 1351, 2000))
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
        self.verticalLayout_37.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setContentsMargins(50, 35, -1, 60)
        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        font3 = QFont()
        font3.setFamilies([u"Sitka Banner Semibold"])
        self.frame_32.setFont(font3)
        self.frame_32.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.label_200 = QLabel(self.frame_32)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setGeometry(QRect(13, 10, 181, 33))
        font4 = QFont()
        font4.setFamilies([u"Sitka Subheading"])
        font4.setPointSize(25)
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
        font5 = QFont()
        font5.setPointSize(17)
        self.label_203.setFont(font5)
        self.label_203.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_204 = QLabel(self.frame_32)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setGeometry(QRect(467, 17, 91, 20))
        self.label_204.setFont(font1)
        self.label_204.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_205 = QLabel(self.frame_32)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setGeometry(QRect(354, 44, 151, 20))
        self.label_205.setFont(font1)
        self.label_205.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.line_52 = QFrame(self.frame_32)
        self.line_52.setObjectName(u"line_52")
        self.line_52.setGeometry(QRect(307, 99, 16, 269))
        self.line_52.setFrameShape(QFrame.Shape.VLine)
        self.line_52.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_207 = QLabel(self.frame_32)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setGeometry(QRect(377, 99, 175, 44))
        font6 = QFont()
        font6.setPointSize(12)
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
        font7 = QFont()
        font7.setPointSize(10)
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
        self.label_206.setPixmap(QPixmap(u":/shivam/PropImages/Thane/Thane-AsharMerac/Thane-2.1.Elevtion.jpg"))
        self.label_206.setScaledContents(True)

        self.gridLayout_3.addWidget(self.frame_32, 0, 1, 1, 1)

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
        self.label_215.setFont(font1)
        self.label_215.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_216 = QLabel(self.frame_33)
        self.label_216.setObjectName(u"label_216")
        self.label_216.setGeometry(QRect(354, 44, 151, 20))
        self.label_216.setFont(font1)
        self.label_216.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_217 = QLabel(self.frame_33)
        self.label_217.setObjectName(u"label_217")
        self.label_217.setGeometry(QRect(10, 99, 291, 269))
        self.label_217.setStyleSheet(u"border-radius:5px;")
        self.label_217.setPixmap(QPixmap(u":/shivam/PropImages/Thane/Thane-ShivlayaHeights/Thane-3.jpg"))
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
        self.label_270.setFont(font1)
        self.label_270.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_271 = QLabel(self.frame_38)
        self.label_271.setObjectName(u"label_271")
        self.label_271.setGeometry(QRect(354, 44, 151, 20))
        self.label_271.setFont(font1)
        self.label_271.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_272 = QLabel(self.frame_38)
        self.label_272.setObjectName(u"label_272")
        self.label_272.setGeometry(QRect(10, 99, 291, 269))
        self.label_272.setStyleSheet(u"border-radius:5px;")
        self.label_272.setPixmap(QPixmap(u":/shivam/PropImages/Thane/Thane-Balkum.Thane.west/Thane-1.jpg"))
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
        self.label_259.setFont(font1)
        self.label_259.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_260 = QLabel(self.frame_37)
        self.label_260.setObjectName(u"label_260")
        self.label_260.setGeometry(QRect(354, 44, 151, 20))
        self.label_260.setFont(font1)
        self.label_260.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_261 = QLabel(self.frame_37)
        self.label_261.setObjectName(u"label_261")
        self.label_261.setGeometry(QRect(-50, 99, 351, 269))
        self.label_261.setStyleSheet(u"border-radius:5px;")
        self.label_261.setPixmap(QPixmap(u":/shivam/PropImages/Thane/Thane-TulsiArian/Thane-6.roof.jpg"))
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
        self.label_261.raise_()
        self.label_255.raise_()
        self.label_256.raise_()
        self.label_257.raise_()
        self.pushButton_24.raise_()
        self.label_258.raise_()
        self.label_259.raise_()
        self.label_260.raise_()
        self.line_67.raise_()
        self.label_262.raise_()
        self.line_68.raise_()
        self.label_263.raise_()
        self.label_264.raise_()
        self.label_265.raise_()
        self.line_69.raise_()

        self.gridLayout_3.addWidget(self.frame_37, 3, 0, 1, 1)

        self.frame_34 = QFrame(self.frame_30)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFont(font3)
        self.frame_34.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.label_222 = QLabel(self.frame_34)
        self.label_222.setObjectName(u"label_222")
        self.label_222.setGeometry(QRect(13, 10, 171, 33))
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
        self.label_225.setFont(font5)
        self.label_225.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_226 = QLabel(self.frame_34)
        self.label_226.setObjectName(u"label_226")
        self.label_226.setGeometry(QRect(461, 17, 91, 20))
        self.label_226.setFont(font1)
        self.label_226.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_227 = QLabel(self.frame_34)
        self.label_227.setObjectName(u"label_227")
        self.label_227.setGeometry(QRect(354, 44, 141, 20))
        self.label_227.setFont(font1)
        self.label_227.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_228 = QLabel(self.frame_34)
        self.label_228.setObjectName(u"label_228")
        self.label_228.setGeometry(QRect(10, 99, 291, 269))
        self.label_228.setStyleSheet(u"border-radius:5px;")
        self.label_228.setPixmap(QPixmap(u":/shivam/PropImages/Thane/Thane-DostiHeron/Thane-4.1Elev.jpg"))
        self.label_228.setScaledContents(True)
        self.line_58 = QFrame(self.frame_34)
        self.line_58.setObjectName(u"line_58")
        self.line_58.setGeometry(QRect(307, 99, 16, 269))
        self.line_58.setFrameShape(QFrame.Shape.VLine)
        self.line_58.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_229 = QLabel(self.frame_34)
        self.label_229.setObjectName(u"label_229")
        self.label_229.setGeometry(QRect(377, 99, 175, 44))
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
        self.label_232.setFont(font7)
        self.label_232.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_60 = QFrame(self.frame_34)
        self.line_60.setObjectName(u"line_60")
        self.line_60.setGeometry(QRect(316, 279, 274, 16))
        self.line_60.setFrameShape(QFrame.Shape.HLine)
        self.line_60.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.frame_34, 1, 1, 1, 1)

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
        self.label_237.setFont(font1)
        self.label_237.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_238 = QLabel(self.frame_35)
        self.label_238.setObjectName(u"label_238")
        self.label_238.setGeometry(QRect(354, 44, 151, 20))
        self.label_238.setFont(font1)
        self.label_238.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_239 = QLabel(self.frame_35)
        self.label_239.setObjectName(u"label_239")
        self.label_239.setGeometry(QRect(10, 99, 291, 269))
        self.label_239.setStyleSheet(u"border-radius:5px;")
        self.label_239.setPixmap(QPixmap(u":/shivam/PropImages/Thane/Thane-ParijasHorizon/Thane-5.jpg"))
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
        self.label_193.setFont(font1)
        self.label_193.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_194 = QLabel(self.frame_31)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setGeometry(QRect(354, 44, 151, 20))
        self.label_194.setFont(font1)
        self.label_194.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_195 = QLabel(self.frame_31)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setGeometry(QRect(10, 99, 291, 269))
        self.label_195.setStyleSheet(u"border-radius:5px;")
        self.label_195.setPixmap(QPixmap(u":/shivam/PropImages/Thane/Thane-Balkum.Thane.west/Thane-1.jpg"))
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
        self.label_248.setFont(font1)
        self.label_248.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_249 = QLabel(self.frame_36)
        self.label_249.setObjectName(u"label_249")
        self.label_249.setGeometry(QRect(354, 44, 151, 20))
        self.label_249.setFont(font1)
        self.label_249.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_250 = QLabel(self.frame_36)
        self.label_250.setObjectName(u"label_250")
        self.label_250.setGeometry(QRect(10, 99, 291, 269))
        self.label_250.setStyleSheet(u"border-radius:5px;")
        self.label_250.setPixmap(QPixmap(u":/shivam/PropImages/WhatsApp Image 2024-07-05 at 20.01.08_33b1ab10.jpg"))
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
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 1351, 2000))
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
        self.label_358.setFont(font1)
        self.label_358.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_359 = QLabel(self.frame_46)
        self.label_359.setObjectName(u"label_359")
        self.label_359.setGeometry(QRect(354, 44, 151, 20))
        self.label_359.setFont(font1)
        self.label_359.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_360 = QLabel(self.frame_46)
        self.label_360.setObjectName(u"label_360")
        self.label_360.setGeometry(QRect(10, 99, 291, 269))
        self.label_360.setStyleSheet(u"border-radius:5px;")
        self.label_360.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Andheri.Tathastu/Mumbai-4.2-Roof.jpg"))
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
        self.label_281.setFont(font1)
        self.label_281.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_282 = QLabel(self.frame_39)
        self.label_282.setObjectName(u"label_282")
        self.label_282.setGeometry(QRect(354, 44, 151, 20))
        self.label_282.setFont(font1)
        self.label_282.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_283 = QLabel(self.frame_39)
        self.label_283.setObjectName(u"label_283")
        self.label_283.setGeometry(QRect(10, 99, 291, 269))
        self.label_283.setStyleSheet(u"border-radius:5px;")
        self.label_283.setPixmap(QPixmap(u":/shivam/PropImages/fs.jpg"))
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
        self.label_325.setFont(font1)
        self.label_325.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_326 = QLabel(self.frame_43)
        self.label_326.setObjectName(u"label_326")
        self.label_326.setGeometry(QRect(354, 44, 151, 20))
        self.label_326.setFont(font1)
        self.label_326.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_327 = QLabel(self.frame_43)
        self.label_327.setObjectName(u"label_327")
        self.label_327.setGeometry(QRect(10, 99, 291, 269))
        self.label_327.setStyleSheet(u"border-radius:5px;")
        self.label_327.setPixmap(QPixmap(u":/shivam/PropImages/namrata_prime_land-talegaon_dabhade_1-pune-namrata_group.jpg"))
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
        self.label_336.setFont(font1)
        self.label_336.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_337 = QLabel(self.frame_44)
        self.label_337.setObjectName(u"label_337")
        self.label_337.setGeometry(QRect(354, 44, 141, 20))
        self.label_337.setFont(font1)
        self.label_337.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_338 = QLabel(self.frame_44)
        self.label_338.setObjectName(u"label_338")
        self.label_338.setGeometry(QRect(10, 99, 291, 269))
        self.label_338.setPixmap(QPixmap(u":/shivam/PropImages/fs-large.jpg"))
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
        self.label_303.setFont(font1)
        self.label_303.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_304 = QLabel(self.frame_41)
        self.label_304.setObjectName(u"label_304")
        self.label_304.setGeometry(QRect(354, 44, 151, 20))
        self.label_304.setFont(font1)
        self.label_304.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_305 = QLabel(self.frame_41)
        self.label_305.setObjectName(u"label_305")
        self.label_305.setGeometry(QRect(10, 99, 291, 269))
        self.label_305.setStyleSheet(u"border-radius:5px;")
        self.label_305.setPixmap(QPixmap(u":/shivam/PropImages/ivoryonlypune.jpg"))
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
        self.label_314.setFont(font1)
        self.label_314.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_315 = QLabel(self.frame_42)
        self.label_315.setObjectName(u"label_315")
        self.label_315.setGeometry(QRect(354, 44, 151, 20))
        self.label_315.setFont(font1)
        self.label_315.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_316 = QLabel(self.frame_42)
        self.label_316.setObjectName(u"label_316")
        self.label_316.setGeometry(QRect(10, 99, 291, 269))
        self.label_316.setStyleSheet(u"border-radius:5px;")
        self.label_316.setPixmap(QPixmap(u":/shivam/PropImages/dosti_greenscapes-hadapsar-pune-dosti_realty.jpg"))
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
        self.label_292.setFont(font1)
        self.label_292.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_293 = QLabel(self.frame_40)
        self.label_293.setObjectName(u"label_293")
        self.label_293.setGeometry(QRect(354, 44, 151, 20))
        self.label_293.setFont(font1)
        self.label_293.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_294 = QLabel(self.frame_40)
        self.label_294.setObjectName(u"label_294")
        self.label_294.setGeometry(QRect(10, 99, 291, 269))
        self.label_294.setStyleSheet(u"border-radius:5px;")
        self.label_294.setPixmap(QPixmap(u":/shivam/PropImages/WhatsApp Image 2024-07-05 at 17.36.54_d9335cd8.jpg"))
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
        self.label_347.setFont(font1)
        self.label_347.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_348 = QLabel(self.frame_45)
        self.label_348.setObjectName(u"label_348")
        self.label_348.setGeometry(QRect(354, 44, 151, 20))
        self.label_348.setFont(font1)
        self.label_348.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_349 = QLabel(self.frame_45)
        self.label_349.setObjectName(u"label_349")
        self.label_349.setGeometry(QRect(10, 99, 291, 269))
        self.label_349.setStyleSheet(u"border-radius:5px;")
        self.label_349.setPixmap(QPixmap(u":/shivam/PropImages/shubharambh_clara-kiwale-pune-shubharambh_landmarks.jpg"))
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
        self.label_8.setPixmap(QPixmap(u":/shivam/PropImages/Get In Touch With Us (1).png"))
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
        self.label_2.setPixmap(QPixmap(u":/shivam/PropImages/Thane/Thane-AsharMerac/Thane-2.jpg"))
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
        self.label_60.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Ghatkopar.Rajshree/Mumbai-1.5.jpg"))
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
        self.label_107.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Ghatkopar.Rajshree/Mumbai-1.jpg"))
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
        self.scrollAreaWidgetContents_15.setGeometry(QRect(0, 0, 1351, 1500))
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
        self.label_111.setPixmap(QPixmap(u":/shivam/PropImages/Get In Touch With Us (2).png"))
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
        self.widget_19.setFont(font1)
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
        self.label_114.setPixmap(QPixmap(u":/shivam/PropImages/Talk to us (1).png"))
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
        self.label_120.setPixmap(QPixmap(u":/shivam/PropImages/Talk to us (3).png"))
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
        self.label_122.setPixmap(QPixmap(u":/shivam/PropImages/Talk to us (4).png"))
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
        self.label_124.setPixmap(QPixmap(u":/shivam/PropImages/Talk to us (5).png"))
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
        self.scrollAreaWidgetContents_14.setGeometry(QRect(0, 0, 1351, 1800))
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
        self.label_115.setPixmap(QPixmap(u":/shivam/PropImages/About Us (3).png"))
        self.label_115.setScaledContents(True)
        self.textEdit_3 = QTextEdit(self.frame_47)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(250, 380, 841, 91))
        self.textEdit_3.setStyleSheet(u"border:none;")
        self.textEdit_3.setReadOnly(True)
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
        self.label_116.setPixmap(QPixmap(u":/shivam/PropImages/About Us (2).png"))
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
        self.toolBox_2.setFont(font1)
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
        self.plainTextEdit_3.setFont(font1)
        self.plainTextEdit_3.setStyleSheet(u"color:white;")
        self.plainTextEdit_3.setReadOnly(True)
        self.toolBox_2.addItem(self.page_21, u"I had submitted my listing, but it has been rejected. Why?                                                                      +")
        self.page_23 = QWidget()
        self.page_23.setObjectName(u"page_23")
        self.page_23.setGeometry(QRect(0, 0, 100, 30))
        self.plainTextEdit_4 = QPlainTextEdit(self.page_23)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setGeometry(QRect(10, 0, 691, 251))
        self.plainTextEdit_4.setFont(font1)
        self.plainTextEdit_4.setStyleSheet(u"color:white;")
        self.plainTextEdit_4.setReadOnly(True)
        self.toolBox_2.addItem(self.page_23, u"How will I get the reward money?                                                                                                             +")
        self.page_24 = QWidget()
        self.page_24.setObjectName(u"page_24")
        self.page_24.setGeometry(QRect(0, 0, 100, 30))
        self.plainTextEdit_5 = QPlainTextEdit(self.page_24)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setGeometry(QRect(10, 0, 691, 251))
        self.plainTextEdit_5.setFont(font1)
        self.plainTextEdit_5.setStyleSheet(u"color:white")
        self.plainTextEdit_5.setReadOnly(True)
        self.toolBox_2.addItem(self.page_24, u"Can I get the reward directly in my account?                                                                                            +")
        self.page_22 = QWidget()
        self.page_22.setObjectName(u"page_22")
        self.page_22.setGeometry(QRect(0, 0, 701, 259))
        self.plainTextEdit_6 = QPlainTextEdit(self.page_22)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setGeometry(QRect(10, 0, 691, 241))
        self.plainTextEdit_6.setFont(font1)
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
        self.label_118.setPixmap(QPixmap(u":/shivam/PropImages/kisspng-computer-icons-user-profile-avatar-job-icon-5b521c56afedc0.0537187115321078627206.png"))
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
        self.label_128.setPixmap(QPixmap(u":/shivam/PropImages/kisspng-computer-icons-user-profile-avatar-job-icon-5b521c56afedc0.0537187115321078627206.png"))
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
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 1351, 1650))
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
        self.label_131.setFont(font1)
        self.label_131.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_132 = QLabel(self.frame_24)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setGeometry(QRect(240, 10, 86, 21))
        self.label_132.setFont(font1)
        self.label_132.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_135 = QLabel(self.frame_24)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setGeometry(QRect(21, 10, 21, 21))
        self.label_135.setPixmap(QPixmap(u":/shivam/PropImages/Coffe-removebg-preview.png"))
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
        self.pushButton_14.setIcon(icon18)
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
        icon20 = QIcon()
        icon20.addFile(u":/shivam/PropImages/Scracth.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon20)
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
        self.pushButton_16.setIcon(icon18)
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
        self.label_52.setPixmap(QPixmap(u":/sanket/images/Ama.png"))
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
        self.label_149.setPixmap(QPixmap(u":/sanket/images/Dominos.png"))
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
        self.label_152.setPixmap(QPixmap(u":/sanket/images/PizzaHut.png"))
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
        self.label_155.setPixmap(QPixmap(u":/sanket/images/flipkart.png"))
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
        self.label_158.setPixmap(QPixmap(u":/sanket/images/Myntra1.png"))
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
        self.label_161.setPixmap(QPixmap(u":/sanket/images/Zomato.jpg"))
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
        self.label_168.setPixmap(QPixmap(u":/shivam/PropImages/Times-When-You-Definitely-Need-a-Professional-Plumber-removebg-preview.png"))
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
        self.label_165.setFont(font1)
        self.label_165.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_165.setPixmap(QPixmap(u":/shivam/PropImages/Coffe-removebg-preview.png"))
        self.label_165.setScaledContents(True)

        self.horizontalLayout_22.addWidget(self.label_165)

        self.label_167 = QLabel(self.layoutWidget9)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setFont(font7)
        self.label_167.setStyleSheet(u"color:rgb(202, 202, 202);")

        self.horizontalLayout_22.addWidget(self.label_167)

        # self.label_166.raise_()
        # self.layoutWidget14.raise_()
        # self.label_168.raise_()
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
        self.label_169.setPixmap(QPixmap(u":/shivam/PropImages/carpentor-removebg-preview.png"))
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
        self.label_171.setFont(font1)
        self.label_171.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_171.setPixmap(QPixmap(u":/shivam/PropImages/Coffe-removebg-preview.png"))
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
        self.label_175.setFont(font1)
        self.label_175.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_175.setPixmap(QPixmap(u":/shivam/PropImages/Coffe-removebg-preview.png"))
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
        self.label_173.setPixmap(QPixmap(u":/shivam/PropImages/ACServices-removebg-preview.png"))
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
        self.label_179.setFont(font1)
        self.label_179.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_179.setPixmap(QPixmap(u":/shivam/PropImages/Coffe-removebg-preview.png"))
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
        self.label_177.setPixmap(QPixmap(u":/shivam/PropImages/pngtree-crouched-woman-painting-wall-renewal-png-image_10034990.png"))
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
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 1368, 700))
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
        self.label_181.setPixmap(QPixmap(u":/shivam/PropImages/Coffe (7).png"))
        self.label_181.setScaledContents(True)
        self.label_182 = QLabel(self.widget_31)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setGeometry(QRect(530, 70, 61, 60))
        self.label_182.setPixmap(QPixmap(u"C:/Users/Shivam/Downloads/Coffe (9).png"))
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
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, -380, 1351, 1600))
        self.scrollAreaWidgetContents_11.setMinimumSize(QSize(0, 1600))
        self.scrollAreaWidgetContents_11.setMaximumSize(QSize(16777215, 1600))
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
        self.label_54.setPixmap(QPixmap(u":/shivam/PropImages/Coffe (13).png"))
        self.label_54.setScaledContents(True)
        self.label_400 = QLabel(self.widget_35)
        self.label_400.setObjectName(u"label_400")
        self.label_400.setGeometry(QRect(540, 10, 741, 281))
        font22 = QFont()
        font22.setFamilies([u"Elephant"])
        font22.setPointSize(48)
        self.label_400.setFont(font22)
        self.label_400.setStyleSheet(u"color:rgb(249, 231, 227);")
        self.widget_36 = QWidget(self.frame_19)
        self.widget_36.setObjectName(u"widget_36")
        self.widget_36.setGeometry(QRect(30, 360, 911, 1151))
        self.widget_36.setStyleSheet(u"border:1px solid hite;")
        self.comboBox_2 = QComboBox(self.widget_36)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(15, 20, 800, 31))
        self.comboBox_2.setStyleSheet(u"background-color:rgb(225, 225, 225);\n"
"font-size:18px  black;\n"
"border:none;")
        self.pushButton_42 = QPushButton(self.widget_36)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setGeometry(QRect(825, 20, 75, 31))
        self.pushButton_42.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:rgb(18, 140, 126);\n"
"color:white;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(24, 185, 166);\n"
"color:black;\n"
"border:1px solid rgb(18, 140, 126);\n"
"}")
        self.stackedWidget = QStackedWidget(self.widget_36)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 74, 891, 1511))
        self.stackedWidget.setStyleSheet(u"border:none;\n"
"border-radius:15px;")
        self.page_25 = QWidget()
        self.page_25.setObjectName(u"page_25")
        self.verticalLayout_52 = QVBoxLayout(self.page_25)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.widget_37 = QWidget(self.page_25)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setEnabled(True)
        self.widget_37.setMinimumSize(QSize(0, 1500))
        self.widget_37.setMaximumSize(QSize(16777215, 1500))
        self.widget_37.setStyleSheet(u"")
        self.label_401 = QLabel(self.widget_37)
        self.label_401.setObjectName(u"label_401")
        self.label_401.setGeometry(QRect(10, 70, 351, 231))
        self.label_401.setStyleSheet(u"border-radius:10px;")
        self.label_401.setPixmap(QPixmap(u"PropImages/AC-Repair.jpg"))
        self.label_401.setScaledContents(True)
        self.textEdit_4 = QTextEdit(self.widget_37)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(380, 70, 481, 231))
        self.textEdit_4.setFont(font20)
        self.textEdit_4.setStyleSheet(u"border:1px solid rgb(18, 140, 126);\n"
"border-radius:0px;")
        self.widget_38 = QWidget(self.widget_37)
        self.widget_38.setObjectName(u"widget_38")
        self.widget_38.setGeometry(QRect(10, 330, 850, 280))
        self.widget_38.setStyleSheet(u"background-color:rgb(229, 229, 229);")
        self.label_403 = QLabel(self.widget_38)
        self.label_403.setObjectName(u"label_403")
        self.label_403.setGeometry(QRect(20, 80, 771, 181))
        self.label_403.setFont(font1)
        self.label_404 = QLabel(self.widget_38)
        self.label_404.setObjectName(u"label_404")
        self.label_404.setGeometry(QRect(20, 20, 741, 51))
        font23 = QFont()
        font23.setPointSize(13)
        font23.setBold(True)
        self.label_404.setFont(font23)
        self.widget_39 = QWidget(self.widget_37)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setGeometry(QRect(10, 890, 851, 161))
        self.widget_39.setStyleSheet(u"background-color:rgb(229, 229, 229);")
        self.label_405 = QLabel(self.widget_39)
        self.label_405.setObjectName(u"label_405")
        self.label_405.setGeometry(QRect(20, 60, 771, 81))
        self.label_405.setFont(font1)
        self.label_406 = QLabel(self.widget_39)
        self.label_406.setObjectName(u"label_406")
        self.label_406.setGeometry(QRect(20, 10, 741, 51))
        self.label_406.setFont(font23)
        self.label_429 = QLabel(self.widget_37)
        self.label_429.setObjectName(u"label_429")
        self.label_429.setGeometry(QRect(75, 30, 221, 30))
        font24 = QFont()
        font24.setFamilies([u"Perpetua"])
        font24.setPointSize(20)
        font24.setBold(True)
        self.label_429.setFont(font24)
        self.label_429.setStyleSheet(u"color:rgb(18, 140, 126);")
        self.layoutWidget10 = QWidget(self.widget_37)
        self.layoutWidget10.setObjectName(u"layoutWidget10")
        self.layoutWidget10.setGeometry(QRect(4, 640, 864, 203))
        self.horizontalLayout_32 = QHBoxLayout(self.layoutWidget10)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.widget_40 = QWidget(self.layoutWidget10)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setMinimumSize(QSize(211, 201))
        self.widget_40.setMaximumSize(QSize(211, 201))
        self.widget_40.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_17 = QWidget(self.widget_40)
        self.layoutWidget_17.setObjectName(u"layoutWidget_17")
        self.layoutWidget_17.setGeometry(QRect(46, 19, 118, 150))
        self.verticalLayout_53 = QVBoxLayout(self.layoutWidget_17)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_414 = QLabel(self.layoutWidget_17)
        self.label_414.setObjectName(u"label_414")
        self.label_414.setMinimumSize(QSize(100, 100))
        self.label_414.setMaximumSize(QSize(100, 100))
        self.label_414.setPixmap(QPixmap(u":/shivam/PropImages/1.png"))
        self.label_414.setScaledContents(True)

        self.verticalLayout_53.addWidget(self.label_414, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_407 = QLabel(self.layoutWidget_17)
        self.label_407.setObjectName(u"label_407")
        font25 = QFont()
        font25.setFamilies([u"Mongolian Baiti"])
        font25.setPointSize(14)
        self.label_407.setFont(font25)

        self.verticalLayout_53.addWidget(self.label_407)


        self.horizontalLayout_32.addWidget(self.widget_40)

        self.widget_41 = QWidget(self.layoutWidget10)
        self.widget_41.setObjectName(u"widget_41")
        self.widget_41.setMinimumSize(QSize(211, 201))
        self.widget_41.setMaximumSize(QSize(211, 201))
        self.widget_41.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_19 = QWidget(self.widget_41)
        self.layoutWidget_19.setObjectName(u"layoutWidget_19")
        self.layoutWidget_19.setGeometry(QRect(54, 20, 102, 150))
        self.verticalLayout_54 = QVBoxLayout(self.layoutWidget_19)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_413 = QLabel(self.layoutWidget_19)
        self.label_413.setObjectName(u"label_413")
        self.label_413.setMinimumSize(QSize(100, 100))
        self.label_413.setMaximumSize(QSize(100, 100))
        self.label_413.setPixmap(QPixmap(u":/shivam/PropImages/3.png"))
        self.label_413.setScaledContents(True)

        self.verticalLayout_54.addWidget(self.label_413)

        self.label_411 = QLabel(self.layoutWidget_19)
        self.label_411.setObjectName(u"label_411")
        self.label_411.setFont(font25)

        self.verticalLayout_54.addWidget(self.label_411)


        self.horizontalLayout_32.addWidget(self.widget_41)

        self.widget_42 = QWidget(self.layoutWidget10)
        self.widget_42.setObjectName(u"widget_42")
        self.widget_42.setMinimumSize(QSize(211, 201))
        self.widget_42.setMaximumSize(QSize(211, 201))
        self.widget_42.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_16 = QWidget(self.widget_42)
        self.layoutWidget_16.setObjectName(u"layoutWidget_16")
        self.layoutWidget_16.setGeometry(QRect(54, 20, 102, 150))
        self.verticalLayout_55 = QVBoxLayout(self.layoutWidget_16)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_415 = QLabel(self.layoutWidget_16)
        self.label_415.setObjectName(u"label_415")
        self.label_415.setMinimumSize(QSize(100, 100))
        self.label_415.setMaximumSize(QSize(100, 100))
        self.label_415.setPixmap(QPixmap(u":/shivam/PropImages/2.png"))
        self.label_415.setScaledContents(True)

        self.verticalLayout_55.addWidget(self.label_415, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_412 = QLabel(self.layoutWidget_16)
        self.label_412.setObjectName(u"label_412")
        self.label_412.setFont(font25)

        self.verticalLayout_55.addWidget(self.label_412)


        self.horizontalLayout_32.addWidget(self.widget_42)

        self.widget_43 = QWidget(self.layoutWidget10)
        self.widget_43.setObjectName(u"widget_43")
        self.widget_43.setMinimumSize(QSize(211, 201))
        self.widget_43.setMaximumSize(QSize(211, 201))
        self.widget_43.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_18 = QWidget(self.widget_43)
        self.layoutWidget_18.setObjectName(u"layoutWidget_18")
        self.layoutWidget_18.setGeometry(QRect(40, 20, 128, 150))
        self.verticalLayout_56 = QVBoxLayout(self.layoutWidget_18)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_416 = QLabel(self.layoutWidget_18)
        self.label_416.setObjectName(u"label_416")
        self.label_416.setMinimumSize(QSize(100, 100))
        self.label_416.setMaximumSize(QSize(100, 100))
        self.label_416.setPixmap(QPixmap(u":/shivam/PropImages/4.png"))
        self.label_416.setScaledContents(True)

        self.verticalLayout_56.addWidget(self.label_416, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_417 = QLabel(self.layoutWidget_18)
        self.label_417.setObjectName(u"label_417")
        self.label_417.setFont(font25)

        self.verticalLayout_56.addWidget(self.label_417)


        self.horizontalLayout_32.addWidget(self.widget_43)


        self.verticalLayout_52.addWidget(self.widget_37)

        self.stackedWidget.addWidget(self.page_25)
        self.page_26 = QWidget()
        self.page_26.setObjectName(u"page_26")
        self.horizontalLayout_34 = QHBoxLayout(self.page_26)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.widget_44 = QWidget(self.page_26)
        self.widget_44.setObjectName(u"widget_44")
        self.widget_44.setEnabled(True)
        self.widget_44.setMinimumSize(QSize(0, 1500))
        self.widget_44.setMaximumSize(QSize(16777215, 1500))
        self.widget_44.setStyleSheet(u"")
        self.label_408 = QLabel(self.widget_44)
        self.label_408.setObjectName(u"label_408")
        self.label_408.setGeometry(QRect(10, 70, 351, 231))
        self.label_408.setStyleSheet(u"border-radius:10px;")
        self.label_408.setPixmap(QPixmap(u"PropImages/AC-Repair.jpg"))
        self.label_408.setScaledContents(True)
        self.textEdit_12 = QTextEdit(self.widget_44)
        self.textEdit_12.setObjectName(u"textEdit_12")
        self.textEdit_12.setGeometry(QRect(380, 70, 481, 231))
        self.textEdit_12.setFont(font20)
        self.textEdit_12.setStyleSheet(u"border:1px solid rgb(18, 140, 126);\n"
"border-radius:0px;")
        self.label_409 = QLabel(self.widget_44)
        self.label_409.setObjectName(u"label_409")
        self.label_409.setGeometry(QRect(70, 30, 231, 30))
        self.label_409.setFont(font24)
        self.label_409.setStyleSheet(u"color:rgb(18, 140, 126);")
        self.widget_45 = QWidget(self.widget_44)
        self.widget_45.setObjectName(u"widget_45")
        self.widget_45.setGeometry(QRect(10, 330, 850, 280))
        self.widget_45.setStyleSheet(u"background-color:rgb(229, 229, 229);")
        self.label_410 = QLabel(self.widget_45)
        self.label_410.setObjectName(u"label_410")
        self.label_410.setGeometry(QRect(20, 80, 771, 181))
        self.label_410.setFont(font1)
        self.label_418 = QLabel(self.widget_45)
        self.label_418.setObjectName(u"label_418")
        self.label_418.setGeometry(QRect(20, 20, 741, 51))
        self.label_418.setFont(font23)
        self.widget_46 = QWidget(self.widget_44)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setGeometry(QRect(10, 890, 851, 161))
        self.widget_46.setStyleSheet(u"background-color:rgb(229, 229, 229);")
        self.label_419 = QLabel(self.widget_46)
        self.label_419.setObjectName(u"label_419")
        self.label_419.setGeometry(QRect(20, 60, 771, 81))
        self.label_419.setFont(font1)
        self.label_420 = QLabel(self.widget_46)
        self.label_420.setObjectName(u"label_420")
        self.label_420.setGeometry(QRect(20, 10, 741, 51))
        self.label_420.setFont(font23)
        self.layoutWidget_20 = QWidget(self.widget_44)
        self.layoutWidget_20.setObjectName(u"layoutWidget_20")
        self.layoutWidget_20.setGeometry(QRect(4, 640, 864, 203))
        self.horizontalLayout_33 = QHBoxLayout(self.layoutWidget_20)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.widget_47 = QWidget(self.layoutWidget_20)
        self.widget_47.setObjectName(u"widget_47")
        self.widget_47.setMinimumSize(QSize(211, 201))
        self.widget_47.setMaximumSize(QSize(211, 201))
        self.widget_47.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_21 = QWidget(self.widget_47)
        self.layoutWidget_21.setObjectName(u"layoutWidget_21")
        self.layoutWidget_21.setGeometry(QRect(46, 19, 118, 150))
        self.verticalLayout_57 = QVBoxLayout(self.layoutWidget_21)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_421 = QLabel(self.layoutWidget_21)
        self.label_421.setObjectName(u"label_421")
        self.label_421.setMinimumSize(QSize(100, 100))
        self.label_421.setMaximumSize(QSize(100, 100))
        self.label_421.setPixmap(QPixmap(u":/shivam/PropImages/1.png"))
        self.label_421.setScaledContents(True)

        self.verticalLayout_57.addWidget(self.label_421, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_422 = QLabel(self.layoutWidget_21)
        self.label_422.setObjectName(u"label_422")
        self.label_422.setFont(font25)

        self.verticalLayout_57.addWidget(self.label_422)


        self.horizontalLayout_33.addWidget(self.widget_47)

        self.widget_48 = QWidget(self.layoutWidget_20)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setMinimumSize(QSize(211, 201))
        self.widget_48.setMaximumSize(QSize(211, 201))
        self.widget_48.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_22 = QWidget(self.widget_48)
        self.layoutWidget_22.setObjectName(u"layoutWidget_22")
        self.layoutWidget_22.setGeometry(QRect(54, 20, 102, 150))
        self.verticalLayout_58 = QVBoxLayout(self.layoutWidget_22)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_423 = QLabel(self.layoutWidget_22)
        self.label_423.setObjectName(u"label_423")
        self.label_423.setMinimumSize(QSize(100, 100))
        self.label_423.setMaximumSize(QSize(100, 100))
        self.label_423.setPixmap(QPixmap(u":/shivam/PropImages/3.png"))
        self.label_423.setScaledContents(True)

        self.verticalLayout_58.addWidget(self.label_423)

        self.label_424 = QLabel(self.layoutWidget_22)
        self.label_424.setObjectName(u"label_424")
        self.label_424.setFont(font25)

        self.verticalLayout_58.addWidget(self.label_424)


        self.horizontalLayout_33.addWidget(self.widget_48)

        self.widget_49 = QWidget(self.layoutWidget_20)
        self.widget_49.setObjectName(u"widget_49")
        self.widget_49.setMinimumSize(QSize(211, 201))
        self.widget_49.setMaximumSize(QSize(211, 201))
        self.widget_49.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_23 = QWidget(self.widget_49)
        self.layoutWidget_23.setObjectName(u"layoutWidget_23")
        self.layoutWidget_23.setGeometry(QRect(54, 20, 102, 150))
        self.verticalLayout_59 = QVBoxLayout(self.layoutWidget_23)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_425 = QLabel(self.layoutWidget_23)
        self.label_425.setObjectName(u"label_425")
        self.label_425.setMinimumSize(QSize(100, 100))
        self.label_425.setMaximumSize(QSize(100, 100))
        self.label_425.setPixmap(QPixmap(u":/shivam/PropImages/2.png"))
        self.label_425.setScaledContents(True)

        self.verticalLayout_59.addWidget(self.label_425, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_426 = QLabel(self.layoutWidget_23)
        self.label_426.setObjectName(u"label_426")
        self.label_426.setFont(font25)

        self.verticalLayout_59.addWidget(self.label_426)


        self.horizontalLayout_33.addWidget(self.widget_49)

        self.widget_50 = QWidget(self.layoutWidget_20)
        self.widget_50.setObjectName(u"widget_50")
        self.widget_50.setMinimumSize(QSize(211, 201))
        self.widget_50.setMaximumSize(QSize(211, 201))
        self.widget_50.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_24 = QWidget(self.widget_50)
        self.layoutWidget_24.setObjectName(u"layoutWidget_24")
        self.layoutWidget_24.setGeometry(QRect(40, 20, 128, 150))
        self.verticalLayout_60 = QVBoxLayout(self.layoutWidget_24)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.label_427 = QLabel(self.layoutWidget_24)
        self.label_427.setObjectName(u"label_427")
        self.label_427.setMinimumSize(QSize(100, 100))
        self.label_427.setMaximumSize(QSize(100, 100))
        self.label_427.setPixmap(QPixmap(u":/shivam/PropImages/4.png"))
        self.label_427.setScaledContents(True)

        self.verticalLayout_60.addWidget(self.label_427, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_428 = QLabel(self.layoutWidget_24)
        self.label_428.setObjectName(u"label_428")
        self.label_428.setFont(font25)

        self.verticalLayout_60.addWidget(self.label_428)


        self.horizontalLayout_33.addWidget(self.widget_50)


        self.horizontalLayout_34.addWidget(self.widget_44)

        self.stackedWidget.addWidget(self.page_26)
        self.page_27 = QWidget()
        self.page_27.setObjectName(u"page_27")
        self.horizontalLayout_36 = QHBoxLayout(self.page_27)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.widget_51 = QWidget(self.page_27)
        self.widget_51.setObjectName(u"widget_51")
        self.widget_51.setEnabled(True)
        self.widget_51.setMinimumSize(QSize(0, 1500))
        self.widget_51.setMaximumSize(QSize(16777215, 1500))
        self.widget_51.setStyleSheet(u"")
        self.label_430 = QLabel(self.widget_51)
        self.label_430.setObjectName(u"label_430")
        self.label_430.setGeometry(QRect(10, 70, 351, 231))
        self.label_430.setStyleSheet(u"border-radius:10px;")
        self.label_430.setPixmap(QPixmap(u"PropImages/AC-Repair.jpg"))
        self.label_430.setScaledContents(True)
        self.textEdit_13 = QTextEdit(self.widget_51)
        self.textEdit_13.setObjectName(u"textEdit_13")
        self.textEdit_13.setGeometry(QRect(380, 70, 481, 231))
        self.textEdit_13.setFont(font20)
        self.textEdit_13.setStyleSheet(u"border:1px solid rgb(18, 140, 126);\n"
"border-radius:0px;")
        self.label_431 = QLabel(self.widget_51)
        self.label_431.setObjectName(u"label_431")
        self.label_431.setGeometry(QRect(70, 30, 231, 30))
        self.label_431.setFont(font24)
        self.label_431.setStyleSheet(u"color:rgb(18, 140, 126);")
        self.widget_52 = QWidget(self.widget_51)
        self.widget_52.setObjectName(u"widget_52")
        self.widget_52.setGeometry(QRect(10, 330, 850, 280))
        self.widget_52.setStyleSheet(u"background-color:rgb(229, 229, 229);")
        self.label_432 = QLabel(self.widget_52)
        self.label_432.setObjectName(u"label_432")
        self.label_432.setGeometry(QRect(20, 80, 771, 181))
        self.label_432.setFont(font1)
        self.label_433 = QLabel(self.widget_52)
        self.label_433.setObjectName(u"label_433")
        self.label_433.setGeometry(QRect(20, 20, 741, 51))
        self.label_433.setFont(font23)
        self.widget_53 = QWidget(self.widget_51)
        self.widget_53.setObjectName(u"widget_53")
        self.widget_53.setGeometry(QRect(10, 890, 851, 161))
        self.widget_53.setStyleSheet(u"background-color:rgb(229, 229, 229);")
        self.label_434 = QLabel(self.widget_53)
        self.label_434.setObjectName(u"label_434")
        self.label_434.setGeometry(QRect(20, 60, 771, 81))
        self.label_434.setFont(font1)
        self.label_435 = QLabel(self.widget_53)
        self.label_435.setObjectName(u"label_435")
        self.label_435.setGeometry(QRect(20, 10, 741, 51))
        self.label_435.setFont(font23)
        self.layoutWidget_25 = QWidget(self.widget_51)
        self.layoutWidget_25.setObjectName(u"layoutWidget_25")
        self.layoutWidget_25.setGeometry(QRect(4, 640, 864, 203))
        self.horizontalLayout_35 = QHBoxLayout(self.layoutWidget_25)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.widget_54 = QWidget(self.layoutWidget_25)
        self.widget_54.setObjectName(u"widget_54")
        self.widget_54.setMinimumSize(QSize(211, 201))
        self.widget_54.setMaximumSize(QSize(211, 201))
        self.widget_54.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_26 = QWidget(self.widget_54)
        self.layoutWidget_26.setObjectName(u"layoutWidget_26")
        self.layoutWidget_26.setGeometry(QRect(46, 19, 118, 150))
        self.verticalLayout_61 = QVBoxLayout(self.layoutWidget_26)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.label_436 = QLabel(self.layoutWidget_26)
        self.label_436.setObjectName(u"label_436")
        self.label_436.setMinimumSize(QSize(100, 100))
        self.label_436.setMaximumSize(QSize(100, 100))
        self.label_436.setPixmap(QPixmap(u":/shivam/PropImages/1.png"))
        self.label_436.setScaledContents(True)

        self.verticalLayout_61.addWidget(self.label_436, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_437 = QLabel(self.layoutWidget_26)
        self.label_437.setObjectName(u"label_437")
        self.label_437.setFont(font25)

        self.verticalLayout_61.addWidget(self.label_437)


        self.horizontalLayout_35.addWidget(self.widget_54)

        self.widget_55 = QWidget(self.layoutWidget_25)
        self.widget_55.setObjectName(u"widget_55")
        self.widget_55.setMinimumSize(QSize(211, 201))
        self.widget_55.setMaximumSize(QSize(211, 201))
        self.widget_55.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_27 = QWidget(self.widget_55)
        self.layoutWidget_27.setObjectName(u"layoutWidget_27")
        self.layoutWidget_27.setGeometry(QRect(54, 20, 102, 150))
        self.verticalLayout_62 = QVBoxLayout(self.layoutWidget_27)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.label_438 = QLabel(self.layoutWidget_27)
        self.label_438.setObjectName(u"label_438")
        self.label_438.setMinimumSize(QSize(100, 100))
        self.label_438.setMaximumSize(QSize(100, 100))
        self.label_438.setPixmap(QPixmap(u":/shivam/PropImages/3.png"))
        self.label_438.setScaledContents(True)

        self.verticalLayout_62.addWidget(self.label_438)

        self.label_439 = QLabel(self.layoutWidget_27)
        self.label_439.setObjectName(u"label_439")
        self.label_439.setFont(font25)

        self.verticalLayout_62.addWidget(self.label_439)


        self.horizontalLayout_35.addWidget(self.widget_55)

        self.widget_56 = QWidget(self.layoutWidget_25)
        self.widget_56.setObjectName(u"widget_56")
        self.widget_56.setMinimumSize(QSize(211, 201))
        self.widget_56.setMaximumSize(QSize(211, 201))
        self.widget_56.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_28 = QWidget(self.widget_56)
        self.layoutWidget_28.setObjectName(u"layoutWidget_28")
        self.layoutWidget_28.setGeometry(QRect(54, 20, 102, 150))
        self.verticalLayout_63 = QVBoxLayout(self.layoutWidget_28)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_440 = QLabel(self.layoutWidget_28)
        self.label_440.setObjectName(u"label_440")
        self.label_440.setMinimumSize(QSize(100, 100))
        self.label_440.setMaximumSize(QSize(100, 100))
        self.label_440.setPixmap(QPixmap(u":/shivam/PropImages/2.png"))
        self.label_440.setScaledContents(True)

        self.verticalLayout_63.addWidget(self.label_440, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_441 = QLabel(self.layoutWidget_28)
        self.label_441.setObjectName(u"label_441")
        self.label_441.setFont(font25)

        self.verticalLayout_63.addWidget(self.label_441)


        self.horizontalLayout_35.addWidget(self.widget_56)

        self.widget_57 = QWidget(self.layoutWidget_25)
        self.widget_57.setObjectName(u"widget_57")
        self.widget_57.setMinimumSize(QSize(211, 201))
        self.widget_57.setMaximumSize(QSize(211, 201))
        self.widget_57.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_29 = QWidget(self.widget_57)
        self.layoutWidget_29.setObjectName(u"layoutWidget_29")
        self.layoutWidget_29.setGeometry(QRect(40, 20, 128, 150))
        self.verticalLayout_64 = QVBoxLayout(self.layoutWidget_29)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label_442 = QLabel(self.layoutWidget_29)
        self.label_442.setObjectName(u"label_442")
        self.label_442.setMinimumSize(QSize(100, 100))
        self.label_442.setMaximumSize(QSize(100, 100))
        self.label_442.setPixmap(QPixmap(u":/shivam/PropImages/4.png"))
        self.label_442.setScaledContents(True)

        self.verticalLayout_64.addWidget(self.label_442, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_443 = QLabel(self.layoutWidget_29)
        self.label_443.setObjectName(u"label_443")
        self.label_443.setFont(font25)

        self.verticalLayout_64.addWidget(self.label_443)


        self.horizontalLayout_35.addWidget(self.widget_57)


        self.horizontalLayout_36.addWidget(self.widget_51)

        self.stackedWidget.addWidget(self.page_27)
        self.page_28 = QWidget()
        self.page_28.setObjectName(u"page_28")
        self.horizontalLayout_38 = QHBoxLayout(self.page_28)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.widget_58 = QWidget(self.page_28)
        self.widget_58.setObjectName(u"widget_58")
        self.widget_58.setEnabled(True)
        self.widget_58.setMinimumSize(QSize(0, 1500))
        self.widget_58.setMaximumSize(QSize(16777215, 1500))
        self.widget_58.setStyleSheet(u"")
        self.label_444 = QLabel(self.widget_58)
        self.label_444.setObjectName(u"label_444")
        self.label_444.setGeometry(QRect(10, 70, 351, 231))
        self.label_444.setStyleSheet(u"border-radius:10px;")
        self.label_444.setPixmap(QPixmap(u":/shivam/PropImages/AC-Repair.jpg"))
        self.label_444.setScaledContents(True)
        self.textEdit_14 = QTextEdit(self.widget_58)
        self.textEdit_14.setObjectName(u"textEdit_14")
        self.textEdit_14.setGeometry(QRect(380, 70, 481, 231))
        self.textEdit_14.setFont(font20)
        self.textEdit_14.setStyleSheet(u"border:1px solid rgb(18, 140, 126);\n"
"border-radius:0px;")
        self.textEdit_14.setReadOnly(True)
        self.label_445 = QLabel(self.widget_58)
        self.label_445.setObjectName(u"label_445")
        self.label_445.setGeometry(QRect(93, 30, 165, 30))
        self.label_445.setFont(font24)
        self.label_445.setStyleSheet(u"color:rgb(18, 140, 126);")
        self.widget_59 = QWidget(self.widget_58)
        self.widget_59.setObjectName(u"widget_59")
        self.widget_59.setGeometry(QRect(10, 330, 850, 280))
        self.widget_59.setStyleSheet(u"background-color:rgb(229, 229, 229);")
        self.label_446 = QLabel(self.widget_59)
        self.label_446.setObjectName(u"label_446")
        self.label_446.setGeometry(QRect(20, 80, 771, 181))
        self.label_446.setFont(font1)
        self.label_447 = QLabel(self.widget_59)
        self.label_447.setObjectName(u"label_447")
        self.label_447.setGeometry(QRect(20, 20, 741, 51))
        self.label_447.setFont(font23)
        self.widget_60 = QWidget(self.widget_58)
        self.widget_60.setObjectName(u"widget_60")
        self.widget_60.setGeometry(QRect(10, 890, 851, 161))
        self.widget_60.setStyleSheet(u"background-color:rgb(229, 229, 229);")
        self.label_448 = QLabel(self.widget_60)
        self.label_448.setObjectName(u"label_448")
        self.label_448.setGeometry(QRect(20, 60, 771, 81))
        self.label_448.setFont(font1)
        self.label_449 = QLabel(self.widget_60)
        self.label_449.setObjectName(u"label_449")
        self.label_449.setGeometry(QRect(20, 10, 741, 51))
        self.label_449.setFont(font23)
        self.layoutWidget_30 = QWidget(self.widget_58)
        self.layoutWidget_30.setObjectName(u"layoutWidget_30")
        self.layoutWidget_30.setGeometry(QRect(4, 640, 864, 203))
        self.horizontalLayout_37 = QHBoxLayout(self.layoutWidget_30)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.widget_61 = QWidget(self.layoutWidget_30)
        self.widget_61.setObjectName(u"widget_61")
        self.widget_61.setMinimumSize(QSize(211, 201))
        self.widget_61.setMaximumSize(QSize(211, 201))
        self.widget_61.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_31 = QWidget(self.widget_61)
        self.layoutWidget_31.setObjectName(u"layoutWidget_31")
        self.layoutWidget_31.setGeometry(QRect(46, 19, 118, 150))
        self.verticalLayout_65 = QVBoxLayout(self.layoutWidget_31)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_450 = QLabel(self.layoutWidget_31)
        self.label_450.setObjectName(u"label_450")
        self.label_450.setMinimumSize(QSize(100, 100))
        self.label_450.setMaximumSize(QSize(100, 100))
        self.label_450.setPixmap(QPixmap(u":/shivam/PropImages/1.png"))
        self.label_450.setScaledContents(True)

        self.verticalLayout_65.addWidget(self.label_450, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_451 = QLabel(self.layoutWidget_31)
        self.label_451.setObjectName(u"label_451")
        self.label_451.setFont(font25)

        self.verticalLayout_65.addWidget(self.label_451)


        self.horizontalLayout_37.addWidget(self.widget_61)

        self.widget_62 = QWidget(self.layoutWidget_30)
        self.widget_62.setObjectName(u"widget_62")
        self.widget_62.setMinimumSize(QSize(211, 201))
        self.widget_62.setMaximumSize(QSize(211, 201))
        self.widget_62.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_32 = QWidget(self.widget_62)
        self.layoutWidget_32.setObjectName(u"layoutWidget_32")
        self.layoutWidget_32.setGeometry(QRect(54, 20, 102, 150))
        self.verticalLayout_66 = QVBoxLayout(self.layoutWidget_32)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.label_452 = QLabel(self.layoutWidget_32)
        self.label_452.setObjectName(u"label_452")
        self.label_452.setMinimumSize(QSize(100, 100))
        self.label_452.setMaximumSize(QSize(100, 100))
        self.label_452.setPixmap(QPixmap(u":/shivam/PropImages/3.png"))
        self.label_452.setScaledContents(True)

        self.verticalLayout_66.addWidget(self.label_452)

        self.label_453 = QLabel(self.layoutWidget_32)
        self.label_453.setObjectName(u"label_453")
        self.label_453.setFont(font25)

        self.verticalLayout_66.addWidget(self.label_453)


        self.horizontalLayout_37.addWidget(self.widget_62)

        self.widget_63 = QWidget(self.layoutWidget_30)
        self.widget_63.setObjectName(u"widget_63")
        self.widget_63.setMinimumSize(QSize(211, 201))
        self.widget_63.setMaximumSize(QSize(211, 201))
        self.widget_63.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_33 = QWidget(self.widget_63)
        self.layoutWidget_33.setObjectName(u"layoutWidget_33")
        self.layoutWidget_33.setGeometry(QRect(54, 20, 102, 150))
        self.verticalLayout_67 = QVBoxLayout(self.layoutWidget_33)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.label_454 = QLabel(self.layoutWidget_33)
        self.label_454.setObjectName(u"label_454")
        self.label_454.setMinimumSize(QSize(100, 100))
        self.label_454.setMaximumSize(QSize(100, 100))
        self.label_454.setPixmap(QPixmap(u":/shivam/PropImages/2.png"))
        self.label_454.setScaledContents(True)

        self.verticalLayout_67.addWidget(self.label_454, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_455 = QLabel(self.layoutWidget_33)
        self.label_455.setObjectName(u"label_455")
        self.label_455.setFont(font25)

        self.verticalLayout_67.addWidget(self.label_455)


        self.horizontalLayout_37.addWidget(self.widget_63)

        self.widget_64 = QWidget(self.layoutWidget_30)
        self.widget_64.setObjectName(u"widget_64")
        self.widget_64.setMinimumSize(QSize(211, 201))
        self.widget_64.setMaximumSize(QSize(211, 201))
        self.widget_64.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_34 = QWidget(self.widget_64)
        self.layoutWidget_34.setObjectName(u"layoutWidget_34")
        self.layoutWidget_34.setGeometry(QRect(40, 20, 128, 150))
        self.verticalLayout_68 = QVBoxLayout(self.layoutWidget_34)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.label_456 = QLabel(self.layoutWidget_34)
        self.label_456.setObjectName(u"label_456")
        self.label_456.setMinimumSize(QSize(100, 100))
        self.label_456.setMaximumSize(QSize(100, 100))
        self.label_456.setPixmap(QPixmap(u":/shivam/PropImages/4.png"))
        self.label_456.setScaledContents(True)

        self.verticalLayout_68.addWidget(self.label_456, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_457 = QLabel(self.layoutWidget_34)
        self.label_457.setObjectName(u"label_457")
        self.label_457.setFont(font25)

        self.verticalLayout_68.addWidget(self.label_457)


        self.horizontalLayout_37.addWidget(self.widget_64)


        self.horizontalLayout_38.addWidget(self.widget_58)

        self.stackedWidget.addWidget(self.page_28)
        self.page_29 = QWidget()
        self.page_29.setObjectName(u"page_29")
        self.horizontalLayout_40 = QHBoxLayout(self.page_29)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.widget_65 = QWidget(self.page_29)
        self.widget_65.setObjectName(u"widget_65")
        self.widget_65.setEnabled(True)
        self.widget_65.setMinimumSize(QSize(0, 1500))
        self.widget_65.setMaximumSize(QSize(16777215, 1500))
        self.widget_65.setStyleSheet(u"")
        self.label_458 = QLabel(self.widget_65)
        self.label_458.setObjectName(u"label_458")
        self.label_458.setGeometry(QRect(10, 70, 351, 231))
        self.label_458.setStyleSheet(u"border-radius:10px;")
        self.label_458.setPixmap(QPixmap(u":/shivam/PropImages/AC-Repair.jpg"))
        self.label_458.setScaledContents(True)
        self.textEdit_15 = QTextEdit(self.widget_65)
        self.textEdit_15.setObjectName(u"textEdit_15")
        self.textEdit_15.setGeometry(QRect(380, 70, 481, 231))
        self.textEdit_15.setFont(font20)
        self.textEdit_15.setStyleSheet(u"border:1px solid rgb(18, 140, 126);\n"
"border-radius:0px;")
        self.label_459 = QLabel(self.widget_65)
        self.label_459.setObjectName(u"label_459")
        self.label_459.setGeometry(QRect(93, 30, 171, 30))
        self.label_459.setFont(font24)
        self.label_459.setStyleSheet(u"color:rgb(18, 140, 126);")
        self.widget_66 = QWidget(self.widget_65)
        self.widget_66.setObjectName(u"widget_66")
        self.widget_66.setGeometry(QRect(10, 330, 850, 280))
        self.widget_66.setStyleSheet(u"background-color:rgb(229, 229, 229);")
        self.label_460 = QLabel(self.widget_66)
        self.label_460.setObjectName(u"label_460")
        self.label_460.setGeometry(QRect(20, 80, 771, 181))
        self.label_460.setFont(font1)
        self.label_461 = QLabel(self.widget_66)
        self.label_461.setObjectName(u"label_461")
        self.label_461.setGeometry(QRect(20, 20, 741, 51))
        self.label_461.setFont(font23)
        self.widget_67 = QWidget(self.widget_65)
        self.widget_67.setObjectName(u"widget_67")
        self.widget_67.setGeometry(QRect(10, 890, 851, 161))
        self.widget_67.setStyleSheet(u"background-color:rgb(229, 229, 229);")
        self.label_462 = QLabel(self.widget_67)
        self.label_462.setObjectName(u"label_462")
        self.label_462.setGeometry(QRect(20, 60, 771, 81))
        self.label_462.setFont(font1)
        self.label_463 = QLabel(self.widget_67)
        self.label_463.setObjectName(u"label_463")
        self.label_463.setGeometry(QRect(20, 10, 741, 51))
        self.label_463.setFont(font23)
        self.layoutWidget_35 = QWidget(self.widget_65)
        self.layoutWidget_35.setObjectName(u"layoutWidget_35")
        self.layoutWidget_35.setGeometry(QRect(4, 640, 864, 203))
        self.horizontalLayout_39 = QHBoxLayout(self.layoutWidget_35)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.widget_68 = QWidget(self.layoutWidget_35)
        self.widget_68.setObjectName(u"widget_68")
        self.widget_68.setMinimumSize(QSize(211, 201))
        self.widget_68.setMaximumSize(QSize(211, 201))
        self.widget_68.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_36 = QWidget(self.widget_68)
        self.layoutWidget_36.setObjectName(u"layoutWidget_36")
        self.layoutWidget_36.setGeometry(QRect(46, 19, 118, 150))
        self.verticalLayout_69 = QVBoxLayout(self.layoutWidget_36)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.label_464 = QLabel(self.layoutWidget_36)
        self.label_464.setObjectName(u"label_464")
        self.label_464.setMinimumSize(QSize(100, 100))
        self.label_464.setMaximumSize(QSize(100, 100))
        self.label_464.setPixmap(QPixmap(u":/shivam/PropImages/1.png"))
        self.label_464.setScaledContents(True)

        self.verticalLayout_69.addWidget(self.label_464, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_465 = QLabel(self.layoutWidget_36)
        self.label_465.setObjectName(u"label_465")
        self.label_465.setFont(font25)

        self.verticalLayout_69.addWidget(self.label_465)


        self.horizontalLayout_39.addWidget(self.widget_68)

        self.widget_69 = QWidget(self.layoutWidget_35)
        self.widget_69.setObjectName(u"widget_69")
        self.widget_69.setMinimumSize(QSize(211, 201))
        self.widget_69.setMaximumSize(QSize(211, 201))
        self.widget_69.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_37 = QWidget(self.widget_69)
        self.layoutWidget_37.setObjectName(u"layoutWidget_37")
        self.layoutWidget_37.setGeometry(QRect(54, 20, 102, 150))
        self.verticalLayout_70 = QVBoxLayout(self.layoutWidget_37)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.label_466 = QLabel(self.layoutWidget_37)
        self.label_466.setObjectName(u"label_466")
        self.label_466.setMinimumSize(QSize(100, 100))
        self.label_466.setMaximumSize(QSize(100, 100))
        self.label_466.setPixmap(QPixmap(u":/shivam/PropImages/3.png"))
        self.label_466.setScaledContents(True)

        self.verticalLayout_70.addWidget(self.label_466)

        self.label_467 = QLabel(self.layoutWidget_37)
        self.label_467.setObjectName(u"label_467")
        self.label_467.setFont(font25)

        self.verticalLayout_70.addWidget(self.label_467)


        self.horizontalLayout_39.addWidget(self.widget_69)

        self.widget_70 = QWidget(self.layoutWidget_35)
        self.widget_70.setObjectName(u"widget_70")
        self.widget_70.setMinimumSize(QSize(211, 201))
        self.widget_70.setMaximumSize(QSize(211, 201))
        self.widget_70.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_38 = QWidget(self.widget_70)
        self.layoutWidget_38.setObjectName(u"layoutWidget_38")
        self.layoutWidget_38.setGeometry(QRect(54, 20, 102, 150))
        self.verticalLayout_71 = QVBoxLayout(self.layoutWidget_38)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.label_468 = QLabel(self.layoutWidget_38)
        self.label_468.setObjectName(u"label_468")
        self.label_468.setMinimumSize(QSize(100, 100))
        self.label_468.setMaximumSize(QSize(100, 100))
        self.label_468.setPixmap(QPixmap(u":/shivam/PropImages/2.png"))
        self.label_468.setScaledContents(True)

        self.verticalLayout_71.addWidget(self.label_468, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_469 = QLabel(self.layoutWidget_38)
        self.label_469.setObjectName(u"label_469")
        self.label_469.setFont(font25)

        self.verticalLayout_71.addWidget(self.label_469)


        self.horizontalLayout_39.addWidget(self.widget_70)

        self.widget_71 = QWidget(self.layoutWidget_35)
        self.widget_71.setObjectName(u"widget_71")
        self.widget_71.setMinimumSize(QSize(211, 201))
        self.widget_71.setMaximumSize(QSize(211, 201))
        self.widget_71.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_39 = QWidget(self.widget_71)
        self.layoutWidget_39.setObjectName(u"layoutWidget_39")
        self.layoutWidget_39.setGeometry(QRect(40, 20, 128, 150))
        self.verticalLayout_72 = QVBoxLayout(self.layoutWidget_39)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.label_470 = QLabel(self.layoutWidget_39)
        self.label_470.setObjectName(u"label_470")
        self.label_470.setMinimumSize(QSize(100, 100))
        self.label_470.setMaximumSize(QSize(100, 100))
        self.label_470.setPixmap(QPixmap(u":/shivam/PropImages/4.png"))
        self.label_470.setScaledContents(True)

        self.verticalLayout_72.addWidget(self.label_470, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_471 = QLabel(self.layoutWidget_39)
        self.label_471.setObjectName(u"label_471")
        self.label_471.setFont(font25)

        self.verticalLayout_72.addWidget(self.label_471)


        self.horizontalLayout_39.addWidget(self.widget_71)


        self.horizontalLayout_40.addWidget(self.widget_65)

        self.stackedWidget.addWidget(self.page_29)
        self.page_30 = QWidget()
        self.page_30.setObjectName(u"page_30")
        self.horizontalLayout_42 = QHBoxLayout(self.page_30)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.widget_72 = QWidget(self.page_30)
        self.widget_72.setObjectName(u"widget_72")
        self.widget_72.setEnabled(True)
        self.widget_72.setMinimumSize(QSize(0, 1500))
        self.widget_72.setMaximumSize(QSize(16777215, 1500))
        self.widget_72.setStyleSheet(u"")
        self.label_472 = QLabel(self.widget_72)
        self.label_472.setObjectName(u"label_472")
        self.label_472.setGeometry(QRect(10, 70, 351, 231))
        self.label_472.setStyleSheet(u"border-radius:10px;")
        self.label_472.setPixmap(QPixmap(u"PropImages/AC-Repair.jpg"))
        self.label_472.setScaledContents(True)
        self.textEdit_16 = QTextEdit(self.widget_72)
        self.textEdit_16.setObjectName(u"textEdit_16")
        self.textEdit_16.setGeometry(QRect(380, 70, 481, 231))
        self.textEdit_16.setFont(font20)
        self.textEdit_16.setStyleSheet(u"border:1px solid rgb(18, 140, 126);\n"
"border-radius:0px;")
        self.label_473 = QLabel(self.widget_72)
        self.label_473.setObjectName(u"label_473")
        self.label_473.setGeometry(QRect(80, 30, 211, 30))
        self.label_473.setFont(font24)
        self.label_473.setStyleSheet(u"color:rgb(18, 140, 126);")
        self.widget_73 = QWidget(self.widget_72)
        self.widget_73.setObjectName(u"widget_73")
        self.widget_73.setGeometry(QRect(10, 330, 850, 280))
        self.widget_73.setStyleSheet(u"background-color:rgb(229, 229, 229);")
        self.label_474 = QLabel(self.widget_73)
        self.label_474.setObjectName(u"label_474")
        self.label_474.setGeometry(QRect(20, 80, 771, 181))
        self.label_474.setFont(font1)
        self.label_475 = QLabel(self.widget_73)
        self.label_475.setObjectName(u"label_475")
        self.label_475.setGeometry(QRect(20, 20, 741, 51))
        self.label_475.setFont(font23)
        self.widget_74 = QWidget(self.widget_72)
        self.widget_74.setObjectName(u"widget_74")
        self.widget_74.setGeometry(QRect(10, 890, 851, 161))
        self.widget_74.setStyleSheet(u"background-color:rgb(229, 229, 229);")
        self.label_476 = QLabel(self.widget_74)
        self.label_476.setObjectName(u"label_476")
        self.label_476.setGeometry(QRect(20, 60, 771, 81))
        self.label_476.setFont(font1)
        self.label_477 = QLabel(self.widget_74)
        self.label_477.setObjectName(u"label_477")
        self.label_477.setGeometry(QRect(20, 10, 741, 51))
        self.label_477.setFont(font23)
        self.layoutWidget_40 = QWidget(self.widget_72)
        self.layoutWidget_40.setObjectName(u"layoutWidget_40")
        self.layoutWidget_40.setGeometry(QRect(4, 640, 864, 203))
        self.horizontalLayout_41 = QHBoxLayout(self.layoutWidget_40)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.widget_75 = QWidget(self.layoutWidget_40)
        self.widget_75.setObjectName(u"widget_75")
        self.widget_75.setMinimumSize(QSize(211, 201))
        self.widget_75.setMaximumSize(QSize(211, 201))
        self.widget_75.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_41 = QWidget(self.widget_75)
        self.layoutWidget_41.setObjectName(u"layoutWidget_41")
        self.layoutWidget_41.setGeometry(QRect(46, 19, 118, 150))
        self.verticalLayout_73 = QVBoxLayout(self.layoutWidget_41)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.label_478 = QLabel(self.layoutWidget_41)
        self.label_478.setObjectName(u"label_478")
        self.label_478.setMinimumSize(QSize(100, 100))
        self.label_478.setMaximumSize(QSize(100, 100))
        self.label_478.setPixmap(QPixmap(u":/shivam/PropImages/1.png"))
        self.label_478.setScaledContents(True)

        self.verticalLayout_73.addWidget(self.label_478, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_479 = QLabel(self.layoutWidget_41)
        self.label_479.setObjectName(u"label_479")
        self.label_479.setFont(font25)

        self.verticalLayout_73.addWidget(self.label_479)


        self.horizontalLayout_41.addWidget(self.widget_75)

        self.widget_76 = QWidget(self.layoutWidget_40)
        self.widget_76.setObjectName(u"widget_76")
        self.widget_76.setMinimumSize(QSize(211, 201))
        self.widget_76.setMaximumSize(QSize(211, 201))
        self.widget_76.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_42 = QWidget(self.widget_76)
        self.layoutWidget_42.setObjectName(u"layoutWidget_42")
        self.layoutWidget_42.setGeometry(QRect(54, 20, 102, 150))
        self.verticalLayout_74 = QVBoxLayout(self.layoutWidget_42)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.label_480 = QLabel(self.layoutWidget_42)
        self.label_480.setObjectName(u"label_480")
        self.label_480.setMinimumSize(QSize(100, 100))
        self.label_480.setMaximumSize(QSize(100, 100))
        self.label_480.setPixmap(QPixmap(u":/shivam/PropImages/3.png"))
        self.label_480.setScaledContents(True)

        self.verticalLayout_74.addWidget(self.label_480)

        self.label_481 = QLabel(self.layoutWidget_42)
        self.label_481.setObjectName(u"label_481")
        self.label_481.setFont(font25)

        self.verticalLayout_74.addWidget(self.label_481)


        self.horizontalLayout_41.addWidget(self.widget_76)

        self.widget_77 = QWidget(self.layoutWidget_40)
        self.widget_77.setObjectName(u"widget_77")
        self.widget_77.setMinimumSize(QSize(211, 201))
        self.widget_77.setMaximumSize(QSize(211, 201))
        self.widget_77.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_43 = QWidget(self.widget_77)
        self.layoutWidget_43.setObjectName(u"layoutWidget_43")
        self.layoutWidget_43.setGeometry(QRect(54, 20, 102, 150))
        self.verticalLayout_75 = QVBoxLayout(self.layoutWidget_43)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.label_482 = QLabel(self.layoutWidget_43)
        self.label_482.setObjectName(u"label_482")
        self.label_482.setMinimumSize(QSize(100, 100))
        self.label_482.setMaximumSize(QSize(100, 100))
        self.label_482.setPixmap(QPixmap(u":/shivam/PropImages/2.png"))
        self.label_482.setScaledContents(True)

        self.verticalLayout_75.addWidget(self.label_482, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_483 = QLabel(self.layoutWidget_43)
        self.label_483.setObjectName(u"label_483")
        self.label_483.setFont(font25)

        self.verticalLayout_75.addWidget(self.label_483)


        self.horizontalLayout_41.addWidget(self.widget_77)

        self.widget_78 = QWidget(self.layoutWidget_40)
        self.widget_78.setObjectName(u"widget_78")
        self.widget_78.setMinimumSize(QSize(211, 201))
        self.widget_78.setMaximumSize(QSize(211, 201))
        self.widget_78.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:100px;")
        self.layoutWidget_44 = QWidget(self.widget_78)
        self.layoutWidget_44.setObjectName(u"layoutWidget_44")
        self.layoutWidget_44.setGeometry(QRect(40, 20, 128, 150))
        self.verticalLayout_76 = QVBoxLayout(self.layoutWidget_44)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.label_484 = QLabel(self.layoutWidget_44)
        self.label_484.setObjectName(u"label_484")
        self.label_484.setMinimumSize(QSize(100, 100))
        self.label_484.setMaximumSize(QSize(100, 100))
        self.label_484.setPixmap(QPixmap(u":/shivam/PropImages/4.png"))
        self.label_484.setScaledContents(True)

        self.verticalLayout_76.addWidget(self.label_484, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_485 = QLabel(self.layoutWidget_44)
        self.label_485.setObjectName(u"label_485")
        self.label_485.setFont(font25)

        self.verticalLayout_76.addWidget(self.label_485)


        self.horizontalLayout_41.addWidget(self.widget_78)


        self.horizontalLayout_42.addWidget(self.widget_72)

        self.stackedWidget.addWidget(self.page_30)
        self.widget_79 = QWidget(self.frame_19)
        self.widget_79.setObjectName(u"widget_79")
        self.widget_79.setGeometry(QRect(950, 360, 380, 491))
        self.widget_79.setStyleSheet(u"")
        self.label_402 = QLabel(self.widget_79)
        self.label_402.setObjectName(u"label_402")
        self.label_402.setGeometry(QRect(30, 30, 321, 31))
        font26 = QFont()
        font26.setPointSize(13)
        self.label_402.setFont(font26)
        self.label_402.setStyleSheet(u"border:none;\n"
"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.pushButton_43 = QPushButton(self.widget_79)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setGeometry(QRect(110, 430, 161, 30))
        self.pushButton_43.setStyleSheet(u"QPushButton\n"
"{background-color: rgb(18, 139, 126);\n"
"border-radius:10px;\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(35, 47, 49);\n"
"	border:1px solid rgb(18, 140, 126);\n"
"	color:white;\n"
"}")
        self.layoutWidget11 = QWidget(self.widget_79)
        self.layoutWidget11.setObjectName(u"layoutWidget11")
        self.layoutWidget11.setGeometry(QRect(40, 100, 302, 297))
        self.verticalLayout_77 = QVBoxLayout(self.layoutWidget11)
        self.verticalLayout_77.setSpacing(30)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_4 = QLineEdit(self.layoutWidget11)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(300, 35))
        self.lineEdit_4.setMaximumSize(QSize(300, 35))
        self.lineEdit_4.setBaseSize(QSize(0, 35))
        self.lineEdit_4.setStyleSheet(u"QLineEdit\n"
"{background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:none;\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"border-bottom:2px solid rgb(18, 140, 126);\n"
"}")

        self.verticalLayout_77.addWidget(self.lineEdit_4)

        self.lineEdit_2 = QLineEdit(self.layoutWidget11)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(300, 35))
        self.lineEdit_2.setMaximumSize(QSize(300, 35))
        self.lineEdit_2.setBaseSize(QSize(0, 35))
        self.lineEdit_2.setStyleSheet(u"QLineEdit\n"
"{background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:none;\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"border-bottom:2px solid rgb(18, 140, 126);\n"
"}")

        self.verticalLayout_77.addWidget(self.lineEdit_2)

        self.lineEdit_6 = QLineEdit(self.layoutWidget11)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(300, 35))
        self.lineEdit_6.setMaximumSize(QSize(300, 35))
        self.lineEdit_6.setBaseSize(QSize(0, 35))
        self.lineEdit_6.setStyleSheet(u"QLineEdit\n"
"{background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:none;\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"border-bottom:2px solid rgb(18, 140, 126);\n"
"}")

        self.verticalLayout_77.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.layoutWidget11)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(300, 35))
        self.lineEdit_7.setMaximumSize(QSize(300, 35))
        self.lineEdit_7.setBaseSize(QSize(0, 35))
        self.lineEdit_7.setStyleSheet(u"QLineEdit\n"
"{background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:none;\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"border-bottom:2px solid rgb(18, 140, 126);\n"
"}")

        self.verticalLayout_77.addWidget(self.lineEdit_7)

        self.lineEdit_5 = QLineEdit(self.layoutWidget11)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(300, 35))
        self.lineEdit_5.setMaximumSize(QSize(300, 35))
        self.lineEdit_5.setBaseSize(QSize(0, 35))
        self.lineEdit_5.setStyleSheet(u"QLineEdit\n"
"{background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:none;\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"border-bottom:2px solid rgb(18, 140, 126);\n"
"}")

        self.verticalLayout_77.addWidget(self.lineEdit_5)

        self.label_486 = QLabel(self.frame_19)
        self.label_486.setObjectName(u"label_486")
        self.label_486.setGeometry(QRect(951, 870, 381, 40))
        self.label_486.setFont(font26)
        self.label_486.setStyleSheet(u"\n"
"background-color: rgb(198, 198, 198);\n"
"border-radius:10px;")
        self.pushButton_44 = QPushButton(self.frame_19)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setGeometry(QRect(1080, 950, 220, 91))
        self.pushButton_44.setMinimumSize(QSize(220, 91))
        self.pushButton_44.setMaximumSize(QSize(220, 91))
        self.pushButton_44.setFont(font20)
        self.pushButton_44.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.pushButton_45 = QPushButton(self.frame_19)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setGeometry(QRect(1080, 1060, 220, 91))
        self.pushButton_45.setMinimumSize(QSize(220, 91))
        self.pushButton_45.setMaximumSize(QSize(220, 91))
        self.pushButton_45.setFont(font1)
        self.pushButton_45.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.pushButton_46 = QPushButton(self.frame_19)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setGeometry(QRect(1080, 1170, 220, 91))
        self.pushButton_46.setMinimumSize(QSize(220, 91))
        self.pushButton_46.setMaximumSize(QSize(220, 91))
        self.pushButton_46.setFont(font1)
        self.pushButton_46.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.pushButton_47 = QPushButton(self.frame_19)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setGeometry(QRect(1080, 1280, 220, 91))
        self.pushButton_47.setMinimumSize(QSize(220, 91))
        self.pushButton_47.setMaximumSize(QSize(220, 91))
        self.pushButton_47.setFont(font1)
        self.pushButton_47.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.pushButton_48 = QPushButton(self.frame_19)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setGeometry(QRect(1080, 1390, 220, 91))
        self.pushButton_48.setMinimumSize(QSize(220, 91))
        self.pushButton_48.setMaximumSize(QSize(220, 91))
        self.pushButton_48.setFont(font1)
        self.pushButton_48.setStyleSheet(u"background-color: rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.label_487 = QLabel(self.frame_19)
        self.label_487.setObjectName(u"label_487")
        self.label_487.setGeometry(QRect(980, 950, 90, 91))
        self.label_487.setStyleSheet(u"border:3px solid rgb(18, 139, 126);\n"
"border-radius:10px;\n"
"background:none;")
        self.label_487.setPixmap(QPixmap(u":/shivam/PropImages/washing-removebg-preview (1).png"))
        self.label_487.setScaledContents(True)
        self.label_488 = QLabel(self.frame_19)
        self.label_488.setObjectName(u"label_488")
        self.label_488.setGeometry(QRect(980, 1060, 90, 91))
        self.label_488.setStyleSheet(u"border:3px solid rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.label_488.setPixmap(QPixmap(u":/shivam/PropImages/paint-removebg-preview.png"))
        self.label_488.setScaledContents(True)
        self.label_489 = QLabel(self.frame_19)
        self.label_489.setObjectName(u"label_489")
        self.label_489.setGeometry(QRect(980, 1170, 90, 91))
        self.label_489.setStyleSheet(u"border:3px solid rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.label_489.setPixmap(QPixmap(u":/shivam/PropImages/construction-removebg-preview.png"))
        self.label_489.setScaledContents(True)
        self.label_490 = QLabel(self.frame_19)
        self.label_490.setObjectName(u"label_490")
        self.label_490.setGeometry(QRect(980, 1280, 90, 91))
        self.label_490.setStyleSheet(u"border:3px solid rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.label_490.setPixmap(QPixmap(u":/shivam/PropImages/note-removebg-preview.png"))
        self.label_490.setScaledContents(True)
        self.label_491 = QLabel(self.frame_19)
        self.label_491.setObjectName(u"label_491")
        self.label_491.setGeometry(QRect(980, 1390, 90, 91))
        self.label_491.setStyleSheet(u"border:3px solid rgb(18, 140, 126);\n"
"border-radius:10px;")
        self.label_491.setPixmap(QPixmap(u":/shivam/PropImages/tenant.png"))
        self.label_491.setScaledContents(True)
        self.line_15 = QFrame(self.frame_19)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setGeometry(QRect(940, 840, 431, 1))
        self.line_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_15.setFrameShape(QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

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
"    background:rgb(7, 94, 84);\n"
" }")
        self.scrollArea_12.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_12.setWidgetResizable(True)
        self.scrollAreaWidgetContents_12 = QWidget()
        self.scrollAreaWidgetContents_12.setObjectName(u"scrollAreaWidgetContents_12")
        self.scrollAreaWidgetContents_12.setGeometry(QRect(0, -4200, 1351, 5200))
        self.scrollAreaWidgetContents_12.setMinimumSize(QSize(0, 5200))
        self.scrollAreaWidgetContents_12.setMaximumSize(QSize(16777215, 5200))
        self.verticalLayout_34 = QVBoxLayout(self.scrollAreaWidgetContents_12)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.scrollAreaWidgetContents_12)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 3000))
        self.frame_20.setStyleSheet(u"")
        self.widget_80 = QWidget(self.frame_20)
        self.widget_80.setObjectName(u"widget_80")
        self.widget_80.setGeometry(QRect(30, 30, 1300, 300))
        self.widget_80.setStyleSheet(u"background-color: rgb(18, 140, 126);")
        self.label_55 = QLabel(self.widget_80)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(80, 0, 331, 321))
        self.label_55.setPixmap(QPixmap(u":/shivam/PropImages/Coffe (15).png"))
        self.label_55.setScaledContents(True)
        self.label_492 = QLabel(self.widget_80)
        self.label_492.setObjectName(u"label_492")
        self.label_492.setGeometry(QRect(501, 14, 551, 271))
        font27 = QFont()
        font27.setFamilies([u"Elephant"])
        font27.setPointSize(54)
        self.label_492.setFont(font27)
        self.label_492.setStyleSheet(u"color:rgb(249, 231, 227);")
        self.widget_81 = QWidget(self.frame_20)
        self.widget_81.setObjectName(u"widget_81")
        self.widget_81.setGeometry(QRect(-110, 350, 1035, 1531))
        self.widget_81.setStyleSheet(u"")
        self.label_493 = QLabel(self.widget_81)
        self.label_493.setObjectName(u"label_493")
        self.label_493.setGeometry(QRect(142, 10, 221, 41))
        font28 = QFont()
        font28.setPointSize(15)
        font28.setBold(True)
        font28.setUnderline(False)
        self.label_493.setFont(font28)
        self.label_493.setStyleSheet(u"border:none; color:white;")
        self.frame_59 = QFrame(self.widget_81)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setGeometry(QRect(140, 60, 1020, 211))
        self.frame_59.setStyleSheet(u"border:none;")
        self.frame_59.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Shadow.Raised)
        self.label_495 = QLabel(self.frame_59)
        self.label_495.setObjectName(u"label_495")
        self.label_495.setGeometry(QRect(-30, -60, 1051, 311))
        self.label_495.setStyleSheet(u"border:none;")
        self.label_495.setPixmap(QPixmap(u":/shivam/PropImages/Drawer.jpg"))
        self.label_495.setScaledContents(True)
        self.widget_82 = QWidget(self.widget_81)
        self.widget_82.setObjectName(u"widget_82")
        self.widget_82.setGeometry(QRect(140, 280, 1021, 1321))
        self.widget_82.setStyleSheet(u"background-color: rgb(229, 229, 229);\n"
"border-radius:15px;")
        self.widget_83 = QWidget(self.widget_82)
        self.widget_83.setObjectName(u"widget_83")
        self.widget_83.setGeometry(QRect(0, 0, 1021, 250))
        self.widget_83.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_49 = QPushButton(self.widget_83)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setGeometry(QRect(760, 110, 81, 31))
        font29 = QFont()
        font29.setBold(True)
        self.pushButton_49.setFont(font29)
        self.pushButton_49.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_17 = QTextEdit(self.widget_83)
        self.textEdit_17.setObjectName(u"textEdit_17")
        self.textEdit_17.setGeometry(QRect(60, 40, 551, 171))
        self.textEdit_17.setStyleSheet(u"border:none;")
        self.textEdit_17.setReadOnly(True)
        self.widget_84 = QWidget(self.widget_82)
        self.widget_84.setObjectName(u"widget_84")
        self.widget_84.setGeometry(QRect(0, 250, 1021, 250))
        self.widget_84.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_54 = QPushButton(self.widget_84)
        self.pushButton_54.setObjectName(u"pushButton_54")
        self.pushButton_54.setGeometry(QRect(760, 110, 81, 31))
        self.pushButton_54.setFont(font29)
        self.pushButton_54.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_22 = QTextEdit(self.widget_84)
        self.textEdit_22.setObjectName(u"textEdit_22")
        self.textEdit_22.setGeometry(QRect(60, 40, 551, 171))
        self.textEdit_22.setStyleSheet(u"border:none;")
        self.textEdit_22.setReadOnly(True)
        self.widget_85 = QWidget(self.widget_82)
        self.widget_85.setObjectName(u"widget_85")
        self.widget_85.setGeometry(QRect(0, 500, 1021, 250))
        self.widget_85.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_55 = QPushButton(self.widget_85)
        self.pushButton_55.setObjectName(u"pushButton_55")
        self.pushButton_55.setGeometry(QRect(760, 110, 81, 31))
        self.pushButton_55.setFont(font29)
        self.pushButton_55.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_23 = QTextEdit(self.widget_85)
        self.textEdit_23.setObjectName(u"textEdit_23")
        self.textEdit_23.setGeometry(QRect(60, 40, 581, 201))
        self.textEdit_23.setStyleSheet(u"border:none;")
        self.textEdit_23.setReadOnly(True)
        self.widget_86 = QWidget(self.widget_82)
        self.widget_86.setObjectName(u"widget_86")
        self.widget_86.setGeometry(QRect(0, 750, 1021, 250))
        self.widget_86.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_56 = QPushButton(self.widget_86)
        self.pushButton_56.setObjectName(u"pushButton_56")
        self.pushButton_56.setGeometry(QRect(760, 110, 81, 31))
        self.pushButton_56.setFont(font29)
        self.pushButton_56.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_24 = QTextEdit(self.widget_86)
        self.textEdit_24.setObjectName(u"textEdit_24")
        self.textEdit_24.setGeometry(QRect(60, 50, 551, 171))
        self.textEdit_24.setStyleSheet(u"border:none;")
        self.textEdit_24.setReadOnly(True)
        self.widget_87 = QWidget(self.widget_82)
        self.widget_87.setObjectName(u"widget_87")
        self.widget_87.setGeometry(QRect(0, 1000, 1021, 250))
        self.widget_87.setStyleSheet(u"border-bottom:2px solid black;\n"
"border-radius:0px;")
        self.pushButton_57 = QPushButton(self.widget_87)
        self.pushButton_57.setObjectName(u"pushButton_57")
        self.pushButton_57.setGeometry(QRect(760, 100, 81, 31))
        self.pushButton_57.setFont(font29)
        self.pushButton_57.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_25 = QTextEdit(self.widget_87)
        self.textEdit_25.setObjectName(u"textEdit_25")
        self.textEdit_25.setGeometry(QRect(60, 40, 551, 171))
        self.textEdit_25.setStyleSheet(u"border:none;")
        self.textEdit_25.setReadOnly(True)
        self.widget_88 = QWidget(self.frame_20)
        self.widget_88.setObjectName(u"widget_88")
        self.widget_88.setGeometry(QRect(-110, 1899, 1035, 1661))
        self.widget_88.setStyleSheet(u"")
        self.label_494 = QLabel(self.widget_88)
        self.label_494.setObjectName(u"label_494")
        self.label_494.setGeometry(QRect(142, 10, 221, 41))
        self.label_494.setFont(font28)
        self.label_494.setStyleSheet(u"border:none; color:white;")
        self.frame_60 = QFrame(self.widget_88)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setGeometry(QRect(140, 60, 1020, 211))
        self.frame_60.setStyleSheet(u"border:none;")
        self.frame_60.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Shadow.Raised)
        self.label_496 = QLabel(self.frame_60)
        self.label_496.setObjectName(u"label_496")
        self.label_496.setGeometry(QRect(-20, -10, 1041, 291))
        self.label_496.setStyleSheet(u"border:none;")
        self.label_496.setPixmap(QPixmap(u":/shivam/PropImages/CArpennntorr.jpg"))
        self.label_496.setScaledContents(True)
        self.widget_89 = QWidget(self.widget_88)
        self.widget_89.setObjectName(u"widget_89")
        self.widget_89.setGeometry(QRect(140, 280, 1021, 1400))
        self.widget_89.setStyleSheet(u"background-color: rgb(229, 229, 229);\n"
"border-radius:15px;")
        self.widget_90 = QWidget(self.widget_89)
        self.widget_90.setObjectName(u"widget_90")
        self.widget_90.setGeometry(QRect(0, -10, 1021, 250))
        self.widget_90.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_58 = QPushButton(self.widget_90)
        self.pushButton_58.setObjectName(u"pushButton_58")
        self.pushButton_58.setGeometry(QRect(760, 110, 81, 31))
        self.pushButton_58.setFont(font29)
        self.pushButton_58.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_26 = QTextEdit(self.widget_90)
        self.textEdit_26.setObjectName(u"textEdit_26")
        self.textEdit_26.setGeometry(QRect(60, 40, 551, 171))
        self.textEdit_26.setStyleSheet(u"border:none;")
        self.textEdit_26.setReadOnly(True)
        self.widget_91 = QWidget(self.widget_89)
        self.widget_91.setObjectName(u"widget_91")
        self.widget_91.setGeometry(QRect(0, 240, 1021, 250))
        self.widget_91.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_59 = QPushButton(self.widget_91)
        self.pushButton_59.setObjectName(u"pushButton_59")
        self.pushButton_59.setGeometry(QRect(760, 110, 81, 31))
        self.pushButton_59.setFont(font29)
        self.pushButton_59.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_27 = QTextEdit(self.widget_91)
        self.textEdit_27.setObjectName(u"textEdit_27")
        self.textEdit_27.setGeometry(QRect(60, 40, 551, 171))
        self.textEdit_27.setStyleSheet(u"border:none;")
        self.textEdit_27.setReadOnly(True)
        self.widget_92 = QWidget(self.widget_89)
        self.widget_92.setObjectName(u"widget_92")
        self.widget_92.setGeometry(QRect(0, 490, 1021, 310))
        self.widget_92.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_60 = QPushButton(self.widget_92)
        self.pushButton_60.setObjectName(u"pushButton_60")
        self.pushButton_60.setGeometry(QRect(760, 140, 81, 31))
        self.pushButton_60.setFont(font29)
        self.pushButton_60.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_28 = QTextEdit(self.widget_92)
        self.textEdit_28.setObjectName(u"textEdit_28")
        self.textEdit_28.setGeometry(QRect(60, 30, 621, 241))
        self.textEdit_28.setStyleSheet(u"border:none;")
        self.textEdit_28.setReadOnly(True)
        self.widget_93 = QWidget(self.widget_89)
        self.widget_93.setObjectName(u"widget_93")
        self.widget_93.setGeometry(QRect(0, 800, 1021, 320))
        self.widget_93.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_61 = QPushButton(self.widget_93)
        self.pushButton_61.setObjectName(u"pushButton_61")
        self.pushButton_61.setGeometry(QRect(760, 140, 81, 31))
        self.pushButton_61.setFont(font29)
        self.pushButton_61.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_29 = QTextEdit(self.widget_93)
        self.textEdit_29.setObjectName(u"textEdit_29")
        self.textEdit_29.setGeometry(QRect(60, 40, 601, 241))
        self.textEdit_29.setStyleSheet(u"border:none;")
        self.textEdit_29.setReadOnly(True)
        self.widget_94 = QWidget(self.widget_89)
        self.widget_94.setObjectName(u"widget_94")
        self.widget_94.setGeometry(QRect(0, 1140, 1021, 250))
        self.widget_94.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_62 = QPushButton(self.widget_94)
        self.pushButton_62.setObjectName(u"pushButton_62")
        self.pushButton_62.setGeometry(QRect(760, 110, 81, 31))
        self.pushButton_62.setFont(font29)
        self.pushButton_62.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_30 = QTextEdit(self.widget_94)
        self.textEdit_30.setObjectName(u"textEdit_30")
        self.textEdit_30.setGeometry(QRect(60, -10, 661, 241))
        self.textEdit_30.setStyleSheet(u"border:none;")
        self.textEdit_30.setReadOnly(True)
        self.widget_95 = QWidget(self.frame_20)
        self.widget_95.setObjectName(u"widget_95")
        self.widget_95.setGeometry(QRect(-110, 3580, 1035, 1531))
        self.widget_95.setStyleSheet(u"")
        self.label_497 = QLabel(self.widget_95)
        self.label_497.setObjectName(u"label_497")
        self.label_497.setGeometry(QRect(142, 10, 221, 41))
        self.label_497.setFont(font28)
        self.label_497.setStyleSheet(u"border:none; color:white;")
        self.frame_61 = QFrame(self.widget_95)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setGeometry(QRect(140, 60, 1020, 211))
        self.frame_61.setStyleSheet(u"border:none;")
        self.frame_61.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Shadow.Raised)
        self.label_498 = QLabel(self.frame_61)
        self.label_498.setObjectName(u"label_498")
        self.label_498.setGeometry(QRect(-10, -60, 1031, 331))
        self.label_498.setStyleSheet(u"border:none;")
        self.label_498.setPixmap(QPixmap(u":/shivam/PropImages/door.png"))
        self.label_498.setScaledContents(True)
        self.widget_96 = QWidget(self.widget_95)
        self.widget_96.setObjectName(u"widget_96")
        self.widget_96.setGeometry(QRect(140, 280, 1021, 1321))
        self.widget_96.setStyleSheet(u"background-color: rgb(229, 229, 229);\n"
"border-radius:15px;")
        self.widget_97 = QWidget(self.widget_96)
        self.widget_97.setObjectName(u"widget_97")
        self.widget_97.setGeometry(QRect(0, 0, 1021, 250))
        self.widget_97.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_63 = QPushButton(self.widget_97)
        self.pushButton_63.setObjectName(u"pushButton_63")
        self.pushButton_63.setGeometry(QRect(760, 110, 81, 31))
        self.pushButton_63.setFont(font29)
        self.pushButton_63.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_31 = QTextEdit(self.widget_97)
        self.textEdit_31.setObjectName(u"textEdit_31")
        self.textEdit_31.setGeometry(QRect(60, 40, 551, 171))
        self.textEdit_31.setStyleSheet(u"border:none;")
        self.textEdit_31.setReadOnly(True)
        self.widget_98 = QWidget(self.widget_96)
        self.widget_98.setObjectName(u"widget_98")
        self.widget_98.setGeometry(QRect(0, 250, 1021, 250))
        self.widget_98.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_64 = QPushButton(self.widget_98)
        self.pushButton_64.setObjectName(u"pushButton_64")
        self.pushButton_64.setGeometry(QRect(760, 110, 81, 31))
        self.pushButton_64.setFont(font29)
        self.pushButton_64.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_32 = QTextEdit(self.widget_98)
        self.textEdit_32.setObjectName(u"textEdit_32")
        self.textEdit_32.setGeometry(QRect(60, 30, 551, 181))
        self.textEdit_32.setStyleSheet(u"border:none;")
        self.textEdit_32.setReadOnly(True)
        self.widget_99 = QWidget(self.widget_96)
        self.widget_99.setObjectName(u"widget_99")
        self.widget_99.setGeometry(QRect(0, 500, 1021, 250))
        self.widget_99.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_65 = QPushButton(self.widget_99)
        self.pushButton_65.setObjectName(u"pushButton_65")
        self.pushButton_65.setGeometry(QRect(760, 110, 81, 31))
        self.pushButton_65.setFont(font29)
        self.pushButton_65.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_33 = QTextEdit(self.widget_99)
        self.textEdit_33.setObjectName(u"textEdit_33")
        self.textEdit_33.setGeometry(QRect(60, 40, 551, 171))
        self.textEdit_33.setStyleSheet(u"border:none;")
        self.textEdit_33.setReadOnly(True)
        self.widget_100 = QWidget(self.widget_96)
        self.widget_100.setObjectName(u"widget_100")
        self.widget_100.setGeometry(QRect(0, 750, 1021, 250))
        self.widget_100.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_66 = QPushButton(self.widget_100)
        self.pushButton_66.setObjectName(u"pushButton_66")
        self.pushButton_66.setGeometry(QRect(760, 110, 81, 31))
        self.pushButton_66.setFont(font29)
        self.pushButton_66.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_34 = QTextEdit(self.widget_100)
        self.textEdit_34.setObjectName(u"textEdit_34")
        self.textEdit_34.setGeometry(QRect(60, 20, 551, 221))
        self.textEdit_34.setStyleSheet(u"border:none;")
        self.textEdit_34.setReadOnly(True)
        self.widget_101 = QWidget(self.widget_96)
        self.widget_101.setObjectName(u"widget_101")
        self.widget_101.setGeometry(QRect(0, 1000, 1021, 250))
        self.widget_101.setStyleSheet(u"border-bottom:2px solid black;\n"
"border-radius:0px;")
        self.pushButton_67 = QPushButton(self.widget_101)
        self.pushButton_67.setObjectName(u"pushButton_67")
        self.pushButton_67.setGeometry(QRect(760, 100, 81, 31))
        self.pushButton_67.setFont(font29)
        self.pushButton_67.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_35 = QTextEdit(self.widget_101)
        self.textEdit_35.setObjectName(u"textEdit_35")
        self.textEdit_35.setGeometry(QRect(60, 30, 551, 191))
        self.textEdit_35.setStyleSheet(u"border:none;")
        self.textEdit_35.setReadOnly(True)
        self.frame_80 = QFrame(self.frame_20)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setGeometry(QRect(940, 410, 400, 500))
        self.frame_80.setMinimumSize(QSize(400, 500))
        self.frame_80.setMaximumSize(QSize(400, 500))
        self.frame_80.setStyleSheet(u"border:1px solid rgb(18, 140, 126);\n"
"border-radius:15px;")
        self.frame_80.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_81 = QFrame(self.frame_80)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setGeometry(QRect(0, 0, 400, 50))
        self.frame_81.setMinimumSize(QSize(400, 50))
        self.frame_81.setMaximumSize(QSize(400, 50))
        self.frame_81.setStyleSheet(u"background-color:rgb(18, 140, 126);\n"
"border:none;\n"
"border-radius:0px;")
        self.frame_81.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Shadow.Raised)
        self.label_627 = QLabel(self.frame_81)
        self.label_627.setObjectName(u"label_627")
        self.label_627.setGeometry(QRect(110, 8, 180, 30))
        font30 = QFont()
        font30.setFamilies([u"Segoe UI"])
        font30.setPointSize(18)
        font30.setBold(True)
        self.label_627.setFont(font30)
        self.frame_82 = QFrame(self.frame_80)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setGeometry(QRect(0, 450, 400, 50))
        self.frame_82.setMinimumSize(QSize(400, 50))
        self.frame_82.setMaximumSize(QSize(400, 50))
        self.frame_82.setStyleSheet(u"background-color:rgb(18, 140, 126);\n"
"border:none;\n"
"border-radius:0px;")
        self.frame_82.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_108 = QPushButton(self.frame_82)
        self.pushButton_108.setObjectName(u"pushButton_108")
        self.pushButton_108.setGeometry(QRect(94, 10, 211, 31))
        self.pushButton_108.setFont(font29)
        self.pushButton_108.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.frame_83 = QFrame(self.frame_80)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setGeometry(QRect(10, 60, 380, 70))
        self.frame_83.setMinimumSize(QSize(380, 70))
        self.frame_83.setMaximumSize(QSize(380, 70))
        self.frame_83.setStyleSheet(u"background-color:rgb(229, 229, 229);\n"
"border:none; border-radius:10px;")
        self.frame_83.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Shadow.Raised)
        self.label_628 = QLabel(self.frame_83)
        self.label_628.setObjectName(u"label_628")
        self.label_628.setGeometry(QRect(14, 10, 50, 50))
        self.label_628.setPixmap(QPixmap(u":/shivam/PropImages/pipes.png"))
        self.label_628.setScaledContents(True)
        self.pushButton_84 = QPushButton(self.frame_83)
        self.pushButton_84.setObjectName(u"pushButton_84")
        self.pushButton_84.setGeometry(QRect(342, 25, 21, 21))
        self.pushButton_84.setIcon(icon17)
        self.pushButton_84.setIconSize(QSize(25, 25))
        self.pushButton_84.setCheckable(True)
        self.pushButton_84.setAutoExclusive(True)
        self.layoutWidget_47 = QWidget(self.frame_83)
        self.layoutWidget_47.setObjectName(u"layoutWidget_47")
        self.layoutWidget_47.setGeometry(QRect(78, 7, 115, 56))
        self.verticalLayout_86 = QVBoxLayout(self.layoutWidget_47)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.label_629 = QLabel(self.layoutWidget_47)
        self.label_629.setObjectName(u"label_629")
        self.label_629.setFont(font16)

        self.verticalLayout_86.addWidget(self.label_629)

        self.label_630 = QLabel(self.layoutWidget_47)
        self.label_630.setObjectName(u"label_630")

        self.verticalLayout_86.addWidget(self.label_630)

        self.label_631 = QLabel(self.layoutWidget_47)
        self.label_631.setObjectName(u"label_631")

        self.verticalLayout_86.addWidget(self.label_631)

        self.frame_84 = QFrame(self.frame_80)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setGeometry(QRect(10, 140, 380, 70))
        self.frame_84.setMinimumSize(QSize(380, 70))
        self.frame_84.setMaximumSize(QSize(380, 70))
        self.frame_84.setStyleSheet(u"background-color:rgb(229, 229, 229);\n"
"border:none; border-radius:10px;")
        self.frame_84.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Shadow.Raised)
        self.label_632 = QLabel(self.frame_84)
        self.label_632.setObjectName(u"label_632")
        self.label_632.setGeometry(QRect(14, 10, 50, 50))
        self.label_632.setPixmap(QPixmap(u":/shivam/PropImages/pipes (1).png"))
        self.label_632.setScaledContents(True)
        self.pushButton_85 = QPushButton(self.frame_84)
        self.pushButton_85.setObjectName(u"pushButton_85")
        self.pushButton_85.setGeometry(QRect(342, 25, 21, 21))
        self.pushButton_85.setIcon(icon17)
        self.pushButton_85.setIconSize(QSize(25, 25))
        self.pushButton_85.setCheckable(True)
        self.pushButton_85.setAutoRepeat(False)
        self.pushButton_85.setAutoExclusive(True)
        self.layoutWidget_48 = QWidget(self.frame_84)
        self.layoutWidget_48.setObjectName(u"layoutWidget_48")
        self.layoutWidget_48.setGeometry(QRect(78, 7, 115, 56))
        self.verticalLayout_87 = QVBoxLayout(self.layoutWidget_48)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.label_633 = QLabel(self.layoutWidget_48)
        self.label_633.setObjectName(u"label_633")
        self.label_633.setFont(font16)

        self.verticalLayout_87.addWidget(self.label_633)

        self.label_634 = QLabel(self.layoutWidget_48)
        self.label_634.setObjectName(u"label_634")

        self.verticalLayout_87.addWidget(self.label_634)

        self.label_635 = QLabel(self.layoutWidget_48)
        self.label_635.setObjectName(u"label_635")

        self.verticalLayout_87.addWidget(self.label_635)

        self.frame_85 = QFrame(self.frame_80)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setGeometry(QRect(10, 220, 380, 70))
        self.frame_85.setMinimumSize(QSize(380, 70))
        self.frame_85.setMaximumSize(QSize(380, 70))
        self.frame_85.setStyleSheet(u"background-color:rgb(229, 229, 229);\n"
"border:none; border-radius:10px;")
        self.frame_85.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Shadow.Raised)
        self.label_636 = QLabel(self.frame_85)
        self.label_636.setObjectName(u"label_636")
        self.label_636.setGeometry(QRect(14, 10, 50, 50))
        self.label_636.setPixmap(QPixmap(u":/shivam/PropImages/pipes.png"))
        self.label_636.setScaledContents(True)
        self.pushButton_86 = QPushButton(self.frame_85)
        self.pushButton_86.setObjectName(u"pushButton_86")
        self.pushButton_86.setGeometry(QRect(342, 25, 21, 21))
        self.pushButton_86.setIcon(icon17)
        self.pushButton_86.setIconSize(QSize(25, 25))
        self.pushButton_86.setCheckable(True)
        self.pushButton_86.setAutoRepeat(False)
        self.pushButton_86.setAutoExclusive(True)
        self.layoutWidget_49 = QWidget(self.frame_85)
        self.layoutWidget_49.setObjectName(u"layoutWidget_49")
        self.layoutWidget_49.setGeometry(QRect(78, 7, 115, 56))
        self.verticalLayout_88 = QVBoxLayout(self.layoutWidget_49)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.label_637 = QLabel(self.layoutWidget_49)
        self.label_637.setObjectName(u"label_637")
        self.label_637.setFont(font16)

        self.verticalLayout_88.addWidget(self.label_637)

        self.label_638 = QLabel(self.layoutWidget_49)
        self.label_638.setObjectName(u"label_638")

        self.verticalLayout_88.addWidget(self.label_638)

        self.label_639 = QLabel(self.layoutWidget_49)
        self.label_639.setObjectName(u"label_639")

        self.verticalLayout_88.addWidget(self.label_639)


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
"    background:rgb(7, 94, 84);\n"
" }")
        self.scrollArea_13.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_13.setWidgetResizable(True)
        self.scrollAreaWidgetContents_13 = QWidget()
        self.scrollAreaWidgetContents_13.setObjectName(u"scrollAreaWidgetContents_13")
        self.scrollAreaWidgetContents_13.setGeometry(QRect(0, -2000, 1351, 3000))
        self.scrollAreaWidgetContents_13.setMinimumSize(QSize(0, 3000))
        self.scrollAreaWidgetContents_13.setMaximumSize(QSize(16777215, 3000))
        self.verticalLayout_36 = QVBoxLayout(self.scrollAreaWidgetContents_13)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_102 = QFrame(self.scrollAreaWidgetContents_13)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setMinimumSize(QSize(0, 3000))
        self.frame_102.setStyleSheet(u"")
        self.widget_102 = QWidget(self.frame_102)
        self.widget_102.setObjectName(u"widget_102")
        self.widget_102.setGeometry(QRect(30, 30, 1300, 300))
        self.widget_102.setStyleSheet(u"background-color: rgb(18, 140, 126);")
        self.label_938 = QLabel(self.widget_102)
        self.label_938.setObjectName(u"label_938")
        self.label_938.setGeometry(QRect(20, -60, 391, 361))
        self.label_938.setPixmap(QPixmap(u":/shivam/PropImages/carpentry2 (1).png"))
        self.label_938.setScaledContents(True)
        self.label_939 = QLabel(self.widget_102)
        self.label_939.setObjectName(u"label_939")
        self.label_939.setGeometry(QRect(501, 14, 551, 271))
        self.label_939.setFont(font27)
        self.label_939.setStyleSheet(u"color:rgb(249, 231, 227);")
        self.widget_103 = QWidget(self.frame_102)
        self.widget_103.setObjectName(u"widget_103")
        self.widget_103.setGeometry(QRect(-110, 350, 1035, 1031))
        self.widget_103.setStyleSheet(u"")
        self.label_940 = QLabel(self.widget_103)
        self.label_940.setObjectName(u"label_940")
        self.label_940.setGeometry(QRect(142, 10, 221, 41))
        self.label_940.setFont(font28)
        self.label_940.setStyleSheet(u"border:none; color:white;")
        self.frame_103 = QFrame(self.widget_103)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setGeometry(QRect(140, 60, 1020, 211))
        self.frame_103.setStyleSheet(u"border:none;")
        self.frame_103.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Shadow.Raised)
        self.label_941 = QLabel(self.frame_103)
        self.label_941.setObjectName(u"label_941")
        self.label_941.setGeometry(QRect(0, -20, 1021, 251))
        self.label_941.setStyleSheet(u"border:none;")
        self.label_941.setPixmap(QPixmap(u":/shivam/PropImages/plumbingbanner3.jpg"))
        self.label_941.setScaledContents(True)
        self.widget_104 = QWidget(self.widget_103)
        self.widget_104.setObjectName(u"widget_104")
        self.widget_104.setGeometry(QRect(140, 280, 1021, 1321))
        self.widget_104.setStyleSheet(u"background-color: rgb(229, 229, 229);\n"
"border-radius:15px;")
        self.widget_105 = QWidget(self.widget_104)
        self.widget_105.setObjectName(u"widget_105")
        self.widget_105.setGeometry(QRect(0, 0, 1021, 250))
        self.widget_105.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_104 = QPushButton(self.widget_105)
        self.pushButton_104.setObjectName(u"pushButton_104")
        self.pushButton_104.setGeometry(QRect(750, 110, 81, 31))
        self.pushButton_104.setFont(font29)
        self.pushButton_104.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_18 = QTextEdit(self.widget_105)
        self.textEdit_18.setObjectName(u"textEdit_18")
        self.textEdit_18.setGeometry(QRect(60, 30, 551, 181))
        self.textEdit_18.setStyleSheet(u"border:none;")
        self.textEdit_18.setReadOnly(True)
        self.widget_106 = QWidget(self.widget_104)
        self.widget_106.setObjectName(u"widget_106")
        self.widget_106.setGeometry(QRect(0, 250, 1021, 250))
        self.widget_106.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_105 = QPushButton(self.widget_106)
        self.pushButton_105.setObjectName(u"pushButton_105")
        self.pushButton_105.setGeometry(QRect(750, 110, 81, 31))
        self.pushButton_105.setFont(font29)
        self.pushButton_105.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_36 = QTextEdit(self.widget_106)
        self.textEdit_36.setObjectName(u"textEdit_36")
        self.textEdit_36.setGeometry(QRect(60, 30, 551, 181))
        self.textEdit_36.setStyleSheet(u"border:none;")
        self.textEdit_36.setReadOnly(True)
        self.widget_107 = QWidget(self.widget_104)
        self.widget_107.setObjectName(u"widget_107")
        self.widget_107.setGeometry(QRect(0, 500, 1021, 250))
        self.widget_107.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_106 = QPushButton(self.widget_107)
        self.pushButton_106.setObjectName(u"pushButton_106")
        self.pushButton_106.setGeometry(QRect(750, 110, 81, 31))
        self.pushButton_106.setFont(font29)
        self.pushButton_106.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_37 = QTextEdit(self.widget_107)
        self.textEdit_37.setObjectName(u"textEdit_37")
        self.textEdit_37.setGeometry(QRect(60, 30, 581, 201))
        self.textEdit_37.setStyleSheet(u"border:none;")
        self.textEdit_37.setReadOnly(True)
        self.widget_110 = QWidget(self.frame_102)
        self.widget_110.setObjectName(u"widget_110")
        self.widget_110.setGeometry(QRect(-110, 1410, 1035, 1661))
        self.widget_110.setStyleSheet(u"")
        self.label_942 = QLabel(self.widget_110)
        self.label_942.setObjectName(u"label_942")
        self.label_942.setGeometry(QRect(142, 10, 221, 41))
        self.label_942.setFont(font28)
        self.label_942.setStyleSheet(u"border:none; color:white;")
        self.frame_104 = QFrame(self.widget_110)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setGeometry(QRect(140, 60, 1020, 211))
        self.frame_104.setStyleSheet(u"border:none;")
        self.frame_104.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Shadow.Raised)
        self.label_943 = QLabel(self.frame_104)
        self.label_943.setObjectName(u"label_943")
        self.label_943.setGeometry(QRect(-20, -40, 1041, 291))
        self.label_943.setStyleSheet(u"border:none;")
        self.label_943.setPixmap(QPixmap(u":/shivam/PropImages/plumbingbanner1.jpg"))
        self.label_943.setScaledContents(True)
        self.widget_111 = QWidget(self.widget_110)
        self.widget_111.setObjectName(u"widget_111")
        self.widget_111.setGeometry(QRect(140, 280, 1021, 1280))
        self.widget_111.setStyleSheet(u"background-color: rgb(229, 229, 229);\n"
"border-radius:15px;")
        self.widget_112 = QWidget(self.widget_111)
        self.widget_112.setObjectName(u"widget_112")
        self.widget_112.setGeometry(QRect(0, -10, 1021, 250))
        self.widget_112.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_109 = QPushButton(self.widget_112)
        self.pushButton_109.setObjectName(u"pushButton_109")
        self.pushButton_109.setGeometry(QRect(750, 110, 81, 31))
        self.pushButton_109.setFont(font29)
        self.pushButton_109.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_40 = QTextEdit(self.widget_112)
        self.textEdit_40.setObjectName(u"textEdit_40")
        self.textEdit_40.setGeometry(QRect(60, 30, 571, 181))
        self.textEdit_40.setStyleSheet(u"border:none;")
        self.textEdit_40.setReadOnly(True)
        self.widget_113 = QWidget(self.widget_111)
        self.widget_113.setObjectName(u"widget_113")
        self.widget_113.setGeometry(QRect(0, 240, 1021, 250))
        self.widget_113.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_110 = QPushButton(self.widget_113)
        self.pushButton_110.setObjectName(u"pushButton_110")
        self.pushButton_110.setGeometry(QRect(750, 110, 81, 31))
        self.pushButton_110.setFont(font29)
        self.pushButton_110.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_41 = QTextEdit(self.widget_113)
        self.textEdit_41.setObjectName(u"textEdit_41")
        self.textEdit_41.setGeometry(QRect(60, 20, 551, 191))
        self.textEdit_41.setStyleSheet(u"border:none;")
        self.textEdit_41.setReadOnly(True)
        self.widget_114 = QWidget(self.widget_111)
        self.widget_114.setObjectName(u"widget_114")
        self.widget_114.setGeometry(QRect(0, 490, 1021, 260))
        self.widget_114.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_111 = QPushButton(self.widget_114)
        self.pushButton_111.setObjectName(u"pushButton_111")
        self.pushButton_111.setGeometry(QRect(750, 120, 81, 31))
        self.pushButton_111.setFont(font29)
        self.pushButton_111.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_42 = QTextEdit(self.widget_114)
        self.textEdit_42.setObjectName(u"textEdit_42")
        self.textEdit_42.setGeometry(QRect(60, 30, 621, 201))
        self.textEdit_42.setStyleSheet(u"border:none;")
        self.textEdit_42.setReadOnly(True)
        self.widget_115 = QWidget(self.widget_111)
        self.widget_115.setObjectName(u"widget_115")
        self.widget_115.setGeometry(QRect(0, 750, 1021, 280))
        self.widget_115.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_112 = QPushButton(self.widget_115)
        self.pushButton_112.setObjectName(u"pushButton_112")
        self.pushButton_112.setGeometry(QRect(750, 130, 81, 31))
        self.pushButton_112.setFont(font29)
        self.pushButton_112.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_43 = QTextEdit(self.widget_115)
        self.textEdit_43.setObjectName(u"textEdit_43")
        self.textEdit_43.setGeometry(QRect(60, 20, 601, 211))
        self.textEdit_43.setStyleSheet(u"border:none;")
        self.textEdit_43.setReadOnly(True)
        self.widget_116 = QWidget(self.widget_111)
        self.widget_116.setObjectName(u"widget_116")
        self.widget_116.setGeometry(QRect(0, 1030, 1021, 250))
        self.widget_116.setStyleSheet(u"border-bottom:4px solid black;\n"
"border-radius:0px;")
        self.pushButton_113 = QPushButton(self.widget_116)
        self.pushButton_113.setObjectName(u"pushButton_113")
        self.pushButton_113.setGeometry(QRect(750, 110, 81, 31))
        self.pushButton_113.setFont(font29)
        self.pushButton_113.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.textEdit_44 = QTextEdit(self.widget_116)
        self.textEdit_44.setObjectName(u"textEdit_44")
        self.textEdit_44.setGeometry(QRect(60, 30, 661, 191))
        self.textEdit_44.setStyleSheet(u"border:none;")
        self.textEdit_44.setReadOnly(True)
        self.frame_72 = QFrame(self.frame_102)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setGeometry(QRect(940, 410, 400, 500))
        self.frame_72.setMinimumSize(QSize(400, 500))
        self.frame_72.setMaximumSize(QSize(400, 500))
        self.frame_72.setStyleSheet(u"border:1px solid rgb(18, 140, 126);\n"
"border-radius:15px;")
        self.frame_72.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_73 = QFrame(self.frame_72)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setGeometry(QRect(0, 0, 400, 50))
        self.frame_73.setMinimumSize(QSize(400, 50))
        self.frame_73.setMaximumSize(QSize(400, 50))
        self.frame_73.setStyleSheet(u"background-color:rgb(18, 140, 126);\n"
"border:none;\n"
"border-radius:0px;")
        self.frame_73.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Shadow.Raised)
        self.label_614 = QLabel(self.frame_73)
        self.label_614.setObjectName(u"label_614")
        self.label_614.setGeometry(QRect(110, 8, 180, 30))
        self.label_614.setFont(font30)
        self.frame_76 = QFrame(self.frame_72)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setGeometry(QRect(0, 450, 400, 50))
        self.frame_76.setMinimumSize(QSize(400, 50))
        self.frame_76.setMaximumSize(QSize(400, 50))
        self.frame_76.setStyleSheet(u"background-color:rgb(18, 140, 126);\n"
"border:none;\n"
"border-radius:0px;")
        self.frame_76.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_107 = QPushButton(self.frame_76)
        self.pushButton_107.setObjectName(u"pushButton_107")
        self.pushButton_107.setGeometry(QRect(94, 10, 211, 31))
        self.pushButton_107.setFont(font29)
        self.pushButton_107.setStyleSheet(u"QPushButton{background-color: rgb(18, 140, 126);\n"
"border:1px solid black;\n"
"border-radius:10px;}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(166, 166, 166);\n"
"color:white;\n"
"border:1px solid black;\n"
"}")
        self.frame_77 = QFrame(self.frame_72)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setGeometry(QRect(10, 60, 380, 70))
        self.frame_77.setMinimumSize(QSize(380, 70))
        self.frame_77.setMaximumSize(QSize(380, 70))
        self.frame_77.setStyleSheet(u"background-color:rgb(229, 229, 229);\n"
"border:none; border-radius:10px;")
        self.frame_77.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Shadow.Raised)
        self.label_615 = QLabel(self.frame_77)
        self.label_615.setObjectName(u"label_615")
        self.label_615.setGeometry(QRect(14, 10, 50, 50))
        self.label_615.setPixmap(QPixmap(u":/shivam/PropImages/toolbox (1).png"))
        self.label_615.setScaledContents(True)
        self.pushButton_79 = QPushButton(self.frame_77)
        self.pushButton_79.setObjectName(u"pushButton_79")
        self.pushButton_79.setGeometry(QRect(342, 25, 21, 21))
        self.pushButton_79.setIcon(icon17)
        self.pushButton_79.setIconSize(QSize(25, 25))
        self.pushButton_79.setCheckable(True)
        self.pushButton_79.setAutoExclusive(True)
        self.layoutWidget12 = QWidget(self.frame_77)
        self.layoutWidget12.setObjectName(u"layoutWidget12")
        self.layoutWidget12.setGeometry(QRect(78, 7, 115, 56))
        self.verticalLayout_21 = QVBoxLayout(self.layoutWidget12)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_616 = QLabel(self.layoutWidget12)
        self.label_616.setObjectName(u"label_616")
        self.label_616.setFont(font16)

        self.verticalLayout_21.addWidget(self.label_616)

        self.label_617 = QLabel(self.layoutWidget12)
        self.label_617.setObjectName(u"label_617")

        self.verticalLayout_21.addWidget(self.label_617)

        self.label_618 = QLabel(self.layoutWidget12)
        self.label_618.setObjectName(u"label_618")

        self.verticalLayout_21.addWidget(self.label_618)

        self.frame_78 = QFrame(self.frame_72)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setGeometry(QRect(10, 140, 380, 70))
        self.frame_78.setMinimumSize(QSize(380, 70))
        self.frame_78.setMaximumSize(QSize(380, 70))
        self.frame_78.setStyleSheet(u"background-color:rgb(229, 229, 229);\n"
"border:none; border-radius:10px;")
        self.frame_78.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Shadow.Raised)
        self.label_619 = QLabel(self.frame_78)
        self.label_619.setObjectName(u"label_619")
        self.label_619.setGeometry(QRect(14, 10, 50, 50))
        self.label_619.setPixmap(QPixmap(u":/shivam/PropImages/toolbox (2).png"))
        self.label_619.setScaledContents(True)
        self.pushButton_82 = QPushButton(self.frame_78)
        self.pushButton_82.setObjectName(u"pushButton_82")
        self.pushButton_82.setGeometry(QRect(342, 25, 21, 21))
        self.pushButton_82.setIcon(icon17)
        self.pushButton_82.setIconSize(QSize(25, 25))
        self.pushButton_82.setCheckable(True)
        self.pushButton_82.setAutoRepeat(False)
        self.pushButton_82.setAutoExclusive(True)
        self.layoutWidget_2 = QWidget(self.frame_78)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(78, 7, 115, 56))
        self.verticalLayout_84 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.label_620 = QLabel(self.layoutWidget_2)
        self.label_620.setObjectName(u"label_620")
        self.label_620.setFont(font16)

        self.verticalLayout_84.addWidget(self.label_620)

        self.label_621 = QLabel(self.layoutWidget_2)
        self.label_621.setObjectName(u"label_621")

        self.verticalLayout_84.addWidget(self.label_621)

        self.label_622 = QLabel(self.layoutWidget_2)
        self.label_622.setObjectName(u"label_622")

        self.verticalLayout_84.addWidget(self.label_622)

        self.frame_79 = QFrame(self.frame_72)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setGeometry(QRect(10, 220, 380, 70))
        self.frame_79.setMinimumSize(QSize(380, 70))
        self.frame_79.setMaximumSize(QSize(380, 70))
        self.frame_79.setStyleSheet(u"background-color:rgb(229, 229, 229);\n"
"border:none; border-radius:10px;")
        self.frame_79.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Shadow.Raised)
        self.label_623 = QLabel(self.frame_79)
        self.label_623.setObjectName(u"label_623")
        self.label_623.setGeometry(QRect(14, 10, 50, 50))
        self.label_623.setPixmap(QPixmap(u":/shivam/PropImages/toolbox.png"))
        self.label_623.setScaledContents(True)
        self.pushButton_83 = QPushButton(self.frame_79)
        self.pushButton_83.setObjectName(u"pushButton_83")
        self.pushButton_83.setGeometry(QRect(342, 25, 21, 21))
        self.pushButton_83.setIcon(icon17)
        self.pushButton_83.setIconSize(QSize(25, 25))
        self.pushButton_83.setCheckable(True)
        self.pushButton_83.setAutoRepeat(False)
        self.pushButton_83.setAutoExclusive(True)
        self.layoutWidget_45 = QWidget(self.frame_79)
        self.layoutWidget_45.setObjectName(u"layoutWidget_45")
        self.layoutWidget_45.setGeometry(QRect(78, 7, 115, 56))
        self.verticalLayout_85 = QVBoxLayout(self.layoutWidget_45)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.label_624 = QLabel(self.layoutWidget_45)
        self.label_624.setObjectName(u"label_624")
        self.label_624.setFont(font16)

        self.verticalLayout_85.addWidget(self.label_624)

        self.label_625 = QLabel(self.layoutWidget_45)
        self.label_625.setObjectName(u"label_625")

        self.verticalLayout_85.addWidget(self.label_625)

        self.label_626 = QLabel(self.layoutWidget_45)
        self.label_626.setObjectName(u"label_626")

        self.verticalLayout_85.addWidget(self.label_626)


        self.verticalLayout_36.addWidget(self.frame_102)

        self.scrollArea_13.setWidget(self.scrollAreaWidgetContents_13)

        self.verticalLayout_35.addWidget(self.scrollArea_13)


        self.horizontalLayout_12.addWidget(self.widget_14)

        self.stackedWidget_3.addWidget(self.page_14)
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.verticalLayout_79 = QVBoxLayout(self.page_15)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.page_15)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 0))
        self.frame_21.setMaximumSize(QSize(16777215, 16777215))
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.widget_108 = QWidget(self.frame_21)
        self.widget_108.setObjectName(u"widget_108")
        self.widget_108.setGeometry(QRect(30, 30, 1310, 300))
        self.widget_108.setStyleSheet(u"background-color: rgb(18, 140, 126);")
        self.label_944 = QLabel(self.widget_108)
        self.label_944.setObjectName(u"label_944")
        self.label_944.setGeometry(QRect(80, -10, 351, 311))
        self.label_944.setPixmap(QPixmap(u":/shivam/PropImages/InteriorHeader.png"))
        self.label_944.setScaledContents(True)
        self.label_945 = QLabel(self.widget_108)
        self.label_945.setObjectName(u"label_945")
        self.label_945.setGeometry(QRect(610, 30, 551, 231))
        font31 = QFont()
        font31.setFamilies([u"Elephant"])
        font31.setPointSize(71)
        self.label_945.setFont(font31)
        self.label_945.setStyleSheet(u"color:rgb(249, 231, 227);")
        self.label_670 = QLabel(self.frame_21)
        self.label_670.setObjectName(u"label_670")
        self.label_670.setGeometry(QRect(360, 360, 591, 331))
        self.label_670.setPixmap(QPixmap(u":/shivam/PropImages/coming soon.png"))
        self.label_670.setScaledContents(True)

        self.verticalLayout_79.addWidget(self.frame_21)

        self.stackedWidget_3.addWidget(self.page_15)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.verticalLayout_81 = QVBoxLayout(self.page_16)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_16 = QScrollArea(self.page_16)
        self.scrollArea_16.setObjectName(u"scrollArea_16")
        self.scrollArea_16.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(7, 94, 84);\n"
" }")
        self.scrollArea_16.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_16.setWidgetResizable(True)
        self.scrollAreaWidgetContents_16 = QWidget()
        self.scrollAreaWidgetContents_16.setObjectName(u"scrollAreaWidgetContents_16")
        self.scrollAreaWidgetContents_16.setGeometry(QRect(0, 0, 1351, 3500))
        self.scrollAreaWidgetContents_16.setMinimumSize(QSize(0, 3500))
        self.scrollAreaWidgetContents_16.setMaximumSize(QSize(16777215, 3500))
        self.verticalLayout_80 = QVBoxLayout(self.scrollAreaWidgetContents_16)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.frame_105 = QFrame(self.scrollAreaWidgetContents_16)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setMinimumSize(QSize(0, 3000))
        self.frame_105.setStyleSheet(u"")
        self.frame_70 = QFrame(self.frame_105)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setGeometry(QRect(20, 20, 1320, 841))
        self.frame_70.setFont(font3)
        self.frame_70.setStyleSheet(u"QFrame{\n"
"background-color: rgb(35, 47, 49);\n"
"border-bottom:1px solid white;\n"
"}")
        self.frame_70.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Shadow.Raised)
        self.label_56 = QLabel(self.frame_70)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(80, 20, 251, 40))
        font32 = QFont()
        font32.setFamilies([u"Sitka Subheading"])
        font32.setPointSize(35)
        self.label_56.setFont(font32)
        self.label_56.setStyleSheet(u"color: rgb(255, 255, 255); border:none;")
        self.label_586 = QLabel(self.frame_70)
        self.label_586.setObjectName(u"label_586")
        self.label_586.setGeometry(QRect(80, 65, 16, 16))
        self.label_586.setStyleSheet(u"color: rgb(255, 255, 255); border:none;")
        self.label_587 = QLabel(self.frame_70)
        self.label_587.setObjectName(u"label_587")
        self.label_587.setGeometry(QRect(99, 65, 150, 16))
        self.label_587.setStyleSheet(u"color: rgb(85, 255, 127); border:none;")
        self.pushButton_76 = QPushButton(self.frame_70)
        self.pushButton_76.setObjectName(u"pushButton_76")
        self.pushButton_76.setGeometry(QRect(1087, 99, 71, 21))
        font33 = QFont()
        font33.setPointSize(7)
        self.pushButton_76.setFont(font33)
        self.pushButton_76.setStyleSheet(u"QPushButton\n"
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
        self.label_588 = QLabel(self.frame_70)
        self.label_588.setObjectName(u"label_588")
        self.label_588.setGeometry(QRect(961, 25, 182, 31))
        self.label_588.setFont(font5)
        self.label_588.setStyleSheet(u"color: rgb(255, 255, 255); border:none;")
        self.label_589 = QLabel(self.frame_70)
        self.label_589.setObjectName(u"label_589")
        self.label_589.setGeometry(QRect(1140, 32, 95, 20))
        self.label_589.setFont(font1)
        self.label_589.setStyleSheet(u"color:rgb(118, 118, 118);\n"
" border:none;")
        self.label_590 = QLabel(self.frame_70)
        self.label_590.setObjectName(u"label_590")
        self.label_590.setGeometry(QRect(1040, 61, 151, 20))
        self.label_590.setFont(font1)
        self.label_590.setStyleSheet(u"color: rgb(85, 255, 127); border:none;")
        self.label_591 = QLabel(self.frame_70)
        self.label_591.setObjectName(u"label_591")
        self.label_591.setGeometry(QRect(80, 140, 601, 541))
        self.label_591.setStyleSheet(u"border:none;")
        self.label_591.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Santacruz.Courtyard/Mumbai-6.5.jpg"))
        self.label_591.setScaledContents(True)
        self.label_595 = QLabel(self.frame_70)
        self.label_595.setObjectName(u"label_595")
        self.label_595.setGeometry(QRect(80, 100, 550, 18))
        self.label_595.setFont(font1)
        self.label_595.setStyleSheet(u"color:rgb(118, 118, 118);\n"
" border:none;")
        self.label_596 = QLabel(self.frame_70)
        self.label_596.setObjectName(u"label_596")
        self.label_596.setGeometry(QRect(690, 420, 540, 261))
        self.label_596.setStyleSheet(u"border:none;")
        self.label_596.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Santacruz.Courtyard/Mumbai-6.6.jpg"))
        self.label_596.setScaledContents(True)
        self.label_597 = QLabel(self.frame_70)
        self.label_597.setObjectName(u"label_597")
        self.label_597.setGeometry(QRect(690, 140, 541, 271))
        self.label_597.setStyleSheet(u"border:none;")
        self.label_597.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Santacruz.Courtyard/Mumbai-6.6.Lby4.jpg"))
        self.label_597.setScaledContents(True)
        self.layoutWidget13 = QWidget(self.frame_70)
        self.layoutWidget13.setObjectName(u"layoutWidget13")
        self.layoutWidget13.setGeometry(QRect(80, 690, 1151, 110))
        self.horizontalLayout_43 = QHBoxLayout(self.layoutWidget13)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_592 = QLabel(self.layoutWidget13)
        self.label_592.setObjectName(u"label_592")
        self.label_592.setFont(font17)
        self.label_592.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-bottom:1px solid rgb(37, 211, 102)")

        self.horizontalLayout_43.addWidget(self.label_592, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_593 = QLabel(self.layoutWidget13)
        self.label_593.setObjectName(u"label_593")
        self.label_593.setFont(font17)
        self.label_593.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-bottom:1px solid rgb(37, 211, 102)")

        self.horizontalLayout_43.addWidget(self.label_593, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_594 = QLabel(self.layoutWidget13)
        self.label_594.setObjectName(u"label_594")
        self.label_594.setFont(font17)
        self.label_594.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-bottom:1px solid rgb(37, 211, 102)")

        self.horizontalLayout_43.addWidget(self.label_594, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_71 = QFrame(self.frame_105)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setGeometry(QRect(20, 870, 1320, 841))
        self.frame_71.setFont(font3)
        self.frame_71.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"border:none;\n"
"")
        self.frame_71.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_8 = QLineEdit(self.frame_71)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(731, 150, 400, 35))
        self.lineEdit_8.setMinimumSize(QSize(0, 35))
        self.lineEdit_8.setBaseSize(QSize(0, 35))
        self.lineEdit_8.setStyleSheet(u"QLineEdit\n"
"{background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:none;\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"border-bottom:2px solid rgb(18, 140, 126);\n"
"}")
        self.lineEdit_9 = QLineEdit(self.frame_71)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(731, 270, 400, 35))
        self.lineEdit_9.setMinimumSize(QSize(0, 35))
        self.lineEdit_9.setBaseSize(QSize(0, 35))
        self.lineEdit_9.setStyleSheet(u"QLineEdit\n"
"{background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:none;\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"border-bottom:2px solid rgb(18, 140, 126);\n"
"}")
        self.lineEdit_10 = QLineEdit(self.frame_71)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(731, 210, 400, 35))
        self.lineEdit_10.setMinimumSize(QSize(0, 35))
        self.lineEdit_10.setBaseSize(QSize(0, 35))
        self.lineEdit_10.setStyleSheet(u"QLineEdit\n"
"{background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:none;\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"border-bottom:2px solid rgb(18, 140, 126);\n"
"}")
        self.pushButton_78 = QPushButton(self.frame_71)
        self.pushButton_78.setObjectName(u"pushButton_78")
        self.pushButton_78.setGeometry(QRect(850, 340, 161, 31))
        self.pushButton_78.setStyleSheet(u"QPushButton\n"
"{background-color:rgb(165, 165, 165);\n"
"border-radius:10px;\n"
"border:white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color:rgb(35, 47, 49);\n"
"	border:1px solid rgb(165, 165, 165);\n"
"	color:white;\n"
"}")
        self.label_598 = QLabel(self.frame_71)
        self.label_598.setObjectName(u"label_598")
        self.label_598.setGeometry(QRect(730, 60, 311, 51))
        self.label_598.setFont(font20)
        self.label_598.setStyleSheet(u"color:white;")
        self.label_599 = QLabel(self.frame_71)
        self.label_599.setObjectName(u"label_599")
        self.label_599.setGeometry(QRect(730, 110, 151, 16))
        font34 = QFont()
        font34.setPointSize(8)
        self.label_599.setFont(font34)
        self.label_599.setStyleSheet(u"color:rgb(198, 198, 198);")
        self.label_600 = QLabel(self.frame_71)
        self.label_600.setObjectName(u"label_600")
        self.label_600.setGeometry(QRect(130, 50, 510, 61))
        font35 = QFont()
        font35.setPointSize(26)
        font35.setBold(True)
        self.label_600.setFont(font35)
        self.label_600.setStyleSheet(u"color:rgb(18, 140, 126);\n"
"border:1px solid white;")
        self.label_602 = QLabel(self.frame_71)
        self.label_602.setObjectName(u"label_602")
        self.label_602.setGeometry(QRect(130, 120, 510, 35))
        self.label_602.setStyleSheet(u"background-color:white;")
        self.label_604 = QLabel(self.frame_71)
        self.label_604.setObjectName(u"label_604")
        self.label_604.setGeometry(QRect(130, 160, 510, 35))
        self.label_604.setStyleSheet(u"background-color:white;")
        self.label_605 = QLabel(self.frame_71)
        self.label_605.setObjectName(u"label_605")
        self.label_605.setGeometry(QRect(130, 200, 510, 35))
        self.label_605.setStyleSheet(u"background-color:white;")
        self.label_606 = QLabel(self.frame_71)
        self.label_606.setObjectName(u"label_606")
        self.label_606.setGeometry(QRect(130, 240, 510, 35))
        self.label_606.setStyleSheet(u"background-color:white;")
        self.label_607 = QLabel(self.frame_71)
        self.label_607.setObjectName(u"label_607")
        self.label_607.setGeometry(QRect(130, 280, 510, 35))
        self.label_607.setStyleSheet(u"background-color:white;")
        self.label_608 = QLabel(self.frame_71)
        self.label_608.setObjectName(u"label_608")
        self.label_608.setGeometry(QRect(130, 320, 510, 35))
        self.label_608.setStyleSheet(u"background-color:white;")
        self.label_610 = QLabel(self.frame_71)
        self.label_610.setObjectName(u"label_610")
        self.label_610.setGeometry(QRect(130, 360, 510, 35))
        self.label_610.setStyleSheet(u"background-color:white;")
        self.widget_109 = QWidget(self.frame_71)
        self.widget_109.setObjectName(u"widget_109")
        self.widget_109.setGeometry(QRect(680, 51, 510, 347))
        self.widget_109.setStyleSheet(u"border:1px solid white;\n"
"background:none;")
        self.label_601 = QLabel(self.frame_71)
        self.label_601.setObjectName(u"label_601")
        self.label_601.setGeometry(QRect(289, 430, 750, 280))
        self.label_601.setPixmap(QPixmap(u":/shivam/PropImages/courtyardnear.png"))
        self.label_601.setScaledContents(True)
        self.label_603 = QLabel(self.frame_71)
        self.label_603.setObjectName(u"label_603")
        self.label_603.setGeometry(QRect(970, 481, 69, 21))
        self.label_603.setStyleSheet(u"background-color:white")
        self.label_609 = QLabel(self.frame_71)
        self.label_609.setObjectName(u"label_609")
        self.label_609.setGeometry(QRect(0, 730, 1320, 71))
        self.label_609.setFont(font5)
        self.label_609.setStyleSheet(u"color:white;")
        self.widget_109.raise_()
        self.lineEdit_8.raise_()
        self.lineEdit_9.raise_()
        self.lineEdit_10.raise_()
        self.pushButton_78.raise_()
        self.label_598.raise_()
        self.label_599.raise_()
        self.label_600.raise_()
        self.label_602.raise_()
        self.label_604.raise_()
        self.label_605.raise_()
        self.label_606.raise_()
        self.label_607.raise_()
        self.label_608.raise_()
        self.label_610.raise_()
        self.label_601.raise_()
        self.label_603.raise_()
        self.label_609.raise_()
        self.label_611 = QLabel(self.frame_105)
        self.label_611.setObjectName(u"label_611")
        self.label_611.setGeometry(QRect(106, 1920, 1161, 591))
        self.label_611.setPixmap(QPixmap(u":/shivam/PropImages/PropertyCurtyarddesign.jpg"))
        self.label_611.setScaledContents(True)
        self.textEdit_19 = QTextEdit(self.frame_105)
        self.textEdit_19.setObjectName(u"textEdit_19")
        self.textEdit_19.setGeometry(QRect(123, 2540, 1131, 690))
        self.textEdit_19.setStyleSheet(u"border:none;")
        self.label_612 = QLabel(self.frame_105)
        self.label_612.setObjectName(u"label_612")
        self.label_612.setGeometry(QRect(260, 1690, 851, 221))
        self.label_612.setPixmap(QPixmap(u":/shivam/PropImages/amenities.png"))

        self.verticalLayout_80.addWidget(self.frame_105)

        self.scrollArea_16.setWidget(self.scrollAreaWidgetContents_16)

        self.verticalLayout_81.addWidget(self.scrollArea_16)

        self.stackedWidget_3.addWidget(self.page_16)
        self.page_17 = QWidget()
        self.page_17.setObjectName(u"page_17")
        self.verticalLayout_83 = QVBoxLayout(self.page_17)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_17 = QScrollArea(self.page_17)
        self.scrollArea_17.setObjectName(u"scrollArea_17")
        self.scrollArea_17.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:rgb(7, 94, 84);\n"
" }")
        self.scrollArea_17.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_17.setWidgetResizable(True)
        self.scrollAreaWidgetContents_17 = QWidget()
        self.scrollAreaWidgetContents_17.setObjectName(u"scrollAreaWidgetContents_17")
        self.scrollAreaWidgetContents_17.setGeometry(QRect(0, 0, 1351, 3500))
        self.scrollAreaWidgetContents_17.setMinimumSize(QSize(0, 3500))
        self.scrollAreaWidgetContents_17.setMaximumSize(QSize(16777215, 3500))
        self.verticalLayout_82 = QVBoxLayout(self.scrollAreaWidgetContents_17)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.frame_106 = QFrame(self.scrollAreaWidgetContents_17)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMinimumSize(QSize(0, 3000))
        self.frame_106.setStyleSheet(u"")
        self.frame_74 = QFrame(self.frame_106)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setGeometry(QRect(20, 20, 1320, 841))
        self.frame_74.setFont(font3)
        self.frame_74.setStyleSheet(u"QFrame{\n"
"background-color: rgb(35, 47, 49);\n"
"border-bottom:1px solid white;\n"
"}")
        self.frame_74.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Shadow.Raised)
        self.label_641 = QLabel(self.frame_74)
        self.label_641.setObjectName(u"label_641")
        self.label_641.setGeometry(QRect(80, 20, 251, 40))
        self.label_641.setFont(font32)
        self.label_641.setStyleSheet(u"color: rgb(255, 255, 255); border:none;")
        self.label_642 = QLabel(self.frame_74)
        self.label_642.setObjectName(u"label_642")
        self.label_642.setGeometry(QRect(80, 65, 16, 16))
        self.label_642.setStyleSheet(u"color: rgb(255, 255, 255); border:none;")
        self.label_643 = QLabel(self.frame_74)
        self.label_643.setObjectName(u"label_643")
        self.label_643.setGeometry(QRect(99, 65, 150, 16))
        self.label_643.setStyleSheet(u"color: rgb(85, 255, 127); border:none;")
        self.pushButton_80 = QPushButton(self.frame_74)
        self.pushButton_80.setObjectName(u"pushButton_80")
        self.pushButton_80.setGeometry(QRect(1087, 99, 71, 21))
        self.pushButton_80.setFont(font33)
        self.pushButton_80.setStyleSheet(u"QPushButton\n"
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
        self.label_644 = QLabel(self.frame_74)
        self.label_644.setObjectName(u"label_644")
        self.label_644.setGeometry(QRect(961, 25, 182, 31))
        self.label_644.setFont(font5)
        self.label_644.setStyleSheet(u"color: rgb(255, 255, 255); border:none;")
        self.label_645 = QLabel(self.frame_74)
        self.label_645.setObjectName(u"label_645")
        self.label_645.setGeometry(QRect(1140, 32, 95, 20))
        self.label_645.setFont(font1)
        self.label_645.setStyleSheet(u"color:rgb(118, 118, 118);\n"
" border:none;")
        self.label_646 = QLabel(self.frame_74)
        self.label_646.setObjectName(u"label_646")
        self.label_646.setGeometry(QRect(1040, 61, 151, 20))
        self.label_646.setFont(font1)
        self.label_646.setStyleSheet(u"color: rgb(85, 255, 127); border:none;")
        self.label_647 = QLabel(self.frame_74)
        self.label_647.setObjectName(u"label_647")
        self.label_647.setGeometry(QRect(80, 140, 601, 541))
        self.label_647.setStyleSheet(u"border:none;")
        self.label_647.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Malad.PratapLibertyOne/Mumbai-2.jpg"))
        self.label_647.setScaledContents(True)
        self.label_648 = QLabel(self.frame_74)
        self.label_648.setObjectName(u"label_648")
        self.label_648.setGeometry(QRect(80, 100, 550, 18))
        self.label_648.setFont(font1)
        self.label_648.setStyleSheet(u"color:rgb(118, 118, 118);\n"
" border:none;")
        self.label_649 = QLabel(self.frame_74)
        self.label_649.setObjectName(u"label_649")
        self.label_649.setGeometry(QRect(690, 420, 540, 261))
        self.label_649.setStyleSheet(u"border:none;")
        self.label_649.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Malad.PratapLibertyOne/Mumbai-2.3.jpg"))
        self.label_649.setScaledContents(True)
        self.label_650 = QLabel(self.frame_74)
        self.label_650.setObjectName(u"label_650")
        self.label_650.setGeometry(QRect(690, 140, 541, 271))
        self.label_650.setStyleSheet(u"border:none;")
        self.label_650.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Malad.PratapLibertyOne/Mumbai-2.2.jpg"))
        self.label_650.setScaledContents(True)
        self.layoutWidget_46 = QWidget(self.frame_74)
        self.layoutWidget_46.setObjectName(u"layoutWidget_46")
        self.layoutWidget_46.setGeometry(QRect(80, 690, 1151, 101))
        self.horizontalLayout_45 = QHBoxLayout(self.layoutWidget_46)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_651 = QLabel(self.layoutWidget_46)
        self.label_651.setObjectName(u"label_651")
        self.label_651.setFont(font17)
        self.label_651.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-bottom:1px solid rgb(37, 211, 102)")

        self.horizontalLayout_45.addWidget(self.label_651, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_652 = QLabel(self.layoutWidget_46)
        self.label_652.setObjectName(u"label_652")
        self.label_652.setFont(font17)
        self.label_652.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-bottom:1px solid rgb(37, 211, 102)")

        self.horizontalLayout_45.addWidget(self.label_652, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_653 = QLabel(self.layoutWidget_46)
        self.label_653.setObjectName(u"label_653")
        self.label_653.setFont(font17)
        self.label_653.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-bottom:1px solid rgb(37, 211, 102)")

        self.horizontalLayout_45.addWidget(self.label_653, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_75 = QFrame(self.frame_106)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setGeometry(QRect(20, 870, 1320, 841))
        self.frame_75.setFont(font3)
        self.frame_75.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"border:none;\n"
"")
        self.frame_75.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_14 = QLineEdit(self.frame_75)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(QRect(731, 150, 400, 35))
        self.lineEdit_14.setMinimumSize(QSize(0, 35))
        self.lineEdit_14.setBaseSize(QSize(0, 35))
        self.lineEdit_14.setStyleSheet(u"QLineEdit\n"
"{background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:none;\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"border-bottom:2px solid rgb(18, 140, 126);\n"
"}")
        self.lineEdit_15 = QLineEdit(self.frame_75)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setGeometry(QRect(731, 270, 400, 35))
        self.lineEdit_15.setMinimumSize(QSize(0, 35))
        self.lineEdit_15.setBaseSize(QSize(0, 35))
        self.lineEdit_15.setStyleSheet(u"QLineEdit\n"
"{background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:none;\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"border-bottom:2px solid rgb(18, 140, 126);\n"
"}")
        self.lineEdit_16 = QLineEdit(self.frame_75)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setGeometry(QRect(731, 210, 400, 35))
        self.lineEdit_16.setMinimumSize(QSize(0, 35))
        self.lineEdit_16.setBaseSize(QSize(0, 35))
        self.lineEdit_16.setStyleSheet(u"QLineEdit\n"
"{background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:none;\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"border-bottom:2px solid rgb(18, 140, 126);\n"
"}")
        self.pushButton_81 = QPushButton(self.frame_75)
        self.pushButton_81.setObjectName(u"pushButton_81")
        self.pushButton_81.setGeometry(QRect(850, 340, 161, 31))
        self.pushButton_81.setStyleSheet(u"QPushButton\n"
"{background-color:rgb(165, 165, 165);\n"
"border-radius:10px;\n"
"border:white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color:rgb(35, 47, 49);\n"
"	border:1px solid rgb(165, 165, 165);\n"
"	color:white;\n"
"}")
        self.label_654 = QLabel(self.frame_75)
        self.label_654.setObjectName(u"label_654")
        self.label_654.setGeometry(QRect(730, 60, 341, 51))
        self.label_654.setFont(font20)
        self.label_654.setStyleSheet(u"color:white;")
        self.label_655 = QLabel(self.frame_75)
        self.label_655.setObjectName(u"label_655")
        self.label_655.setGeometry(QRect(730, 110, 151, 16))
        self.label_655.setFont(font34)
        self.label_655.setStyleSheet(u"color:rgb(198, 198, 198);")
        self.label_656 = QLabel(self.frame_75)
        self.label_656.setObjectName(u"label_656")
        self.label_656.setGeometry(QRect(130, 50, 510, 61))
        self.label_656.setFont(font35)
        self.label_656.setStyleSheet(u"color:rgb(18, 140, 126);\n"
"border:1px solid white;")
        self.label_657 = QLabel(self.frame_75)
        self.label_657.setObjectName(u"label_657")
        self.label_657.setGeometry(QRect(130, 120, 510, 35))
        self.label_657.setStyleSheet(u"background-color:white;")
        self.label_658 = QLabel(self.frame_75)
        self.label_658.setObjectName(u"label_658")
        self.label_658.setGeometry(QRect(130, 160, 510, 35))
        self.label_658.setStyleSheet(u"background-color:white;")
        self.label_659 = QLabel(self.frame_75)
        self.label_659.setObjectName(u"label_659")
        self.label_659.setGeometry(QRect(130, 200, 510, 35))
        self.label_659.setStyleSheet(u"background-color:white;")
        self.label_660 = QLabel(self.frame_75)
        self.label_660.setObjectName(u"label_660")
        self.label_660.setGeometry(QRect(130, 240, 510, 35))
        self.label_660.setStyleSheet(u"background-color:white;")
        self.label_661 = QLabel(self.frame_75)
        self.label_661.setObjectName(u"label_661")
        self.label_661.setGeometry(QRect(130, 280, 510, 35))
        self.label_661.setStyleSheet(u"background-color:white;")
        self.label_662 = QLabel(self.frame_75)
        self.label_662.setObjectName(u"label_662")
        self.label_662.setGeometry(QRect(130, 320, 510, 35))
        self.label_662.setStyleSheet(u"background-color:white;")
        self.label_663 = QLabel(self.frame_75)
        self.label_663.setObjectName(u"label_663")
        self.label_663.setGeometry(QRect(130, 360, 510, 35))
        self.label_663.setStyleSheet(u"background-color:white;")
        self.widget_118 = QWidget(self.frame_75)
        self.widget_118.setObjectName(u"widget_118")
        self.widget_118.setGeometry(QRect(680, 51, 510, 347))
        self.widget_118.setStyleSheet(u"border:1px solid white;\n"
"background:none;")
        self.label_664 = QLabel(self.frame_75)
        self.label_664.setObjectName(u"label_664")
        self.label_664.setGeometry(QRect(289, 430, 750, 280))
        self.label_664.setPixmap(QPixmap(u":/shivam/PropImages/libertyonenear.png"))
        self.label_664.setScaledContents(True)
        self.label_666 = QLabel(self.frame_75)
        self.label_666.setObjectName(u"label_666")
        self.label_666.setGeometry(QRect(0, 730, 1320, 71))
        self.label_666.setFont(font5)
        self.label_666.setStyleSheet(u"color:white;")
        self.widget_118.raise_()
        self.lineEdit_14.raise_()
        self.lineEdit_15.raise_()
        self.lineEdit_16.raise_()
        self.pushButton_81.raise_()
        self.label_654.raise_()
        self.label_655.raise_()
        self.label_656.raise_()
        self.label_657.raise_()
        self.label_658.raise_()
        self.label_659.raise_()
        self.label_660.raise_()
        self.label_661.raise_()
        self.label_662.raise_()
        self.label_663.raise_()
        self.label_664.raise_()
        self.label_666.raise_()
        self.label_667 = QLabel(self.frame_106)
        self.label_667.setObjectName(u"label_667")
        self.label_667.setGeometry(QRect(106, 2020, 1161, 591))
        self.label_667.setPixmap(QPixmap(u":/shivam/PropImages/PropertyCurtyarddesign.jpg"))
        self.label_667.setScaledContents(True)
        self.textEdit_21 = QTextEdit(self.frame_106)
        self.textEdit_21.setObjectName(u"textEdit_21")
        self.textEdit_21.setGeometry(QRect(123, 2630, 1131, 690))
        self.textEdit_21.setStyleSheet(u"border:none;")
        self.label_668 = QLabel(self.frame_106)
        self.label_668.setObjectName(u"label_668")
        self.label_668.setGeometry(QRect(330, 1680, 721, 321))
        self.label_668.setPixmap(QPixmap(u":/shivam/PropImages/amenties1.png"))

        self.verticalLayout_82.addWidget(self.frame_106)

        self.scrollArea_17.setWidget(self.scrollAreaWidgetContents_17)

        self.verticalLayout_83.addWidget(self.scrollArea_17)

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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1351, 3000))
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
"    background:rgb(7, 94, 84);\n"
" }")
        self.scrollArea_4.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1351, 6000))
        self.scrollAreaWidgetContents_4.setMinimumSize(QSize(0, 6000))
        self.scrollAreaWidgetContents_4.setMaximumSize(QSize(16777215, 6000))
        self.verticalLayout_24 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 3000))
        self.frame_15.setStyleSheet(u"")
        self.verticalLayout_78 = QVBoxLayout(self.frame_15)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(10)
        self.gridLayout_5.setContentsMargins(50, 35, -1, 60)
        self.frame_64 = QFrame(self.frame_15)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFont(font3)
        self.frame_64.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_64.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Shadow.Raised)
        self.label_520 = QLabel(self.frame_64)
        self.label_520.setObjectName(u"label_520")
        self.label_520.setGeometry(QRect(13, 10, 147, 33))
        self.label_520.setFont(font4)
        self.label_520.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_521 = QLabel(self.frame_64)
        self.label_521.setObjectName(u"label_521")
        self.label_521.setGeometry(QRect(16, 49, 16, 16))
        self.label_521.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_522 = QLabel(self.frame_64)
        self.label_522.setObjectName(u"label_522")
        self.label_522.setGeometry(QRect(35, 49, 100, 16))
        self.label_522.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_52 = QPushButton(self.frame_64)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_52.setStyleSheet(u"QPushButton\n"
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
        self.label_523 = QLabel(self.frame_64)
        self.label_523.setObjectName(u"label_523")
        self.label_523.setGeometry(QRect(298, 10, 182, 31))
        self.label_523.setFont(font5)
        self.label_523.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_524 = QLabel(self.frame_64)
        self.label_524.setObjectName(u"label_524")
        self.label_524.setGeometry(QRect(477, 17, 75, 20))
        self.label_524.setFont(font1)
        self.label_524.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_525 = QLabel(self.frame_64)
        self.label_525.setObjectName(u"label_525")
        self.label_525.setGeometry(QRect(354, 44, 151, 20))
        self.label_525.setFont(font1)
        self.label_525.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_526 = QLabel(self.frame_64)
        self.label_526.setObjectName(u"label_526")
        self.label_526.setGeometry(QRect(10, 99, 291, 269))
        self.label_526.setStyleSheet(u"border-radius:5px;")
        self.label_526.setPixmap(QPixmap(u"PropImages/Mumbai/Mumbai-Andheri.Tathastu/Mumbai-4.1.jpg"))
        self.label_526.setScaledContents(True)
        self.line_34 = QFrame(self.frame_64)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setGeometry(QRect(307, 99, 16, 269))
        self.line_34.setFrameShape(QFrame.Shape.VLine)
        self.line_34.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_527 = QLabel(self.frame_64)
        self.label_527.setObjectName(u"label_527")
        self.label_527.setGeometry(QRect(377, 99, 175, 44))
        self.label_527.setFont(font6)
        self.label_527.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_35 = QFrame(self.frame_64)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setGeometry(QRect(316, 185, 274, 16))
        self.line_35.setFrameShape(QFrame.Shape.HLine)
        self.line_35.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_528 = QLabel(self.frame_64)
        self.label_528.setObjectName(u"label_528")
        self.label_528.setGeometry(QRect(377, 194, 120, 44))
        self.label_528.setFont(font6)
        self.label_528.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_529 = QLabel(self.frame_64)
        self.label_529.setObjectName(u"label_529")
        self.label_529.setGeometry(QRect(373, 290, 152, 66))
        self.label_529.setFont(font6)
        self.label_529.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_530 = QLabel(self.frame_64)
        self.label_530.setObjectName(u"label_530")
        self.label_530.setGeometry(QRect(10, 75, 500, 18))
        self.label_530.setFont(font7)
        self.label_530.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_36 = QFrame(self.frame_64)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setGeometry(QRect(316, 279, 274, 16))
        self.line_36.setFrameShape(QFrame.Shape.HLine)
        self.line_36.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.frame_64, 1, 0, 1, 1)

        self.frame_68 = QFrame(self.frame_15)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFont(font3)
        self.frame_68.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_68.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Shadow.Raised)
        self.label_564 = QLabel(self.frame_68)
        self.label_564.setObjectName(u"label_564")
        self.label_564.setGeometry(QRect(13, 10, 181, 33))
        self.label_564.setFont(font4)
        self.label_564.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_565 = QLabel(self.frame_68)
        self.label_565.setObjectName(u"label_565")
        self.label_565.setGeometry(QRect(16, 49, 16, 16))
        self.label_565.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_566 = QLabel(self.frame_68)
        self.label_566.setObjectName(u"label_566")
        self.label_566.setGeometry(QRect(35, 49, 81, 16))
        self.label_566.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_70 = QPushButton(self.frame_68)
        self.pushButton_70.setObjectName(u"pushButton_70")
        self.pushButton_70.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_70.setStyleSheet(u"QPushButton\n"
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
        self.label_567 = QLabel(self.frame_68)
        self.label_567.setObjectName(u"label_567")
        self.label_567.setGeometry(QRect(285, 10, 191, 31))
        self.label_567.setFont(font5)
        self.label_567.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_568 = QLabel(self.frame_68)
        self.label_568.setObjectName(u"label_568")
        self.label_568.setGeometry(QRect(477, 17, 75, 20))
        self.label_568.setFont(font1)
        self.label_568.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_569 = QLabel(self.frame_68)
        self.label_569.setObjectName(u"label_569")
        self.label_569.setGeometry(QRect(354, 44, 151, 20))
        self.label_569.setFont(font1)
        self.label_569.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_570 = QLabel(self.frame_68)
        self.label_570.setObjectName(u"label_570")
        self.label_570.setGeometry(QRect(10, 99, 291, 269))
        self.label_570.setStyleSheet(u"border-radius:5px;")
        self.label_570.setPixmap(QPixmap(u":/shivam/PropImages/WhatsApp Image 2024-07-05 at 17.29.33_eac17ca7.jpg"))
        self.label_570.setScaledContents(True)
        self.line_46 = QFrame(self.frame_68)
        self.line_46.setObjectName(u"line_46")
        self.line_46.setGeometry(QRect(307, 99, 16, 269))
        self.line_46.setFrameShape(QFrame.Shape.VLine)
        self.line_46.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_571 = QLabel(self.frame_68)
        self.label_571.setObjectName(u"label_571")
        self.label_571.setGeometry(QRect(377, 99, 175, 44))
        self.label_571.setFont(font6)
        self.label_571.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_47 = QFrame(self.frame_68)
        self.line_47.setObjectName(u"line_47")
        self.line_47.setGeometry(QRect(316, 185, 274, 16))
        self.line_47.setFrameShape(QFrame.Shape.HLine)
        self.line_47.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_572 = QLabel(self.frame_68)
        self.label_572.setObjectName(u"label_572")
        self.label_572.setGeometry(QRect(377, 194, 120, 44))
        self.label_572.setFont(font6)
        self.label_572.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_573 = QLabel(self.frame_68)
        self.label_573.setObjectName(u"label_573")
        self.label_573.setGeometry(QRect(377, 290, 152, 66))
        self.label_573.setFont(font6)
        self.label_573.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_574 = QLabel(self.frame_68)
        self.label_574.setObjectName(u"label_574")
        self.label_574.setGeometry(QRect(10, 75, 501, 18))
        self.label_574.setFont(font7)
        self.label_574.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_48 = QFrame(self.frame_68)
        self.line_48.setObjectName(u"line_48")
        self.line_48.setGeometry(QRect(316, 279, 274, 16))
        self.line_48.setFrameShape(QFrame.Shape.HLine)
        self.line_48.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.frame_68, 3, 0, 1, 1)

        self.frame_67 = QFrame(self.frame_15)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFont(font3)
        self.frame_67.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_67.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Shadow.Raised)
        self.label_553 = QLabel(self.frame_67)
        self.label_553.setObjectName(u"label_553")
        self.label_553.setGeometry(QRect(13, 10, 161, 33))
        self.label_553.setFont(font4)
        self.label_553.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_554 = QLabel(self.frame_67)
        self.label_554.setObjectName(u"label_554")
        self.label_554.setGeometry(QRect(16, 49, 16, 16))
        self.label_554.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_555 = QLabel(self.frame_67)
        self.label_555.setObjectName(u"label_555")
        self.label_555.setGeometry(QRect(35, 49, 81, 16))
        self.label_555.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_69 = QPushButton(self.frame_67)
        self.pushButton_69.setObjectName(u"pushButton_69")
        self.pushButton_69.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_69.setStyleSheet(u"QPushButton\n"
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
        self.label_556 = QLabel(self.frame_67)
        self.label_556.setObjectName(u"label_556")
        self.label_556.setGeometry(QRect(298, 10, 182, 31))
        self.label_556.setFont(font5)
        self.label_556.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_557 = QLabel(self.frame_67)
        self.label_557.setObjectName(u"label_557")
        self.label_557.setGeometry(QRect(477, 17, 75, 20))
        self.label_557.setFont(font1)
        self.label_557.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_558 = QLabel(self.frame_67)
        self.label_558.setObjectName(u"label_558")
        self.label_558.setGeometry(QRect(354, 44, 151, 20))
        self.label_558.setFont(font1)
        self.label_558.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_559 = QLabel(self.frame_67)
        self.label_559.setObjectName(u"label_559")
        self.label_559.setGeometry(QRect(10, 99, 291, 269))
        self.label_559.setStyleSheet(u"border-radius:5px;")
        self.label_559.setPixmap(QPixmap(u"PropImages/Mumbai/Mumbai-3-LowerParel.LodhaPark/Mumbai-3.1_1_11zon.jpg"))
        self.label_559.setScaledContents(True)
        self.line_43 = QFrame(self.frame_67)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setGeometry(QRect(307, 99, 16, 269))
        self.line_43.setFrameShape(QFrame.Shape.VLine)
        self.line_43.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_560 = QLabel(self.frame_67)
        self.label_560.setObjectName(u"label_560")
        self.label_560.setGeometry(QRect(377, 99, 175, 44))
        self.label_560.setFont(font6)
        self.label_560.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_44 = QFrame(self.frame_67)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setGeometry(QRect(316, 185, 274, 16))
        self.line_44.setFrameShape(QFrame.Shape.HLine)
        self.line_44.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_561 = QLabel(self.frame_67)
        self.label_561.setObjectName(u"label_561")
        self.label_561.setGeometry(QRect(377, 194, 120, 44))
        self.label_561.setFont(font6)
        self.label_561.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_562 = QLabel(self.frame_67)
        self.label_562.setObjectName(u"label_562")
        self.label_562.setGeometry(QRect(377, 290, 152, 66))
        self.label_562.setFont(font6)
        self.label_562.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_563 = QLabel(self.frame_67)
        self.label_563.setObjectName(u"label_563")
        self.label_563.setGeometry(QRect(10, 75, 471, 18))
        self.label_563.setFont(font7)
        self.label_563.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_45 = QFrame(self.frame_67)
        self.line_45.setObjectName(u"line_45")
        self.line_45.setGeometry(QRect(316, 279, 274, 16))
        self.line_45.setFrameShape(QFrame.Shape.HLine)
        self.line_45.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.frame_67, 2, 1, 1, 1)

        self.frame_66 = QFrame(self.frame_15)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFont(font3)
        self.frame_66.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_66.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Shadow.Raised)
        self.label_542 = QLabel(self.frame_66)
        self.label_542.setObjectName(u"label_542")
        self.label_542.setGeometry(QRect(13, 10, 241, 33))
        self.label_542.setFont(font4)
        self.label_542.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_543 = QLabel(self.frame_66)
        self.label_543.setObjectName(u"label_543")
        self.label_543.setGeometry(QRect(16, 49, 16, 16))
        self.label_543.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_544 = QLabel(self.frame_66)
        self.label_544.setObjectName(u"label_544")
        self.label_544.setGeometry(QRect(35, 49, 111, 16))
        self.label_544.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_68 = QPushButton(self.frame_66)
        self.pushButton_68.setObjectName(u"pushButton_68")
        self.pushButton_68.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_68.setStyleSheet(u"QPushButton\n"
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
        self.label_545 = QLabel(self.frame_66)
        self.label_545.setObjectName(u"label_545")
        self.label_545.setGeometry(QRect(284, 10, 201, 31))
        self.label_545.setFont(font5)
        self.label_545.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_546 = QLabel(self.frame_66)
        self.label_546.setObjectName(u"label_546")
        self.label_546.setGeometry(QRect(477, 17, 75, 20))
        self.label_546.setFont(font1)
        self.label_546.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_547 = QLabel(self.frame_66)
        self.label_547.setObjectName(u"label_547")
        self.label_547.setGeometry(QRect(354, 44, 151, 20))
        self.label_547.setFont(font1)
        self.label_547.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_548 = QLabel(self.frame_66)
        self.label_548.setObjectName(u"label_548")
        self.label_548.setGeometry(QRect(10, 99, 291, 269))
        self.label_548.setStyleSheet(u"border-radius:5px;")
        self.label_548.setPixmap(QPixmap(u"PropImages/Mumbai/Mumbai-Ghatkopar.Rajshree/Mumbai-1.jpg"))
        self.label_548.setScaledContents(True)
        self.line_40 = QFrame(self.frame_66)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setGeometry(QRect(307, 99, 16, 269))
        self.line_40.setFrameShape(QFrame.Shape.VLine)
        self.line_40.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_549 = QLabel(self.frame_66)
        self.label_549.setObjectName(u"label_549")
        self.label_549.setGeometry(QRect(377, 99, 175, 44))
        self.label_549.setFont(font6)
        self.label_549.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_41 = QFrame(self.frame_66)
        self.line_41.setObjectName(u"line_41")
        self.line_41.setGeometry(QRect(316, 185, 274, 16))
        self.line_41.setFrameShape(QFrame.Shape.HLine)
        self.line_41.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_550 = QLabel(self.frame_66)
        self.label_550.setObjectName(u"label_550")
        self.label_550.setGeometry(QRect(377, 194, 120, 44))
        self.label_550.setFont(font6)
        self.label_550.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_551 = QLabel(self.frame_66)
        self.label_551.setObjectName(u"label_551")
        self.label_551.setGeometry(QRect(377, 290, 152, 66))
        self.label_551.setFont(font6)
        self.label_551.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_552 = QLabel(self.frame_66)
        self.label_552.setObjectName(u"label_552")
        self.label_552.setGeometry(QRect(10, 75, 521, 18))
        self.label_552.setFont(font7)
        self.label_552.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_42 = QFrame(self.frame_66)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setGeometry(QRect(316, 279, 274, 16))
        self.line_42.setFrameShape(QFrame.Shape.HLine)
        self.line_42.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.frame_66, 2, 0, 1, 1)

        self.frame_62 = QFrame(self.frame_15)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFont(font3)
        self.frame_62.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_62.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Shadow.Raised)
        self.label_7 = QLabel(self.frame_62)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(13, 10, 147, 33))
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_499 = QLabel(self.frame_62)
        self.label_499.setObjectName(u"label_499")
        self.label_499.setGeometry(QRect(16, 49, 16, 16))
        self.label_499.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_500 = QLabel(self.frame_62)
        self.label_500.setObjectName(u"label_500")
        self.label_500.setGeometry(QRect(35, 49, 52, 16))
        self.label_500.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_50 = QPushButton(self.frame_62)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_50.setStyleSheet(u"QPushButton\n"
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
        self.label_501 = QLabel(self.frame_62)
        self.label_501.setObjectName(u"label_501")
        self.label_501.setGeometry(QRect(298, 10, 182, 31))
        self.label_501.setFont(font5)
        self.label_501.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_502 = QLabel(self.frame_62)
        self.label_502.setObjectName(u"label_502")
        self.label_502.setGeometry(QRect(477, 17, 75, 20))
        self.label_502.setFont(font1)
        self.label_502.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_503 = QLabel(self.frame_62)
        self.label_503.setObjectName(u"label_503")
        self.label_503.setGeometry(QRect(354, 44, 151, 20))
        self.label_503.setFont(font1)
        self.label_503.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_504 = QLabel(self.frame_62)
        self.label_504.setObjectName(u"label_504")
        self.label_504.setGeometry(QRect(10, 99, 291, 269))
        self.label_504.setStyleSheet(u"border-radius:5px;")
        self.label_504.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Santacruz.Courtyard/Mumbai-6.5.jpg"))
        self.label_504.setScaledContents(True)
        self.line_28 = QFrame(self.frame_62)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setGeometry(QRect(307, 99, 16, 269))
        self.line_28.setFrameShape(QFrame.Shape.VLine)
        self.line_28.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_505 = QLabel(self.frame_62)
        self.label_505.setObjectName(u"label_505")
        self.label_505.setGeometry(QRect(377, 99, 175, 44))
        self.label_505.setFont(font6)
        self.label_505.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_29 = QFrame(self.frame_62)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setGeometry(QRect(316, 185, 274, 16))
        self.line_29.setFrameShape(QFrame.Shape.HLine)
        self.line_29.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_506 = QLabel(self.frame_62)
        self.label_506.setObjectName(u"label_506")
        self.label_506.setGeometry(QRect(377, 194, 120, 44))
        self.label_506.setFont(font6)
        self.label_506.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_507 = QLabel(self.frame_62)
        self.label_507.setObjectName(u"label_507")
        self.label_507.setGeometry(QRect(377, 288, 152, 66))
        self.label_507.setFont(font6)
        self.label_507.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_508 = QLabel(self.frame_62)
        self.label_508.setObjectName(u"label_508")
        self.label_508.setGeometry(QRect(10, 75, 410, 18))
        self.label_508.setFont(font7)
        self.label_508.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_30 = QFrame(self.frame_62)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setGeometry(QRect(316, 279, 274, 16))
        self.line_30.setFrameShape(QFrame.Shape.HLine)
        self.line_30.setFrameShadow(QFrame.Shadow.Sunken)
        self.pushButton_74 = QPushButton(self.frame_62)
        self.pushButton_74.setObjectName(u"pushButton_74")
        self.pushButton_74.setGeometry(QRect(10, 100, 291, 271))
        self.pushButton_74.setStyleSheet(u"border:none;\n"
"background-color:none;")

        self.gridLayout_5.addWidget(self.frame_62, 0, 0, 1, 1)

        self.frame_69 = QFrame(self.frame_15)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFont(font3)
        self.frame_69.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_69.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Shadow.Raised)
        self.label_575 = QLabel(self.frame_69)
        self.label_575.setObjectName(u"label_575")
        self.label_575.setGeometry(QRect(13, 10, 231, 33))
        self.label_575.setFont(font4)
        self.label_575.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_576 = QLabel(self.frame_69)
        self.label_576.setObjectName(u"label_576")
        self.label_576.setGeometry(QRect(16, 49, 16, 16))
        self.label_576.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_577 = QLabel(self.frame_69)
        self.label_577.setObjectName(u"label_577")
        self.label_577.setGeometry(QRect(35, 49, 101, 16))
        self.label_577.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_71 = QPushButton(self.frame_69)
        self.pushButton_71.setObjectName(u"pushButton_71")
        self.pushButton_71.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_71.setStyleSheet(u"QPushButton\n"
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
        self.label_578 = QLabel(self.frame_69)
        self.label_578.setObjectName(u"label_578")
        self.label_578.setGeometry(QRect(294, 10, 182, 31))
        self.label_578.setFont(font5)
        self.label_578.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_579 = QLabel(self.frame_69)
        self.label_579.setObjectName(u"label_579")
        self.label_579.setGeometry(QRect(467, 17, 91, 20))
        self.label_579.setFont(font1)
        self.label_579.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_580 = QLabel(self.frame_69)
        self.label_580.setObjectName(u"label_580")
        self.label_580.setGeometry(QRect(354, 44, 151, 20))
        self.label_580.setFont(font1)
        self.label_580.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_581 = QLabel(self.frame_69)
        self.label_581.setObjectName(u"label_581")
        self.label_581.setGeometry(QRect(10, 99, 291, 269))
        self.label_581.setStyleSheet(u"border-radius:5px;")
        self.label_581.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Ghatkopar.Rajshree/Mumbai-1.6-RF.jpg"))
        self.label_581.setScaledContents(True)
        self.line_97 = QFrame(self.frame_69)
        self.line_97.setObjectName(u"line_97")
        self.line_97.setGeometry(QRect(307, 99, 16, 269))
        self.line_97.setFrameShape(QFrame.Shape.VLine)
        self.line_97.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_582 = QLabel(self.frame_69)
        self.label_582.setObjectName(u"label_582")
        self.label_582.setGeometry(QRect(377, 99, 175, 44))
        self.label_582.setFont(font6)
        self.label_582.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_98 = QFrame(self.frame_69)
        self.line_98.setObjectName(u"line_98")
        self.line_98.setGeometry(QRect(316, 185, 274, 16))
        self.line_98.setFrameShape(QFrame.Shape.HLine)
        self.line_98.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_583 = QLabel(self.frame_69)
        self.label_583.setObjectName(u"label_583")
        self.label_583.setGeometry(QRect(377, 194, 120, 44))
        self.label_583.setFont(font6)
        self.label_583.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_584 = QLabel(self.frame_69)
        self.label_584.setObjectName(u"label_584")
        self.label_584.setGeometry(QRect(377, 290, 152, 66))
        self.label_584.setFont(font6)
        self.label_584.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_585 = QLabel(self.frame_69)
        self.label_585.setObjectName(u"label_585")
        self.label_585.setGeometry(QRect(10, 75, 410, 18))
        self.label_585.setFont(font7)
        self.label_585.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_99 = QFrame(self.frame_69)
        self.line_99.setObjectName(u"line_99")
        self.line_99.setGeometry(QRect(316, 279, 274, 16))
        self.line_99.setFrameShape(QFrame.Shape.HLine)
        self.line_99.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.frame_69, 3, 1, 1, 1)

        self.frame_65 = QFrame(self.frame_15)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFont(font3)
        self.frame_65.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_65.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Shadow.Raised)
        self.label_531 = QLabel(self.frame_65)
        self.label_531.setObjectName(u"label_531")
        self.label_531.setGeometry(QRect(13, 10, 220, 33))
        self.label_531.setFont(font4)
        self.label_531.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_532 = QLabel(self.frame_65)
        self.label_532.setObjectName(u"label_532")
        self.label_532.setGeometry(QRect(16, 49, 16, 16))
        self.label_532.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_533 = QLabel(self.frame_65)
        self.label_533.setObjectName(u"label_533")
        self.label_533.setGeometry(QRect(35, 49, 200, 16))
        self.label_533.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_53 = QPushButton(self.frame_65)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_53.setStyleSheet(u"QPushButton\n"
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
        self.label_534 = QLabel(self.frame_65)
        self.label_534.setObjectName(u"label_534")
        self.label_534.setGeometry(QRect(283, 10, 191, 31))
        self.label_534.setFont(font5)
        self.label_534.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_535 = QLabel(self.frame_65)
        self.label_535.setObjectName(u"label_535")
        self.label_535.setGeometry(QRect(477, 17, 75, 20))
        self.label_535.setFont(font1)
        self.label_535.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_536 = QLabel(self.frame_65)
        self.label_536.setObjectName(u"label_536")
        self.label_536.setGeometry(QRect(354, 44, 151, 20))
        self.label_536.setFont(font1)
        self.label_536.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_537 = QLabel(self.frame_65)
        self.label_537.setObjectName(u"label_537")
        self.label_537.setGeometry(QRect(10, 99, 291, 269))
        self.label_537.setStyleSheet(u"border-radius:5px;")
        self.label_537.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Boriwali.VKLALHariPhasI/Mumbai - 5.jpg"))
        self.label_537.setScaledContents(True)
        self.line_37 = QFrame(self.frame_65)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setGeometry(QRect(307, 99, 16, 269))
        self.line_37.setFrameShape(QFrame.Shape.VLine)
        self.line_37.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_538 = QLabel(self.frame_65)
        self.label_538.setObjectName(u"label_538")
        self.label_538.setGeometry(QRect(377, 99, 175, 44))
        self.label_538.setFont(font6)
        self.label_538.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_38 = QFrame(self.frame_65)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setGeometry(QRect(316, 185, 274, 16))
        self.line_38.setFrameShape(QFrame.Shape.HLine)
        self.line_38.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_539 = QLabel(self.frame_65)
        self.label_539.setObjectName(u"label_539")
        self.label_539.setGeometry(QRect(377, 194, 120, 44))
        self.label_539.setFont(font6)
        self.label_539.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_540 = QLabel(self.frame_65)
        self.label_540.setObjectName(u"label_540")
        self.label_540.setGeometry(QRect(377, 290, 152, 66))
        self.label_540.setFont(font6)
        self.label_540.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_541 = QLabel(self.frame_65)
        self.label_541.setObjectName(u"label_541")
        self.label_541.setGeometry(QRect(10, 75, 421, 18))
        self.label_541.setFont(font7)
        self.label_541.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_39 = QFrame(self.frame_65)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setGeometry(QRect(316, 279, 274, 16))
        self.line_39.setFrameShape(QFrame.Shape.HLine)
        self.line_39.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.frame_65, 1, 1, 1, 1)

        self.frame_63 = QFrame(self.frame_15)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFont(font3)
        self.frame_63.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_63.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Shadow.Raised)
        self.label_509 = QLabel(self.frame_63)
        self.label_509.setObjectName(u"label_509")
        self.label_509.setGeometry(QRect(13, 10, 180, 33))
        self.label_509.setFont(font4)
        self.label_509.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_510 = QLabel(self.frame_63)
        self.label_510.setObjectName(u"label_510")
        self.label_510.setGeometry(QRect(16, 49, 16, 16))
        self.label_510.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_511 = QLabel(self.frame_63)
        self.label_511.setObjectName(u"label_511")
        self.label_511.setGeometry(QRect(35, 49, 150, 16))
        self.label_511.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_51 = QPushButton(self.frame_63)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_51.setStyleSheet(u"QPushButton\n"
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
        self.label_512 = QLabel(self.frame_63)
        self.label_512.setObjectName(u"label_512")
        self.label_512.setGeometry(QRect(298, 10, 182, 31))
        self.label_512.setFont(font5)
        self.label_512.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_513 = QLabel(self.frame_63)
        self.label_513.setObjectName(u"label_513")
        self.label_513.setGeometry(QRect(477, 17, 95, 20))
        self.label_513.setFont(font1)
        self.label_513.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_514 = QLabel(self.frame_63)
        self.label_514.setObjectName(u"label_514")
        self.label_514.setGeometry(QRect(354, 44, 151, 20))
        self.label_514.setFont(font1)
        self.label_514.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_515 = QLabel(self.frame_63)
        self.label_515.setObjectName(u"label_515")
        self.label_515.setGeometry(QRect(10, 99, 291, 269))
        self.label_515.setStyleSheet(u"border-radius:5px;")
        self.label_515.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Malad.PratapLibertyOne/Mumbai-2.jpg"))
        self.label_515.setScaledContents(True)
        self.line_31 = QFrame(self.frame_63)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setGeometry(QRect(307, 99, 16, 269))
        self.line_31.setFrameShape(QFrame.Shape.VLine)
        self.line_31.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_516 = QLabel(self.frame_63)
        self.label_516.setObjectName(u"label_516")
        self.label_516.setGeometry(QRect(377, 99, 175, 44))
        self.label_516.setFont(font6)
        self.label_516.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_32 = QFrame(self.frame_63)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setGeometry(QRect(316, 185, 274, 16))
        self.line_32.setFrameShape(QFrame.Shape.HLine)
        self.line_32.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_517 = QLabel(self.frame_63)
        self.label_517.setObjectName(u"label_517")
        self.label_517.setGeometry(QRect(377, 194, 120, 44))
        self.label_517.setFont(font6)
        self.label_517.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_518 = QLabel(self.frame_63)
        self.label_518.setObjectName(u"label_518")
        self.label_518.setGeometry(QRect(377, 290, 152, 66))
        self.label_518.setFont(font6)
        self.label_518.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_519 = QLabel(self.frame_63)
        self.label_519.setObjectName(u"label_519")
        self.label_519.setGeometry(QRect(10, 75, 550, 18))
        self.label_519.setFont(font7)
        self.label_519.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_33 = QFrame(self.frame_63)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setGeometry(QRect(316, 279, 274, 16))
        self.line_33.setFrameShape(QFrame.Shape.HLine)
        self.line_33.setFrameShadow(QFrame.Shadow.Sunken)
        self.pushButton_75 = QPushButton(self.frame_63)
        self.pushButton_75.setObjectName(u"pushButton_75")
        self.pushButton_75.setGeometry(QRect(10, 100, 291, 271))
        self.pushButton_75.setStyleSheet(u"border:none;\n"
"background-color:none;")

        self.gridLayout_5.addWidget(self.frame_63, 0, 1, 1, 1)


        self.verticalLayout_78.addLayout(self.gridLayout_5)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(10)
        self.gridLayout_6.setContentsMargins(50, 35, -1, 60)
        self.frame_86 = QFrame(self.frame_15)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFont(font3)
        self.frame_86.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_86.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Shadow.Raised)
        self.label_762 = QLabel(self.frame_86)
        self.label_762.setObjectName(u"label_762")
        self.label_762.setGeometry(QRect(13, 10, 181, 33))
        self.label_762.setFont(font4)
        self.label_762.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_763 = QLabel(self.frame_86)
        self.label_763.setObjectName(u"label_763")
        self.label_763.setGeometry(QRect(16, 49, 16, 16))
        self.label_763.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_764 = QLabel(self.frame_86)
        self.label_764.setObjectName(u"label_764")
        self.label_764.setGeometry(QRect(35, 49, 81, 16))
        self.label_764.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_88 = QPushButton(self.frame_86)
        self.pushButton_88.setObjectName(u"pushButton_88")
        self.pushButton_88.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_88.setStyleSheet(u"QPushButton\n"
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
        self.label_765 = QLabel(self.frame_86)
        self.label_765.setObjectName(u"label_765")
        self.label_765.setGeometry(QRect(300, 10, 182, 31))
        self.label_765.setFont(font5)
        self.label_765.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_766 = QLabel(self.frame_86)
        self.label_766.setObjectName(u"label_766")
        self.label_766.setGeometry(QRect(467, 17, 91, 20))
        self.label_766.setFont(font1)
        self.label_766.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_767 = QLabel(self.frame_86)
        self.label_767.setObjectName(u"label_767")
        self.label_767.setGeometry(QRect(354, 44, 151, 20))
        self.label_767.setFont(font1)
        self.label_767.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.line_148 = QFrame(self.frame_86)
        self.line_148.setObjectName(u"line_148")
        self.line_148.setGeometry(QRect(307, 99, 16, 269))
        self.line_148.setFrameShape(QFrame.Shape.VLine)
        self.line_148.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_768 = QLabel(self.frame_86)
        self.label_768.setObjectName(u"label_768")
        self.label_768.setGeometry(QRect(377, 99, 175, 44))
        self.label_768.setFont(font6)
        self.label_768.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_149 = QFrame(self.frame_86)
        self.line_149.setObjectName(u"line_149")
        self.line_149.setGeometry(QRect(316, 185, 274, 16))
        self.line_149.setFrameShape(QFrame.Shape.HLine)
        self.line_149.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_769 = QLabel(self.frame_86)
        self.label_769.setObjectName(u"label_769")
        self.label_769.setGeometry(QRect(377, 194, 120, 44))
        self.label_769.setFont(font6)
        self.label_769.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_770 = QLabel(self.frame_86)
        self.label_770.setObjectName(u"label_770")
        self.label_770.setGeometry(QRect(377, 289, 152, 66))
        self.label_770.setFont(font6)
        self.label_770.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_771 = QLabel(self.frame_86)
        self.label_771.setObjectName(u"label_771")
        self.label_771.setGeometry(QRect(10, 75, 191, 18))
        self.label_771.setFont(font7)
        self.label_771.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_150 = QFrame(self.frame_86)
        self.line_150.setObjectName(u"line_150")
        self.line_150.setGeometry(QRect(316, 279, 274, 16))
        self.line_150.setFrameShape(QFrame.Shape.HLine)
        self.line_150.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_772 = QLabel(self.frame_86)
        self.label_772.setObjectName(u"label_772")
        self.label_772.setGeometry(QRect(10, 99, 291, 269))
        self.label_772.setStyleSheet(u"border-radius:5px;")
        self.label_772.setPixmap(QPixmap(u":/shivam/PropImages/Thane/Thane-AsharMerac/Thane-2.1.Elevtion.jpg"))
        self.label_772.setScaledContents(True)

        self.gridLayout_6.addWidget(self.frame_86, 0, 1, 1, 1)

        self.frame_87 = QFrame(self.frame_15)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFont(font3)
        self.frame_87.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_87.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Shadow.Raised)
        self.label_773 = QLabel(self.frame_87)
        self.label_773.setObjectName(u"label_773")
        self.label_773.setGeometry(QRect(13, 10, 261, 33))
        self.label_773.setFont(font4)
        self.label_773.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_774 = QLabel(self.frame_87)
        self.label_774.setObjectName(u"label_774")
        self.label_774.setGeometry(QRect(16, 49, 16, 16))
        self.label_774.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_775 = QLabel(self.frame_87)
        self.label_775.setObjectName(u"label_775")
        self.label_775.setGeometry(QRect(35, 49, 71, 16))
        self.label_775.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_89 = QPushButton(self.frame_87)
        self.pushButton_89.setObjectName(u"pushButton_89")
        self.pushButton_89.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_89.setStyleSheet(u"QPushButton\n"
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
        self.label_776 = QLabel(self.frame_87)
        self.label_776.setObjectName(u"label_776")
        self.label_776.setGeometry(QRect(298, 10, 231, 31))
        self.label_776.setFont(font8)
        self.label_776.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_777 = QLabel(self.frame_87)
        self.label_777.setObjectName(u"label_777")
        self.label_777.setGeometry(QRect(477, 17, 75, 20))
        self.label_777.setFont(font1)
        self.label_777.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_778 = QLabel(self.frame_87)
        self.label_778.setObjectName(u"label_778")
        self.label_778.setGeometry(QRect(354, 44, 151, 20))
        self.label_778.setFont(font1)
        self.label_778.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_779 = QLabel(self.frame_87)
        self.label_779.setObjectName(u"label_779")
        self.label_779.setGeometry(QRect(10, 99, 291, 269))
        self.label_779.setStyleSheet(u"border-radius:5px;")
        self.label_779.setPixmap(QPixmap(u":/shivam/PropImages/Thane/Thane-ShivlayaHeights/Thane-3.jpg"))
        self.label_779.setScaledContents(True)
        self.line_151 = QFrame(self.frame_87)
        self.line_151.setObjectName(u"line_151")
        self.line_151.setGeometry(QRect(307, 99, 16, 269))
        self.line_151.setFrameShape(QFrame.Shape.VLine)
        self.line_151.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_780 = QLabel(self.frame_87)
        self.label_780.setObjectName(u"label_780")
        self.label_780.setGeometry(QRect(377, 99, 175, 44))
        self.label_780.setFont(font6)
        self.label_780.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_152 = QFrame(self.frame_87)
        self.line_152.setObjectName(u"line_152")
        self.line_152.setGeometry(QRect(316, 185, 274, 16))
        self.line_152.setFrameShape(QFrame.Shape.HLine)
        self.line_152.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_781 = QLabel(self.frame_87)
        self.label_781.setObjectName(u"label_781")
        self.label_781.setGeometry(QRect(377, 194, 120, 44))
        self.label_781.setFont(font6)
        self.label_781.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_782 = QLabel(self.frame_87)
        self.label_782.setObjectName(u"label_782")
        self.label_782.setGeometry(QRect(377, 290, 152, 66))
        self.label_782.setFont(font6)
        self.label_782.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_783 = QLabel(self.frame_87)
        self.label_783.setObjectName(u"label_783")
        self.label_783.setGeometry(QRect(10, 75, 421, 18))
        self.label_783.setFont(font7)
        self.label_783.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_153 = QFrame(self.frame_87)
        self.line_153.setObjectName(u"line_153")
        self.line_153.setGeometry(QRect(316, 279, 274, 16))
        self.line_153.setFrameShape(QFrame.Shape.HLine)
        self.line_153.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.frame_87, 1, 0, 1, 1)

        self.frame_88 = QFrame(self.frame_15)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setFont(font3)
        self.frame_88.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_88.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Shadow.Raised)
        self.label_784 = QLabel(self.frame_88)
        self.label_784.setObjectName(u"label_784")
        self.label_784.setGeometry(QRect(13, 10, 161, 33))
        self.label_784.setFont(font4)
        self.label_784.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_785 = QLabel(self.frame_88)
        self.label_785.setObjectName(u"label_785")
        self.label_785.setGeometry(QRect(16, 49, 16, 16))
        self.label_785.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_786 = QLabel(self.frame_88)
        self.label_786.setObjectName(u"label_786")
        self.label_786.setGeometry(QRect(35, 49, 111, 16))
        self.label_786.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_90 = QPushButton(self.frame_88)
        self.pushButton_90.setObjectName(u"pushButton_90")
        self.pushButton_90.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_90.setStyleSheet(u"QPushButton\n"
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
        self.label_787 = QLabel(self.frame_88)
        self.label_787.setObjectName(u"label_787")
        self.label_787.setGeometry(QRect(285, 10, 191, 31))
        self.label_787.setFont(font5)
        self.label_787.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_788 = QLabel(self.frame_88)
        self.label_788.setObjectName(u"label_788")
        self.label_788.setGeometry(QRect(477, 17, 91, 20))
        self.label_788.setFont(font1)
        self.label_788.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_789 = QLabel(self.frame_88)
        self.label_789.setObjectName(u"label_789")
        self.label_789.setGeometry(QRect(354, 44, 151, 20))
        self.label_789.setFont(font1)
        self.label_789.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_790 = QLabel(self.frame_88)
        self.label_790.setObjectName(u"label_790")
        self.label_790.setGeometry(QRect(10, 99, 291, 269))
        self.label_790.setStyleSheet(u"border-radius:5px;")
        self.label_790.setPixmap(QPixmap(u":/shivam/PropImages/Lake1.jpg"))
        self.label_790.setScaledContents(True)
        self.line_154 = QFrame(self.frame_88)
        self.line_154.setObjectName(u"line_154")
        self.line_154.setGeometry(QRect(307, 99, 16, 269))
        self.line_154.setFrameShape(QFrame.Shape.VLine)
        self.line_154.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_791 = QLabel(self.frame_88)
        self.label_791.setObjectName(u"label_791")
        self.label_791.setGeometry(QRect(377, 99, 175, 44))
        self.label_791.setFont(font6)
        self.label_791.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_155 = QFrame(self.frame_88)
        self.line_155.setObjectName(u"line_155")
        self.line_155.setGeometry(QRect(316, 185, 274, 16))
        self.line_155.setFrameShape(QFrame.Shape.HLine)
        self.line_155.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_792 = QLabel(self.frame_88)
        self.label_792.setObjectName(u"label_792")
        self.label_792.setGeometry(QRect(377, 194, 120, 44))
        self.label_792.setFont(font6)
        self.label_792.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_793 = QLabel(self.frame_88)
        self.label_793.setObjectName(u"label_793")
        self.label_793.setGeometry(QRect(377, 290, 152, 66))
        self.label_793.setFont(font6)
        self.label_793.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_794 = QLabel(self.frame_88)
        self.label_794.setObjectName(u"label_794")
        self.label_794.setGeometry(QRect(10, 75, 410, 18))
        self.label_794.setFont(font7)
        self.label_794.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_156 = QFrame(self.frame_88)
        self.line_156.setObjectName(u"line_156")
        self.line_156.setGeometry(QRect(316, 279, 274, 16))
        self.line_156.setFrameShape(QFrame.Shape.HLine)
        self.line_156.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.frame_88, 3, 1, 1, 1)

        self.frame_89 = QFrame(self.frame_15)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setFont(font3)
        self.frame_89.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_89.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Shadow.Raised)
        self.label_795 = QLabel(self.frame_89)
        self.label_795.setObjectName(u"label_795")
        self.label_795.setGeometry(QRect(13, 10, 181, 33))
        self.label_795.setFont(font4)
        self.label_795.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_796 = QLabel(self.frame_89)
        self.label_796.setObjectName(u"label_796")
        self.label_796.setGeometry(QRect(16, 49, 16, 16))
        self.label_796.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_797 = QLabel(self.frame_89)
        self.label_797.setObjectName(u"label_797")
        self.label_797.setGeometry(QRect(35, 49, 81, 16))
        self.label_797.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_91 = QPushButton(self.frame_89)
        self.pushButton_91.setObjectName(u"pushButton_91")
        self.pushButton_91.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_91.setStyleSheet(u"QPushButton\n"
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
        self.label_798 = QLabel(self.frame_89)
        self.label_798.setObjectName(u"label_798")
        self.label_798.setGeometry(QRect(298, 10, 182, 31))
        self.label_798.setFont(font5)
        self.label_798.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_799 = QLabel(self.frame_89)
        self.label_799.setObjectName(u"label_799")
        self.label_799.setGeometry(QRect(472, 17, 75, 20))
        self.label_799.setFont(font1)
        self.label_799.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_800 = QLabel(self.frame_89)
        self.label_800.setObjectName(u"label_800")
        self.label_800.setGeometry(QRect(354, 44, 151, 20))
        self.label_800.setFont(font1)
        self.label_800.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_801 = QLabel(self.frame_89)
        self.label_801.setObjectName(u"label_801")
        self.label_801.setGeometry(QRect(10, 99, 291, 269))
        self.label_801.setStyleSheet(u"border-radius:5px;")
        self.label_801.setPixmap(QPixmap(u":/shivam/PropImages/WhatsApp Image 2024-07-05 at 20.11.02_1a624b3c.jpg"))
        self.label_801.setScaledContents(True)
        self.line_157 = QFrame(self.frame_89)
        self.line_157.setObjectName(u"line_157")
        self.line_157.setGeometry(QRect(307, 99, 16, 269))
        self.line_157.setFrameShape(QFrame.Shape.VLine)
        self.line_157.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_802 = QLabel(self.frame_89)
        self.label_802.setObjectName(u"label_802")
        self.label_802.setGeometry(QRect(377, 99, 175, 44))
        self.label_802.setFont(font6)
        self.label_802.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_158 = QFrame(self.frame_89)
        self.line_158.setObjectName(u"line_158")
        self.line_158.setGeometry(QRect(316, 185, 274, 16))
        self.line_158.setFrameShape(QFrame.Shape.HLine)
        self.line_158.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_803 = QLabel(self.frame_89)
        self.label_803.setObjectName(u"label_803")
        self.label_803.setGeometry(QRect(377, 194, 120, 44))
        self.label_803.setFont(font6)
        self.label_803.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_804 = QLabel(self.frame_89)
        self.label_804.setObjectName(u"label_804")
        self.label_804.setGeometry(QRect(377, 290, 152, 66))
        self.label_804.setFont(font6)
        self.label_804.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_805 = QLabel(self.frame_89)
        self.label_805.setObjectName(u"label_805")
        self.label_805.setGeometry(QRect(10, 75, 421, 18))
        self.label_805.setFont(font7)
        self.label_805.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_159 = QFrame(self.frame_89)
        self.line_159.setObjectName(u"line_159")
        self.line_159.setGeometry(QRect(316, 279, 274, 16))
        self.line_159.setFrameShape(QFrame.Shape.HLine)
        self.line_159.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.frame_89, 3, 0, 1, 1)

        self.frame_90 = QFrame(self.frame_15)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setFont(font3)
        self.frame_90.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_90.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Shadow.Raised)
        self.label_806 = QLabel(self.frame_90)
        self.label_806.setObjectName(u"label_806")
        self.label_806.setGeometry(QRect(13, 10, 171, 33))
        self.label_806.setFont(font4)
        self.label_806.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_807 = QLabel(self.frame_90)
        self.label_807.setObjectName(u"label_807")
        self.label_807.setGeometry(QRect(16, 49, 16, 16))
        self.label_807.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_808 = QLabel(self.frame_90)
        self.label_808.setObjectName(u"label_808")
        self.label_808.setGeometry(QRect(35, 49, 81, 16))
        self.label_808.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_92 = QPushButton(self.frame_90)
        self.pushButton_92.setObjectName(u"pushButton_92")
        self.pushButton_92.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_92.setStyleSheet(u"QPushButton\n"
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
        self.label_809 = QLabel(self.frame_90)
        self.label_809.setObjectName(u"label_809")
        self.label_809.setGeometry(QRect(294, 10, 182, 31))
        self.label_809.setFont(font5)
        self.label_809.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_810 = QLabel(self.frame_90)
        self.label_810.setObjectName(u"label_810")
        self.label_810.setGeometry(QRect(461, 17, 91, 20))
        self.label_810.setFont(font1)
        self.label_810.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_811 = QLabel(self.frame_90)
        self.label_811.setObjectName(u"label_811")
        self.label_811.setGeometry(QRect(354, 44, 141, 20))
        self.label_811.setFont(font1)
        self.label_811.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_812 = QLabel(self.frame_90)
        self.label_812.setObjectName(u"label_812")
        self.label_812.setGeometry(QRect(10, 99, 291, 269))
        self.label_812.setStyleSheet(u"border-radius:5px;")
        self.label_812.setPixmap(QPixmap(u":/shivam/PropImages/Thane/Thane-DostiHeron/Thane-4.1Elev.jpg"))
        self.label_812.setScaledContents(True)
        self.line_160 = QFrame(self.frame_90)
        self.line_160.setObjectName(u"line_160")
        self.line_160.setGeometry(QRect(307, 99, 16, 269))
        self.line_160.setFrameShape(QFrame.Shape.VLine)
        self.line_160.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_813 = QLabel(self.frame_90)
        self.label_813.setObjectName(u"label_813")
        self.label_813.setGeometry(QRect(377, 99, 175, 44))
        self.label_813.setFont(font6)
        self.label_813.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_161 = QFrame(self.frame_90)
        self.line_161.setObjectName(u"line_161")
        self.line_161.setGeometry(QRect(316, 185, 274, 16))
        self.line_161.setFrameShape(QFrame.Shape.HLine)
        self.line_161.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_814 = QLabel(self.frame_90)
        self.label_814.setObjectName(u"label_814")
        self.label_814.setGeometry(QRect(377, 194, 120, 44))
        self.label_814.setFont(font6)
        self.label_814.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_815 = QLabel(self.frame_90)
        self.label_815.setObjectName(u"label_815")
        self.label_815.setGeometry(QRect(377, 290, 152, 66))
        self.label_815.setFont(font6)
        self.label_815.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_816 = QLabel(self.frame_90)
        self.label_816.setObjectName(u"label_816")
        self.label_816.setGeometry(QRect(10, 75, 241, 18))
        self.label_816.setFont(font7)
        self.label_816.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_162 = QFrame(self.frame_90)
        self.line_162.setObjectName(u"line_162")
        self.line_162.setGeometry(QRect(316, 279, 274, 16))
        self.line_162.setFrameShape(QFrame.Shape.HLine)
        self.line_162.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.frame_90, 1, 1, 1, 1)

        self.frame_91 = QFrame(self.frame_15)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setFont(font3)
        self.frame_91.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_91.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Shadow.Raised)
        self.label_817 = QLabel(self.frame_91)
        self.label_817.setObjectName(u"label_817")
        self.label_817.setGeometry(QRect(13, 10, 231, 33))
        self.label_817.setFont(font4)
        self.label_817.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_818 = QLabel(self.frame_91)
        self.label_818.setObjectName(u"label_818")
        self.label_818.setGeometry(QRect(16, 49, 16, 16))
        self.label_818.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_819 = QLabel(self.frame_91)
        self.label_819.setObjectName(u"label_819")
        self.label_819.setGeometry(QRect(35, 49, 90, 16))
        self.label_819.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_93 = QPushButton(self.frame_91)
        self.pushButton_93.setObjectName(u"pushButton_93")
        self.pushButton_93.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_93.setStyleSheet(u"QPushButton\n"
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
        self.label_820 = QLabel(self.frame_91)
        self.label_820.setObjectName(u"label_820")
        self.label_820.setGeometry(QRect(298, 10, 182, 31))
        self.label_820.setFont(font5)
        self.label_820.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_821 = QLabel(self.frame_91)
        self.label_821.setObjectName(u"label_821")
        self.label_821.setGeometry(QRect(471, 17, 81, 20))
        self.label_821.setFont(font1)
        self.label_821.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_822 = QLabel(self.frame_91)
        self.label_822.setObjectName(u"label_822")
        self.label_822.setGeometry(QRect(354, 44, 151, 20))
        self.label_822.setFont(font1)
        self.label_822.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_823 = QLabel(self.frame_91)
        self.label_823.setObjectName(u"label_823")
        self.label_823.setGeometry(QRect(10, 99, 291, 269))
        self.label_823.setStyleSheet(u"border-radius:5px;")
        self.label_823.setPixmap(QPixmap(u":/shivam/PropImages/Thane/Thane-ParijasHorizon/Thane-5.jpg"))
        self.label_823.setScaledContents(True)
        self.line_163 = QFrame(self.frame_91)
        self.line_163.setObjectName(u"line_163")
        self.line_163.setGeometry(QRect(307, 99, 16, 269))
        self.line_163.setFrameShape(QFrame.Shape.VLine)
        self.line_163.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_824 = QLabel(self.frame_91)
        self.label_824.setObjectName(u"label_824")
        self.label_824.setGeometry(QRect(377, 99, 175, 44))
        self.label_824.setFont(font6)
        self.label_824.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_164 = QFrame(self.frame_91)
        self.line_164.setObjectName(u"line_164")
        self.line_164.setGeometry(QRect(316, 185, 274, 16))
        self.line_164.setFrameShape(QFrame.Shape.HLine)
        self.line_164.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_825 = QLabel(self.frame_91)
        self.label_825.setObjectName(u"label_825")
        self.label_825.setGeometry(QRect(377, 194, 120, 44))
        self.label_825.setFont(font6)
        self.label_825.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_826 = QLabel(self.frame_91)
        self.label_826.setObjectName(u"label_826")
        self.label_826.setGeometry(QRect(377, 290, 152, 66))
        self.label_826.setFont(font6)
        self.label_826.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_827 = QLabel(self.frame_91)
        self.label_827.setObjectName(u"label_827")
        self.label_827.setGeometry(QRect(10, 75, 281, 18))
        self.label_827.setFont(font7)
        self.label_827.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_165 = QFrame(self.frame_91)
        self.line_165.setObjectName(u"line_165")
        self.line_165.setGeometry(QRect(316, 279, 274, 16))
        self.line_165.setFrameShape(QFrame.Shape.HLine)
        self.line_165.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.frame_91, 2, 0, 1, 1)

        self.frame_92 = QFrame(self.frame_15)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setFont(font3)
        self.frame_92.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_92.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Shadow.Raised)
        self.label_828 = QLabel(self.frame_92)
        self.label_828.setObjectName(u"label_828")
        self.label_828.setGeometry(QRect(13, 10, 161, 33))
        self.label_828.setFont(font4)
        self.label_828.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_829 = QLabel(self.frame_92)
        self.label_829.setObjectName(u"label_829")
        self.label_829.setGeometry(QRect(16, 49, 16, 16))
        self.label_829.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_830 = QLabel(self.frame_92)
        self.label_830.setObjectName(u"label_830")
        self.label_830.setGeometry(QRect(35, 49, 81, 16))
        self.label_830.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_94 = QPushButton(self.frame_92)
        self.pushButton_94.setObjectName(u"pushButton_94")
        self.pushButton_94.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_94.setStyleSheet(u"QPushButton\n"
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
        self.label_831 = QLabel(self.frame_92)
        self.label_831.setObjectName(u"label_831")
        self.label_831.setGeometry(QRect(287, 10, 191, 31))
        self.label_831.setFont(font5)
        self.label_831.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_832 = QLabel(self.frame_92)
        self.label_832.setObjectName(u"label_832")
        self.label_832.setGeometry(QRect(477, 17, 75, 20))
        self.label_832.setFont(font1)
        self.label_832.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_833 = QLabel(self.frame_92)
        self.label_833.setObjectName(u"label_833")
        self.label_833.setGeometry(QRect(354, 44, 151, 20))
        self.label_833.setFont(font1)
        self.label_833.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_834 = QLabel(self.frame_92)
        self.label_834.setObjectName(u"label_834")
        self.label_834.setGeometry(QRect(10, 99, 291, 269))
        self.label_834.setStyleSheet(u"border-radius:5px;")
        self.label_834.setPixmap(QPixmap(u":/shivam/PropImages/Thane/Thane-Balkum.Thane.west/Thane-1.jpg"))
        self.label_834.setScaledContents(True)
        self.line_166 = QFrame(self.frame_92)
        self.line_166.setObjectName(u"line_166")
        self.line_166.setGeometry(QRect(307, 99, 16, 269))
        self.line_166.setFrameShape(QFrame.Shape.VLine)
        self.line_166.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_835 = QLabel(self.frame_92)
        self.label_835.setObjectName(u"label_835")
        self.label_835.setGeometry(QRect(377, 99, 175, 44))
        self.label_835.setFont(font6)
        self.label_835.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_167 = QFrame(self.frame_92)
        self.line_167.setObjectName(u"line_167")
        self.line_167.setGeometry(QRect(316, 185, 274, 16))
        self.line_167.setFrameShape(QFrame.Shape.HLine)
        self.line_167.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_836 = QLabel(self.frame_92)
        self.label_836.setObjectName(u"label_836")
        self.label_836.setGeometry(QRect(377, 194, 120, 44))
        self.label_836.setFont(font6)
        self.label_836.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_837 = QLabel(self.frame_92)
        self.label_837.setObjectName(u"label_837")
        self.label_837.setGeometry(QRect(377, 290, 152, 66))
        self.label_837.setFont(font6)
        self.label_837.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_838 = QLabel(self.frame_92)
        self.label_838.setObjectName(u"label_838")
        self.label_838.setGeometry(QRect(10, 75, 410, 18))
        self.label_838.setFont(font7)
        self.label_838.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_168 = QFrame(self.frame_92)
        self.line_168.setObjectName(u"line_168")
        self.line_168.setGeometry(QRect(316, 279, 274, 16))
        self.line_168.setFrameShape(QFrame.Shape.HLine)
        self.line_168.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.frame_92, 0, 0, 1, 1)

        self.frame_93 = QFrame(self.frame_15)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFont(font3)
        self.frame_93.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_93.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Shadow.Raised)
        self.label_839 = QLabel(self.frame_93)
        self.label_839.setObjectName(u"label_839")
        self.label_839.setGeometry(QRect(13, 10, 231, 33))
        self.label_839.setFont(font4)
        self.label_839.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_840 = QLabel(self.frame_93)
        self.label_840.setObjectName(u"label_840")
        self.label_840.setGeometry(QRect(16, 49, 16, 16))
        self.label_840.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_841 = QLabel(self.frame_93)
        self.label_841.setObjectName(u"label_841")
        self.label_841.setGeometry(QRect(35, 49, 71, 16))
        self.label_841.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_95 = QPushButton(self.frame_93)
        self.pushButton_95.setObjectName(u"pushButton_95")
        self.pushButton_95.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_95.setStyleSheet(u"QPushButton\n"
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
        self.label_842 = QLabel(self.frame_93)
        self.label_842.setObjectName(u"label_842")
        self.label_842.setGeometry(QRect(280, 10, 201, 31))
        self.label_842.setFont(font5)
        self.label_842.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_843 = QLabel(self.frame_93)
        self.label_843.setObjectName(u"label_843")
        self.label_843.setGeometry(QRect(484, 17, 75, 20))
        self.label_843.setFont(font1)
        self.label_843.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_844 = QLabel(self.frame_93)
        self.label_844.setObjectName(u"label_844")
        self.label_844.setGeometry(QRect(354, 44, 151, 20))
        self.label_844.setFont(font1)
        self.label_844.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_845 = QLabel(self.frame_93)
        self.label_845.setObjectName(u"label_845")
        self.label_845.setGeometry(QRect(10, 99, 291, 269))
        self.label_845.setStyleSheet(u"border-radius:5px;")
        self.label_845.setPixmap(QPixmap(u":/shivam/PropImages/WhatsApp Image 2024-07-05 at 20.01.08_33b1ab10.jpg"))
        self.label_845.setScaledContents(True)
        self.line_169 = QFrame(self.frame_93)
        self.line_169.setObjectName(u"line_169")
        self.line_169.setGeometry(QRect(307, 99, 16, 269))
        self.line_169.setFrameShape(QFrame.Shape.VLine)
        self.line_169.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_846 = QLabel(self.frame_93)
        self.label_846.setObjectName(u"label_846")
        self.label_846.setGeometry(QRect(377, 99, 175, 44))
        self.label_846.setFont(font6)
        self.label_846.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_170 = QFrame(self.frame_93)
        self.line_170.setObjectName(u"line_170")
        self.line_170.setGeometry(QRect(316, 185, 274, 16))
        self.line_170.setFrameShape(QFrame.Shape.HLine)
        self.line_170.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_847 = QLabel(self.frame_93)
        self.label_847.setObjectName(u"label_847")
        self.label_847.setGeometry(QRect(377, 194, 120, 44))
        self.label_847.setFont(font6)
        self.label_847.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_848 = QLabel(self.frame_93)
        self.label_848.setObjectName(u"label_848")
        self.label_848.setGeometry(QRect(377, 292, 152, 66))
        self.label_848.setFont(font6)
        self.label_848.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_849 = QLabel(self.frame_93)
        self.label_849.setObjectName(u"label_849")
        self.label_849.setGeometry(QRect(10, 75, 410, 18))
        self.label_849.setFont(font7)
        self.label_849.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_171 = QFrame(self.frame_93)
        self.line_171.setObjectName(u"line_171")
        self.line_171.setGeometry(QRect(316, 279, 274, 16))
        self.line_171.setFrameShape(QFrame.Shape.HLine)
        self.line_171.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.frame_93, 2, 1, 1, 1)


        self.verticalLayout_78.addLayout(self.gridLayout_6)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setSpacing(50)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(50, 35, -1, 60)
        self.frame_94 = QFrame(self.frame_15)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setFont(font3)
        self.frame_94.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_94.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Shadow.Raised)
        self.label_850 = QLabel(self.frame_94)
        self.label_850.setObjectName(u"label_850")
        self.label_850.setGeometry(QRect(13, 10, 221, 33))
        self.label_850.setFont(font4)
        self.label_850.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_851 = QLabel(self.frame_94)
        self.label_851.setObjectName(u"label_851")
        self.label_851.setGeometry(QRect(16, 49, 16, 16))
        self.label_851.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_852 = QLabel(self.frame_94)
        self.label_852.setObjectName(u"label_852")
        self.label_852.setGeometry(QRect(35, 49, 190, 16))
        self.label_852.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_96 = QPushButton(self.frame_94)
        self.pushButton_96.setObjectName(u"pushButton_96")
        self.pushButton_96.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_96.setStyleSheet(u"QPushButton\n"
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
        self.label_853 = QLabel(self.frame_94)
        self.label_853.setObjectName(u"label_853")
        self.label_853.setGeometry(QRect(301, 10, 191, 31))
        self.label_853.setFont(font8)
        self.label_853.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_854 = QLabel(self.frame_94)
        self.label_854.setObjectName(u"label_854")
        self.label_854.setGeometry(QRect(482, 17, 75, 20))
        self.label_854.setFont(font1)
        self.label_854.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_855 = QLabel(self.frame_94)
        self.label_855.setObjectName(u"label_855")
        self.label_855.setGeometry(QRect(354, 44, 151, 20))
        self.label_855.setFont(font1)
        self.label_855.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_856 = QLabel(self.frame_94)
        self.label_856.setObjectName(u"label_856")
        self.label_856.setGeometry(QRect(10, 99, 291, 269))
        self.label_856.setStyleSheet(u"border-radius:5px;")
        self.label_856.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Ghatkopar.Rajshree/Mumbai-1.6-RF.jpg"))
        self.label_856.setScaledContents(True)
        self.line_172 = QFrame(self.frame_94)
        self.line_172.setObjectName(u"line_172")
        self.line_172.setGeometry(QRect(307, 99, 16, 269))
        self.line_172.setFrameShape(QFrame.Shape.VLine)
        self.line_172.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_857 = QLabel(self.frame_94)
        self.label_857.setObjectName(u"label_857")
        self.label_857.setGeometry(QRect(377, 99, 175, 44))
        self.label_857.setFont(font6)
        self.label_857.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_173 = QFrame(self.frame_94)
        self.line_173.setObjectName(u"line_173")
        self.line_173.setGeometry(QRect(316, 185, 274, 16))
        self.line_173.setFrameShape(QFrame.Shape.HLine)
        self.line_173.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_858 = QLabel(self.frame_94)
        self.label_858.setObjectName(u"label_858")
        self.label_858.setGeometry(QRect(377, 194, 120, 44))
        self.label_858.setFont(font6)
        self.label_858.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_859 = QLabel(self.frame_94)
        self.label_859.setObjectName(u"label_859")
        self.label_859.setGeometry(QRect(377, 290, 152, 66))
        self.label_859.setFont(font6)
        self.label_859.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_860 = QLabel(self.frame_94)
        self.label_860.setObjectName(u"label_860")
        self.label_860.setGeometry(QRect(10, 75, 181, 18))
        self.label_860.setFont(font7)
        self.label_860.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_174 = QFrame(self.frame_94)
        self.line_174.setObjectName(u"line_174")
        self.line_174.setGeometry(QRect(316, 279, 274, 16))
        self.line_174.setFrameShape(QFrame.Shape.HLine)
        self.line_174.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.frame_94, 3, 1, 1, 1)

        self.frame_95 = QFrame(self.frame_15)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setFont(font3)
        self.frame_95.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_95.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Shadow.Raised)
        self.label_861 = QLabel(self.frame_95)
        self.label_861.setObjectName(u"label_861")
        self.label_861.setGeometry(QRect(13, 10, 231, 33))
        self.label_861.setFont(font4)
        self.label_861.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_862 = QLabel(self.frame_95)
        self.label_862.setObjectName(u"label_862")
        self.label_862.setGeometry(QRect(16, 49, 16, 16))
        self.label_862.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_863 = QLabel(self.frame_95)
        self.label_863.setObjectName(u"label_863")
        self.label_863.setGeometry(QRect(35, 49, 81, 16))
        self.label_863.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_97 = QPushButton(self.frame_95)
        self.pushButton_97.setObjectName(u"pushButton_97")
        self.pushButton_97.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_97.setStyleSheet(u"QPushButton\n"
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
        self.label_864 = QLabel(self.frame_95)
        self.label_864.setObjectName(u"label_864")
        self.label_864.setGeometry(QRect(298, 10, 182, 31))
        self.label_864.setFont(font5)
        self.label_864.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_865 = QLabel(self.frame_95)
        self.label_865.setObjectName(u"label_865")
        self.label_865.setGeometry(QRect(477, 17, 75, 20))
        self.label_865.setFont(font1)
        self.label_865.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_866 = QLabel(self.frame_95)
        self.label_866.setObjectName(u"label_866")
        self.label_866.setGeometry(QRect(354, 44, 151, 20))
        self.label_866.setFont(font1)
        self.label_866.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_867 = QLabel(self.frame_95)
        self.label_867.setObjectName(u"label_867")
        self.label_867.setGeometry(QRect(10, 99, 291, 269))
        self.label_867.setStyleSheet(u"border-radius:5px;")
        self.label_867.setPixmap(QPixmap(u":/shivam/PropImages/fs.jpg"))
        self.label_867.setScaledContents(True)
        self.line_175 = QFrame(self.frame_95)
        self.line_175.setObjectName(u"line_175")
        self.line_175.setGeometry(QRect(307, 99, 16, 269))
        self.line_175.setFrameShape(QFrame.Shape.VLine)
        self.line_175.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_868 = QLabel(self.frame_95)
        self.label_868.setObjectName(u"label_868")
        self.label_868.setGeometry(QRect(377, 99, 175, 44))
        self.label_868.setFont(font6)
        self.label_868.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_176 = QFrame(self.frame_95)
        self.line_176.setObjectName(u"line_176")
        self.line_176.setGeometry(QRect(316, 185, 274, 16))
        self.line_176.setFrameShape(QFrame.Shape.HLine)
        self.line_176.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_869 = QLabel(self.frame_95)
        self.label_869.setObjectName(u"label_869")
        self.label_869.setGeometry(QRect(377, 194, 120, 44))
        self.label_869.setFont(font6)
        self.label_869.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_870 = QLabel(self.frame_95)
        self.label_870.setObjectName(u"label_870")
        self.label_870.setGeometry(QRect(377, 290, 152, 66))
        self.label_870.setFont(font6)
        self.label_870.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_871 = QLabel(self.frame_95)
        self.label_871.setObjectName(u"label_871")
        self.label_871.setGeometry(QRect(10, 72, 591, 18))
        self.label_871.setFont(font7)
        self.label_871.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_177 = QFrame(self.frame_95)
        self.line_177.setObjectName(u"line_177")
        self.line_177.setGeometry(QRect(316, 279, 274, 16))
        self.line_177.setFrameShape(QFrame.Shape.HLine)
        self.line_177.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.frame_95, 0, 0, 1, 1)

        self.frame_96 = QFrame(self.frame_15)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setFont(font3)
        self.frame_96.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_96.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Shadow.Raised)
        self.label_872 = QLabel(self.frame_96)
        self.label_872.setObjectName(u"label_872")
        self.label_872.setGeometry(QRect(13, 10, 331, 33))
        self.label_872.setFont(font9)
        self.label_872.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_873 = QLabel(self.frame_96)
        self.label_873.setObjectName(u"label_873")
        self.label_873.setGeometry(QRect(16, 49, 16, 16))
        self.label_873.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_874 = QLabel(self.frame_96)
        self.label_874.setObjectName(u"label_874")
        self.label_874.setGeometry(QRect(35, 49, 101, 16))
        self.label_874.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_98 = QPushButton(self.frame_96)
        self.pushButton_98.setObjectName(u"pushButton_98")
        self.pushButton_98.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_98.setStyleSheet(u"QPushButton\n"
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
        self.label_875 = QLabel(self.frame_96)
        self.label_875.setObjectName(u"label_875")
        self.label_875.setGeometry(QRect(330, 10, 171, 30))
        self.label_875.setFont(font8)
        self.label_875.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_876 = QLabel(self.frame_96)
        self.label_876.setObjectName(u"label_876")
        self.label_876.setGeometry(QRect(500, 17, 70, 20))
        self.label_876.setFont(font1)
        self.label_876.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_877 = QLabel(self.frame_96)
        self.label_877.setObjectName(u"label_877")
        self.label_877.setGeometry(QRect(354, 44, 151, 20))
        self.label_877.setFont(font1)
        self.label_877.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_878 = QLabel(self.frame_96)
        self.label_878.setObjectName(u"label_878")
        self.label_878.setGeometry(QRect(10, 99, 291, 269))
        self.label_878.setStyleSheet(u"border-radius:5px;")
        self.label_878.setPixmap(QPixmap(u":/shivam/PropImages/namrata_prime_land-talegaon_dabhade_1-pune-namrata_group.jpg"))
        self.label_878.setScaledContents(True)
        self.line_178 = QFrame(self.frame_96)
        self.line_178.setObjectName(u"line_178")
        self.line_178.setGeometry(QRect(307, 99, 16, 269))
        self.line_178.setFrameShape(QFrame.Shape.VLine)
        self.line_178.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_879 = QLabel(self.frame_96)
        self.label_879.setObjectName(u"label_879")
        self.label_879.setGeometry(QRect(377, 99, 175, 44))
        self.label_879.setFont(font6)
        self.label_879.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_179 = QFrame(self.frame_96)
        self.line_179.setObjectName(u"line_179")
        self.line_179.setGeometry(QRect(316, 185, 274, 16))
        self.line_179.setFrameShape(QFrame.Shape.HLine)
        self.line_179.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_880 = QLabel(self.frame_96)
        self.label_880.setObjectName(u"label_880")
        self.label_880.setGeometry(QRect(377, 194, 120, 44))
        self.label_880.setFont(font6)
        self.label_880.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_881 = QLabel(self.frame_96)
        self.label_881.setObjectName(u"label_881")
        self.label_881.setGeometry(QRect(377, 288, 152, 66))
        self.label_881.setFont(font6)
        self.label_881.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_882 = QLabel(self.frame_96)
        self.label_882.setObjectName(u"label_882")
        self.label_882.setGeometry(QRect(10, 75, 410, 18))
        self.label_882.setFont(font7)
        self.label_882.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_180 = QFrame(self.frame_96)
        self.line_180.setObjectName(u"line_180")
        self.line_180.setGeometry(QRect(316, 279, 274, 16))
        self.line_180.setFrameShape(QFrame.Shape.HLine)
        self.line_180.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.frame_96, 2, 0, 1, 1)

        self.frame_97 = QFrame(self.frame_15)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setFont(font3)
        self.frame_97.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_97.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Shadow.Raised)
        self.label_883 = QLabel(self.frame_97)
        self.label_883.setObjectName(u"label_883")
        self.label_883.setGeometry(QRect(13, 10, 171, 33))
        self.label_883.setFont(font4)
        self.label_883.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_884 = QLabel(self.frame_97)
        self.label_884.setObjectName(u"label_884")
        self.label_884.setGeometry(QRect(16, 49, 16, 16))
        self.label_884.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_885 = QLabel(self.frame_97)
        self.label_885.setObjectName(u"label_885")
        self.label_885.setGeometry(QRect(35, 49, 231, 16))
        self.label_885.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_99 = QPushButton(self.frame_97)
        self.pushButton_99.setObjectName(u"pushButton_99")
        self.pushButton_99.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_99.setStyleSheet(u"QPushButton\n"
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
        self.label_886 = QLabel(self.frame_97)
        self.label_886.setObjectName(u"label_886")
        self.label_886.setGeometry(QRect(298, 10, 182, 31))
        self.label_886.setFont(font5)
        self.label_886.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_887 = QLabel(self.frame_97)
        self.label_887.setObjectName(u"label_887")
        self.label_887.setGeometry(QRect(477, 17, 75, 20))
        self.label_887.setFont(font1)
        self.label_887.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_888 = QLabel(self.frame_97)
        self.label_888.setObjectName(u"label_888")
        self.label_888.setGeometry(QRect(354, 44, 141, 20))
        self.label_888.setFont(font1)
        self.label_888.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_889 = QLabel(self.frame_97)
        self.label_889.setObjectName(u"label_889")
        self.label_889.setGeometry(QRect(10, 99, 291, 269))
        self.label_889.setPixmap(QPixmap(u":/shivam/PropImages/fs-large.jpg"))
        self.label_889.setScaledContents(True)
        self.line_181 = QFrame(self.frame_97)
        self.line_181.setObjectName(u"line_181")
        self.line_181.setGeometry(QRect(307, 99, 16, 269))
        self.line_181.setFrameShape(QFrame.Shape.VLine)
        self.line_181.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_890 = QLabel(self.frame_97)
        self.label_890.setObjectName(u"label_890")
        self.label_890.setGeometry(QRect(377, 99, 175, 44))
        self.label_890.setFont(font6)
        self.label_890.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_182 = QFrame(self.frame_97)
        self.line_182.setObjectName(u"line_182")
        self.line_182.setGeometry(QRect(316, 185, 274, 16))
        self.line_182.setFrameShape(QFrame.Shape.HLine)
        self.line_182.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_891 = QLabel(self.frame_97)
        self.label_891.setObjectName(u"label_891")
        self.label_891.setGeometry(QRect(377, 194, 120, 44))
        self.label_891.setFont(font6)
        self.label_891.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_892 = QLabel(self.frame_97)
        self.label_892.setObjectName(u"label_892")
        self.label_892.setGeometry(QRect(377, 290, 161, 66))
        self.label_892.setFont(font6)
        self.label_892.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_893 = QLabel(self.frame_97)
        self.label_893.setObjectName(u"label_893")
        self.label_893.setGeometry(QRect(10, 75, 261, 18))
        self.label_893.setFont(font7)
        self.label_893.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_183 = QFrame(self.frame_97)
        self.line_183.setObjectName(u"line_183")
        self.line_183.setGeometry(QRect(316, 279, 274, 16))
        self.line_183.setFrameShape(QFrame.Shape.HLine)
        self.line_183.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.frame_97, 2, 1, 1, 1)

        self.frame_98 = QFrame(self.frame_15)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setFont(font3)
        self.frame_98.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_98.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Shadow.Raised)
        self.label_894 = QLabel(self.frame_98)
        self.label_894.setObjectName(u"label_894")
        self.label_894.setGeometry(QRect(13, 10, 201, 33))
        self.label_894.setFont(font4)
        self.label_894.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_895 = QLabel(self.frame_98)
        self.label_895.setObjectName(u"label_895")
        self.label_895.setGeometry(QRect(16, 49, 16, 16))
        self.label_895.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_896 = QLabel(self.frame_98)
        self.label_896.setObjectName(u"label_896")
        self.label_896.setGeometry(QRect(35, 49, 91, 16))
        self.label_896.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_100 = QPushButton(self.frame_98)
        self.pushButton_100.setObjectName(u"pushButton_100")
        self.pushButton_100.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_100.setStyleSheet(u"QPushButton\n"
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
        self.label_897 = QLabel(self.frame_98)
        self.label_897.setObjectName(u"label_897")
        self.label_897.setGeometry(QRect(282, 10, 191, 31))
        self.label_897.setFont(font5)
        self.label_897.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_898 = QLabel(self.frame_98)
        self.label_898.setObjectName(u"label_898")
        self.label_898.setGeometry(QRect(477, 17, 91, 20))
        self.label_898.setFont(font1)
        self.label_898.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_899 = QLabel(self.frame_98)
        self.label_899.setObjectName(u"label_899")
        self.label_899.setGeometry(QRect(354, 44, 151, 20))
        self.label_899.setFont(font1)
        self.label_899.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_900 = QLabel(self.frame_98)
        self.label_900.setObjectName(u"label_900")
        self.label_900.setGeometry(QRect(-70, 99, 391, 269))
        self.label_900.setStyleSheet(u"border-radius:5px;")
        self.label_900.setPixmap(QPixmap(u":/shivam/PropImages/ivoryonlypune.jpg"))
        self.label_900.setScaledContents(True)
        self.line_184 = QFrame(self.frame_98)
        self.line_184.setObjectName(u"line_184")
        self.line_184.setGeometry(QRect(307, 99, 16, 269))
        self.line_184.setFrameShape(QFrame.Shape.VLine)
        self.line_184.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_901 = QLabel(self.frame_98)
        self.label_901.setObjectName(u"label_901")
        self.label_901.setGeometry(QRect(373, 99, 211, 44))
        self.label_901.setFont(font6)
        self.label_901.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_185 = QFrame(self.frame_98)
        self.line_185.setObjectName(u"line_185")
        self.line_185.setGeometry(QRect(316, 185, 274, 16))
        self.line_185.setFrameShape(QFrame.Shape.HLine)
        self.line_185.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_902 = QLabel(self.frame_98)
        self.label_902.setObjectName(u"label_902")
        self.label_902.setGeometry(QRect(377, 194, 120, 44))
        self.label_902.setFont(font6)
        self.label_902.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_903 = QLabel(self.frame_98)
        self.label_903.setObjectName(u"label_903")
        self.label_903.setGeometry(QRect(377, 290, 152, 66))
        self.label_903.setFont(font6)
        self.label_903.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_904 = QLabel(self.frame_98)
        self.label_904.setObjectName(u"label_904")
        self.label_904.setGeometry(QRect(10, 75, 371, 18))
        self.label_904.setFont(font7)
        self.label_904.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_186 = QFrame(self.frame_98)
        self.line_186.setObjectName(u"line_186")
        self.line_186.setGeometry(QRect(316, 279, 274, 16))
        self.line_186.setFrameShape(QFrame.Shape.HLine)
        self.line_186.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.frame_98, 1, 0, 1, 1)

        self.frame_99 = QFrame(self.frame_15)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFont(font3)
        self.frame_99.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_99.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Shadow.Raised)
        self.label_905 = QLabel(self.frame_99)
        self.label_905.setObjectName(u"label_905")
        self.label_905.setGeometry(QRect(13, 10, 271, 33))
        self.label_905.setFont(font4)
        self.label_905.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_906 = QLabel(self.frame_99)
        self.label_906.setObjectName(u"label_906")
        self.label_906.setGeometry(QRect(16, 49, 16, 16))
        self.label_906.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_907 = QLabel(self.frame_99)
        self.label_907.setObjectName(u"label_907")
        self.label_907.setGeometry(QRect(35, 49, 81, 16))
        self.label_907.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_101 = QPushButton(self.frame_99)
        self.pushButton_101.setObjectName(u"pushButton_101")
        self.pushButton_101.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_101.setStyleSheet(u"QPushButton\n"
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
        self.label_908 = QLabel(self.frame_99)
        self.label_908.setObjectName(u"label_908")
        self.label_908.setGeometry(QRect(298, 10, 182, 31))
        self.label_908.setFont(font5)
        self.label_908.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_909 = QLabel(self.frame_99)
        self.label_909.setObjectName(u"label_909")
        self.label_909.setGeometry(QRect(477, 17, 91, 20))
        self.label_909.setFont(font1)
        self.label_909.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_910 = QLabel(self.frame_99)
        self.label_910.setObjectName(u"label_910")
        self.label_910.setGeometry(QRect(354, 44, 151, 20))
        self.label_910.setFont(font1)
        self.label_910.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_911 = QLabel(self.frame_99)
        self.label_911.setObjectName(u"label_911")
        self.label_911.setGeometry(QRect(10, 99, 291, 269))
        self.label_911.setStyleSheet(u"border-radius:5px;")
        self.label_911.setPixmap(QPixmap(u":/shivam/PropImages/dosti_greenscapes-hadapsar-pune-dosti_realty.jpg"))
        self.label_911.setScaledContents(True)
        self.line_187 = QFrame(self.frame_99)
        self.line_187.setObjectName(u"line_187")
        self.line_187.setGeometry(QRect(307, 99, 16, 269))
        self.line_187.setFrameShape(QFrame.Shape.VLine)
        self.line_187.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_912 = QLabel(self.frame_99)
        self.label_912.setObjectName(u"label_912")
        self.label_912.setGeometry(QRect(377, 99, 175, 44))
        self.label_912.setFont(font6)
        self.label_912.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_188 = QFrame(self.frame_99)
        self.line_188.setObjectName(u"line_188")
        self.line_188.setGeometry(QRect(316, 185, 274, 16))
        self.line_188.setFrameShape(QFrame.Shape.HLine)
        self.line_188.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_913 = QLabel(self.frame_99)
        self.label_913.setObjectName(u"label_913")
        self.label_913.setGeometry(QRect(377, 194, 120, 44))
        self.label_913.setFont(font6)
        self.label_913.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_914 = QLabel(self.frame_99)
        self.label_914.setObjectName(u"label_914")
        self.label_914.setGeometry(QRect(377, 290, 152, 66))
        self.label_914.setFont(font6)
        self.label_914.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_915 = QLabel(self.frame_99)
        self.label_915.setObjectName(u"label_915")
        self.label_915.setGeometry(QRect(10, 75, 221, 18))
        self.label_915.setFont(font7)
        self.label_915.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_189 = QFrame(self.frame_99)
        self.line_189.setObjectName(u"line_189")
        self.line_189.setGeometry(QRect(316, 279, 274, 16))
        self.line_189.setFrameShape(QFrame.Shape.HLine)
        self.line_189.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.frame_99, 1, 1, 1, 1)

        self.frame_100 = QFrame(self.frame_15)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setFont(font3)
        self.frame_100.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_100.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Shadow.Raised)
        self.label_916 = QLabel(self.frame_100)
        self.label_916.setObjectName(u"label_916")
        self.label_916.setGeometry(QRect(13, 10, 251, 33))
        self.label_916.setFont(font4)
        self.label_916.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_917 = QLabel(self.frame_100)
        self.label_917.setObjectName(u"label_917")
        self.label_917.setGeometry(QRect(16, 49, 16, 16))
        self.label_917.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_918 = QLabel(self.frame_100)
        self.label_918.setObjectName(u"label_918")
        self.label_918.setGeometry(QRect(35, 49, 101, 16))
        self.label_918.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_102 = QPushButton(self.frame_100)
        self.pushButton_102.setObjectName(u"pushButton_102")
        self.pushButton_102.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_102.setStyleSheet(u"QPushButton\n"
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
        self.label_919 = QLabel(self.frame_100)
        self.label_919.setObjectName(u"label_919")
        self.label_919.setGeometry(QRect(310, 9, 171, 31))
        self.label_919.setFont(font8)
        self.label_919.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_920 = QLabel(self.frame_100)
        self.label_920.setObjectName(u"label_920")
        self.label_920.setGeometry(QRect(488, 15, 80, 20))
        self.label_920.setFont(font1)
        self.label_920.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_921 = QLabel(self.frame_100)
        self.label_921.setObjectName(u"label_921")
        self.label_921.setGeometry(QRect(354, 44, 151, 20))
        self.label_921.setFont(font1)
        self.label_921.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_922 = QLabel(self.frame_100)
        self.label_922.setObjectName(u"label_922")
        self.label_922.setGeometry(QRect(10, 99, 291, 269))
        self.label_922.setStyleSheet(u"border-radius:5px;")
        self.label_922.setPixmap(QPixmap(u":/shivam/PropImages/namrata_prime_land-talegaon_dabhade_1-pune-namrata_group.jpg"))
        self.label_922.setScaledContents(True)
        self.line_190 = QFrame(self.frame_100)
        self.line_190.setObjectName(u"line_190")
        self.line_190.setGeometry(QRect(307, 99, 16, 269))
        self.line_190.setFrameShape(QFrame.Shape.VLine)
        self.line_190.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_923 = QLabel(self.frame_100)
        self.label_923.setObjectName(u"label_923")
        self.label_923.setGeometry(QRect(377, 99, 175, 44))
        self.label_923.setFont(font6)
        self.label_923.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_191 = QFrame(self.frame_100)
        self.line_191.setObjectName(u"line_191")
        self.line_191.setGeometry(QRect(316, 185, 274, 16))
        self.line_191.setFrameShape(QFrame.Shape.HLine)
        self.line_191.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_924 = QLabel(self.frame_100)
        self.label_924.setObjectName(u"label_924")
        self.label_924.setGeometry(QRect(377, 194, 120, 44))
        self.label_924.setFont(font6)
        self.label_924.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_925 = QLabel(self.frame_100)
        self.label_925.setObjectName(u"label_925")
        self.label_925.setGeometry(QRect(377, 291, 152, 66))
        self.label_925.setFont(font6)
        self.label_925.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_926 = QLabel(self.frame_100)
        self.label_926.setObjectName(u"label_926")
        self.label_926.setGeometry(QRect(10, 72, 501, 18))
        self.label_926.setFont(font7)
        self.label_926.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_192 = QFrame(self.frame_100)
        self.line_192.setObjectName(u"line_192")
        self.line_192.setGeometry(QRect(316, 279, 274, 16))
        self.line_192.setFrameShape(QFrame.Shape.HLine)
        self.line_192.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.frame_100, 0, 1, 1, 1)

        self.frame_101 = QFrame(self.frame_15)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setFont(font3)
        self.frame_101.setStyleSheet(u"background-color: rgb(35, 47, 49);\n"
"")
        self.frame_101.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Shadow.Raised)
        self.label_927 = QLabel(self.frame_101)
        self.label_927.setObjectName(u"label_927")
        self.label_927.setGeometry(QRect(13, 10, 291, 33))
        self.label_927.setFont(font9)
        self.label_927.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_928 = QLabel(self.frame_101)
        self.label_928.setObjectName(u"label_928")
        self.label_928.setGeometry(QRect(16, 49, 16, 16))
        self.label_928.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_929 = QLabel(self.frame_101)
        self.label_929.setObjectName(u"label_929")
        self.label_929.setGeometry(QRect(35, 49, 71, 16))
        self.label_929.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.pushButton_103 = QPushButton(self.frame_101)
        self.pushButton_103.setObjectName(u"pushButton_103")
        self.pushButton_103.setGeometry(QRect(77, 382, 151, 31))
        self.pushButton_103.setStyleSheet(u"QPushButton\n"
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
        self.label_930 = QLabel(self.frame_101)
        self.label_930.setObjectName(u"label_930")
        self.label_930.setGeometry(QRect(312, 10, 161, 31))
        self.label_930.setFont(font8)
        self.label_930.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_931 = QLabel(self.frame_101)
        self.label_931.setObjectName(u"label_931")
        self.label_931.setGeometry(QRect(477, 17, 81, 20))
        self.label_931.setFont(font1)
        self.label_931.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_932 = QLabel(self.frame_101)
        self.label_932.setObjectName(u"label_932")
        self.label_932.setGeometry(QRect(354, 44, 151, 20))
        self.label_932.setFont(font1)
        self.label_932.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_933 = QLabel(self.frame_101)
        self.label_933.setObjectName(u"label_933")
        self.label_933.setGeometry(QRect(10, 99, 291, 269))
        self.label_933.setStyleSheet(u"border-radius:5px;")
        self.label_933.setPixmap(QPixmap(u":/shivam/PropImages/shubharambh_clara-kiwale-pune-shubharambh_landmarks.jpg"))
        self.label_933.setScaledContents(True)
        self.line_193 = QFrame(self.frame_101)
        self.line_193.setObjectName(u"line_193")
        self.line_193.setGeometry(QRect(307, 99, 16, 269))
        self.line_193.setFrameShape(QFrame.Shape.VLine)
        self.line_193.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_934 = QLabel(self.frame_101)
        self.label_934.setObjectName(u"label_934")
        self.label_934.setGeometry(QRect(377, 99, 201, 44))
        self.label_934.setFont(font6)
        self.label_934.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_194 = QFrame(self.frame_101)
        self.line_194.setObjectName(u"line_194")
        self.line_194.setGeometry(QRect(316, 185, 274, 16))
        self.line_194.setFrameShape(QFrame.Shape.HLine)
        self.line_194.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_935 = QLabel(self.frame_101)
        self.label_935.setObjectName(u"label_935")
        self.label_935.setGeometry(QRect(377, 194, 120, 44))
        self.label_935.setFont(font6)
        self.label_935.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_936 = QLabel(self.frame_101)
        self.label_936.setObjectName(u"label_936")
        self.label_936.setGeometry(QRect(377, 290, 152, 66))
        self.label_936.setFont(font6)
        self.label_936.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_937 = QLabel(self.frame_101)
        self.label_937.setObjectName(u"label_937")
        self.label_937.setGeometry(QRect(10, 75, 491, 18))
        self.label_937.setFont(font7)
        self.label_937.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.line_195 = QFrame(self.frame_101)
        self.line_195.setObjectName(u"line_195")
        self.line_195.setGeometry(QRect(316, 279, 274, 16))
        self.line_195.setFrameShape(QFrame.Shape.HLine)
        self.line_195.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.frame_101, 3, 0, 1, 1)


        self.verticalLayout_78.addLayout(self.gridLayout_7)


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
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 1351, 2800))
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
        self.frame_Video = QFrame(self.frame_16)
        self.frame_Video.setObjectName(u"frame_Video")
        self.frame_Video.setGeometry(QRect(25, 25, 1300, 550))
        self.frame_Video.setMinimumSize(QSize(0, 550))
        self.frame_Video.setMaximumSize(QSize(1300, 550))
        self.frame_Video.setStyleSheet(u"QFrame\n"
"{\n"
"	border:1px solid black;\n"
"}")
        self.verticalLayout_89 = QVBoxLayout(self.frame_Video)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.label_640 = QLabel(self.frame_Video)
        self.label_640.setObjectName(u"label_640")
        self.label_640.setMinimumSize(QSize(1280, 0))
        self.label_640.setPixmap(QPixmap(r"images\MiddlemanHome.png"))
        self.label_640.setScaledContents(True)

        self.verticalLayout_89.addWidget(self.label_640)

        self.widget_29 = QWidget(self.frame_16)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setGeometry(QRect(24, 640, 1300, 50))
        self.widget_29.setStyleSheet(u"background-color: rgb(7, 94, 84);")
        self.label_5 = QLabel(self.widget_29)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 10, 751, 31))
        font36 = QFont()
        font36.setFamilies([u"Lucida Bright"])
        font36.setPointSize(19)
        self.label_5.setFont(font36)
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
        font37 = QFont()
        font37.setPointSize(22)
        self.label_51.setFont(font37)
        self.label_51.setStyleSheet(u"color:white;")
        self.widget_30 = QWidget(self.frame_16)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setGeometry(QRect(28, 1220, 1300, 300))
        self.widget_30.setStyleSheet(u"background-color: rgb(18, 140, 126);")
        self.label_185 = QLabel(self.widget_30)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setGeometry(QRect(440, 20, 701, 141))
        font38 = QFont()
        font38.setPointSize(40)
        font38.setBold(True)
        self.label_185.setFont(font38)
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
        self.label_187.setFont(font34)
        self.label_365 = QLabel(self.widget_30)
        self.label_365.setObjectName(u"label_365")
        self.label_365.setGeometry(QRect(60, -10, 331, 311))
        self.label_365.setPixmap(QPixmap(u":/shivam/PropImages/Coffe (7).png"))
        self.label_365.setScaledContents(True)
        self.label_367 = QLabel(self.frame_16)
        self.label_367.setObjectName(u"label_367")
        self.label_367.setGeometry(QRect(26, 1570, 1299, 51))
        font39 = QFont()
        font39.setPointSize(26)
        self.label_367.setFont(font39)
        self.label_367.setStyleSheet(u"color:rgb(198, 198, 198);")
        self.layoutWidget14 = QWidget(self.frame_16)
        self.layoutWidget14.setObjectName(u"layoutWidget14")
        self.layoutWidget14.setGeometry(QRect(26, 750, 1301, 311))
        self.horizontalLayout_26 = QHBoxLayout(self.layoutWidget14)
        self.horizontalLayout_26.setSpacing(50)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.widget_25 = QWidget(self.layoutWidget14)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setFont(font1)
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
        icon21 = QIcon()
        icon21.addFile(u":/shivam/PropImages/Coffe (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon21)
        self.pushButton_17.setIconSize(QSize(180, 180))
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setAutoExclusive(True)

        self.horizontalLayout_26.addWidget(self.widget_25)

        self.widget_26 = QWidget(self.layoutWidget14)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setFont(font1)
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
        icon22 = QIcon()
        icon22.addFile(u":/shivam/PropImages/Coffe (3).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_36.setIcon(icon22)
        self.pushButton_36.setIconSize(QSize(180, 180))
        self.pushButton_36.setCheckable(True)
        self.pushButton_36.setAutoExclusive(True)
        self.label_613 = QLabel(self.widget_26)
        self.label_613.setObjectName(u"label_613")
        self.label_613.setGeometry(QRect(85, 94, 111, 41))
        font40 = QFont()
        font40.setFamilies([u"Segoe UI Emoji"])
        font40.setPointSize(11)
        font40.setBold(True)
        self.label_613.setFont(font40)
        self.label_613.setStyleSheet(u"border:none; background:none; color:red;")

        self.horizontalLayout_26.addWidget(self.widget_26)

        self.widget_27 = QWidget(self.layoutWidget14)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setFont(font1)
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
        icon23 = QIcon()
        icon23.addFile(u":/shivam/PropImages/Coffe (4).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_37.setIcon(icon23)
        self.pushButton_37.setIconSize(QSize(180, 180))
        self.pushButton_37.setCheckable(True)
        self.pushButton_37.setAutoExclusive(True)

        self.horizontalLayout_26.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.layoutWidget14)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setFont(font1)
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
        icon24 = QIcon()
        icon24.addFile(u":/shivam/PropImages/Coffe (5).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_38.setIcon(icon24)
        self.pushButton_38.setIconSize(QSize(200, 200))
        self.pushButton_38.setCheckable(True)
        self.pushButton_38.setAutoExclusive(True)

        self.horizontalLayout_26.addWidget(self.widget_28)

        self.layoutWidget15 = QWidget(self.frame_16)
        self.layoutWidget15.setObjectName(u"layoutWidget15")
        self.layoutWidget15.setGeometry(QRect(120, 1670, 1127, 272))
        self.horizontalLayout_27 = QHBoxLayout(self.layoutWidget15)
        self.horizontalLayout_27.setSpacing(100)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setSpacing(15)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_368 = QLabel(self.layoutWidget15)
        self.label_368.setObjectName(u"label_368")
        self.label_368.setMinimumSize(QSize(181, 181))
        self.label_368.setMaximumSize(QSize(181, 181))
        self.label_368.setFont(font12)
        self.label_368.setStyleSheet(u"color:rgb(198, 198, 198);\n"
"border:5px solid rgb(18, 140, 126);\n"
"border-radius:90px;;")

        self.verticalLayout_48.addWidget(self.label_368)

        self.label_372 = QLabel(self.layoutWidget15)
        self.label_372.setObjectName(u"label_372")
        font41 = QFont()
        font41.setPointSize(19)
        font41.setBold(True)
        self.label_372.setFont(font41)
        self.label_372.setStyleSheet(u"color:rgb(198, 198, 198);")

        self.verticalLayout_48.addWidget(self.label_372)


        self.horizontalLayout_27.addLayout(self.verticalLayout_48)

        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setSpacing(15)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_370 = QLabel(self.layoutWidget15)
        self.label_370.setObjectName(u"label_370")
        self.label_370.setMinimumSize(QSize(181, 181))
        self.label_370.setMaximumSize(QSize(181, 181))
        self.label_370.setFont(font12)
        self.label_370.setStyleSheet(u"color:rgb(198, 198, 198);\n"
"border:5px solid rgb(18, 140, 126);\n"
"border-radius:90px;;")

        self.verticalLayout_50.addWidget(self.label_370, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_374 = QLabel(self.layoutWidget15)
        self.label_374.setObjectName(u"label_374")
        self.label_374.setFont(font41)
        self.label_374.setStyleSheet(u"color:rgb(198, 198, 198);")

        self.verticalLayout_50.addWidget(self.label_374, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_27.addLayout(self.verticalLayout_50)

        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setSpacing(15)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_369 = QLabel(self.layoutWidget15)
        self.label_369.setObjectName(u"label_369")
        self.label_369.setMinimumSize(QSize(181, 181))
        self.label_369.setMaximumSize(QSize(181, 181))
        self.label_369.setFont(font12)
        self.label_369.setStyleSheet(u"color:rgb(198, 198, 198);\n"
"border:5px solid rgb(18, 140, 126);\n"
"border-radius:90px;;")

        self.verticalLayout_49.addWidget(self.label_369, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_373 = QLabel(self.layoutWidget15)
        self.label_373.setObjectName(u"label_373")
        font42 = QFont()
        font42.setPointSize(18)
        font42.setBold(True)
        self.label_373.setFont(font42)
        self.label_373.setStyleSheet(u"color:rgb(198, 198, 198);")

        self.verticalLayout_49.addWidget(self.label_373, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_27.addLayout(self.verticalLayout_49)

        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setSpacing(15)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.label_371 = QLabel(self.layoutWidget15)
        self.label_371.setObjectName(u"label_371")
        self.label_371.setMinimumSize(QSize(181, 181))
        self.label_371.setMaximumSize(QSize(181, 181))
        self.label_371.setFont(font12)
        self.label_371.setStyleSheet(u"color:rgb(198, 198, 198);\n"
"border:5px solid rgb(18, 140, 126);\n"
"border-radius:90px;;")

        self.verticalLayout_51.addWidget(self.label_371, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_375 = QLabel(self.layoutWidget15)
        self.label_375.setObjectName(u"label_375")
        self.label_375.setFont(font41)
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
        self.label_376.setPixmap(QPixmap(u":/shivam/PropImages/Coffe (12).png"))
        self.label_376.setScaledContents(True)
        self.label_377 = QLabel(self.widget_32)
        self.label_377.setObjectName(u"label_377")
        self.label_377.setGeometry(QRect(130, 120, 151, 161))
        self.label_377.setStyleSheet(u"border:none;")
        self.label_377.setPixmap(QPixmap(u":/shivam/PropImages/Black White Minimalist SImple Monogram Typography Logo (12).png"))
        self.label_377.setScaledContents(True)
        self.label_378 = QLabel(self.widget_32)
        self.label_378.setObjectName(u"label_378")
        self.label_378.setGeometry(QRect(420, 40, 701, 171))
        font43 = QFont()
        font43.setFamilies([u"Bell MT"])
        font43.setPointSize(55)
        self.label_378.setFont(font43)
        self.label_379 = QLabel(self.widget_32)
        self.label_379.setObjectName(u"label_379")
        self.label_379.setGeometry(QRect(420, 260, 201, 31))
        font44 = QFont()
        font44.setFamilies([u"Segoe UI"])
        font44.setPointSize(17)
        self.label_379.setFont(font44)
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
        self.label_385.setPixmap(QPixmap(u":/shivam/PropImages/app-store.png"))
        self.label_385.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.label_385)

        self.label_386 = QLabel(self.layoutWidget_13)
        self.label_386.setObjectName(u"label_386")
        self.label_386.setFont(font1)

        self.horizontalLayout_29.addWidget(self.label_386)

        self.layoutWidget16 = QWidget(self.widget_32)
        self.layoutWidget16.setObjectName(u"layoutWidget16")
        self.layoutWidget16.setGeometry(QRect(720, 320, 165, 32))
        self.horizontalLayout_28 = QHBoxLayout(self.layoutWidget16)
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_384 = QLabel(self.layoutWidget16)
        self.label_384.setObjectName(u"label_384")
        self.label_384.setMinimumSize(QSize(30, 30))
        self.label_384.setMaximumSize(QSize(30, 30))
        self.label_384.setPixmap(QPixmap(u":/shivam/PropImages/playstore.png"))
        self.label_384.setScaledContents(True)

        self.horizontalLayout_28.addWidget(self.label_384)

        self.label_383 = QLabel(self.layoutWidget16)
        self.label_383.setObjectName(u"label_383")
        self.label_383.setFont(font1)

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
        self.label_382.setPixmap(QPixmap(u":/shivam/PropImages/kisspng-computer-icons-user-profile-avatar-job-icon-5b521c56afedc0.0537187115321078627206.png"))
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
        self.label_393.setPixmap(QPixmap(u":/shivam/PropImages/kisspng-computer-icons-user-profile-avatar-job-icon-5b521c56afedc0.0537187115321078627206.png"))
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
        font45 = QFont()
        font45.setFamilies([u"Segoe UI Variable Display Light"])
        font45.setPointSize(19)
        self.label_399.setFont(font45)
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
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 1351, 2000))
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
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(354, 44, 151, 20))
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 99, 291, 269))
        self.label_13.setStyleSheet(u"border-radius:5px;")
        self.label_13.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Santacruz.Courtyard/Mumbai-6.5.jpg"))
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
        self.pushButton_72 = QPushButton(self.frame)
        self.pushButton_72.setObjectName(u"pushButton_72")
        self.pushButton_72.setGeometry(QRect(8, 98, 295, 271))
        self.pushButton_72.setStyleSheet(u"border:none;\n"
"background-color:none;")

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
        self.label_22.setFont(font1)
        self.label_22.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_23 = QLabel(self.frame_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(354, 44, 151, 20))
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_24 = QLabel(self.frame_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 99, 291, 269))
        self.label_24.setStyleSheet(u"border-radius:5px;")
        self.label_24.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Malad.PratapLibertyOne/Mumbai-2.jpg"))
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
        self.pushButton_73 = QPushButton(self.frame_4)
        self.pushButton_73.setObjectName(u"pushButton_73")
        self.pushButton_73.setGeometry(QRect(10, 100, 295, 271))
        self.pushButton_73.setStyleSheet(u"border:none;\n"
"background-color:none;")

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
        self.label_33.setFont(font1)
        self.label_33.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_34 = QLabel(self.frame_8)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(354, 44, 151, 20))
        self.label_34.setFont(font1)
        self.label_34.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_35 = QLabel(self.frame_8)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(10, 99, 291, 269))
        self.label_35.setStyleSheet(u"border-radius:5px;")
        self.label_35.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Andheri.Tathastu/Mumbai-4.4.jpg"))
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
        self.label_44.setFont(font1)
        self.label_44.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_45 = QLabel(self.frame_9)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(354, 44, 151, 20))
        self.label_45.setFont(font1)
        self.label_45.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_46 = QLabel(self.frame_9)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(10, 99, 291, 269))
        self.label_46.setStyleSheet(u"border-radius:5px;")
        self.label_46.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Boriwali.VKLALHariPhasI/Mumbai - 5.jpg"))
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
        self.label_66.setFont(font1)
        self.label_66.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_67 = QLabel(self.frame_10)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(354, 44, 151, 20))
        self.label_67.setFont(font1)
        self.label_67.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_68 = QLabel(self.frame_10)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(10, 99, 291, 269))
        self.label_68.setStyleSheet(u"border-radius:5px;")
        self.label_68.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Ghatkopar.Rajshree/Mumbai-1.jpg"))
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
        self.label_77.setFont(font1)
        self.label_77.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_78 = QLabel(self.frame_11)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(354, 44, 151, 20))
        self.label_78.setFont(font1)
        self.label_78.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_79 = QLabel(self.frame_11)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(10, 99, 291, 269))
        self.label_79.setStyleSheet(u"border-radius:5px;")
        self.label_79.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-3-LowerParel.LodhaPark/Mumbai-3.1_1_11zon.jpg"))
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
        self.label_88.setFont(font1)
        self.label_88.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_89 = QLabel(self.frame_12)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(354, 44, 151, 20))
        self.label_89.setFont(font1)
        self.label_89.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_90 = QLabel(self.frame_12)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setGeometry(QRect(10, 99, 291, 269))
        self.label_90.setStyleSheet(u"border-radius:5px;")
        self.label_90.setPixmap(QPixmap(u":/shivam/PropImages/WhatsApp Image 2024-07-05 at 17.29.33_eac17ca7.jpg"))
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
        self.label_99.setFont(font1)
        self.label_99.setStyleSheet(u"color:rgb(118, 118, 118);\n"
"")
        self.label_100 = QLabel(self.frame_13)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setGeometry(QRect(354, 44, 151, 20))
        self.label_100.setFont(font1)
        self.label_100.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.label_101 = QLabel(self.frame_13)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setGeometry(QRect(10, 99, 291, 269))
        self.label_101.setStyleSheet(u"border-radius:5px;")
        self.label_101.setPixmap(QPixmap(u":/shivam/PropImages/Mumbai/Mumbai-Ghatkopar.Rajshree/Mumbai-1.6-RF.jpg"))
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
        #-----------------------------------        
        self.pushButton_33.clicked.connect(self.logout_win_frame)
        self.pushButton.clicked.connect(self.filter_win_frame)
        self.Dashboard_7.clicked.connect(self.feedback_win_frame)
        self.pushButton_11.clicked.connect(self.notification_win_frame)
        self.pushButton_11.clicked.connect(self.internet_checker) # Internet checker 
        
        self.loginbutton_3.clicked.connect(self.owner_win_frame) 
        # self.comboBox.currentIndexChanged.connect(self.fetch_city)  # If belo lambda will not work then is for backend
        self.comboBox.currentIndexChanged.connect(lambda index: setattr(self, 'cmb_city', self.comboBox.itemText(index)))
        self.comboBox_2.currentIndexChanged.connect(lambda index :self.ac_service(index))
        self.pushButton_32.clicked.connect(self.fetch_city_price_type) # Search Button fetching the values 
        self.loginbutton.clicked.connect(self.contact_us_wp) 
        self.loginbutton_2.clicked.connect(self.contact_us_email)
#--------Scratches Frame        
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
        self.pushButton_42.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        
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
        
        carpentry = [
                (self.pushButton_49,1),
                (self.pushButton_54,2),
                (self.pushButton_55,3),
                (self.pushButton_56,4),
                (self.pushButton_57,5),
                (self.pushButton_58,6),
                (self.pushButton_59,7),
                (self.pushButton_60,8),
                (self.pushButton_61,9),
                (self.pushButton_62,10),
                (self.pushButton_63,11),
                (self.pushButton_64,12)
              
        ]
        
        plumbing = [
                (self.pushButton_104,1),
                (self.pushButton_105,2),
                (self.pushButton_106,3),
                (self.pushButton_109,4),
                (self.pushButton_110,5),
                (self.pushButton_111,6),
                
        ]
        

        # Combine all buttons into a single list
        all_buttons = mumbai_buttons + pune_buttons + thane_buttons

        # Connect each button to the get_an_email method with an additional argument
        for button, property_detail in all_buttons:
                button.clicked.connect(partial(self.clck_more_info, property_detail))
                
        for buttonss,service_de in carpentry:
                buttonss.clicked.connect(partial(self.carpentry_adding, service_de))
        
        for buttonss,service_de in plumbing:
                buttonss.clicked.connect(partial(self.plumbing_frm, service_de))
        
        self.frame_83.hide()
        self.frame_84.hide()
        self.frame_85.hide()
        self.frame_77.hide()
        self.frame_78.hide()
        self.frame_79.hide()
        
        # self.clos_button = QPushButton(self.mainmenu)
        # self.clos_button.setGeometry(QRect(910,20,30,20))
        # self.clos_button.setStyleSheet(u"background-color: rgb(37, 211, 102);\n"
        # "color:rgb(26, 26, 26);\n"
        # "border-radius:5px;")
        self.pushButton_77.clicked.connect(self.clr_all)

        self.pushButton_108.clicked.connect(self.check_carpent) 
        self.pushButton_107.clicked.connect(self.check_plumbing) 
                
                
        
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
        self.Profile_3.clicked.connect(lambda : self.stackedWidget_3.setCurrentIndex(7))
        self.Dashboard_5.clicked.connect(lambda : self.stackedWidget_3.setCurrentIndex(8))
        self.Messages_3.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(9))
        self.Dashboard_3.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(10))
        self.frame_3.hide()
        self.toolBox.setCurrentIndex(0)
        self.pushButton_72.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(11))
        self.pushButton_73.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(12))
        self.pushButton_87.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(18))
        self.pushButton_17.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(0))
        self.pushButton_37.clicked.connect(lambda: self.stackedWidget_3.setCurrentIndex(10))


        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(22)
        self.comboBox.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(18)
        self.toolBox_2.setCurrentIndex(3)
        self.toolBox_2.layout().setSpacing(10)
        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MiddleMaN", None))
        self.pushButton_39.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<strong>M</strong>iddle <strong>M</strong>an", None))
        self.pushButton_87.setText(QCoreApplication.translate("MainWindow", u" Home", None))
        self.Dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Mumbai", None))
        self.Profile_2.setText(QCoreApplication.translate("MainWindow", u"Thane", None))
        self.Messages_2.setText(QCoreApplication.translate("MainWindow", u"Pune", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"New Project", None))
        self.Messages_3.setText(QCoreApplication.translate("MainWindow", u"Plumbing", None))
        self.Dashboard_3.setText(QCoreApplication.translate("MainWindow", u"Interior Design", None))
        self.Profile_3.setText(QCoreApplication.translate("MainWindow", u"Ac Services", None))
        self.Dashboard_5.setText(QCoreApplication.translate("MainWindow", u"Carpentry", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Other Services", None))
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
        self.pushButton_77.setText("")
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"  new", None))
        self.pushButton_6.setText("")
        self.pushButton_33.setText("")
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
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"2,000 MM cash will expire in ", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"22 Aug 2024", None))
        self.label_135.setText("")
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Gift Cards", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"My rewards", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u" 2000 MMcash", None))
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
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"2000 MMCash", None))
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
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal AC Service", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Essential AC Service", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Premium AC Service", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"AC Inspection", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"AC Installation", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"AC Uninstallation", None))

        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select one from below", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.label_401.setText("")
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"> Essential AC Service</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"> starts from\u00a0</"
                        "span><span style=\" font-weight:700; color:#ffffff;\">\u20b9838 - \u20b9429</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"paint0_linear_1267_5900\"></a><span style=\" color:#ffffff;\"> </span><span style=\" color:#ffffff;\">Get it for\u00a0</span><span style=\" font-weight:700; color:#ffffff;\">\u20b9364</span><span style=\" color:#ffffff;\"> using UPI</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" color:#ffffff;\">1] Servicing of AC unit, cooling coil and drain tray</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" color:#ffffff;\">2] 3X Cooling with Jet-Pump Technology</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><spa"
                        "n style=\" color:#ffffff;\">3] Assured warranty of 30 days</span></p></body></html>", None))
        self.label_403.setText(QCoreApplication.translate("MainWindow", u"Service Includes :\n"
"  Pre- service inspection\n"
"  Complete diagnosis of the AC (Including gas checks) to identify repairs\n"
"  Post-service Inspection\n"
"  Gas check, cooling efficiency, other functionality checked.\n"
"  Assured warranty\n"
"  30 days warranty on AC service/installation and 180 days warranty on spare parts.\n"
"  Appliance protection upto INR 10,000/- on servicing jobs*", None))
        self.label_404.setText(QCoreApplication.translate("MainWindow", u"Increase the efficiency of your AC and get improved cooling. Cleaning of filter, cooling coil\n"
"& checking of gas level.", None))
        self.label_405.setText(QCoreApplication.translate("MainWindow", u"AC stand, spare part and gas charging cost\n"
"Core cutting ,POP filling and mason/wood work\n"
"No warranty on AC uninstallation", None))
        self.label_406.setText(QCoreApplication.translate("MainWindow", u"Service does not include.", None))
        self.label_429.setText(QCoreApplication.translate("MainWindow", u"Normal AC Service", None))
        self.label_414.setText("")
        self.label_407.setText(QCoreApplication.translate("MainWindow", u"    Same day\n"
"on time service", None))
        self.label_413.setText("")
        self.label_411.setText(QCoreApplication.translate("MainWindow", u"Lowest Price\n"
"  Guarantee", None))
        self.label_415.setText("")
        self.label_412.setText(QCoreApplication.translate("MainWindow", u"Professional\n"
"   Partners", None))
        self.label_416.setText("")
        self.label_417.setText(QCoreApplication.translate("MainWindow", u"       30 days\n"
"service warranty", None))
        self.label_408.setText("")
        self.textEdit_12.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"> Essential AC Service</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"> starts from\u00a0</"
                        "span><span style=\" font-weight:700; color:#ffffff;\">\u20b91050 - \u20b91200</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"paint0_linear_1267_5900\"></a><span style=\" color:#ffffff;\"> </span><span style=\" color:#ffffff;\">Get it for\u00a0</span><span style=\" font-weight:700; color:#ffffff;\">\u20b9900</span><span style=\" color:#ffffff;\"> using UPI</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" color:#ffffff;\">1] Servicing of AC unit, cooling coil and drain tray</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" color:#ffffff;\">2] 3X Cooling with Jet-Pump Technology</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><s"
                        "pan style=\" color:#ffffff;\">3] Assured warranty of 60 days</span></p></body></html>", None))
        self.label_409.setText(QCoreApplication.translate("MainWindow", u"Essential AC Service", None))
        self.label_410.setText(QCoreApplication.translate("MainWindow", u"Service Includes :\n"
"  Pre- service inspection\n"
"  Complete diagnosis of the AC (Including gas checks) to identify repairs\n"
"  Post-service Inspection\n"
"  Gas check, cooling efficiency, other functionality checked.\n"
"  Assured warranty\n"
"  30 days warranty on AC service/installation and 180 days warranty on spare parts.\n"
"  Appliance protection upto INR 10,000/- on servicing jobs*", None))
        self.label_418.setText(QCoreApplication.translate("MainWindow", u"Increase the efficiency of your AC and get improved cooling. Cleaning of filter, cooling coil\n"
"& checking of gas level.", None))
        self.label_419.setText(QCoreApplication.translate("MainWindow", u"AC stand, spare part and gas charging cost\n"
"Core cutting ,POP filling and mason/wood work\n"
"No warranty on AC uninstallation", None))
        self.label_420.setText(QCoreApplication.translate("MainWindow", u"Service does not include.", None))
        self.label_421.setText("")
        self.label_422.setText(QCoreApplication.translate("MainWindow", u"    Same day\n"
"on time service", None))
        self.label_423.setText("")
        self.label_424.setText(QCoreApplication.translate("MainWindow", u"Lowest Price\n"
"  Guarantee", None))
        self.label_425.setText("")
        self.label_426.setText(QCoreApplication.translate("MainWindow", u"Professional\n"
"   Partners", None))
        self.label_427.setText("")
        self.label_428.setText(QCoreApplication.translate("MainWindow", u"       30 days\n"
"service warranty", None))
        self.label_430.setText("")
        self.textEdit_13.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"> Premium AC Service</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"> starts from\u00a0</sp"
                        "an><span style=\" font-weight:700; color:#ffffff;\">\u20b91250 - \u20b91500</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"paint0_linear_1267_5900\"></a><span style=\" color:#ffffff;\"> </span><span style=\" color:#ffffff;\">Get it for\u00a0</span><span style=\" font-weight:700; color:#ffffff;\">\u20b91200</span><span style=\" color:#ffffff;\"> using UPI</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" color:#ffffff;\">1] Servicing of AC unit, cooling coil and drain tray</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" color:#ffffff;\">2] 3X Cooling with Jet-Pump Technology</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><sp"
                        "an style=\" color:#ffffff;\">3] Assured warranty of 120 days</span></p></body></html>", None))
        self.label_431.setText(QCoreApplication.translate("MainWindow", u"Premium AC Service", None))
        self.label_432.setText(QCoreApplication.translate("MainWindow", u"Service Includes :\n"
"  Pre- service inspection\n"
"  Complete diagnosis of the AC (Including gas checks) to identify repairs\n"
"  Post-service Inspection\n"
"  Gas check, cooling efficiency, other functionality checked.\n"
"  Assured warranty\n"
"  30 days warranty on AC service/installation and 180 days warranty on spare parts.\n"
"  Appliance protection upto INR 10,000/- on servicing jobs*", None))
        self.label_433.setText(QCoreApplication.translate("MainWindow", u"Increase the efficiency of your AC and get improved cooling. Cleaning of filter, cooling coil\n"
"& checking of gas level.", None))
        self.label_434.setText(QCoreApplication.translate("MainWindow", u"AC stand, spare part and gas charging cost\n"
"Core cutting ,POP filling and mason/wood work\n"
"No warranty on AC uninstallation", None))
        self.label_435.setText(QCoreApplication.translate("MainWindow", u"Service does not include.", None))
        self.label_436.setText("")
        self.label_437.setText(QCoreApplication.translate("MainWindow", u"    Same day\n"
"on time service", None))
        self.label_438.setText("")
        self.label_439.setText(QCoreApplication.translate("MainWindow", u"Lowest Price\n"
"  Guarantee", None))
        self.label_440.setText("")
        self.label_441.setText(QCoreApplication.translate("MainWindow", u"Professional\n"
"   Partners", None))
        self.label_442.setText("")
        self.label_443.setText(QCoreApplication.translate("MainWindow", u"       30 days\n"
"service warranty", None))
        self.label_444.setText("")
        self.textEdit_14.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"> AC Inspection</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"> starts from\u00a0</span><s"
                        "pan style=\" font-weight:700; color:#ffffff;\">\u20b91250 - \u20b91500</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"paint0_linear_1267_5900\"></a><span style=\" color:#ffffff;\"> </span><span style=\" color:#ffffff;\">Get it for\u00a0</span><span style=\" font-weight:700; color:#ffffff;\">\u20b91200</span><span style=\" color:#ffffff;\"> using UPI</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" color:#ffffff;\">1] Servicing of AC unit, cooling coil and drain tray</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" color:#ffffff;\">2] 3X Cooling with Jet-Pump Technology</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span st"
                        "yle=\" color:#ffffff;\">3] Assured warranty of 120 days</span></p></body></html>", None))
        self.label_445.setText(QCoreApplication.translate("MainWindow", u"AC Inspection", None))
        self.label_446.setText(QCoreApplication.translate("MainWindow", u"Service Includes :\n"
"     Pre- service inspection\n"
"     Complete diagnosis of the AC (Including gas checks) to identify repairs\n"
"     Post-service Inspection\n"
"     Gas check, cooling efficiency, other functionality checked.\n"
"     Assured warranty\n"
"     30 days warranty on AC service/installation and 180 days warranty on spare parts.\n"
"     Appliance protection upto INR 10,000/- on servicing jobs*", None))
        self.label_447.setText(QCoreApplication.translate("MainWindow", u"Increase the efficiency of your AC and get improved cooling. Cleaning of filter, cooling coil\n"
"& checking of gas level.", None))
        self.label_448.setText(QCoreApplication.translate("MainWindow", u"AC stand, spare part and gas charging cost\n"
"Core cutting ,POP filling and mason/wood work\n"
"No warranty on AC uninstallation", None))
        self.label_449.setText(QCoreApplication.translate("MainWindow", u"Service does not include.", None))
        self.label_450.setText("")
        self.label_451.setText(QCoreApplication.translate("MainWindow", u"    Same day\n"
"on time service", None))
        self.label_452.setText("")
        self.label_453.setText(QCoreApplication.translate("MainWindow", u"Lowest Price\n"
"  Guarantee", None))
        self.label_454.setText("")
        self.label_455.setText(QCoreApplication.translate("MainWindow", u"Professional\n"
"   Partners", None))
        self.label_456.setText("")
        self.label_457.setText(QCoreApplication.translate("MainWindow", u"       30 days\n"
"service warranty", None))
        self.label_458.setText("")
        self.textEdit_15.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"AC_INSTALLATION_ADDON_OPTION\"></a><span style=\" color:#ffffff;\">A</span><span style=\" color:#ffffff;\">C Installation</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-ind"
                        "ent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">starts from\u00a0</span><span style=\" font-weight:700; color:#ffffff;\">\u20b91,518</span><span style=\" color:#ffffff;\"> - </span><span style=\" font-weight:700; color:#ffffff;\">\u20b9 769</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"paint0_linear_1267_5900\"></a><span style=\" color:#ffffff;\">G</span><span style=\" color:#ffffff;\">et it for\u00a0</span><span style=\" font-weight:700; color:#ffffff;\">\u20b9653</span><span style=\" color:#ffffff;\">\u00a0using VIP</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" color:#ffffff;\">1] Pre-service, Post-service checks &amp; Installation</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" color:#ffffff;\""
                        ">2] 30 days assured warranty on installation</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" color:#ffffff;\">3] Additional spare part cost, gas charges, mason work not included</span></p></body></html>", None))
        self.label_459.setText(QCoreApplication.translate("MainWindow", u"AC Installation", None))
        self.label_460.setText(QCoreApplication.translate("MainWindow", u"Service Includes : \n"
"Pre- service inspecion\n"
"Complete diagnosis of the AC (Including gas checks) to identify repairs\n"
"Post-service Inspection\n"
"Gas check, cooling efficiency, other functionality checked.\n"
"Assured warranty\n"
"30 days warranty on AC service/installation and 180 days warranty on spare parts.\n"
"Appliance protection upto INR 10,000/- on servicing jobs*", None))
        self.label_461.setText(QCoreApplication.translate("MainWindow", u"Increase the efficiency of your AC and get improved cooling. Cleaning of filter, cooling coil\n"
"& checking of gas level.", None))
        self.label_462.setText(QCoreApplication.translate("MainWindow", u"AC stand, spare part and gas charging cost\n"
"Core cutting ,POP filling and mason/wood work\n"
"No warranty on AC uninstallation", None))
        self.label_463.setText(QCoreApplication.translate("MainWindow", u"Service does not include.", None))
        self.label_464.setText("")
        self.label_465.setText(QCoreApplication.translate("MainWindow", u"    Same day\n"
"on time service", None))
        self.label_466.setText("")
        self.label_467.setText(QCoreApplication.translate("MainWindow", u"Lowest Price\n"
"  Guarantee", None))
        self.label_468.setText("")
        self.label_469.setText(QCoreApplication.translate("MainWindow", u"Professional\n"
"   Partners", None))
        self.label_470.setText("")
        self.label_471.setText(QCoreApplication.translate("MainWindow", u"       30 days\n"
"service warranty", None))
        self.label_472.setText("")
        self.textEdit_16.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"AC_UNINSTALLATION_ADDON_OPTION\"></a><span style=\" color:#ffffff;\">A</span><span style=\" color:#ffffff;\">C Uninstallation</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">starts from\u00a0</span><span style=\" font-weight:700; color:#ffffff;\">\u20b9938</span><span styl"
                        "e=\" color:#ffffff;\"> - </span><span style=\" font-weight:700; color:#ffffff;\">\u20b9469</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"paint0_linear_1267_5900\"></a><span style=\" color:#ffffff;\">G</span><span style=\" color:#ffffff;\">et it for\u00a0</span><span style=\" font-weight:700; color:#ffffff;\">\u20b9398</span><span style=\" color:#ffffff;\">\u00a0using VIP</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" color:#ffffff;\">1] Pre-service, Post-service checks &amp; Un-installation of unit</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" color:#ffffff;\">2] Warranty not applicable on un-installation</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-"
                        "block-indent:1; text-indent:0px;\"><span style=\" color:#ffffff;\">3] Additional spare part cost, gas charges, mason work not included</span></p></body></html>", None))
        self.label_473.setText(QCoreApplication.translate("MainWindow", u"AC Uninstallation", None))
        self.label_474.setText(QCoreApplication.translate("MainWindow", u"Service Includes : \n"
"Pre- service inspection\n"
"Complete diagnosis of the AC (Including gas checks) to identify repairs\n"
"Post-service Inspection\n"
"Gas check, cooling efficiency, other functionality checked.\n"
"Assured warranty\n"
"30 days warranty on AC service/installation and 180 days warranty on spare parts.\n"
"Appliance protection upto INR 10,000/- on servicing jobs*", None))
        self.label_475.setText(QCoreApplication.translate("MainWindow", u"Increase the efficiency of your AC and get improved cooling. Cleaning of filter, cooling coil\n"
"& checking of gas level.", None))
        self.label_476.setText(QCoreApplication.translate("MainWindow", u"AC stand, spare part and gas charging cost\n"
"Core cutting ,POP filling and mason/wood work\n"
"No warranty on AC uninstallation", None))
        self.label_477.setText(QCoreApplication.translate("MainWindow", u"Service does not include.", None))
        self.label_478.setText("")
        self.label_479.setText(QCoreApplication.translate("MainWindow", u"    Same day\n"
"on time service", None))
        self.label_480.setText("")
        self.label_481.setText(QCoreApplication.translate("MainWindow", u"Lowest Price\n"
"  Guarantee", None))
        self.label_482.setText("")
        self.label_483.setText(QCoreApplication.translate("MainWindow", u"Professional\n"
"   Partners", None))
        self.label_484.setText("")
        self.label_485.setText(QCoreApplication.translate("MainWindow", u"       30 days\n"
"service warranty", None))
        self.label_402.setText(QCoreApplication.translate("MainWindow", u"                   Enter Your Info Here..", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"Send Details", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Full Name", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Contact number ", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Email Id", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Address", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Pincode", None))
        self.label_486.setText(QCoreApplication.translate("MainWindow", u"                          Our More Services", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"Plumbing Services", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"Interior Designing", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"Carpentry", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"Rent Reciept", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"Tenant Verification", None))
        self.label_487.setText("")
        self.label_488.setText("")
        self.label_489.setText("")
        self.label_490.setText("")
        self.label_491.setText("")
        self.label_55.setText("")
        self.label_492.setText(QCoreApplication.translate("MainWindow", u"ALL\n"
"CARPENTRY\n"
"SERVICES", None))
        self.label_493.setText(QCoreApplication.translate("MainWindow", u"CUPBOARD / DRAWER", None))
        self.label_495.setText("")
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_17.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Channel (One set)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 119</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inde"
                        "nt:0px;\"><span style=\" font-size:16pt;\">Get it for \u20b9101 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Installation or replacement of one channel set</span></p></body></html>", None))
        self.pushButton_54.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_22.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Cupboard hinge service (Up to two)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 149</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Get it for \u20b9126 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Installation or replacement of 2 cupboard hinges</span></p></body></html>", None))
        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_23.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Cupboard Sliding Door</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 319</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-"
                        "indent:0px;\"><span style=\" font-size:16pt;\">Get it for \u20b9271 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">___________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*repair work of sliding door's channel</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>", None))
        self.pushButton_56.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_24.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Handle Installation / Replacement</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 99</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Get it for \u20b984 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Installation or replacement of one handle</span></p></body></html>", None))
        self.pushButton_57.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_25.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Channel Repair</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 149</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:"
                        "0px;\"><span style=\" font-size:16pt;\">Get it for \u20b9126 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Adjacement of one channel set</span></p></body></html>", None))
        self.label_494.setText(QCoreApplication.translate("MainWindow", u"Bed", None))
        self.label_496.setText("")
        self.pushButton_58.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_26.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Bed Support</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 369</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px"
                        ";\"><span style=\" font-size:16pt;\">Get it for \u20b9313 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Repair of Bed mattress support</span></p></body></html>", None))
        self.pushButton_59.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_27.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Headboard</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 239</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        "><span style=\" font-size:16pt;\">Get it for \u20b9203 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Repair of either single leg of headboard</span> </p></body></html>", None))
        self.pushButton_60.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_28.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Single Bed Assembly (Without Storage)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 320</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block"
                        "-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Get it for \u20b9272 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Assembly of one single bed </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*procurment of spare parts (at extra cost)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-si"
                        "ze:16pt;\">*clean-up after the service</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Service Warranty &amp; damage cover</span></p></body></html>", None))
        self.pushButton_61.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_29.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Double Bed Assembly</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 440</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-in"
                        "dent:0px;\"><span style=\" font-size:16pt;\">Get it for \u20b9374 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Assembly of one single bed with/without storage</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*procurment of spare parts (at extra cost)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inden"
                        "t:0px;\"><span style=\" font-size:16pt;\">*clean-up after the service</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Service Warranty &amp; damage cover*</span></p></body></html>", None))
        self.pushButton_62.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_30.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Day Bed / Diwan Assembly</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 400</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; te"
                        "xt-indent:0px;\"><span style=\" font-size:16pt;\">Get it for \u20b9340 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Assembly of one day bed</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*procurment of spare parts (at extra cost)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span styl"
                        "e=\" font-size:16pt;\">*clean-up after the service</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Service Warranty &amp; damage cover*</span></p></body></html>", None))
        self.label_497.setText(QCoreApplication.translate("MainWindow", u"Door", None))
        self.label_498.setText("")
        self.pushButton_63.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_31.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Door Lock Replacement</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 369</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-"
                        "indent:0px;\"><span style=\" font-size:16pt;\">Get it for \u20b9313 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Replacement of one door lock in wooden door</span></p></body></html>", None))
        self.pushButton_64.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_32.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Door</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 219</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><sp"
                        "an style=\" font-size:16pt;\">Get it for \u20b9186 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Repair of one wooden door ( alignment fixing, sanding &amp; scraping, door jam fixing)</span></p></body></html>", None))
        self.pushButton_65.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_33.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Door Lock Installation</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 479</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\"><span style=\" font-size:16pt;\">Get it for \u20b9407 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Installation of one new lock in a wooden door.</span></p></body></html>", None))
        self.pushButton_66.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_34.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Sliding Door</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 319</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0p"
                        "x;\"><span style=\" font-size:16pt;\">Get it for \u20b9271 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Repair work of sliding door channel or replacement of bearings</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_67.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_35.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Door Dismantling</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 279</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inden"
                        "t:0px;\"><span style=\" font-size:16pt;\">Get it for \u20b9273 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Installation of upto 4 hinges in a wooden door along with dismentling of one wooden door</span></p></body></html>", None))
        self.label_627.setText(QCoreApplication.translate("MainWindow", u"Order Summary", None))
        self.pushButton_108.setText(QCoreApplication.translate("MainWindow", u"Checkout", None))
        self.label_628.setText("")
        self.pushButton_84.setText("")
        self.label_629.setText(QCoreApplication.translate("MainWindow", u"Item 3", None))
        self.label_630.setText(QCoreApplication.translate("MainWindow", u"\u20b9 122", None))
        self.label_631.setText(QCoreApplication.translate("MainWindow", u"Description for Item3", None))
        self.label_632.setText("")
        self.pushButton_85.setText("")
        self.label_633.setText(QCoreApplication.translate("MainWindow", u"Item 2", None))
        self.label_634.setText(QCoreApplication.translate("MainWindow", u"\u20b9 1404", None))
        self.label_635.setText(QCoreApplication.translate("MainWindow", u"Description for Item2", None))
        self.label_636.setText("")
        self.pushButton_86.setText("")
        self.label_637.setText(QCoreApplication.translate("MainWindow", u"Item 1", None))
        self.label_638.setText(QCoreApplication.translate("MainWindow", u"\u20b9 104", None))
        self.label_639.setText(QCoreApplication.translate("MainWindow", u"Description for Item1", None))
        self.label_938.setText("")
        self.label_939.setText(QCoreApplication.translate("MainWindow", u"ALL\n"
"PLUMBING\n"
"SERVICES", None))
        self.label_940.setText(QCoreApplication.translate("MainWindow", u"CUPBOARD / DRAWER", None))
        self.label_941.setText("")
        self.pushButton_104.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_18.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Wash Basin</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 409</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
                        "\"><span style=\" font-size:16pt;\">Get it for \u20b9347 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Installation of all kinds of wash-basin(sink)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Procurement of spare parts (at extra cost)</span></p></body></html>", None))
        self.pushButton_105.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_36.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Wash Basin Blockage Removal</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 149</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0;"
                        " text-indent:0px;\"><span style=\" font-size:16pt;\">Get it for \u20b9126 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Blockage removal of wash basin and waste pipe</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Procurement of spare parts (at extra cost)</span></p></body></html>", None))
        self.pushButton_106.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_37.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Wash Basin Leakage</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 99</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inde"
                        "nt:0px;\"><span style=\" font-size:16pt;\">Get it for \u20b984 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">___________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Repair or Replacement of 1 waste pipe</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Material charges additional, if any</span></p></body></html>", None))
        self.label_942.setText(QCoreApplication.translate("MainWindow", u"Toilet", None))
        self.label_943.setText("")
        self.pushButton_109.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_40.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Toilet Seat Cover</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 149</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inde"
                        "nt:0px;\"><span style=\" font-size:16pt;\">Get it for \u20b9129 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Replacement of 1 toilet seat cover</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Material charges additional, if any</span></p></body></html>", None))
        self.pushButton_110.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_41.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Jet Spray</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 99</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        "><span style=\" font-size:16pt;\">Get it for \u20b984 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Jet spray or wall mounted holder installation/replacement</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Material Cost will be additional, if any</span></p></body></html>", None))
        self.pushButton_111.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_42.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Toilet Plot Blockage Removal</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 320</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0"
                        "; text-indent:0px;\"><span style=\" font-size:16pt;\">Get it for \u20b9272 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Cleaning a clogged toilet</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*For Indian and Western toilet</span></p></body></html>", None))
        self.pushButton_112.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_43.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Indian Toilet</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 1449</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:"
                        "0px;\"><span style=\" font-size:16pt;\">Get it for \u20b91299 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Installation of indian toilet in an already prepared platform section</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">*Material charges additional, if any</span></p></body></html>", None))
        self.pushButton_113.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.textEdit_44.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\">Wall Mounted Western Toilet</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#128c7e;\">\u20b9 1699</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0"
                        "; text-indent:0px;\"><span style=\" font-size:16pt;\">Get it for \u20b91549 using VIP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_____________________________________________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Replacement of wall mounted one-part and two-part toilet</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Material charges additional, if any</span></p></body></html>", None))
        self.label_614.setText(QCoreApplication.translate("MainWindow", u"Order Summary", None))
        self.pushButton_107.setText(QCoreApplication.translate("MainWindow", u"Checkout", None))
        self.label_615.setText("")
        self.pushButton_79.setText("")
        self.label_616.setText(QCoreApplication.translate("MainWindow", u"Item 4", None))
        self.label_617.setText(QCoreApplication.translate("MainWindow", u"\u20b9 122", None))
        self.label_618.setText(QCoreApplication.translate("MainWindow", u"Description for Item4", None))
        self.label_619.setText("")
        self.pushButton_82.setText("")
        self.label_620.setText(QCoreApplication.translate("MainWindow", u"Item 2", None))
        self.label_621.setText(QCoreApplication.translate("MainWindow", u"\u20b9 1404", None))
        self.label_622.setText(QCoreApplication.translate("MainWindow", u"Description for Item2", None))
        self.label_623.setText("")
        self.pushButton_83.setText("")
        self.label_624.setText(QCoreApplication.translate("MainWindow", u"Item 3", None))
        self.label_625.setText(QCoreApplication.translate("MainWindow", u"\u20b9 104", None))
        self.label_626.setText(QCoreApplication.translate("MainWindow", u"Description for Item3", None))
        self.label_944.setText("")
        self.label_945.setText(QCoreApplication.translate("MainWindow", u"Interior\n"
"Designer", None))
        self.label_670.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Courtyard", None))
        self.label_586.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_587.setText(QCoreApplication.translate("MainWindow", u"MS Reality", None))
        self.pushButton_76.setText(QCoreApplication.translate("MainWindow", u" Get more info ", None))
        self.label_588.setText(QCoreApplication.translate("MainWindow", u"\u20b92.2 Cr - 3.41 Cr | ", None))
        self.label_589.setText(QCoreApplication.translate("MainWindow", u"\u20b934 K/sq.ft", None))
        self.label_590.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b91.09 L", None))
        self.label_591.setText("")
        self.label_595.setText(QCoreApplication.translate("MainWindow", u"Opp Kalina University, Kalina, Santacruz East, Western Suburbs, Mumbai", None))
        self.label_596.setText("")
        self.label_597.setText("")
        self.label_592.setText(QCoreApplication.translate("MainWindow", u"2, 2.5, 3 BHK Apartments\n"
"    Configurations", None))
        self.label_593.setText(QCoreApplication.translate("MainWindow", u"    March, 2028\n"
"Possession Starts", None))
        self.label_594.setText(QCoreApplication.translate("MainWindow", u"648 sqft - 1004 sqft\n"
"     (Carpet area)", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Name", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Email", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Contact", None))
        self.pushButton_78.setText(QCoreApplication.translate("MainWindow", u"Get Contact", None))
        self.label_598.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Contact Sellers in   </span><span style=\" font-size:22pt; font-weight:700; color:#128c7e;\">Courtyard</span></p></body></html>", None))
        self.label_599.setText(QCoreApplication.translate("MainWindow", u"*Please share your contact", None))
        self.label_600.setText(QCoreApplication.translate("MainWindow", u"       Why Courtyard?", None))
        self.label_602.setText(QCoreApplication.translate("MainWindow", u" 1] Jodi Apartments Options available", None))
        self.label_604.setText(QCoreApplication.translate("MainWindow", u" 2] Freehold Land Parcel", None))
        self.label_605.setText(QCoreApplication.translate("MainWindow", u" 3] Debt Free Project", None))
        self.label_606.setText(QCoreApplication.translate("MainWindow", u" 4] Project with Open Space and Multiple amenities", None))
        self.label_607.setText(QCoreApplication.translate("MainWindow", u" 5] Low-density Project", None))
        self.label_608.setText(QCoreApplication.translate("MainWindow", u" 6] 500m from Highway", None))
        self.label_610.setText(QCoreApplication.translate("MainWindow", u" 7] 2-3 mins from BKC", None))
        self.label_601.setText("")
        self.label_603.setText("")
        self.label_609.setText(QCoreApplication.translate("MainWindow", u"------------------------------------------------------o                                                o------------------------------------------------------", None))
        self.label_611.setText("")
        self.textEdit_19.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:x-large; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700; color:#128c7e;\">About Courtyard ?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -q"
                        "t-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Courtyard by MS Realty is a luxurious residential under-construction project in Kalina, Santacruz East, Mumbai. The project offers lavish 2, 2.5 and 3 BHK apartments with sizes ranging from 648 sq. ft. to 1004 sq. ft. The project comprises 4 buildings with a total of 198 units. The project is designed to provide a comfortable and peaceful living experience to its residents. The apartments are well-ventilated and designed to offer maximum space utilization.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p sty"
                        "le=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700; color:#128c7e;\">About the Builder :</span><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">We create human spaces that are a synthesis of lifestyle and comfort. MS Realty, an extension of one of the world\u2019s largest diamond manufacturing companies, M Suresh Group, is a Mumbai-based company. We have been in the business of producing diamonds of the highest quality for decades, and with the same principle and philosophy, we are also spreading our wings in the real estate business. Lifestyles are evolving, and so are the spaces we occupy. We believe in designing spaces that follow the golden ratio. The spaces are efficient and functional, taking into account the ergonomics of their inhabitants; every movement. To re"
                        "build the sync between humans and spaces, we create spaces that help people live, grow and enjoy.</span><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700; color:#128c7e;\">About the Locality :</span><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Kalina, Santacruz East is a prime residential locality in Mumbai. The area is well connected to other parts of the city through various modes of transportation. The locality has several hospitals and schools in its vicinity. Some of the nearby hospitals include Asian Heart Institute, Guru Nanak Hospital, and Lilavati Hospital. Some of the nearby "
                        "schools include Mumbai University, Dhirubhai Ambani Intl School, Kohinoor Intl School, and Mount Litera School. The area is also well-connected to major highways, airports, and stations, making it an ideal location for residential purposes.</span><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700; color:#128c7e;\">Project Amenities :</span><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Courtyard by MS Realty offers a wide range of amenities to its residents. The project features a Fully Equipped GYM, Multi-Purpose Banquet Hall, Lounge Area, Swimming Pool, Landscape Garden, Landscape Terra"
                        "ce and Indoor Play Area. The project has been designed to provide a comfortable and luxurious living experience to its residents. The amenities are designed to cater to the needs of all age groups and offer a perfect balance of luxury and comfort.\u00a0</span></p></body></html>", None))
        self.label_612.setText("")
        self.label_641.setText(QCoreApplication.translate("MainWindow", u"Liberty One", None))
        self.label_642.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_643.setText(QCoreApplication.translate("MainWindow", u"DOWNTOWN LIFESPACES", None))
        self.pushButton_80.setText(QCoreApplication.translate("MainWindow", u" Get more info ", None))
        self.label_644.setText(QCoreApplication.translate("MainWindow", u"\u20b91.3 Cr - 2.9 Cr | ", None))
        self.label_645.setText(QCoreApplication.translate("MainWindow", u"\u20b931.53 K/sq.ft", None))
        self.label_646.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b963.03 K", None))
        self.label_647.setText("")
        self.label_648.setText(QCoreApplication.translate("MainWindow", u"Mamletdarwadi Main Rd, Malad, Navy Colony, Kanchpada, Malad West, Mumbai", None))
        self.label_649.setText("")
        self.label_650.setText("")
        self.label_651.setText(QCoreApplication.translate("MainWindow", u"1,2 BHK Apartments\n"
"    Configurations", None))
        self.label_652.setText(QCoreApplication.translate("MainWindow", u"     June, 2026\n"
"Possession Starts", None))
        self.label_653.setText(QCoreApplication.translate("MainWindow", u"529 sq.ft. - 652 sq.ft.\n"
"   (Carpet Area)", None))
        self.lineEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Name", None))
        self.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Email", None))
        self.lineEdit_16.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Contact", None))
        self.pushButton_81.setText(QCoreApplication.translate("MainWindow", u"Get Contact", None))
        self.label_654.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Contact Sellers in </span><span style=\" font-size:22pt; font-weight:700; color:#128c7e;\">Liberty One</span></p></body></html>", None))
        self.label_655.setText(QCoreApplication.translate("MainWindow", u"*Please share your contact", None))
        self.label_656.setText(QCoreApplication.translate("MainWindow", u"       Why Liberty One?", None))
        self.label_657.setText(QCoreApplication.translate("MainWindow", u" 1] Jodi Apartments Options available", None))
        self.label_658.setText(QCoreApplication.translate("MainWindow", u" 2] Freehold Land Parcel", None))
        self.label_659.setText(QCoreApplication.translate("MainWindow", u" 3] Debt Free Project", None))
        self.label_660.setText(QCoreApplication.translate("MainWindow", u" 4] Project with Open Space and Multiple amenities", None))
        self.label_661.setText(QCoreApplication.translate("MainWindow", u" 5] Low-density Project", None))
        self.label_662.setText(QCoreApplication.translate("MainWindow", u" 6] 500m from Highway", None))
        self.label_663.setText(QCoreApplication.translate("MainWindow", u" 7] 2-3 mins from BKC", None))
        self.label_664.setText("")
        self.label_666.setText(QCoreApplication.translate("MainWindow", u"------------------------------------------------------o                                                o------------------------------------------------------", None))
        self.label_667.setText("")
        self.textEdit_21.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:x-large; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700; color:#128c7e;\">About Liberty One ?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; "
                        "-qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Courtyard by MS Realty is a luxurious residential under-construction project in Kalina, Santacruz East, Mumbai. The project offers lavish 2, 2.5 and 3 BHK apartments with sizes ranging from 648 sq. ft. to 1004 sq. ft. The project comprises 4 buildings with a total of 198 units. The project is designed to provide a comfortable and peaceful living experience to its residents. The apartments are well-ventilated and designed to offer maximum space utilization.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p s"
                        "tyle=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700; color:#128c7e;\">About the Builder :</span><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">We create human spaces that are a synthesis of lifestyle and comfort. MS Realty, an extension of one of the world\u2019s largest diamond manufacturing companies, M Suresh Group, is a Mumbai-based company. We have been in the business of producing diamonds of the highest quality for decades, and with the same principle and philosophy, we are also spreading our wings in the real estate business. Lifestyles are evolving, and so are the spaces we occupy. We believe in designing spaces that follow the golden ratio. The spaces are efficient and functional, taking into account the ergonomics of their inhabitants; every movement. To "
                        "rebuild the sync between humans and spaces, we create spaces that help people live, grow and enjoy.</span><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700; color:#128c7e;\">About the Locality :</span><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Kalina, Santacruz East is a prime residential locality in Mumbai. The area is well connected to other parts of the city through various modes of transportation. The locality has several hospitals and schools in its vicinity. Some of the nearby hospitals include Asian Heart Institute, Guru Nanak Hospital, and Lilavati Hospital. Some of the nearb"
                        "y schools include Mumbai University, Dhirubhai Ambani Intl School, Kohinoor Intl School, and Mount Litera School. The area is also well-connected to major highways, airports, and stations, making it an ideal location for residential purposes.</span><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700; color:#128c7e;\">Project Amenities :</span><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Courtyard by MS Realty offers a wide range of amenities to its residents. The project features a Fully Equipped GYM, Multi-Purpose Banquet Hall, Lounge Area, Swimming Pool, Landscape Garden, Landscape Ter"
                        "race and Indoor Play Area. The project has been designed to provide a comfortable and luxurious living experience to its residents. The amenities are designed to cater to the needs of all age groups and offer a perfect balance of luxury and comfort.\u00a0</span></p></body></html>", None))
        self.label_668.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Notify", None))
        self.label_520.setText(QCoreApplication.translate("MainWindow", u"Tathastu", None))
        self.label_521.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_522.setText(QCoreApplication.translate("MainWindow", u"H abd D Projects", None))
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_523.setText(QCoreApplication.translate("MainWindow", u"\u20b91.2 Cr - 3.16 Cr | ", None))
        self.label_524.setText(QCoreApplication.translate("MainWindow", u"\u20b930 K/sq.ft", None))
        self.label_525.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b959.72 K", None))
        self.label_526.setText("")
        self.label_527.setText(QCoreApplication.translate("MainWindow", u"1, 2, 3 BHK Apartments\n"
"Configurations", None))
        self.label_528.setText(QCoreApplication.translate("MainWindow", u"July, 2026\n"
"Possession Starts", None))
        self.label_529.setText(QCoreApplication.translate("MainWindow", u"401 sq.ft. - 1054 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_530.setText(QCoreApplication.translate("MainWindow", u"Tathastu 22/A, Dawood Baug, Off J.P. Rd., Andheri West, Western Suburbs, Mumbai", None))
        self.label_564.setText(QCoreApplication.translate("MainWindow", u"Green Stone", None))
        self.label_565.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_566.setText(QCoreApplication.translate("MainWindow", u"APLITE GROUP", None))
        self.pushButton_70.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_567.setText(QCoreApplication.translate("MainWindow", u"\u20b91.72 Cr - 3.06 Cr | ", None))
        self.label_568.setText(QCoreApplication.translate("MainWindow", u"\u20b943 K/sq.ft", None))
        self.label_569.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b985.39 K", None))
        self.label_570.setText("")
        self.label_571.setText(QCoreApplication.translate("MainWindow", u"1, 2 BHK Apartments\n"
"Configurations", None))
        self.label_572.setText(QCoreApplication.translate("MainWindow", u"Dec, 2027\n"
"Possession Starts", None))
        self.label_573.setText(QCoreApplication.translate("MainWindow", u"400 sq.ft. - 741 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_574.setText(QCoreApplication.translate("MainWindow", u"Ramabai Ambedkar Marg, Opposite Haj House, 3rd Floor, C Wing, Fort, Mumbai", None))
        self.label_553.setText(QCoreApplication.translate("MainWindow", u"Lodha Park", None))
        self.label_554.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_555.setText(QCoreApplication.translate("MainWindow", u"LODHA GROUP", None))
        self.pushButton_69.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_556.setText(QCoreApplication.translate("MainWindow", u"\u20b93.4 Cr - 4.41 Cr | ", None))
        self.label_557.setText(QCoreApplication.translate("MainWindow", u"\u20b934 K/sq.ftl", None))
        self.label_558.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b91.64 Lacs", None))
        self.label_559.setText("")
        self.label_560.setText(QCoreApplication.translate("MainWindow", u"3, 4 BHK Apartments\n"
"Configurations", None))
        self.label_561.setText(QCoreApplication.translate("MainWindow", u"Dec, 2019\n"
"Possession Starts", None))
        self.label_562.setText(QCoreApplication.translate("MainWindow", u"2016 sq.ft. - 2421 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_563.setText(QCoreApplication.translate("MainWindow", u"Opposite Hard Rock Cafe, Pandurang Budhkar Marg, Worli, Lower Parel, Mumbai", None))
        self.label_542.setText(QCoreApplication.translate("MainWindow", u"Rajshree Eleven", None))
        self.label_543.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_544.setText(QCoreApplication.translate("MainWindow", u"RAJSHREE BUILDERS", None))
        self.pushButton_68.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_545.setText(QCoreApplication.translate("MainWindow", u"\u20b92.12 Cr - 4.41 Cr | ", None))
        self.label_546.setText(QCoreApplication.translate("MainWindow", u"\u20b91.5 L/sq.ft", None))
        self.label_547.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b91.25 Lacs", None))
        self.label_548.setText("")
        self.label_549.setText(QCoreApplication.translate("MainWindow", u"2, 3 BHK Apartments\n"
"Configurations", None))
        self.label_550.setText(QCoreApplication.translate("MainWindow", u"Ready to Move\n"
"Possession Starts", None))
        self.label_551.setText(QCoreApplication.translate("MainWindow", u"638 sq.ft. - 1174 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_552.setText(QCoreApplication.translate("MainWindow", u"Building No. 11, Behind Siddhivinayak Mandir, off. Hingwala Lane, Ghatkopar (E), Mumbai", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Courtyard", None))
        self.label_499.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_500.setText(QCoreApplication.translate("MainWindow", u"Ms reality", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_501.setText(QCoreApplication.translate("MainWindow", u"\u20b92.2 Cr - 3.41 Cr | ", None))
        self.label_502.setText(QCoreApplication.translate("MainWindow", u"\u20b934 K/sq.ft", None))
        self.label_503.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b91.09 Lacs", None))
        self.label_504.setText("")
        self.label_505.setText(QCoreApplication.translate("MainWindow", u"2, 2.5, 3 BHK Apartments\n"
"Configurations", None))
        self.label_506.setText(QCoreApplication.translate("MainWindow", u"Mar, 2028\n"
"Possession Starts", None))
        self.label_507.setText(QCoreApplication.translate("MainWindow", u"648 sq.ft. - 1004 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_508.setText(QCoreApplication.translate("MainWindow", u"Opp Kalina University, Kalina, Santacruz East, Western Suburbs, Mumbai", None))
        self.pushButton_74.setText("")
        self.label_575.setText(QCoreApplication.translate("MainWindow", u"Lashkaria Pearl", None))
        self.label_576.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_577.setText(QCoreApplication.translate("MainWindow", u"LAKSHARIA PEARL", None))
        self.pushButton_71.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_578.setText(QCoreApplication.translate("MainWindow", u"\u20b960.0 L - 91.0 L | ", None))
        self.label_579.setText(QCoreApplication.translate("MainWindow", u"\u20b925.8 K/sq.ft", None))
        self.label_580.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b942.70 K", None))
        self.label_581.setText("")
        self.label_582.setText(QCoreApplication.translate("MainWindow", u"1 BHK Apartments\n"
"Configurations", None))
        self.label_583.setText(QCoreApplication.translate("MainWindow", u"Nov, 2024\n"
"Possession Starts", None))
        self.label_584.setText(QCoreApplication.translate("MainWindow", u"333 sq.ft. - 351 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_585.setText(QCoreApplication.translate("MainWindow", u"Lashkaria Pearl, Link Road, Near Gandhi School, Oshiwara, Mumbai", None))
        self.label_531.setText(QCoreApplication.translate("MainWindow", u"VKLAL Phase I", None))
        self.label_532.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_533.setText(QCoreApplication.translate("MainWindow", u"VIKYALAL INVESTMENT COMPANY", None))
        self.pushButton_53.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_534.setText(QCoreApplication.translate("MainWindow", u"\u20b975.22 L - 88.27 L | ", None))
        self.label_535.setText(QCoreApplication.translate("MainWindow", u"\u20b934 K/sq.ftl", None))
        self.label_536.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b934.34 K", None))
        self.label_537.setText("")
        self.label_538.setText(QCoreApplication.translate("MainWindow", u"1 BHK Apartments\n"
"Configurations", None))
        self.label_539.setText(QCoreApplication.translate("MainWindow", u"Dec, 2025\n"
"Possession Starts", None))
        self.label_540.setText(QCoreApplication.translate("MainWindow", u"332 sq.ft. - 412 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_541.setText(QCoreApplication.translate("MainWindow", u"Sant Gadge Maharaj Marg, Kajupada, Borivali, Western Suburbs, Mumbai", None))
        self.label_509.setText(QCoreApplication.translate("MainWindow", u"Liberty One", None))
        self.label_510.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_511.setText(QCoreApplication.translate("MainWindow", u"DOWNTOWN LIFESPACES", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_512.setText(QCoreApplication.translate("MainWindow", u"\u20b91.3 Cr - 2.9 Cr | ", None))
        self.label_513.setText(QCoreApplication.translate("MainWindow", u"\u20b931.53 K/sq.ft", None))
        self.label_514.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b963.03 K", None))
        self.label_515.setText("")
        self.label_516.setText(QCoreApplication.translate("MainWindow", u"1,2 BHK Apartments\n"
"Configurations", None))
        self.label_517.setText(QCoreApplication.translate("MainWindow", u"June, 2026\n"
"Possession Starts", None))
        self.label_518.setText(QCoreApplication.translate("MainWindow", u"529 sq.ft. - 652 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_519.setText(QCoreApplication.translate("MainWindow", u"Mamletdarwadi Main Rd, Malad, Navy Colony, Kanchpada, Malad West, Mumbai", None))
        self.pushButton_75.setText("")
        self.label_762.setText(QCoreApplication.translate("MainWindow", u"Ashar Merac", None))
        self.label_763.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_764.setText(QCoreApplication.translate("MainWindow", u"ASHAR GROUP", None))
        self.pushButton_88.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_765.setText(QCoreApplication.translate("MainWindow", u"\u20b970 K - 1.69 Cr | ", None))
        self.label_766.setText(QCoreApplication.translate("MainWindow", u"\u20b920.18 K/sq.ft", None))
        self.label_767.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b938.72 K", None))
        self.label_768.setText(QCoreApplication.translate("MainWindow", u"1, 2, 3 BHK Apartments\n"
"Configurations", None))
        self.label_769.setText(QCoreApplication.translate("MainWindow", u"Dec, 2028\n"
"Possession Starts", None))
        self.label_770.setText(QCoreApplication.translate("MainWindow", u"390 sq.ft. - 830 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_771.setText(QCoreApplication.translate("MainWindow", u"Ashar Merac, Thane(West), Thane", None))
        self.label_772.setText("")
        self.label_773.setText(QCoreApplication.translate("MainWindow", u"Shivalaya Heights", None))
        self.label_774.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_775.setText(QCoreApplication.translate("MainWindow", u"RUDIS INFRA", None))
        self.pushButton_89.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_776.setText(QCoreApplication.translate("MainWindow", u"\u20b936.99 L - 64.78 L |", None))
        self.label_777.setText(QCoreApplication.translate("MainWindow", u"\u20b934 K/sq.ftl", None))
        self.label_778.setText(QCoreApplication.translate("MainWindow", u"Emi start at  19.59 K", None))
        self.label_779.setText("")
        self.label_780.setText(QCoreApplication.translate("MainWindow", u"1, 2 BHK Apartments\n"
"Configurations", None))
        self.label_781.setText(QCoreApplication.translate("MainWindow", u"Dec, 2027\n"
"Possession Starts", None))
        self.label_782.setText(QCoreApplication.translate("MainWindow", u"418 sq.ft. - 732 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_783.setText(QCoreApplication.translate("MainWindow", u"153, Hissa No-1/1/ & Hissa No-2, Shilphata, Beyond Thane, Navi Mumbai", None))
        self.label_784.setText(QCoreApplication.translate("MainWindow", u"Lakescape", None))
        self.label_785.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_786.setText(QCoreApplication.translate("MainWindow", u"HOMEBAZAAR.COM", None))
        self.pushButton_90.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_787.setText(QCoreApplication.translate("MainWindow", u"\u20b91.54 Cr - 1.96 Cr | ", None))
        self.label_788.setText(QCoreApplication.translate("MainWindow", u"\u20b921.26 K/sq.ft", None))
        self.label_789.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b971.99 K", None))
        self.label_790.setText("")
        self.label_791.setText(QCoreApplication.translate("MainWindow", u"2, 3 BHK Apartments\n"
"Configurations", None))
        self.label_792.setText(QCoreApplication.translate("MainWindow", u"Dec, 2028\n"
"Possession Starts", None))
        self.label_793.setText(QCoreApplication.translate("MainWindow", u"680 sq.ft. - 925 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_794.setText(QCoreApplication.translate("MainWindow", u"G B Road, Kavesar Village, Thane West, Ghodbunder Road, Thane", None))
        self.label_795.setText(QCoreApplication.translate("MainWindow", u"Tulsi Ariana\n"
"", None))
        self.label_796.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_797.setText(QCoreApplication.translate("MainWindow", u"TULSI REALITY", None))
        self.pushButton_91.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_798.setText(QCoreApplication.translate("MainWindow", u"\u20b990.0 L - 1.8 Cr | ", None))
        self.label_799.setText(QCoreApplication.translate("MainWindow", u"\u20b954 K/sq.ftl", None))
        self.label_800.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b945.68 K", None))
        self.label_801.setText("")
        self.label_802.setText(QCoreApplication.translate("MainWindow", u"2, 4 BHK Apartments\n"
"Configurations", None))
        self.label_803.setText(QCoreApplication.translate("MainWindow", u"Dec, 2024\n"
"Possession Starts", None))
        self.label_804.setText(QCoreApplication.translate("MainWindow", u"734 sq.ft. - 1449 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_805.setText(QCoreApplication.translate("MainWindow", u"Vasant Valley Road, Near Poddar International School, Kalyan West, Thane", None))
        self.label_806.setText(QCoreApplication.translate("MainWindow", u"Dosti Heron", None))
        self.label_807.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_808.setText(QCoreApplication.translate("MainWindow", u"DOSTI REALTY", None))
        self.pushButton_92.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_809.setText(QCoreApplication.translate("MainWindow", u"\u20b945.0 L - 1.1 Cr | ", None))
        self.label_810.setText(QCoreApplication.translate("MainWindow", u"\u20b915.63 K/sq.ft", None))
        self.label_811.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b923.83 K", None))
        self.label_812.setText("")
        self.label_813.setText(QCoreApplication.translate("MainWindow", u"Studio, 1, 2 BHK Apartments\n"
"Configurations", None))
        self.label_814.setText(QCoreApplication.translate("MainWindow", u"Dec, 2027\n"
"Possession Starts", None))
        self.label_815.setText(QCoreApplication.translate("MainWindow", u"288 sq.ft. - 604 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_816.setText(QCoreApplication.translate("MainWindow", u"Dosti Heron, Balkum, Thane West, Thane", None))
        self.label_817.setText(QCoreApplication.translate("MainWindow", u"Parijas Horizon\n"
"", None))
        self.label_818.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_819.setText(QCoreApplication.translate("MainWindow", u"PARIJAS GROUP", None))
        self.pushButton_93.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_820.setText(QCoreApplication.translate("MainWindow", u"\u20b945.3 L - 66.0 L | ", None))
        self.label_821.setText(QCoreApplication.translate("MainWindow", u"\u20b98.85 K/sq.ft", None))
        self.label_822.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b923..05 K", None))
        self.label_823.setText("")
        self.label_824.setText(QCoreApplication.translate("MainWindow", u"1, 2 BHK Apartments\n"
"Configurations", None))
        self.label_825.setText(QCoreApplication.translate("MainWindow", u"Jun, 2028\n"
"Possession Starts", None))
        self.label_826.setText(QCoreApplication.translate("MainWindow", u"484 sq.ft. - 757 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_827.setText(QCoreApplication.translate("MainWindow", u"Gandhare, Kalyan West, Beyond Thane, Thane", None))
        self.label_828.setText(QCoreApplication.translate("MainWindow", u"Dosti Olive", None))
        self.label_829.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_830.setText(QCoreApplication.translate("MainWindow", u"DOSTI REALITY", None))
        self.pushButton_94.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_831.setText(QCoreApplication.translate("MainWindow", u"\u20b91.25 Cr - 2.04 Cr | ", None))
        self.label_832.setText(QCoreApplication.translate("MainWindow", u"\u20b934 K/sq.ft", None))
        self.label_833.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b962.86 K", None))
        self.label_834.setText("")
        self.label_835.setText(QCoreApplication.translate("MainWindow", u"2, 3 BHK Apartments\n"
"Configurations", None))
        self.label_836.setText(QCoreApplication.translate("MainWindow", u"Sep, 2028\n"
"Possession Starts", None))
        self.label_837.setText(QCoreApplication.translate("MainWindow", u"628 sq.ft. - 1022 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_838.setText(QCoreApplication.translate("MainWindow", u"Balkum, Thane West, Thane", None))
        self.label_839.setText(QCoreApplication.translate("MainWindow", u"Tisai Residency", None))
        self.label_840.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_841.setText(QCoreApplication.translate("MainWindow", u"SKY TOUCH", None))
        self.pushButton_95.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_842.setText(QCoreApplication.translate("MainWindow", u"\u20b941.63 l - 63.23 Cr | ", None))
        self.label_843.setText(QCoreApplication.translate("MainWindow", u"\u20b96 K/sq.ft", None))
        self.label_844.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b921.76 K", None))
        self.label_845.setText("")
        self.label_846.setText(QCoreApplication.translate("MainWindow", u"1, 2 BHK Apartments\n"
"Configurations", None))
        self.label_847.setText(QCoreApplication.translate("MainWindow", u"Jun, 2027\n"
"Possession Starts", None))
        self.label_848.setText(QCoreApplication.translate("MainWindow", u"685 sq.ft. - 1050 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_849.setText(QCoreApplication.translate("MainWindow", u"Namdev Wadi, Behind Tisai Marriage Hall, Tisgaon, Kalyan (E ), Thane", None))
        self.label_850.setText(QCoreApplication.translate("MainWindow", u"Sukhwani Nysa", None))
        self.label_851.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_852.setText(QCoreApplication.translate("MainWindow", u"Ms Ravet, Pimpri Chinchwad, Pune", None))
        self.pushButton_96.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_853.setText(QCoreApplication.translate("MainWindow", u"\u20b933.52 L - 56.32 L | ", None))
        self.label_854.setText(QCoreApplication.translate("MainWindow", u"\u20b934 K/sq.ftl", None))
        self.label_855.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b917.75 K", None))
        self.label_856.setText("")
        self.label_857.setText(QCoreApplication.translate("MainWindow", u"2 BHK Apartments\n"
"Configurations", None))
        self.label_858.setText(QCoreApplication.translate("MainWindow", u"Jun, 2024\n"
"Possession Starts", None))
        self.label_859.setText(QCoreApplication.translate("MainWindow", u"466 sq.ft. - 783 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_860.setText(QCoreApplication.translate("MainWindow", u"Ravet, Pimpri Chinchwad, Pune", None))
        self.label_861.setText(QCoreApplication.translate("MainWindow", u"Silver Gardenia", None))
        self.label_862.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_863.setText(QCoreApplication.translate("MainWindow", u"SILVER GROUP", None))
        self.pushButton_97.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_864.setText(QCoreApplication.translate("MainWindow", u"\u20b960.0 L - 1.7 Cr | ", None))
        self.label_865.setText(QCoreApplication.translate("MainWindow", u"\u20b924 K/sq.ftl", None))
        self.label_866.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b935.23 K", None))
        self.label_867.setText("")
        self.label_868.setText(QCoreApplication.translate("MainWindow", u"2, 3, 4, 5 BHK Apartments\n"
"Configurations", None))
        self.label_869.setText(QCoreApplication.translate("MainWindow", u"Dec, 2025\n"
"Possession Starts", None))
        self.label_870.setText(QCoreApplication.translate("MainWindow", u"716 sq.ft. - 1655 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_871.setText(QCoreApplication.translate("MainWindow", u"Silver Gardenia, Dehu-Moshi Road, Opp. D-Mart, Borhadewadi, PCMC, Pimpri Chinchwad, Pune", None))
        self.label_872.setText(QCoreApplication.translate("MainWindow", u"Namrata Prime Land", None))
        self.label_873.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_874.setText(QCoreApplication.translate("MainWindow", u"NAMRATA GROUP", None))
        self.pushButton_98.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_875.setText(QCoreApplication.translate("MainWindow", u"\u20b926.37 L - 44.5 L | ", None))
        self.label_876.setText(QCoreApplication.translate("MainWindow", u"\u20b97 K/sq.ftl", None))
        self.label_877.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b913.97 K", None))
        self.label_878.setText("")
        self.label_879.setText(QCoreApplication.translate("MainWindow", u"1, 2 BHK Apartments\n"
"Configurations", None))
        self.label_880.setText(QCoreApplication.translate("MainWindow", u"Sep, 2023\n"
"Possession Starts", None))
        self.label_881.setText(QCoreApplication.translate("MainWindow", u"429 sq.ft. - 636 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_882.setText(QCoreApplication.translate("MainWindow", u"Station Road, Dnyaneshwar Nagar, Talegaon Dabhade, Pune", None))
        self.label_883.setText(QCoreApplication.translate("MainWindow", u"The Nature", None))
        self.label_884.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_885.setText(QCoreApplication.translate("MainWindow", u"MAHARASHTRA HOUSING CORPORATION", None))
        self.pushButton_99.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_886.setText(QCoreApplication.translate("MainWindow", u"\u20b91.86 Cr - 2.9 Cr | ", None))
        self.label_887.setText(QCoreApplication.translate("MainWindow", u"\u20b934 K/sq.ftl", None))
        self.label_888.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b992.34 K", None))
        self.label_889.setText("")
        self.label_890.setText(QCoreApplication.translate("MainWindow", u"2 BHK Apartments\n"
"Configurations", None))
        self.label_891.setText(QCoreApplication.translate("MainWindow", u"Dec, 2025\n"
"Possession Starts", None))
        self.label_892.setText(QCoreApplication.translate("MainWindow", u"1383 sq.ft. - 3000 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_893.setText(QCoreApplication.translate("MainWindow", u"The Nature, Mukaiwadi, Pirangut Road, Pune", None))
        self.label_894.setText(QCoreApplication.translate("MainWindow", u"Ivory Heights", None))
        self.label_895.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_896.setText(QCoreApplication.translate("MainWindow", u"AAKAR REALTIES", None))
        self.pushButton_100.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_897.setText(QCoreApplication.translate("MainWindow", u"\u20b934.31 L - 52.05 L | ", None))
        self.label_898.setText(QCoreApplication.translate("MainWindow", u"\u20b911.75 K/sq.ft", None))
        self.label_899.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b918.7 K", None))
        self.label_900.setText("")
        self.label_901.setText(QCoreApplication.translate("MainWindow", u"1, 1.5, 2, 2.5 BHK Apartments\n"
"Configurations", None))
        self.label_902.setText(QCoreApplication.translate("MainWindow", u"Dec, 2027\n"
"Possession Starts", None))
        self.label_903.setText(QCoreApplication.translate("MainWindow", u"486 sq.ft. - 713 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_904.setText(QCoreApplication.translate("MainWindow", u"Survey No. 34/2, 34/3, 34/4 Chovisawadi, Charholi Budruk, Pune", None))
        self.label_905.setText(QCoreApplication.translate("MainWindow", u"Dosti Greenscapes", None))
        self.label_906.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_907.setText(QCoreApplication.translate("MainWindow", u"DOSTI REALTY", None))
        self.pushButton_101.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_908.setText(QCoreApplication.translate("MainWindow", u"\u20b978.5 L - 1.66 Cr | ", None))
        self.label_909.setText(QCoreApplication.translate("MainWindow", u"\u20b911.75 K/sq.ftl", None))
        self.label_910.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b938.97 K", None))
        self.label_911.setText("")
        self.label_912.setText(QCoreApplication.translate("MainWindow", u"2, 3, 4 BHK Apartments\n"
"Configurations", None))
        self.label_913.setText(QCoreApplication.translate("MainWindow", u"Dec, 2027\n"
"Possession Starts", None))
        self.label_914.setText(QCoreApplication.translate("MainWindow", u"677 sq.ft. - 1395 sq.ft..\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_915.setText(QCoreApplication.translate("MainWindow", u"Dosti Greenscapes, Hadapsar, Pune", None))
        self.label_916.setText(QCoreApplication.translate("MainWindow", u"Namrata Eco City", None))
        self.label_917.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_918.setText(QCoreApplication.translate("MainWindow", u"NAMRATA GROUP", None))
        self.pushButton_102.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_919.setText(QCoreApplication.translate("MainWindow", u"\u20b925.98 L - 40.66 L | ", None))
        self.label_920.setText(QCoreApplication.translate("MainWindow", u"\u20b94.27 K/sq.ft", None))
        self.label_921.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b913.76 K", None))
        self.label_922.setText("")
        self.label_923.setText(QCoreApplication.translate("MainWindow", u"1, 2 BHK Apartments\n"
"Configurations", None))
        self.label_924.setText(QCoreApplication.translate("MainWindow", u"Ready to Move\n"
"Possession Starts", None))
        self.label_925.setText(QCoreApplication.translate("MainWindow", u"647 sq.ft. - 952 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_926.setText(QCoreApplication.translate("MainWindow", u"S. No. 27/A/1/2B/5, Varale Road, Near New D.Y. Patil College, Talegaon Dabhade, Pune", None))
        self.label_927.setText(QCoreApplication.translate("MainWindow", u"Shubharambh Clara", None))
        self.label_928.setText(QCoreApplication.translate("MainWindow", u"By ", None))
        self.label_929.setText(QCoreApplication.translate("MainWindow", u"URBAN NEST", None))
        self.pushButton_103.setText(QCoreApplication.translate("MainWindow", u"Click for more info ", None))
        self.label_930.setText(QCoreApplication.translate("MainWindow", u"\u20b92.2 Cr - 3.41 Cr | ", None))
        self.label_931.setText(QCoreApplication.translate("MainWindow", u"\u20b99.63 K/sq.ft", None))
        self.label_932.setText(QCoreApplication.translate("MainWindow", u"Emi start at  \u20b935.06 K", None))
        self.label_933.setText("")
        self.label_934.setText(QCoreApplication.translate("MainWindow", u"2, 3 BHK Apartments\n"
"Configurations", None))
        self.label_935.setText(QCoreApplication.translate("MainWindow", u"Dec, 2028\n"
"Possession Starts", None))
        self.label_936.setText(QCoreApplication.translate("MainWindow", u"687 sq.ft. - 1086 sq.ft.\n"
"(Carpet Area)\n"
"Sizes", None))
        self.label_937.setText(QCoreApplication.translate("MainWindow", u"Plot No. 76/1/1, 76/1/2, 76/1/3 And 76/1/1/1/2/1/3 At Ravet, Pimpri Chinchwad, Pune", None))
        self.label_640.setText("")
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
        self.label_613.setText(QCoreApplication.translate("MainWindow", u"Comming Soon", None))
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
        self.pushButton_72.setText("")
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
        self.pushButton_73.setText("")
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

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())