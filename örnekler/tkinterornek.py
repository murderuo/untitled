from tkinter import *
from tkinter.font import Font
import sqlite3 as sql
import re

db = sql.connect("jdata.db")
lesson = ""

def control_uye():
    global db
    cr = db.cursor()
    query = "SELECT * FROM öğrenciler WHERE isim = '{}' AND soyisim = '{}' AND numara = '{}'".format(str(name.get()), str(surname.get()), str(num.get()))
    cr.execute(query)
    data = cr.fetchall()
    db.commit()
    if(len(data) == 0):
        message = "Öğrenci Bulunamadı"
        msg["text"] = message
        return False
    else:
        return True

def control(lessonname, data, info):
    if(info):
        message = "Ders Adı: " + lessonname + "\n" + "Toplam Devamsızlık: " + data
        if(int(data) > 5):
            message += "\nDersten kaldınız..."
    else:
        message = "Ders Adı: " + lessonname + "\n" + "Toplam Devam: " + data
    msg["text"] = message

def set_lesson(lesson_c):
    global lesson
    lesson = lesson_c
    lab_s["text"] = "Seçilen Ders: " + lesson

def devamsizlik(info):
    global db
    global lesson
    cr = db.cursor()
#    number = num.get()
    if(num.get() != "" and name.get() != "" and surname.get() != ""):
        if(lesson == ""):
            message = "Lütfen Ders Belirleyiniz"
            msg["text"] = message
        elif(control_uye()):
            if(info):
                if(lesson == "Fizik"):
                    lessonname = "ders1"
                elif(lesson == "Programlama"):
                    lessonname = "ders2"
                elif(lesson == "Öğretim Tasarımı"):
                    lessonname = "ders3"
                elif(lesson == "Ölçme Değerlendirme"):
                    lessonname = "ders4"
                elif(lesson == "Grafik Canlandırma"):
                    lessonname = "ders5"
                query = "SELECT {} FROM öğrenciler WHERE isim = '{}' AND soyisim = '{}' AND numara = '{}'".format(lessonname, str(name.get()), str(surname.get()), str(num.get()))
                cr.execute(query)
                data = cr.fetchall()
                data = str(data)
                data = re.sub('[^0-9]','',data)
                data = int(data)
                data += 1
                data = str(data)
                query = "UPDATE öğrenciler SET {} = '{}' WHERE isim = '{}' AND soyisim = '{}' AND numara = '{}'".format(lessonname, data, str(name.get()), str(surname.get()), str(num.get()))
                cr.execute(query)
                control(lesson,data,info)
            else:
                if(lesson == "Fizik"):
                    lessonname = "ders_d1"
                elif(lesson == "Programlama"):
                    lessonname = "ders_d2"
                elif(lesson == "Öğretim Tasarımı"):
                    lessonname = "ders_d3"
                elif(lesson == "Ölçme Değerlendirme"):
                    lessonname = "ders_d4"
                elif(lesson == "Grafik Canlandırma"):
                    lessonname = "ders_d5"

                query = "SELECT {} FROM öğrenciler WHERE isim = '{}' AND soyisim = '{}' AND numara = '{}'".format(lessonname, str(name.get()), str(surname.get()), str(num.get()))
                cr.execute(query)
                data = cr.fetchall()
                data = str(data)
                data = re.sub('[^0-9]','',data)
                data = int(data)
                data += 1
                data = str(data)
                query = "UPDATE öğrenciler SET {} = '{}' WHERE isim = '{}' AND soyisim = '{}' AND numara = '{}'".format(lessonname, data, str(name.get()), str(surname.get()), str(num.get()))
                cr.execute(query)
                control(lesson,data,info)
            db.commit()

def add():
	global db
	cr = db.cursor()
	query = "SELECT * FROM öğrenciler WHERE isim = '{}' AND soyisim = '{}' AND numara = '{}'".format(str(name.get()), str(surname.get()), str(num.get()))
	num_query = "SELECT * FROM öğrenciler WHERE numara = '{}'".format(str(num.get()))
	cr.execute(query)
	data = cr.fetchall()
	cr.execute(num_query)
	num_control = cr.fetchall()
	db.commit()
	if(len(data) == 0):
		if(len(num_control) == 0):
			query = "INSERT INTO öğrenciler VALUES ('{}', '{}', '{}', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0')".format(str(name.get()), str(surname.get()), str(num.get()))
			cr.execute(query)
			message = "Öğrenci Eklendi"
			msg["text"] = message
		else:
			message = "Numara Mevcut"
			msg["text"] = message
	else:
		message = "Öğrenci Mevcut"
		msg["text"] = message

