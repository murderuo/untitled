from tkinter import *
# from booktranslate import
from file_save_class import FileSaves
import pyperclip
import time
# import main

from programlar.booktranslate import main

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

    def getTrans(self,word):
        # word=pyperclip.paste
        trans=main.translateGoogleCloud(word)
        self.textArea.insert(INSERT,trans)

    def saveTextArea(self):
        mean=self.textArea.get()
        FileSaves.saveWord(mean)


app=Tk()
bt=BookTranslator()

# print("sasdasda")

# #
recent_value = ""

while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        time.sleep(1)
        bt.getTrans(tmp_value.strip())
        # mean=bt.getTrans(tmp_value.strip())
        # bt.saveTextArea(tmp_value)
    time.sleep(0.5)




# bt.getTrans()
mainloop()

