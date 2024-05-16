import ttkbootstrap as tb
from tkinter import *
import tkinter.messagebox as tmsg

root = tb.Window(themename="darkly")
root.geometry("666x444")
root.resizable(False,False)
root.title("Switching tabs")

def Switch(indicator_lb):
    indicator_lb["bg"] = "#0097e8"
    

f1 = tb.Frame(root,bootstyle = "primary")
f1.pack(pady = 5)

f1.pack_propagate(False)
f1.configure(width = 666,height=40)

home_button = Button(f1,text="Home",font=("robot",13),bd=0,fg="#0097e8",activebackground="#0097e8")
home_button.place(x = 0,y=0,width=125)
home_lb = Label(f1,bg="#0097e8")
home_lb.place(x = 15,y=33,width=88,height=3)

menu_button = Button(f1,text="Menu",font=("robot",13),bd=0,fg="#0097e8",activebackground="#0097e8")
menu_button.place(x = 120,y=0,width=125)
# menu_lb = Label(f1,bg="#0097e8")
# menu_lb.place(x = 140,y=33,width=88,height=3)

contact_button = Button(f1,text="Contact",font=("robot",13),bd=0,fg="#0097e8",activebackground="#0097e8")
contact_button.place(x = 250,y=0,width=125)
# contact_lb = Label(f1,bg="#0097e8")
# contact_lb.place(x = 270,y=33,width=88,height=3)

about_button = Button(f1,text="About",font=("robot",13),bd=0,fg="#0097e8",activebackground="#0097e8")
about_button.place(x = 380,y=0,width=125)
# about_lb = Label(f1,bg="#0097e8")
# about_lb.place(x = 400,y=33,width=88,height=3)

feedback_button = Button(f1,text="Feedback",font=("robot",13),bd=0,fg="#0097e8",activebackground="#0097e8")
feedback_button.place(x = 520,y=0,width=125)
# feedback_lb = Label(f1,bg="#0097e8")
# feedback_lb.place(x = 530,y=33,width=100,height=3)

f1 = tb.Frame(root,bootstyle = "white")
f1.pack(fill=BOTH,expand=True)

# f1.pack_propagate(False)
# f1.configure(width = 666,height=40)



root.mainloop()