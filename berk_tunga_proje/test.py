from tkinter import *
import requests
from bs4 import BeautifulSoup

root = Tk()
root.geometry("600x300")

######### REQUESTS ##########
r = requests.get("https://www.doviz.com")
soup = BeautifulSoup(r.content, "html.parser")
currencies = soup.find_all("div", attrs={"class":"item"})

#### ISBANKASI ####
r_ısbankası = requests.get("https://www.isbank.com.tr/doviz-kurlari")
soup = BeautifulSoup(r_ısbankası.content, "html.parser")

##### DOLAR ######
dolar_alıs_ısbankası = soup.find("table", attrs={"class":"dk_MT"}).select("tr:nth-of-type(2) > td:nth-of-type(2)")[0].text
dolar_alıs_ısbankası = dolar_alıs_ısbankası.replace(",", ".")
dolar_alıs_ısbankası = float(dolar_alıs_ısbankası.strip())

dolar_satıs_isbankası = soup.find("table", attrs={"class":"dk_MT"}).select("tr:nth-of-type(2) > td:nth-of-type(3)")[0].text
dolar_satıs_isbankası = dolar_satıs_isbankası.replace(",", ".")
dolar_satıs_isbankası = float(dolar_satıs_isbankası.strip())

##print("dolar alıs ıs bankası - ", dolar_alıs_ısbankası)
#print("dolar satıs ıs bankası - ", dolar_satıs_isbankası)

##### EURO ######
euro_alıs_isbankası = soup.find("table", attrs={"class":"dk_MT"}).select("tr:nth-of-type(3) > td:nth-of-type(2)")[0].text
euro_alıs_isbankası = euro_alıs_isbankası.replace(",", ".")
euro_alıs_isbankası = float(euro_alıs_isbankası.strip())

euro_satıs_isbankası = soup.find("table", attrs={"class":"dk_MT"}).select("tr:nth-of-type(3) > td:nth-of-type(3)")[0].text
euro_satıs_isbankası = euro_satıs_isbankası.replace(",", ".")
euro_satıs_isbankası = float(euro_satıs_isbankası.strip())

#print("eu alıs ıs bankası - ", euro_alıs_isbankası)
#print("eu satıs ıs bankası - ", euro_satıs_isbankası)

####### YAPIKREDI
r_yapıkredi = requests.get("https://www.yapikredi.com.tr/yatirimci-kosesi/doviz-bilgileri")
soup = BeautifulSoup(r_yapıkredi.content, "html.parser")

##### DOLAR ######
dolar_alıs_yapıkredi = soup.find("table", attrs={"class":"table table-striped table-text-right table-bordered"}).select("tr:nth-of-type(1) > td:nth-of-type(3)")[0].text
dolar_alıs_yapıkredi = dolar_alıs_yapıkredi.replace(",", ".")
dolar_alıs_yapıkredi = float(dolar_alıs_yapıkredi.strip())

dolar_satıs_yapıkredi = soup.find("table", attrs={"class":"table table-striped table-text-right table-bordered"}).select("tr:nth-of-type(1) > td:nth-of-type(4)")[0].text
dolar_satıs_yapıkredi = dolar_satıs_yapıkredi.replace(",", ".")
dolar_satıs_yapıkredi = float(dolar_satıs_yapıkredi.strip())

#print("dolar alıs - ", dolar_alıs_yapıkredi)
#print("dolar satıs - ", dolar_satıs_yapıkredi)

############### EURO ####
euro_alıs_yapıkredi = soup.find("table", attrs={"class":"table table-striped table-text-right table-bordered"}).select("tr:nth-of-type(2) > td:nth-of-type(3)")[0].text
euro_alıs_yapıkredi = euro_alıs_yapıkredi.replace(",", ".")
euro_alıs_yapıkredi = float(euro_alıs_yapıkredi.strip())

euro_satıs_yapıkredi = soup.find("table", attrs={"class":"table table-striped table-text-right table-bordered"}).select("tr:nth-of-type(2) > td:nth-of-type(4)")[0].text
euro_satıs_yapıkredi = euro_satıs_yapıkredi.replace(",", ".")
euro_satıs_yapıkredi = float(euro_satıs_yapıkredi.strip())

