# import xlsxwriter module
import xlsxwriter as xl
import time
import locale
import random
locale.setlocale(locale.LC_ALL, 'turkish')
tarih=time.strftime('%x')

class ExportExcel(xl.Workbook):
    def __init__(self):
        xl.Workbook.__init__(self)
        self.filenameNumber=random.randint(0,999)
        self.filename='rapor'+str(self.filenameNumber)+'.xlsx'
        # self.wbook=xl.Workbook()
        # self.wbook.add_worksheet('say1')
        # self.wbook.close()
        self.createFile()
        self.ekleCalismaSayfasi()

    def createFile(self):
        self.wbook=xl.Workbook(self.filename)
        # self.wbook.add_worksheet('Say1')
        # for i in range(6):
        #     self.wsheet.write(0,i,'test',self.baslikFormat())
        # self.wbook.close()
        # self.ekleCalismaSayfasi()
        # self.closeFile()

    def closeFile(self):
        self.wbook.close()

    def ekleCalismaSayfasi(self,cs_adi='Sayfa1'):
        self.wsheet=self.wbook.add_worksheet(cs_adi)
        # return self.worksheet

    def baslikFormat(self):
        self.baslik_formati=self.wbook.add_format()
        self.baslik_formati.set_bold()
        self.baslik_formati.set_border(1)
        self.baslik_formati.set_align('center')
        self.baslik_formati.set_align('vcenter')
        self.baslik_formati.set_font('Arial')
        self.baslik_formati.set_font_size(12)
        return self.baslik_formati

    def metniKaydirOrtala(self):
        self.metni_kaydir=self.wbook.add_format()
        self.metni_kaydir.set_text_wrap()
        self.metni_kaydir.set_align('center')
        self.metni_kaydir.set_align('vcenter')
        self.metni_kaydir.set_font('Arial')
        self.metni_kaydir.set_font_size(11)
        self.metni_kaydir.set_border(1)
        return self.metni_kaydir


    def metniKaydirSolaYasla(self):
        self.metni_kaydir_solayasla=self.wbook.add_format()
        self.metni_kaydir_solayasla.set_text_wrap()
        self.metni_kaydir_solayasla.set_align('left')
        self.metni_kaydir_solayasla.set_font('Arial')
        self.metni_kaydir_solayasla.set_font_size(12)
        # self.metni_kaydir_solayasla.set_align('left')
        # self.metni_kaydir.set_border(1)
        return self.metni_kaydir_solayasla

    def dortKoseBorder(self):
        self.dortkoseBorder=self.wbook.add_format()
        self.dortkoseBorder.set_align('center')
        self.dortkoseBorder.set_align('vcenter')
        self.dortkoseBorder.set_font('Arial')
        self.dortkoseBorder.set_border(1)
        return self.dortkoseBorder

    def yataydaOrtala(self):
        self.yatayda_ortala=self.wbook.add_format()
        self.yatayda_ortala.set_align('center')
        self.yatayda_ortala.set_font('Arial')
        self.yatayda_ortala.set_font_size(12)
        return self.yatayda_ortala

    def dikeydeOrtala(self):
        self.dikeyde_ortala=self.wbook.add_format()
        self.dikeyde_ortala.set_align('vcenter')
        self.dikeyde_ortala.set_font('Arial')
        self.dikeyde_ortala.set_font_size(12)
        return self.dikeyde_ortala

    # def yazdirTest(self):
    #     self.closeFile()

    def dosyayiHazirla(self):

        self.wsheet.set_column('A:A', 4)
        self.wsheet.set_column('B:B', 22)
        self.wsheet.set_column('C:C', 12)
        self.wsheet.set_column('D:D', 19)
        self.wsheet.set_column('E:E', 19)
        self.wsheet.set_column('F:F', 15)
        self.wsheet.set_column('G:G', 15)
        self.wsheet.set_row(2,19)

    def raporBaslikYaz(self):
        self.dosyayiHazirla()
        self.wsheet.write(2,0,"S.N",self.baslikFormat())
        self.wsheet.write(2,1,"Gideceği Yer",self.baslikFormat())
        self.wsheet.write(2,2,"Tarih",self.baslikFormat())
        self.wsheet.write(2,3,"Sayısı",self.baslikFormat())
        self.wsheet.write(2,4,"Konusu",self.baslikFormat())
        self.wsheet.write(2,5,"EK",self.baslikFormat())
        self.wsheet.write(2,6,"POSTA TÜRÜ",self.baslikFormat())
        self.wsheet.write(0,6,tarih,self.yataydaOrtala())
        # self.wsheet.write(3,1,'İçişleri Bakanlığına(Bilgi İşlem Dairesi Başkanlığı)\n---------\n Tübitak Yerleşkesikamu Sertifikasyon Merkeziyeni İdari Bina Pk 74gebze 41470 Kocaeli',self.metniKaydirOrtala())

    def yazdir(self,r,c,data,format,row_height=110):
        self.wsheet.write(r,c,data,format)
        # self.wsheet.set_row(r,row_height)
    #
    def satirYuksekligi(self,r,h=110):
        self.wsheet.set_row(r,h)

    def teslimHazirla(self,r):
        self.wsheet.write(r+7,1,"Teslim Edenin\nAdı:\nSoyadi:",self.metniKaydirSolaYasla())
        self.wsheet.set_row(r+7,54)
        self.wsheet.write(r+7,4,"Teslim Alanın\nAdı:\nSoyadi:",self.metniKaydirSolaYasla())

    def yazdirilacakAlanBelirle(self,r):
        satir=r+8
        self.wsheet.print_area(f'A1:G{satir}')
        self.wsheet.fit_to_pages(1,1)


