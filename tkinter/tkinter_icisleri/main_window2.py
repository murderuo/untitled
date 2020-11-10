from PIL import Image,ImageTk
# from tkinter import Tk,Label,StringVar,GROOVE,CENTER
import tkinter as tk
import re
from login_script import IcısleriLogın
from tkinter import messagebox

import time

class Evrak(tk.Tk):

    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        # self.ibot=IcısleriLogın()
        # Label.__init__(self,*args,**kwargs)
        # StringVar.__init__(self,*args,**kwargs)
        # GROOVE.__init__(self,*args,**kwargs)
        # CENTER.__init__(self,*args,**kwargs)
        # self.root=Tk()
        # self.root.geometry('450x150')
        # self.root.title('EVRAK KONTROL')
        # self.root.resizable(False,False)
        self.evraks=tuple()
        self.int_var_gelenevrak=0
        self.int_var_taslak=0
        self.int_var_postalanEvrak=0
        self.variables=[tk.StringVar() for i in range(6)]
        self.gelenEvrakLabel=tk.Label(self,textvariable=self.variables[0],bd=2,width=20,height=2,relief=tk.GROOVE,wraplength=150,justify=tk.CENTER)
        self.birimdeKayBekleyen=tk.Label(self,textvariable=self.variables[1],bd=2,width=20,height=2,relief=tk.GROOVE,wraplength=150,justify=tk.CENTER)
        self.disKurGelen=tk.Label(self,textvariable=self.variables[2],bd=2,width=20,height=2,relief=tk.GROOVE,wraplength=150,justify=tk.CENTER)
        self.birimdeKaydedilmis=tk.Label(self,textvariable=self.variables[3],bd=2,width=20,height=2,relief=tk.GROOVE,wraplength=150,justify=tk.CENTER)
        self.postalanEvrak=tk.Label(self,textvariable=self.variables[4],bd=2,width=20,height=2,relief=tk.GROOVE,wraplength=150,justify=tk.CENTER)
        self.taslak=tk.Label(self,textvariable=self.variables[5],bd=2,width=20,height=2,relief=tk.GROOVE,wraplength=150,justify=tk.CENTER)

        self.gelenEvrakLabel.grid(row=0,column=0)
        self.taslak.grid(row=1,column=0)
        self.birimdeKayBekleyen.grid(row=0,column=2)
        self.birimdeKaydedilmis.grid(row=1,column=2)
        self.disKurGelen.grid(row=0,column=1)
        self.postalanEvrak.grid(row=2,column=1)




    def updateValue(self):
        gelenevrak,taslak,birimdeKayBekleyen,disKurGelen,birimdeKaydedilmis,postalanEvrak=self.evraks
        self.variables[0].set(gelenevrak)
        self.variables[1].set(birimdeKayBekleyen)
        self.variables[2].set(disKurGelen)
        self.variables[3].set(birimdeKaydedilmis)
        self.variables[4].set(postalanEvrak)
        self.variables[5].set(taslak)

    def setCurrentValues(self):
        gelenevrak,taslak,birimdeKayBekleyen,disKurGelen,birimdeKaydedilmis,postalanEvrak=self.evraks
        self.int_var_gelenevrak=int(re.findall("[0-9]+",gelenevrak)[0])
        self.int_var_taslak=int(re.findall("[0-9]+",taslak)[0])
        self.int_var_postalanEvrak=int(re.findall("[0-9]+",postalanEvrak)[0])

    # def evrakCounts(self):
    #     return self.evraks

    def evrakKontrol(self):
        gelenevrak,taslak,birimdeKayBekleyen,disKurGelen,birimdeKaydedilmis,postalanEvrak=self.evraks

        #current values
        int_gelenevrak=int(re.findall("[0-9]+",gelenevrak)[0])
        int_taslak=int(re.findall("[0-9]+",taslak)[0])
        int_postalanEvrak=int(re.findall("[0-9]+",postalanEvrak)[0])

        #check
        # print("gelen_varolan{},taslakvarolan{},postavarolan{}".format(self.int_var_gelenevrak,self.int_var_taslak,self.int_var_postalanEvrak))
        # print(f"gelen       {int_gelenevrak},taslak{int_taslak},posta{int_postalanEvrak}")
        #
        if  (int_gelenevrak > self.int_var_gelenevrak ): # int_birimdeKayBekleyen > int_var_birimdeKayBekleyen or int_disKurGelen > int_var_disKurGelen or int_birimdeKaydedilmis > int_var_birimdeKaydedilmis or
            self.int_var_gelenevrak=int_gelenevrak
            return True
        elif (int_taslak > self.int_var_taslak) :# int_birimdeKayBekleyen < int_var_birimdeKayBekleyen or int_disKurGelen < int_var_disKurGelen or int_birimdeKaydedilmis < int_var_birimdeKaydedilmis or
            self.int_var_taslak=int_taslak
            return True
        elif int_postalanEvrak>self.int_var_postalanEvrak:
            self.int_var_postalanEvrak=int_postalanEvrak
            return True
        else: return False


    def showAlert(self):
        messagebox.showinfo("bilgi","######### EVRAK GELDİ ##########")