#print("euro_alıs - ", euro_alıs_yapıkredi)
#print("euro_satıs - ", euro_satıs_yapıkredi)

##### ALTIN
altın_alıs_yapıkredi = soup.find("table", attrs={"class":"table table-striped table-text-right table-bordered"}).select("tr:nth-of-type(3) > td:nth-of-type(3)")[0].text
altın_alıs_yapıkredi = altın_alıs_yapıkredi.replace(",", ".")
altın_alıs_yapıkredi = float(altın_alıs_yapıkredi.strip())

altın_satıs_yapıkredi = soup.find("table", attrs={"class":"table table-striped table-text-right table-bordered"}).select("tr:nth-of-type(3) > td:nth-of-type(4)")[0].text
altın_satıs_yapıkredi = altın_satıs_yapıkredi.replace(",", ".")
altın_satıs_yapıkredi = float(altın_satıs_yapıkredi.strip())

#print("altın_alıs - ", altın_alıs_yapıkredi)
#print("altın_satıs - ", altın_satıs_yapıkredi)


###### KUVEYT
r_kuveyt = requests.get("https://www.kuveytturk.com.tr/finans-portali/")
soup = BeautifulSoup(r_kuveyt.content, "html.parser")

Kuveyt = soup.find_all("div", attrs={"class":"alphabox"})

i = 0
dolar_alıs_kuveyt = 0
euro_alıs_kuveyt = 0
altın_alıs_kuveyt = 0
dolar_satıs_kuveyt = 0
euro_satıs_kuveyt = 0
altın_satıs_kuveyt = 0

for temp in Kuveyt:
    if i < 3:
        #### ALIS
        kuveyt_alıs = temp.select("div:nth-of-type(1) > p")[0].text
        kuveyt_alıs = kuveyt_alıs.replace(",", ".")
        kuveyt_alıs = kuveyt_alıs.replace(" ", "")
        alıs_temp_kuveyt = str(kuveyt_alıs[0:8])
        kuveyt_alıs = float(alıs_temp_kuveyt.strip())
        #### SATIS
        kuveyt_satıs = temp.select("div:nth-of-type(2) > p")[0].text
        kuveyt_satıs = kuveyt_satıs.replace(",", ".")
        kuveyt_satıs = kuveyt_satıs.replace(" ", "")
        satıs_temp_kuveyt = str(kuveyt_satıs[0:8])
        kuveyt_satıs = float(satıs_temp_kuveyt.strip())

        if i == 0:
            dolar_alıs_kuveyt = kuveyt_alıs
            dolar_satıs_kuveyt = kuveyt_satıs
        if i == 1:
            euro_alıs_kuveyt = kuveyt_alıs
            euro_satıs_kuveyt = kuveyt_satıs
        if i == 2:
            altın_alıs_kuveyt = kuveyt_alıs
            altın_satıs_kuveyt = kuveyt_satıs
        i = i + 1

######## HALKBANK
r_halkbank = requests.get("https://www.halkyatirim.com.tr/doviz-kurlari")
soup = BeautifulSoup(r_halkbank.content, "html.parser")

##### DOLAR ######
dolar_alıs_halkbank = soup.find("div", attrs={"class":"table-responsive"})\
    .select("table:nth-of-type(2) > tbody > tr:nth-of-type(1) > td:nth-of-type(3)")[0].text
dolar_alıs_halkbank = dolar_alıs_halkbank.replace(",", ".")
dolar_alıs_halkbank = float(dolar_alıs_halkbank.strip())

dolar_satıs_halkbank = soup.find("div", attrs={"class":"table-responsive"})\
    .select("table:nth-of-type(2) > tbody > tr:nth-of-type(1) > td:nth-of-type(4)")[0].text
dolar_satıs_halkbank = dolar_satıs_halkbank.replace(",", ".")
dolar_satıs_halkbank = float(dolar_satıs_halkbank.strip())


#print(dolar_alıs_halkbank, dolar_satıs_halkbank)