evraklar=[{'Evrak No': '123384', 'Konu': 'Kağıthane İlçe Nüfus Müdürlüğü NES Başvuru Formları', 'Gideceği Yer': 'İçişleri Bakanlığına(Bilgi İşlem Dairesi Başkanlığı), Tübitak Yerleşkesikamu Sertifikasyon Merkeziyeni İdari Bina Pk 74gebze 41470 Kocaeli', 'Tarih': '28.11.2019'}, {'Evrak No': '123830', 'Konu': 'İsay Ek Kullanıcı Talebi', 'Gideceği Yer': 'İçişleri Bakanlığına(Bilgi İşlem Dairesi Başkanlığı)', 'Tarih': '29.11.2019'}, {'Evrak No': '123838', 'Konu': 'İstek Bildirimi - Semra SARAÇ', 'Gideceği Yer': 'Kağıthane Kaymakamlığına(İlçe Yazı İşleri Müdürlüğü)', 'Tarih': '29.11.2019'}, {'Evrak No': '123839', 'Konu': 'Şikayet Bildirimi - Solmaz BOZKURT', 'Gideceği Yer': 'Kağıthane Kaymakamlığına(İlçe Yazı İşleri Müdürlüğü)', 'Tarih': '29.11.2019'}, {'Evrak No': '123848', 'Konu': 'Gülçin Özlem KOZAN', 'Gideceği Yer': 'Ataşehir Kaymakamlığına(İlçe Nüfus Müdürlüğü)', 'Tarih': '29.11.2019'}, {'Evrak No': '123861', 'Konu': 'Deniz KARAHANLI', 'Gideceği Yer': 'Esenyurt Kaymakamlığına(İlçe Nüfus Müdürlüğü)', 'Tarih': '29.11.2019'}]

