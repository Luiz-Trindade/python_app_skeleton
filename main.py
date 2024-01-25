# Simple Python App "Skeleton"
# Created By: Luiz Gabriel Magalhães Trindade
# This Program Is Distributed Under The MIT License
# The MIT License: https://mit-license.org/

#Default App libs
from customtkinter import *
from tkinter import PhotoImage

#Default App Settings
icon_file = "windows.png"
app_title = "Application Title"
app_geometry = "500x200"
set_appearance_mode("dark")
set_default_color_theme("green")
set_widget_scaling(1.5)

class Program(CTk):

    #Constructor Method
    def __init__(self):
        super().__init__()
        self.title(app_title)
        self.geometry(app_geometry)
        
        #Setting the App Icon
        app_icon = PhotoImage(file=icon_file)
        self.iconphoto(False, app_icon)

        #Widgets
        self.data_entry = CTkEntry(master=self, placeholder_text="name", justify="center")
        self.data_entry.pack(pady=10, padx=10)

        self.buttun = CTkButton(master=self, text="click!", command=self.Send)
        self.buttun.pack(pady=10, padx=10)

    #Methods
    def Send(self):
        name = self.data_entry.get()
        print(f"Wellcome, {name}!")

app = Program()
app.mainloop()
