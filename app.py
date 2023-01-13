# Weather app
from tkinter import *
import tkinter as tk 
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime 
# import request
import pytz


# Title & size of the app
root=Tk()
root.title("Weather forecase")
root.geometry("900x500+300+200")
root.resizable(False,False)


# Search box
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=600,y=20)


# Text
textfield = tk.Entry(root,justify="center", width=16, font=("poppins", 12, "bold"), bg="whitesmoke", border=0, fg="black")
textfield.place(x=611, y=110)
textfield.focus()


# Icon
Search_icon = PhotoImage(file= "icon.png")
myimage_icon = Button(image = Search_icon, borderwidth=0, width=19, height=17 ,cursor="hand2", bg="black")
myimage_icon.place(x=773, y=112)


# Logo
Logo_image = PhptoImage(file = "")
logo = Label(image = Logo_image)
logo.place(x=150, y=100)








root.mainloop()