if __name__=="__main__":
    rapor=ExportExcel()
    rapor.raporBaslikYaz()
    r=3;c=0 #c evrak sayısı kadar döngü r ise başlangıç satırı
    for c in range(len(evraklar)):
        if "," in evraklar[c]['Gideceği Yer']:
            yeni_gid_yer=evraklar[c]['Gideceği Yer'].replace(",","\n------------------------------\n")
            # rapor.satirYuksekligi(r,150)
            rapor.yazdir(r,0,str(c+1),rapor.metniKaydirOrtala())
            rapor.yazdir(r,1,yeni_gid_yer,rapor.metniKaydirOrtala())
            if "İçişleri Bakanlığına" in evraklar[c]['Gideceği Yer']:
                rapor.yazdir(r,6,"ELEKTRONİK OLARAK POSTALANACAKTIR\n\n---------------------\n      ...       ",
                             rapor.metniKaydirOrtala())
        else:
            rapor.yazdir(r,0,str(c+1),rapor.metniKaydirOrtala())
            rapor.yazdir(r,1,evraklar[c]['Gideceği Yer'],rapor.metniKaydirOrtala())
            rapor.yazdir(r,6,"",rapor.dortKoseBorder())
        rapor.yazdir(r,2,evraklar[c]['Tarih'],rapor.metniKaydirOrtala())
        rapor.yazdir(r,3,evraklar[c]['Evrak No'],rapor.metniKaydirOrtala())
        rapor.yazdir(r,4,evraklar[c]['Konu'],rapor.metniKaydirOrtala())
        rapor.yazdir(r,5,"",rapor.dortKoseBorder())


        r+=1 #sonraki satır =(diğer evrak)

    rapor.yazdirilacakAlanBelirle(len(evraklar))
    rapor.teslimHazirla(len(evraklar))
    rapor.closeFile()







# # Workbook() takes one, non-optional, argument
# # which is the filename that we want to create.
# workbook = xlsxwriter.Workbook('hello.xlsx')
# # The workbook object is then used to add new
# # worksheet via the add_worksheet() method.
# worksheet = workbook.add_worksheet('Sayfa1')
# # tarih_f=workbook.add_format()
# # tarih_f.set_num_format('dd/mm/yyyy')

# baslik=workbook.add_format()
# baslik.set_bold()
# baslik.set_border(1)
# baslik.set_align('center')

#
# yatay_hucre_center=workbook.add_format()
# yatay_hucre_center.set_align('center')
#
# dikey_hucre_center=workbook.add_format()
# dikey_hucre_center.set_align('vcenter')
#
# yatay_dikey_ortala_with_border=workbook.add_format() #yatay dikey ortala border
# yatay_dikey_ortala_with_border.set_align('center')
# yatay_dikey_ortala_with_border.set_align('vcenter')
# yatay_dikey_ortala_with_border.set_border(1)
#
# yatay_dikey_ortala_no_border=workbook.add_format() #yatay dikey ortala
# yatay_dikey_ortala_no_border.set_align('center')
# yatay_dikey_ortala_no_border.set_align('vcenter')
# # yatay_dikey_ortala.set_border(1)
#
#
#
#
#
#
#
#
#
#
#
# # worksheet.set_zoom(190)
# # worksheet.print_area('A1:H50')
# # worksheet.set_print_scale(70)
# # worksheet.set_paper(9)
# # worksheet.set_page_view()
# worksheet.set_start_page(1)
#
#
# worksheet.set_column('A:A', 4)
# worksheet.set_column('B:B', 22)
# worksheet.set_column('C:C', 10)
# worksheet.set_column('D:D', 19)
# worksheet.set_column('E:E', 19)
# worksheet.set_column('F:F', 15)
# worksheet.set_column('G:G', 15)
#
# worksheet.write(0,6,tarih,yatay_dikey_ortala_no_border)
#
# # Use the worksheet object to write
# # data via the write() method.
# # worksheet.write('A1', 'Hello..')
# # worksheet.write('B1', 'Geeks')
# # worksheet.write('C1', 'For')
# # worksheet.write('D1', 'Geeks')
#
# # Finally, close the Excel file
# # via the close() method.
# workbook.close()