##### EURO ######
euro_alıs_halkbank = soup.find("div", attrs={"class":"table-responsive"})\
    .select("table:nth-of-type(2) > tbody > tr:nth-of-type(2) > td:nth-of-type(3)")[0].text
euro_alıs_halkbank = euro_alıs_halkbank.replace(",", ".")
euro_alıs_halkbank = float(euro_alıs_halkbank.strip())

euro_satıs_halkbank = soup.find("div", attrs={"class":"table-responsive"})\
    .select("table:nth-of-type(2) > tbody > tr:nth-of-type(2) > td:nth-of-type(4)")[0].text
euro_satıs_halkbank = euro_satıs_halkbank.replace(",", ".")
euro_satıs_halkbank = float(euro_satıs_halkbank.strip())


#print(euro_alıs_halkbank, euro_satıs_halkbank)

###### BANKA -SON- #####

###### GUI
Label1 = Label(root, text="").grid(row=0, column=0)
Label2 = Label(root, text="").grid(row=0, column=1, sticky='nswe')   ################################################

frame = LabelFrame(root, text="Bankalar", padx=5, pady=5)
frame.grid(row=0, column=0, padx=10, pady=5)

var0 = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
label_0 = StringVar()
label_1 = StringVar()
label_2 = StringVar()
label_3 = StringVar()
label_4 = StringVar()
label_5 = StringVar()
label_6 = StringVar()
label_7 = StringVar()
label_8 = StringVar()
label_9 = StringVar()
label_10 = StringVar()
label_11 = StringVar()
def update_label0():
    if var0.get() == 1:
        temp_isbankası_dolar_a = str(dolar_alıs_ısbankası)
        temp_isbankası_dolar_s = str(dolar_satıs_isbankası)
        temp_isbankası_euro_a = str(euro_alıs_isbankası)
        temp_isbankası_euro_s = str(euro_satıs_isbankası)
        label_0.set(temp_isbankası_dolar_a +"/"+ temp_isbankası_dolar_s)
        label_1.set(temp_isbankası_euro_a+ "/"+temp_isbankası_euro_s )
        label_2.set("-- / --")
        #print("***")
    else:
        label_0.set("")
        label_1.set("")
        label_2.set("")
def update_label1():
    if var1.get() == 1:
        temp_yk_dolar_a = str(dolar_alıs_yapıkredi)
        temp_yk_dolar_s = str(dolar_satıs_yapıkredi)
        temp_yk_euro_a = str(euro_alıs_yapıkredi)
        temp_yk_euro_s = str(euro_satıs_yapıkredi)
        temp_yk_altın_a = str(altın_alıs_kuveyt)
        temp_yk_altın_s = str(altın_satıs_kuveyt)
        label_3.set(temp_yk_dolar_a + "/" + temp_yk_dolar_s)
        label_4.set(temp_yk_euro_a + "/" + temp_yk_euro_s)
        label_5.set(temp_yk_altın_a+"/"+temp_yk_altın_s)
    else:
        label_3.set("")
        label_4.set("")
        label_5.set("")

def update_label2():
    if var2.get() == 1:
        temp_kuveyt_dolar_a = str(dolar_alıs_kuveyt)
        temp_kuveyt_dolar_s = str(dolar_satıs_kuveyt)
        temp_kuveyt_euro_a = str(euro_alıs_kuveyt)
        temp_kuveyt_euro_s = str(euro_satıs_kuveyt)
        temp_v_altın_a = str(altın_alıs_kuveyt)
        temp_v_altın_s = str(altın_satıs_kuveyt)
        label_6.set(temp_kuveyt_dolar_a + "/" + temp_kuveyt_dolar_s)
        label_7.set(temp_kuveyt_euro_a + "/" + temp_kuveyt_euro_s)
        label_8.set(temp_v_altın_a + "/" + temp_v_altın_s)
    else:
        label_6.set("")
        label_7.set("")
        label_8.set("")
