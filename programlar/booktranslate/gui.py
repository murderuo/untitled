import  tkinter as tk
from tkinter import *

class BookTranslator:
    def __init__(self):
        self.createWigdets()

    def createWigdets(self):
        self.areaFrame=Frame()
        self.areaFrame.grid(column=0,row=0)

        self.textArea=Text(self.areaFrame, width=40,height=15)
        self.textArea.grid(column=0,row=0)

        self.buttonFrame=Frame(bd=1,width=100,height=250,relief=SUNKEN)
        self.buttonFrame.grid(column=1,row=0)

        self.kaydetButon=Button(self.buttonFrame,width=20,height=2,text="Kaydet")
        self.kaydetButon.grid(column=1,row=0,ipady=10)

        self.yeniSayfa=Button(self.buttonFrame,width=20,height=2,text="Yeni Sayfa")
        self.yeniSayfa.grid(column=1,row=1,ipady=10)
        self.durdurButon=Button(self.buttonFrame,width=20,height=2,text="Durdur")
        self.durdurButon.grid(column=1,row=2,ipady=10)
        self.devamButon=Button(self.buttonFrame,width=20,height=2,text="Devam")
        self.devamButon.grid(column=1,row=3,ipady=10)

        self.bottomButtonFrame=Frame()
        self.bottomButtonFrame.grid(row=1)

        self.temizleButon=Button(self.bottomButtonFrame,width=20,height=2,text="Devam")
        self.temizleButon.grid(column=0,row=1)

        self.gerialButton=Button(self.bottomButtonFrame,width=20,height=2,text="Geri al")
        self.gerialButton.grid(column=1,row=1)





app=Tk()
bt=BookTranslator()
mainloop()

