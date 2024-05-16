from customtkinter import *
from PIL import Image

root = CTk()
root.geometry("1920x1080")

#Functions
def home():
    home_lab.configure(fg_color="#DEF4DD")
    rent_lab.configure(fg_color="#CFB2B7")
    buy_lab.configure(fg_color="#CFB2B7")
    about_lab.configure(fg_color="#CFB2B7")
    contact_lab.configure(fg_color="#CFB2B7")
    bar.configure(width=70)
    bar.place(x=983,y=60)

def rent():
    rent_lab.configure(fg_color="#DEF4DD")
    home_lab.configure(fg_color="#CFB2B7")
    buy_lab.configure(fg_color="#CFB2B7")
    about_lab.configure(fg_color="#CFB2B7")
    contact_lab.configure(fg_color="#CFB2B7")

    bar.configure(width=60)
    bar.place(x=1083,y=60)

def buy():
    buy_lab.configure(fg_color="#DEF4DD")
    home_lab.configure(fg_color="#CFB2B7")
    rent_lab.configure(fg_color="#CFB2B7")
    about_lab.configure(fg_color="#CFB2B7")
    contact_lab.configure(fg_color="#CFB2B7")

    bar.configure(width=50)
    bar.place(x=1174,y=60)

def about():
    about_lab.configure(fg_color="#DEF4DD")
    home_lab.configure(fg_color="#CFB2B7")
    rent_lab.configure(fg_color="#CFB2B7")
    buy_lab.configure(fg_color="#CFB2B7")
    contact_lab.configure(fg_color="#CFB2B7")

    bar.configure(width=100)
    bar.place(x=1255,y=60)

def contact():
    contact_lab.configure(fg_color="#DEF4DD")
    home_lab.configure(fg_color="#CFB2B7")
    rent_lab.configure(fg_color="#CFB2B7")
    about_lab.configure(fg_color="#CFB2B7")
    buy_lab.configure(fg_color="#CFB2B7")

    bar.configure(width=115)
    bar.place(x=1385,y=60)



#Image
img = Image.open('homepage_img.jpg')

upload_img = CTkImage(light_image=img,size=(2099,508))

img_label = CTkLabel(root,text='',image=upload_img)
img_label.pack()

#Labels , Buttons 
header = CTkLabel(root,text="Ai Broker",text_color="black",fg_color='#F7E0D0',font=('Actor',30,'underline'))
header.place(x=32,y=20)

home_lab = CTkButton(root,text="Home",text_color="black",bg_color="#CFB2B7",fg_color='#DEF4DD',hover_color="#DEF4DD",font=('Actor',20),corner_radius=10,width=10,command=home)
home_lab.place(x=980,y=30)

rent_lab = CTkButton(root,text="Rent",text_color="black",bg_color="#CFB2B7",fg_color='#CFB2B7',hover_color="#DEF4DD",font=('Actor',20),corner_radius=10,width=10,command=rent)
rent_lab.place(x=1080,y=30)

buy_lab = CTkButton(root,text="Buy",text_color="black",bg_color="#CFB2B7",fg_color='#CFB2B7',hover_color="#DEF4DD",font=('Actor',20),corner_radius=10,width=10,command=buy)
buy_lab.place(x=1170,y=30)

about_lab = CTkButton(root,text="About Us",text_color="black",bg_color="#CFB2B7",fg_color='#CFB2B7',hover_color="#DEF4DD",font=('Actor',20),corner_radius=10,width=10,command=about)
about_lab.place(x=1250,y=30)

contact_lab = CTkButton(root,text="Contact Us",text_color="black",bg_color="#CFB2B7",fg_color='#CFB2B7',hover_color="#DEF4DD",font=('Actor',20),corner_radius=10,width=10,command=contact)
contact_lab.place(x=1380,y=30)

bar = CTkFrame(root,height=8,width=70,corner_radius=10,fg_color='Black')
bar.place(x=983,y=60)


root.mainloop()