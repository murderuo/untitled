from tkinter import *


class Uyari:
    def __init__(self):
        self.root=Tk()
        self.root.geometry('450x110')
        self.root.title('EVRAK KONTROL')
        self.uyariLabel=Label(self.root,text="EVRAK GELDİ",width=45,font=("Helvetica", 45))
        self.uyariLabel.pack()
        self.tamamButon=Button(self.root,text="Tamam",command=self.tamam)
        self.tamamButon.pack()
        self.root.mainloop()

    def tamam(self):
        self.root.destroy()


# pencere=Uyari()