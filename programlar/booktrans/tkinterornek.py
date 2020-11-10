import  tkinter as tk
from tkinter import *

win=tk.Tk()
win.title("python sample")
win.geometry("500x300")

def click_me():
    pass
textareaFrame=LabelFrame(win)
textareaFrame.grid(column=0,row=0)

textarea=Text(textareaFrame,width=40,height=15)
textarea.grid(column=0,row=0)

butonFrame=LabelFrame(win,bd=0)
butonFrame.grid(column=1,row=0)

kaydetButon=Button(butonFrame,width=20,height=2,text="Kaydet")
kaydetButon.grid(column=1,row=0,ipady=10)

yeniSayfa=Button(butonFrame,width=20,height=2,text="Yeni Sayfa")
yeniSayfa.grid(column=1,row=1,ipady=10)

durdurButon=Button(butonFrame,width=20,height=2,text="Durdur")
durdurButon.grid(column=1,row=2,ipady=10)

devamButon=Button(butonFrame,width=20,height=2,text="Devam")
devamButon.grid(column=1,row=3,ipady=10)

temizleButon=Button(win,width=20,height=2,text="Devam")
temizleButon.grid(row=1,ipadx=10)







# ttk.Label(win,text="Deneme Label").grid(column=0,row=0)

# label1=Label(win,text="Ad")
# label1.grid(column=0,row=0)
# isim=Entry(win,width=20)
# isim.grid(column=1,row=0)
#
# # isim.grid(column=1,row=0)
#
# label2=Label(win,text="Soyad")
# label2.grid(column=0,row=1)

# buton.configure(text="clicked................")
# label1.configure(foreground="blue",text=isim.get())
# print(isim.get())



# buton=Button(win,text="click",command=click_me)
# buton.grid(column=2,row=0)











win.mainloop()