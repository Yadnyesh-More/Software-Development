from customtkinter import *
from PIL import Image

root = CTk()
root.title("Menubar")
root.geometry("600x600")
root.resizable(False,False)

def home():
    about_but.configure(fg_color="white")
    menu_but.configure(fg_color="white")
    contact_but.configure(fg_color="white")
    galary_but.configure(fg_color="white")
    home_but.configure(fg_color="#FFF9D0")
    bar.place(x=8,y=45)
    root.after(5,home)

    # page2_lab.destroy()
    # page3_lab.destroy()
    # page4_lab.destroy()
    # page5_lab.destroy()
    # page1_lab = CTkLabel(frame2,text='HOME PAGE !!',fg_color='black',font=("Arieal",50))
    # page1_lab.place(x=50,y=200)

def about():
    # global page2_lab
    galary_but.configure(fg_color="white")
    menu_but.configure(fg_color="white")
    contact_but.configure(fg_color="white")
    home_but.configure(fg_color="white")
    about_but.configure(fg_color="#FFF9D0")
    bar.place(x=8,y=115)

    # page1_lab.destroy()
    # page3_lab.destroy()
    # page4_lab.destroy()
    # page5_lab.destroy()
#   page2_lab = CTkLabel(frame2,text='About PAGE !!',fg_color='black',font=("Arieal",50))
#   page2_lab.place(x=50,y=200) """

def menu():
    # global page3_lab
    home_but.configure(fg_color="white")
    menu_but.configure(fg_color="white")
    contact_but.configure(fg_color="white")
    about_but.configure(fg_color="white")
    menu_but.configure(fg_color="#FFF9D0")
    bar.place(x=8,y=185)

    # page2_lab.destroy()
    # page1_lab.destroy()
    # page4_lab.destroy()
    # page5_lab.destroy()
    # page3_lab = CTkLabel(frame2,text='Menu PAGE !!',fg_color='black',font=("Arieal",50))
    # page3_lab.place(x=50,y=200)


def galary():
    # global page4_lab
    about_but.configure(fg_color="white")
    home_but.configure(fg_color="white")
    contact_but.configure(fg_color="white")
    menu_but.configure(fg_color="white")
    galary_but.configure(fg_color="#FFF9D0")
    bar.place(x=8,y=255)


    # page2_lab.destroy()
    # page3_lab.destroy()
    # page1_lab.destroy()
    # page5_lab.destroy()
    # page4_lab = CTkLabel(frame2,text='Galary PAGE !!',fg_color='black',font=("Arieal",50))
    # page4_lab.place(x=50,y=200)

def contact():
    # global page5_lab
    about_but.configure(fg_color="white")
    menu_but.configure(fg_color="white")
    home_but.configure(fg_color="white")
    galary_but.configure(fg_color="white")
    contact_but.configure(fg_color="#FFF9D0")
    bar.place(x=8,y=325)
    

    # page2_lab.destroy()
    # page3_lab.destroy()
    # page4_lab.destroy()
    # page1_lab.destroy()
    # page5_lab = CTkLabel(frame2,text='Contact PAGE !!',fg_color='black',font=("Arieal",50))
    # page5_lab.place(x=50,y=200)
def compress():
    home_but.destroy()
    about_but.destroy()
    menu_but.destroy()
    galary_but.destroy()
    contact_but.destroy()
    bar.destroy()
    frame1.configure(width=50)
    print("Compress")

    global home_img_lab,about_img_lab,menu_img_lab,galary_img_lab,contact_img_lab
    
    home_img = CTkImage(light_image=Image.open("home.png"),size=(28,28))
    home_img_lab = CTkButton(root,text="",image=home_img,fg_color="white",bg_color="white",width=0,hover_color="white",command=expand)
    home_img_lab.place(x=5,y=60)

    about_img = CTkImage(light_image=Image.open("about.png"),size=(28,28))
    about_img_lab = CTkButton(root,text="",image=about_img,fg_color="white",bg_color="white",width=0,hover_color="white",command=expand)
    about_img_lab.place(x=5,y=120)

    menu_img = CTkImage(light_image=Image.open("idea.png"),size=(28,28))
    menu_img_lab = CTkButton(root,text="",image=menu_img,fg_color="white",bg_color="white",width=0,hover_color="white")
    menu_img_lab.place(x=5,y=180)

    galary_img = CTkImage(light_image=Image.open("image-gallery.png"),size=(28,28))
    galary_img_lab = CTkButton(root,text="",image=galary_img,fg_color="white",bg_color="white",width=0,hover_color="white")
    galary_img_lab.place(x=5,y=240)

    contact_img = CTkImage(light_image=Image.open("customer-service.png"),size=(28,28))
    contact_img_lab = CTkButton(root,text="",image=contact_img,fg_color="white",bg_color="white",width=0,hover_color="white")
    contact_img_lab.place(x=5,y=300)
    menubar_img_lab.configure(command=expand)