# evrak=Evrak()
# evrak.mainloop()



if __name__ == "__main__":
    check=IcısleriLogın()
    sertifikasiz_giris='//*[@id="form1"]/div[3]/div/div[1]/a'
    check.wait(2)
    check.openSite('https://www.e-icisleri.gov.tr/IBYetki/Login.aspx')
    check.wait(1)
    check.findXpathObjectClick(sertifikasiz_giris)
    k_adi='//*[@id="TextBoxKullaniciAd"]'
    k_sifre='//*[@id="TextBoxParola"]'
    check.sendKeys(k_adi,'ugur.okur@icisleri.gov.tr')
    check.wait(1)
    check.sendKeys(k_sifre,'ob478$93m')
    check.getCaptcha()
    check.wait(1)
    check.cropCaptcha(".\\tmp\captcha.png")
    check.wait(1)
    check.showCaptcha()
    ###inputing##
    check.inputCaptcha()
    check.findXpathObjectClick('//*[@id="ButtonGerekce"]')
    check.wait(1)
    check.findXpathObjectClick('//*[@id="PanelGerekce"]/table[1]/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/span/label')
    check.wait(1)
    check.findXpathObjectClick('//*[@id="ctl08_ButonGerekceliSifreliGiris"]')
    check.wait(1)
    check.browserEnterKey()
    check.wait(1)
    check.birimKontrol()
    check.wait(1)
    check.clickEvrakPage()

    evrak_window=Evrak()
    evrak_count=check.getHMTLSourceCode()

    evrak_window.evraks=evrak_count ## getting evrak count evrak_count[0]=gelenevrak, [1]=taslak
    evrak_window.updateValue()
    evrak_window.setCurrentValues()
    # ####evrak cheking####
    def countRefresh():
        check.clickEvrakPage()
        # global int_gelen_ev_sayisi,int_varolan
        # # print(f"gelen:{int_gelen_ev_sayisi}, varolan:{int_varolan}")
        #
        # if int_gelen_ev_sayisi > int_varolan:
        #     int_varolan=int_gelen_ev_sayisi
        #     evrak_window.showAlert()  # print(f"yeni evrak geldi,gelen evrak sayısı {int_gelen_ev_sayisi},varolan {int_varolan}")
        # elif int_gelen_ev_sayisi < int_varolan:
        #     int_varolan=int_gelen_ev_sayisi
        #     # print("yeni evrak yok")
        evrak_count=check.getHMTLSourceCode()
        evrak_window.evraks=evrak_count
        evrak_window.updateValue()
        # evrak_window.evrakKontrol()
        kontrol=evrak_window.evrakKontrol() #checking
        # print(kontrol)
        if kontrol:
            # print("evrak geldi")
            evrak_window.showAlert()

        evrak_window.after(120000,countRefresh)

    evrak_window.geometry('450x110')
    evrak_window.title('EVRAK KONTROL')
    evrak_window.resizable(False,False)

    evrak_window.after(1000,countRefresh)
    evrak_window.mainloop()
