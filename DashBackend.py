from NdashPy import Ui_MainWindow
import pymysql as psql

class Backend:
    def _init_(self):
        self.dash = Ui_MainWindow()
        self.dash.own_button.clicked.connect(self.clickhere)

    def mysql(self):
        self.a = psql.connect(host='localhost',port=3306,user='root',password='root',charset='UTF-8',database='MIddleman')
        self.curr = self.a.cursor()

    def clickhere(self):
        print(self.dash.select_city_lab.text())
        #self.dash.contact_number.text(),self.dash.select_city_lab.text(),self.dash.select_prop_type.text(),self.dash.tell_us_more.text()
    
    def heeeeee(self):
        print(self.dash.MMcash)
    
# Create an instance of Backend
backend = Backend()
# Call the heeeeee method to print the MMcash attribute
backend.heeeeee()