def delete():
	global db
	cr = db.cursor()
	query = "SELECT * FROM öğrenciler WHERE isim = '{}' AND soyisim = '{}' AND numara = '{}'".format(str(name.get()), str(surname.get()), str(num.get()))
	cr.execute(query)
	data = cr.fetchall()
	db.commit()
	if(len(data) != 0):
		query = "DELETE FROM öğrenciler WHERE isim = '{}' AND soyisim = '{}' AND numara = '{}'".format(str(name.get()), str(surname.get()), str(num.get()))
		cr.execute(query)
		message = "Öğrenci Silindi"
		msg["text"] = message
	else:
		message = "Silinecek Olan Öğrenci Mevcut Değil"
		msg["text"] = message


window = Tk()
appfont = Font(family='Helvetica', size=11, weight='bold')

window.title("Öğrenci Devamsızlık Kayıt Sistemi")
window.geometry("380x500")
window.resizable(False, False)
window.configure(bg="dark slate gray")

butt = Button(window, text="Fizik", width=20, command = lambda: set_lesson("Fizik"), font=appfont, fg="black", bg="dark slate gray")
butt.grid(row=0, columnspan=3, sticky=W+E+N+S)

butt = Button(window, text="Programlama", width=20, command = lambda: set_lesson("Programlama"), font=appfont, fg="black", bg="dark slate gray")
butt.grid(row=1, columnspan=3, sticky=W+E+N+S)

butt = Button(window, text="Öğretim Tasarımı", width=20, command = lambda: set_lesson("Öğretim Tasarımı"), font=appfont, fg="black", bg="dark slate gray")
butt.grid(row=2, columnspan=3, sticky=W+E+N+S)

butt = Button(window, text="Ölçme Değerlendirme", width=20, command = lambda: set_lesson("Ölçme Değerlendirme"), font=appfont, fg="black", bg="dark slate gray")
butt.grid(row=3, columnspan=3, sticky=W+E+N+S)

butt = Button(window, text="Grafik Canlandırma", width=20, command = lambda: set_lesson("Grafik Canlandırma"), font=appfont, fg="black", bg="dark slate gray")
butt.grid(row=4, columnspan=3, sticky=W+E+N+S)

lab_s = Label(window, text="Ders Seçilmedi",width=50, font=appfont, fg="black", bg="slate gray")
lab_s.grid(row=5, columnspan=5, sticky=W+E+N+S)

lab = Label(window, text="AD", width=25, font=appfont, fg="black", bg="dim gray")
lab.grid(row=7, column=1, sticky=W+E+N+S)
name = Entry(window, width=25, font=appfont, fg="black", bg="dark sea green")
name.grid(row=7, column=2, sticky=W+E+N+S)

lab = Label(window, text="SOYAD",width=25, font=appfont, fg="black", bg="dim gray")
lab.grid(row=8, column=1, sticky=W+E+N+S)
surname = Entry(window, width=25, font=appfont, fg="black", bg="dark sea green")
surname.grid(row=8, column=2, sticky=W+E+N+S)

lab = Label(window, text="NUMARA",width=25, font=appfont, fg="black", bg="dim gray")
lab.grid(row=9, column=1, sticky=W+E+N+S)
num = Entry(window, width=25, font=appfont, fg="black", bg="dark sea green")
num.grid(row=9, column=2, sticky=W+E+N+S)

butt = Button(window, text="GELMEDİ", width=20, command = lambda: devamsizlik(True), font=appfont, fg="black", bg="gray")
butt.grid(row=10, column=2, sticky=W+E+N+S)

butt = Button(window, text="GELDİ", width=20, command = lambda: devamsizlik(False), font=appfont, fg="black", bg="gray")
butt.grid(row=10, column=1, sticky=W+E+N+S)

butt = Button(window, text="EKLE", width=40, command = add, font=appfont, fg="black", bg="gray")
butt.grid(row=11, columnspan=5, sticky=W+E+N+S)

butt = Button(window, text="SİL", width=40, command = delete, font=appfont, fg="black", bg="gray")
butt.grid(row=12, columnspan=4, sticky=W+E+N+S)

msg = Label(window, text="",width=50, font=appfont, fg="black", bg="dark slate gray")
msg.grid(row=13, columnspan=5, sticky=W+E+N+S)

window.mainloop()