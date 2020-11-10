
import tkinter as tk
import re
from login_script import IcısleriLogın
from tkinter import messagebox
from evrak_postala import Postala
from excel_creator import  ExportExcel


######WHATSAPP NOTIFICATIONS###########
# from twilio.rest import Client
#
# account_sid='AC1c0c34cd89fdc8270d11abe0ce50fca0'
# auth_token='36f68f9858ded01efc6946105f4b0d7f'
# client=Client(account_sid,auth_token)
#
# evrak_bildirim="EVRAK GELDI DIKKAT :::::"
# posta_bildirim="POSTALANACAK EVRAK VAR DIKKAT ::::::"
# ###########################################
#
# def sendNotif(bildirim):
#     message=client.messages.create(from_='whatsapp:+14155238886', body=bildirim, to='whatsapp:+905375447979')


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
        self.postalanacakEvrakBilgileri=[]
        self.int_var_gelenevrak=0
        # self.int_var_taslak=0
        self.int_var_postalanEvrak=0
        self.variables=[tk.StringVar() for i in range(6)]
        self.gelenEvrakLabel=tk.Label(self,textvariable=self.variables[0],bd=2,width=20,height=2,relief=tk.GROOVE,wraplength=150,justify=tk.CENTER)
        self.birimdeKayBekleyen=tk.Label(self,textvariable=self.variables[1],bd=2,width=20,height=2,relief=tk.GROOVE,wraplength=150,justify=tk.CENTER)
        self.disKurGelen=tk.Label(self,textvariable=self.variables[2],bd=2,width=20,height=2,relief=tk.GROOVE,wraplength=150,justify=tk.CENTER)
        self.birimdeKaydedilmis=tk.Label(self,textvariable=self.variables[3],bd=2,width=20,height=2,relief=tk.GROOVE,wraplength=150,justify=tk.CENTER)
        self.postalanEvrak=tk.Label(self,textvariable=self.variables[4],bd=2,width=20,height=2,relief=tk.GROOVE,wraplength=150,justify=tk.CENTER)
        self.taslak=tk.Label(self,textvariable=self.variables[5],bd=2,width=20,height=2,relief=tk.GROOVE,wraplength=150,justify=tk.CENTER)
        #postalabuton
        self.postalaButon=tk.Button(self,text="Rapor Oluştur",state=tk.ACTIVE,command=self.Postala)
        #############
        self.gelenEvrakLabel.grid(row=0,column=0)
        self.taslak.grid(row=1,column=0)
        self.birimdeKayBekleyen.grid(row=0,column=2)
        self.birimdeKaydedilmis.grid(row=1,column=2)
        self.disKurGelen.grid(row=0,column=1)
        self.postalanEvrak.grid(row=2,column=1)
        self.postalaButon.grid(row=2,column=2)

    def Postala(self):
        evraklar=self.postalanacakEvrakBilgileri
        rapor=ExportExcel()
        rapor.raporBaslikYaz()
        r=3
      # c evrak sayısı kadar döngü r ise başlangıç satırı
        for c in range(len(evraklar)):
            if "," in evraklar[c]['Gideceği Yer']:
                yeni_gid_yer=evraklar[c]['Gideceği Yer'].replace(",","\n--------------------------\n")
                # rapor.satirYuksekligi(r,150)
                rapor.yazdir(r,0,str(c+1),rapor.metniKaydirOrtala())
                rapor.yazdir(r,1,yeni_gid_yer,rapor.metniKaydirOrtala())
                if "İçişleri Bakanlığına" in evraklar[c]['Gideceği Yer']:
                    rapor.yazdir(r,6,"ELEKTRONİK OLARAK POSTALANACAKTIR\n--------------------\n      ...       ",
                                 rapor.metniKaydirOrtala())
            else:
                rapor.yazdir(r,0,str(c+1),rapor.metniKaydirOrtala())
                rapor.yazdir(r,1,evraklar[c]['Gideceği Yer'],rapor.metniKaydirOrtala())
                rapor.yazdir(r,6,"",rapor.dortKoseBorder())
            rapor.yazdir(r,2,evraklar[c]['Tarih'],rapor.metniKaydirOrtala())
            rapor.yazdir(r,3,evraklar[c]['Evrak No'],rapor.metniKaydirOrtala())
            rapor.yazdir(r,4,evraklar[c]['Konu'],rapor.metniKaydirOrtala())
            rapor.yazdir(r,5,"",rapor.dortKoseBorder())
            r+=1
        rapor.yazdirilacakAlanBelirle(len(evraklar))
        rapor.teslimHazirla(len(evraklar))
        rapor.closeFile()
        self.postalaButon.config(state=tk.DISABLED)
        self.postalanacakEvrakBilgileri=[]
        self.raporOlustuAlert()

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

    def evrakKontrol(self):
        gelenevrak,taslak,birimdeKayBekleyen,disKurGelen,birimdeKaydedilmis,postalanEvrak=self.evraks
        #current values
        int_gelenevrak=int(re.findall("[0-9]+",gelenevrak)[0])
        int_taslak=int(re.findall("[0-9]+",taslak)[0])
        int_postalanEvrak=int(re.findall("[0-9]+",postalanEvrak)[0])
        if  (int_gelenevrak > self.int_var_gelenevrak ):
            self.int_var_gelenevrak=int_gelenevrak
            return 2
        elif (int_taslak > self.int_var_taslak) :
            self.int_var_taslak=int_taslak
            return 3
        elif int_postalanEvrak>self.int_var_postalanEvrak:
            self.int_var_postalanEvrak=int_postalanEvrak
            self.postalaButon.config(state=tk.ACTIVE)
            return 4
        else: return False

    def showGelenEvrakAlert(self):
        messagebox.showinfo("bilgi","######### EVRAK GELDİ ##########")

    def showPostalaEvrakAlert(self):
        messagebox.showinfo("bilgi","######### POSTALANACAK EVRAK VAR ##########")

    def raporOlustuAlert(self):
        messagebox.showinfo("bilgi","######### POSTA RAPORU OLUŞTU ##########")

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
    check.sendKeys(k_sifre,'de273-mtv')
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
    ######posta bilgisi fonksiyon####
    def postaBilgisi():
        check.gitPostalanacakPage()
        check.wait(3)
        kaynak_kodu=check.getPageSourceCode()
        pst=Postala()
        if pst.getEvrakBilgileri(kaynak_kodu)!=False:
            evrak_window.postalanacakEvrakBilgileri=pst.getEvrakBilgileri(kaynak_kodu)
            # evrak_window.int_var_postalanEvrak=0
            # print(evrak_window.postalanacakEvrakBilgileri)
            # print("Posta bilgileri alındı.")
        check.wait(2)
        check.gitEvrakPage()


    ######evrak cheking####
    def countRefresh():
        check.clickEvrakPage()
        evrak_count=check.getHMTLSourceCode()
        evrak_window.evraks=evrak_count
        evrak_window.updateValue()
        kontrol=evrak_window.evrakKontrol() #checking
        if kontrol==2:
            evrak_window.showGelenEvrakAlert()
            # sendNotif(evrak_bildirim)

        elif kontrol==4:
            evrak_window.showPostalaEvrakAlert()
            # sendNotif(posta_bildirim)
        # elif kontrol==3:       #TASLAK KONTROL
        #     evrak_window.showGelenEvrakAlert()
        #     sendNotif(evrak_bildirim)
        if len(evrak_window.postalanacakEvrakBilgileri) != 0:
            # print("postalanacak evrak var")
            postaBilgisi()

        # print("Postalacak evrak yok")
        # ######################### POSTALA KISMI ###########
        # check.openSite('https://www.e-icisleri.gov.tr/Evrak/Posta/PostalanmayiBekleyen.aspx')
        # check.wait(2)
        # kaynak_kodu=check.getPageSourceCode()
        # pst=Postala()
        # pst.getSourceCode(kaynak_kodu)
        # check.clickEvrakPage()
        # check.wait(2)
        ########################
        evrak_window.after(120000,countRefresh)

    ######evrakpostadetayal###
    postaBilgisi()
    evrak_window.geometry('450x110')
    evrak_window.title('EVRAK KONTROL')
    evrak_window.resizable(False,False)






    evrak_window.after(1000,countRefresh)
    evrak_window.mainloop()
