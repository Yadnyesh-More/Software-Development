from customtkinter import *
from Class1 import Hello

class MainApp:
    def __init__(self):
        self.toor = CTk()
        self.toor.geometry("666x444")
        cla = Hello()
        CTkButton(self.toor, text="New file", corner_radius=4, command=lambda: cla.config(self.toor)).pack(padx=10, pady=20)
        self.toor.mainloop()

if __name__ == "__main__":
    app = MainApp()