def expand():
    # frame1 = CTkFrame(root,width=160,bg_color='blue',height=600,fg_color='white')
    # frame1.pack(fill=Y,anchor='w')
    global home_but,about_but,menu_but,galary_but,contact_but,bar

    home_img_lab.destroy()
    about_img_lab.destroy()
    menu_img_lab.destroy()
    galary_img_lab.destroy()
    contact_img_lab.destroy()

    frame1.configure(width=160)
    
    home_but = CTkButton(frame1,text="HOME",fg_color='#FFF9D0',text_color='black',hover_color='#FFF9D0',font=("Arieal",20),command=home)
    home_but.place(x=10,y=50)

    about_but = CTkButton(frame1,text="ABOUT",fg_color='white',text_color='black',hover_color='#FFF9D0',font=("Arieal",20),command=about)
    about_but.place(x=10,y=120)

    menu_but = CTkButton(frame1,text="MENU",fg_color='white',text_color='black',hover_color='#FFF9D0',font=("Arieal",20),command=menu)
    menu_but.place(x=10,y=190)

    galary_but = CTkButton(frame1,text="GALARY",fg_color='white',text_color='black',hover_color='#FFF9D0',font=("Arieal",20),command=galary)
    galary_but.place(x=10,y=260)

    contact_but = CTkButton(frame1,text="CONTACT",fg_color='white',text_color='black',hover_color='#FFF9D0',font=("Arieal",20),command=contact)
    contact_but.place(x=10,y=330)

    bar = CTkFrame(frame1,height=40,width=5,fg_color='black')
    bar.place(x=8,y=45)

    menubar_img_lab.configure(command=compress)


frame1 = CTkFrame(root,width=50,bg_color='blue',height=600,fg_color='white')
frame1.pack(fill=Y,anchor='w')

frame2 = CTkFrame(root,width=1500,fg_color="#FFF9D0",height=600)
frame2.place(x=180,y=0)

# home_but = CTkButton(frame1,text="HOME",fg_color='#FFF9D0',text_color='black',hover_color='#FFF9D0',font=("Arieal",20),command=home)
# home_but.place(x=10,y=50)

# about_but = CTkButton(frame1,text="ABOUT",fg_color='white',text_color='black',hover_color='#FFF9D0',font=("Arieal",20),command=about)
# about_but.place(x=10,y=120)

# menu_but = CTkButton(frame1,text="MENU",fg_color='white',text_color='black',hover_color='#FFF9D0',font=("Arieal",20),command=menu)
# menu_but.place(x=10,y=190)

# galary_but = CTkButton(frame1,text="GALARY",fg_color='white',text_color='black',hover_color='#FFF9D0',font=("Arieal",20),command=galary)
# galary_but.place(x=10,y=260)

# contact_but = CTkButton(frame1,text="CONTACT",fg_color='white',text_color='black',hover_color='#FFF9D0',font=("Arieal",20),command=contact)
# contact_but.place(x=10,y=330)

# bar = CTkFrame(frame1,height=40,width=5,fg_color='black')
# bar.place(x=8,y=45)

menubar_img = CTkImage(light_image=Image.open("menu-bar.png"),size=(28,28))
menubar_img_lab = CTkButton(root,text="",image=menubar_img,fg_color="white",bg_color="white",width=0,hover_color="white",command=expand)
menubar_img_lab.place(x=5,y=10)

home_img = CTkImage(light_image=Image.open("home.png"),size=(28,28))
home_img_lab = CTkButton(root,text="",image=home_img,fg_color="white",bg_color="white",width=0,hover_color="white",command=expand)
home_img_lab.place(x=5,y=60)

about_img = CTkImage(light_image=Image.open("about.png"),size=(28,28))
about_img_lab = CTkButton(root,text="",image=about_img,fg_color="white",bg_color="white",width=0,hover_color="white",command=expand)
about_img_lab.place(x=5,y=120)

menu_img = CTkImage(light_image=Image.open("idea.png"),size=(28,28))
menu_img_lab = CTkButton(root,text="",image=menu_img,fg_color="white",bg_color="white",width=0,hover_color="white")
menu_img_lab.place(x=5,y=180)

galary_img = CTkImage(light_image=Image.open("image-gallery.png"),size=(28,28))
galary_img_lab = CTkButton(root,text="",image=galary_img,fg_color="white",bg_color="white",width=0,hover_color="white")
galary_img_lab.place(x=5,y=240)

contact_img = CTkImage(light_image=Image.open("customer-service.png"),size=(28,28))
contact_img_lab = CTkButton(root,text="",image=contact_img,fg_color="white",bg_color="white",width=0,hover_color="white")
contact_img_lab.place(x=5,y=300)



# page1_lab = CTkLabel(frame2,text='PAGE 1 !!',fg_color='black',font=("Arieal",50))
# page1_lab.place(x=100,y=200)


root.mainloop()