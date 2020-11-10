from PIL import Image,ImageTk
# from tkinter import Tk,Label,StringVar,GROOVE,CENTER
import tkinter as tk
from tkinter import messagebox

from random import randint
import re

from login_script import IcısleriLogın
# from    evrak_uyari_pencere import Uyari
import time

class Evrak(tk.Tk):

    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.evraks=tuple()
        self.variables=[tk.StringVar() for i in range(6)]
        self.gelenEvrakLabel=tk.Label(self,textvariable=self.variables[0],bd=2,width=20,height=2,relief=tk.GROOVE,wraplength=150,justify=tk.CENTER)
        self.birimdeKayBekleyen=tk.Label(self,textvariable=self.variables[1],bd=2,width=20,height=2,relief=tk.GROOVE,wraplength=150,justify=tk.CENTER)
        self.disKurGelen=tk.Label(self,textvariable=self.variables[2],bd=2,width=20,height=2,relief=tk.GROOVE,wraplength=150,justify=tk.CENTER)
        self.birimdeKaydedilmis=tk.Label(self,textvariable=self.variables[3],bd=2,width=20,height=2,relief=tk.GROOVE,wraplength=150,justify=tk.CENTER)
        self.postalanEvrak=tk.Label(self,textvariable=self.variables[4],bd=2,width=20,height=2,relief=tk.GROOVE,wraplength=150,justify=tk.CENTER)
        self.taslak=tk.Label(self,textvariable=self.variables[5],bd=2,width=20,height=2,relief=tk.GROOVE,wraplength=150,justify=tk.CENTER)
        self.gelenEvrakLabel.grid(row=0,column=0)
        self.birimdeKayBekleyen.grid(row=1,column=0)
        self.disKurGelen.grid(row=0,column=2)
        self.birimdeKaydedilmis.grid(row=1,column=2)
        self.postalanEvrak.grid(row=2,column=1)
        self.taslak.grid(row=0,column=1)


    def updateValue(self):
        gelenevrak,birimdeKayBekleyen,disKurGelen,birimdeKaydedilmis,postalanEvrak,taslak=self.evraks
        self.variables[0].set(gelenevrak)
        self.variables[1].set(birimdeKayBekleyen)
        self.variables[2].set(disKurGelen)
        self.variables[3].set(birimdeKaydedilmis)
        self.variables[4].set(postalanEvrak)
        self.variables[5].set(taslak)

    def showAlert(self):
        messagebox.showinfo("bilgi","######### EVRAK GELDİ ##########")


if __name__ == "__main__":

    check=(str(randint(1,300)),str(randint(1,300)),str(randint(1,300)),str(randint(1,300)),str(randint(1,300)),
           str(randint(1,300)))

    evrak_window=Evrak()
    evrak_window.evraks=check ## getting evrak count

    check=("gelen evrak("+str(randint(1,12))+")",str(randint(1,300)),str(randint(1,300)),str(randint(1,300)),str(randint(1,300)),
           str(randint(1,300)))
    gelen_ev=check[0]
    gelen_ev_sayisi=re.findall("[0-9]+",gelen_ev)

    varolan=gelen_ev_sayisi[0]
    int_varolan=int(varolan)
    int_gelen_ev_sayisi=int(gelen_ev_sayisi[0])

    def countRefresh():
        global int_gelen_ev_sayisi,int_varolan
        print(f"gelen:{int_gelen_ev_sayisi}, varolan:{int_varolan}")

        if int_gelen_ev_sayisi > int_varolan:
            int_varolan=int_gelen_ev_sayisi
            evrak_window.showAlert()
            # print(f"yeni evrak geldi,gelen evrak sayısı {int_gelen_ev_sayisi},varolan {int_varolan}")
        elif int_gelen_ev_sayisi < int_varolan:
            int_varolan=int_gelen_ev_sayisi
            print("yeni evrak yok")

        check=("gelen evrak("+str(randint(1,12))+")","taslak evrak("+str(randint(1,20))+")",str(randint(1,300)),
               str(randint(1,300)),str(randint(1,300)),str(randint(1,300)))
        gelen_ev=check[0]
        gelen_ev_sayisi=re.findall("[0-9]+",gelen_ev)
        int_gelen_ev_sayisi=int(gelen_ev_sayisi[0])


        evrak_window.evraks=check  ## getting evrak count
        evrak_window.updateValue()
        evrak_window.after(5000,countRefresh)

    evrak_window.geometry('450x110')
    evrak_window.title('EVRAK KONTROL TEST')
    evrak_window.resizable(False,False)
    # countRefresh()
    evrak_window.after(0,countRefresh)
    evrak_window.mainloop()
