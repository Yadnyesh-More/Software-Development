from customtkinter import *

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

    page2_lab.destroy()
    page3_lab.destroy()
    page4_lab.destroy()
    page5_lab.destroy()
    page1_lab = CTkLabel(frame2,text='HOME PAGE !!',fg_color='black',font=("Arieal",50))
    page1_lab.place(x=50,y=200)

def about():
    global page2_lab
    galary_but.configure(fg_color="white")
    menu_but.configure(fg_color="white")
    contact_but.configure(fg_color="white")
    home_but.configure(fg_color="white")
    about_but.configure(fg_color="#FFF9D0")
    bar.place(x=8,y=115)

    page1_lab.destroy()
    page3_lab.destroy()
    page4_lab.destroy()
    page5_lab.destroy()
    page2_lab = CTkLabel(frame2,text='About PAGE !!',fg_color='black',font=("Arieal",50))
    page2_lab.place(x=50,y=200)

def menu():
    global page3_lab
    home_but.configure(fg_color="white")
    menu_but.configure(fg_color="white")
    contact_but.configure(fg_color="white")
    about_but.configure(fg_color="white")
    menu_but.configure(fg_color="#FFF9D0")
    bar.place(x=8,y=185)

    page2_lab.destroy()
    page1_lab.destroy()
    page4_lab.destroy()
    page5_lab.destroy()
    page3_lab = CTkLabel(frame2,text='Menu PAGE !!',fg_color='black',font=("Arieal",50))
    page3_lab.place(x=50,y=200)


def galary():
    global page4_lab
    about_but.configure(fg_color="white")
    home_but.configure(fg_color="white")
    contact_but.configure(fg_color="white")
    menu_but.configure(fg_color="white")
    galary_but.configure(fg_color="#FFF9D0")
    bar.place(x=8,y=255)

    page2_lab.destroy()
    page3_lab.destroy()
    page1_lab.destroy()
    page5_lab.destroy()
    page4_lab = CTkLabel(frame2,text='Galary PAGE !!',fg_color='black',font=("Arieal",50))
    page4_lab.place(x=50,y=200)

def contact():
    global page5_lab
    about_but.configure(fg_color="white")
    menu_but.configure(fg_color="white")
    home_but.configure(fg_color="white")
    galary_but.configure(fg_color="white")
    contact_but.configure(fg_color="#FFF9D0")
    bar.place(x=8,y=325)

    page2_lab.destroy()
    page3_lab.destroy()
    page4_lab.destroy()
    page1_lab.destroy()
    page5_lab = CTkLabel(frame2,text='Contact PAGE !!',fg_color='black',font=("Arieal",50))
    page5_lab.place(x=50,y=200)


frame1 = CTkFrame(root,width=160,bg_color='blue',height=600,fg_color='white')
frame1.pack(fill=Y,anchor='w')

frame2 = CTkFrame(root,width=1500,fg_color="#FFF9D0",height=600)
frame2.place(x=180,y=0)

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

page1_lab = CTkLabel(frame2,text='PAGE 1 !!',fg_color='black',font=("Arieal",50))
page1_lab.place(x=100,y=200)


root.mainloop()