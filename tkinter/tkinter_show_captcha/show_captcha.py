'''Tk_Canvas_Image_url.py
display an image obtained from an internet web page in Tkinter
tested with Python27 and Python33  by  vagaseat   21nov2012
'''

from tkinter import *
from PIL import Image, ImageTk

root = Tk()


canv = Canvas(root,width=250,height=60, bg='white')
canv.grid(row=2, column=3)

img = ImageTk.PhotoImage(Image.open(".\#Captcha.jpg"))  # PIL solution
canv.create_image(0, 0, anchor=NW, image=img)

mainloop()