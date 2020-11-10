'''Tk_Canvas_Image_url.py
display an image obtained from an internet web page in Tkinter
tested with Python27 and Python33  by  vagaseat   21nov2012
'''
import io
import base64
try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen

from PIL import Image, ImageTk

root = tk.Tk()
root.title("display a website image")
# # a little more than width and height of image
# w = 520
# h = 320
# x = 80
# y = 100
# # use width x height + x_offset + y_offset (no spaces!)
# root.geometry("%dx%d+%d+%d" % (w, h, x, y))
# this GIF picture previously downloaded to tinypic.com
pic_url = "https://www.e-icisleri.gov.tr/GeneleAcikSayfalar/Captcha/CaptchaImage.aspx?f967af2e-4b0e-4dc2-9196-30f273f2f1ed.jfif"

# open the web page picture and read it into a memory stream
# and convert to an image Tkinter can handle
my_page = urlopen(pic_url)
# create an image file object
my_picture = io.BytesIO(my_page.read())
# use PIL to open image formats like .jpg  .png  .gif  etc.
pil_img = Image.open(my_picture)
# convert to an image Tkinter can use
tk_img = ImageTk.PhotoImage(pil_img)
# put the image on a typical widget
label = tk.Label(root, image=tk_img)
label.pack(padx=5, pady=5)
root.mainloop()