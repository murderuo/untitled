from tkinter import *


pencere=Tk()


def changeLabel():
    label1=Label(pencere,text="Tıklama fonksiyonu çalıştı");
    label1.pack()




buton=Button(pencere,text="tıkla",command=changeLabel)

buton.pack()


pencere.mainloop()

# class Uygulama():
#     def __init__(self):
#         self.guiPenAr()
#     def guiPenAr(self):
#         self.etiket = Label(text="A¸sa˘gıdaki kutucu˘ga e.posta adresinizi yazınız!")
#         self.etiket.pack()
#         self.giris = Entry()
#         self.giris.pack()
#         self.cerceve = Frame()
#         self.cerceve.pack(side=BOTTOM,
#                             padx=5,
#                             pady=5)
#         self.dugme = Button(self.cerceve,
#                             text="Gönder",
#                             width=5,
#                             )
#         self.dugme.pack(side=LEFT,padx=5)
#         self.dugme2 = Button(self.cerceve,
#         text="˙Iptal",
#         width=5)
#         self.dugme2.pack()
# uyg = Uygulama()