def update_label3():
    if var3.get() == 1:
        temp_hb_dolar_a = str(dolar_alıs_halkbank)
        temp_hb_dolar_s = str(dolar_satıs_halkbank)
        temp_hb_euro_a = str(euro_alıs_halkbank)
        temp_hb_euro_s = str(euro_satıs_halkbank)
        label_9.set(temp_hb_dolar_a + "/" + temp_hb_dolar_s)
        label_10.set(temp_hb_euro_a + "/" + temp_hb_euro_s)
        label_11.set( "--/--")
    else:
        label_9.set("")
        label_10.set("")
        label_11.set("")

c1 = Checkbutton(frame, text="İş Bankası",variable=var0, onvalue=1, offvalue=0, command=update_label0)
c2 = Checkbutton(frame, text="YapıKredi",variable=var1, onvalue=1, offvalue=0, command=update_label1)
c3 = Checkbutton(frame, text="Kuveyt Türk",variable=var2, onvalue=1, offvalue=0, command=update_label2)
c4 = Checkbutton(frame, text="HalkBank",variable=var3, onvalue=1, offvalue=0, command=update_label3)
c1.grid(row=0, column=0, sticky=W)
c2.grid(row=1, column=0, sticky=W)
c3.grid(row=2, column=0, sticky=W)
c4.grid(row=3, column=0, sticky=W)
frameData = LabelFrame(root, text="    USD                EURO             DOLAR    ", padx=5, pady=5, width=400)
frameData.grid(row=0, column=1, padx=10, pady=5, sticky='nswe')

Labelaaaa= Label(frameData, text="Alış / Satış").grid(row=0, column=0, sticky=W)
Labelbbbb = Label(frameData, text="     Alış / Satış").grid(row=0, column=1)
Labelcccc = Label(frameData, text="     Alış / Satış").grid(row=0, column=2, sticky=E)

##### BANKA LABELLAR

###### İS BANKASI
LabelUSD_isbankası = Label(frameData, textvariable=label_0)
LabelEUR_isbankası = Label(frameData, textvariable=label_1)
LabelXAU_isbankası = Label(frameData, textvariable=label_2)
LabelUSD_isbankası.grid(row=1, column=0)
LabelEUR_isbankası.grid(row=1, column=1)
LabelXAU_isbankası.grid(row=1, column=2)

######### YK
LabelUSD_yk = Label(frameData, textvariable=label_3)
LabelEUR_yk = Label(frameData, textvariable=label_4)
LabelXAU_yk = Label(frameData, textvariable=label_5)
LabelUSD_yk.grid(row=2, column=0)
LabelEUR_yk.grid(row=2, column=1)
LabelXAU_yk.grid(row=2, column=2)

######## KUVEYT
LabelUSD_kuveyt = Label(frameData, textvariable=label_6)
LabelEUR_kuveyt = Label(frameData, textvariable=label_7)
LabelXAU_kuveyt = Label(frameData, textvariable=label_8)
LabelUSD_kuveyt.grid(row=3, column=0)
LabelEUR_kuveyt.grid(row=3, column=1)
LabelXAU_kuveyt.grid(row=3, column=2)

######### HALKBANK
LabelUSD_halkbank= Label(frameData, textvariable=label_9)
LabelEUR_halkbank = Label(frameData, textvariable=label_10)
LabelXAU_halkbank = Label(frameData, textvariable=label_11)
LabelUSD_halkbank.grid(row=4, column=0)
LabelEUR_halkbank.grid(row=4, column=1)
LabelXAU_halkbank.grid(row=4, column=2)

###############################

frameData = LabelFrame(root, text="Değerler", padx=5, pady=5, width=100)
frameData.grid(row=0, column=2, padx=10, pady=5, sticky=W)

altın = StringVar()
dollar = StringVar()
euro = StringVar()
for currency in currencies:
    if currency.find("span", attrs={"class":"name"}).text == "GRAM ALTIN":
        altın = currency.find("span", attrs={"class": "value"}).text
        #print(currency.find("span", attrs={"class": "name"}).text + " <-> " + currency.find("span", attrs={"class": "value"}).text)
    elif currency.find("span", attrs={"class":"name"}).text == "DOLAR":
        dollar = currency.find("span", attrs={"class": "value"}).text
        #print(currency.find("span", attrs={"class": "name"}).text +" <-> " + currency.find("span", attrs={"class": "value"}).text)
    elif currency.find("span", attrs={"class":"name"}).text == "EURO":
        euro = currency.find("span", attrs={"class": "value"}).text
        a = currency.find("span", attrs={"class": "name"}).text
        b = currency.find("span", attrs={"class": "value"}).text
        b = b.replace(",", ".")
        float(b)
        #print( a + " <-> " + b)

