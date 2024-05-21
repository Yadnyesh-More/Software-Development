from customtkinter import *

class Hello:
    def config(self, main_window):
        main_window.destroy()  # Destroy the main window
        self.root = CTk()
        self.root.geometry("666x444")
        CTkLabel(self.root, text="Hello, I am a different file but in the same folder").pack()
        self.root.mainloop()