USD_Data = Label(frameData, text="USD").grid(row=1, column=0, sticky=S)
EURO_Data = Label(frameData, text="EURO").grid(row=2, column=0, sticky=S)
ALTIN_Data = Label(frameData, text="ALTIN").grid(row=3, column=0, sticky=S)

USD_Data_0 = Label(frameData, text=dollar)
EURO_Data_0 = Label(frameData, text=euro)
ALTIN_Data_0 = Label(frameData, text=altın)
USD_Data_0.grid(row=1, column=1, sticky=W)
EURO_Data_0.grid(row=2, column=1, sticky=W)
ALTIN_Data_0.grid(row=3, column=1, sticky=W)

######################
result_altın = float()
result_dolar = float()
result_euro = float()
def convert_from_TL():

    amount = amount_TL.get()

    for currency in currencies:
        if currency.find("span", attrs={"class": "name"}).text == "GRAM ALTIN":
            altın = currency.find("span", attrs={"class": "value"}).text
            altın = altın.replace(",", ".")
            altın = float(altın)
            result_altın = amount / altın
            b = round(result_altın, 2)
            place_holder(ALTIN_Entry, b)

        elif currency.find("span", attrs={"class": "name"}).text == "DOLAR":
            dollar = currency.find("span", attrs={"class": "value"}).text
            dollar = dollar.replace(",", ".")
            dollar = float(dollar)
            result_dolar = amount / dollar
            b = round(result_dolar, 2)
            place_holder(USD_Entry, b)

        elif currency.find("span", attrs={"class": "name"}).text == "EURO":
            euro = currency.find("span", attrs={"class": "value"}).text
            euro = euro.replace(",", ".")
            euro = float(euro)
            result_euro = amount / euro
            b = round(result_euro, 2)
            place_holder(EURO_Entry, b)

def place_holder(Entry,amount):
    Entry.insert(0, amount)

frameConverter = LabelFrame(root, text="Çevirici", padx=5, pady=5, width=400)
frameConverter.grid(row=1, column=0, padx=10, pady=5, sticky='nswe')

TL = Label(frameConverter, text="TL").grid(row=0, column=0, sticky=W)
USD = Label(frameConverter, text="USD").grid(row=1, column=0, sticky=W)
EURO = Label(frameConverter, text="EURO").grid(row=2, column=0, sticky=W)
ALTIN = Label(frameConverter, text="ALTIN").grid(row=3, column=0, sticky=W)

amount_TL = IntVar()
amount_USD = IntVar()
amount_EUR = IntVar()
amount_XAU = IntVar()
#amount_TL.trace("w", lambda name, index, mode, amount_TL=amount_TL: convert_from_TL(amount_TL))     ##### çevirici

TL_Entry = Entry(frameConverter, textvariable=amount_TL)
USD_Entry = Entry(frameConverter, textvariable=amount_USD)
EURO_Entry = Entry(frameConverter, textvariable=amount_EUR)
ALTIN_Entry = Entry(frameConverter, textvariable=amount_XAU)
TL_Entry.grid(row=0, column=1, sticky=W)
USD_Entry.grid(row=1, column=1, sticky=W)
EURO_Entry.grid(row=2, column=1, sticky=W)
ALTIN_Entry.grid(row=3, column=1, sticky=W)



####  FONKSIYON

def clear():
    TL_Entry.delete(0, END)
    USD_Entry.delete(0, END)
    EURO_Entry.delete(0, END)
    ALTIN_Entry.delete(0, END)

button1 = Button(frameConverter, text="Clear", bg="red", fg="black",command=clear)
button1.grid(row=4, column=0)
button2 = Button(frameConverter, text="Convert", bg="green", fg="black",command=convert_from_TL)
button2.grid(row=4, column=1)

root.mainloop()
