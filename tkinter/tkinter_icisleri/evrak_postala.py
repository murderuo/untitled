from bs4 import BeautifulSoup as bs

class Postala(bs):

    def __init__(self,*args,**kwargs):
        # bs.__init__(self,*args,**kwargs)
        self.postalanacakEvraksayisi=0
    def getPostalanacakEvrakSayisi(self,post_count):
        self.postalanacakEvraksayisi=post_count
    def getEvrakBilgileri(self,source_code):
        # source_code=source_c.replace(u'\xc4',"i")

        self.evraks=[]
        # self.html_source=bs(source_code,'html.parser')
        self.html_source=bs(source_code,'lxml')
        self.posta_table=self.html_source.find('table',id='ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen')
        # print(self.posta_table)
        if self.posta_table==None:
            return False
        self.tbody=self.posta_table.find('tbody')
        # print(self.tbody)
        self.tbody_head_row=self.tbody.tr
        self.all_table_header_th=self.tbody_head_row.find_all('th')

        self.EvrakNo=self.all_table_header_th[0].get_text()
        self.EvrakKonu=self.all_table_header_th[1].get_text().split('/')[0]
        self.EvrakGidecegiYer=self.all_table_header_th[1].get_text().split('/')[1]
        self.EvrakTarih=self.all_table_header_th[3].get_text().split('/')[1]
        # print(
        #     f'{self.EvrakNo.strip()},{self.EvrakKonu.strip()},{self.EvrakGidecegiYer.strip()},{self.EvrakTarih.strip()}')
        #########################evraks######################
        self.evraklar_tr=self.tbody_head_row.find_next_siblings(
            'tr')  # dizi olarak her bir evrakın tr satırını döndürür
        for evrak in self.evraklar_tr:
            self.evrak_all_td=evrak.find_all('td',class_='columnborder')
            i=0
            for evrak_td in self.evrak_all_td:
                if i == 0:
                    EvrakNo=evrak_td.find('span')
                    if EvrakNo != None:
                        self.evNo=EvrakNo.get_text(strip=True)
                        i+=1
                        continue
                elif i == 1:
                    all_spans=evrak_td.find_all('span')
                    j=0  # 2adet span olduğu için 2 kere döndüreceğiz
                    for span in all_spans:
                        if j == 0:
                            self.evKonu=span.get('title')
                            # print(self.evKonu)
                            j+=1
                            continue
                        elif j == 1:
                            self.evGidYer_text=span.get_text(strip=True)
                            self.evGidYer=self.evGidYer_text


                            #.replace("\xc4","i")
                            # print(self.evGidYer)
                            j=0
                            break
                    i+=1
                    continue
                elif i == 3:
                    evTarih=evrak_td.get_text(strip=True)
                    self.evTar=evTarih.replace('Dağıtımlı','').replace('Günlüdür',"").replace("İvedi","").replace('-',"")  # print(self.evTar)
                i+=1

            self.evraks.append({self.EvrakNo.strip():self.evNo,self.EvrakKonu.strip():self.evKonu,self.EvrakGidecegiYer.strip():
                                 self.evGidYer.replace('\xa0'," "),self.EvrakTarih.strip():self.evTar})

        return self.evraks
            # print(f'Evrakno:{self.evNo},Evrak Konu:{self.evKonu},Evrak gideceği yer:{self.evGidYer},Tarih:{self.evTar}')  # # print(EvrakNo,EvrakKonu,EvrakGidecegiYer)  # if EvrakNo!=None:  #     self.evNo=EvrakNo.get_text()  #     print(self.evNo)  #     continue  # elif EvrakKonu!=None:  #     self.evKonu=EvrakKonu.get('title')  # .get_text(strip=True)  #     print(self.evKonu)  #     continue  # elif EvrakGidecegiYer!=None:  #     self.evGidYer=EvrakGidecegiYer.get_text()  #     print(self.evGidYer)  # elif evrak_td.get_text(strip=True)=='İstanbul Valiliği İstanbul Bilgi İşlem Şube Müdürlüğü':  #     continue  # else:  #     self.evTarih=evrak_td.get_text(strip=True)  #     print(self.evTarih.replace('Dağıtımlı',''))  # i+=1  # if i==3:break
            # return f'Evrakno:{self.evNo},Evrak Konu:{self.evKonu},Evrak gideceği yer:{self.evGidYer},Tarih:{self.evTar}'.join()

if __name__ == '__main__':
    sk5="""    <table id="ctl00_ctl00_cph1_cphGelenGiden_TablePostalanmayiBekleyenEvraklarGenel" style="width: 100%">
                            <tbody>
                             <tr>
                              <td align="center" style="width: 100%">
                               <div>
                                <table border="1" cellpadding="4" cellspacing="0" class="grid1" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen" rules="all" style="width:100%;border-collapse:collapse;">
                                 <tbody>
                                  <tr>
								  <th scope="col">
                                    <table>
                                     <tbody>
                                      <tr>
                                       <td>
                                        <img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_arrowEvrakNo" src="../../App_Themes/Main/Images/Ikonlar/yukariokth.jpg" style="border-width:0px;">
                                       </td>
                                       <td>
                                        <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl02$LinkButtonEvrakNo&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_LinkButtonEvrakNo" jqueryclass="jLinkButton">
                                         Evrak No
                                        </a>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </th>
                                   <th scope="col">
                                    <table>
                                     <tbody>
                                      <tr>
                                       <td>
                                       </td>
                                       <td>
                                        <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl02$LinkButtonKonu&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_LinkButtonKonu" jqueryclass="jLinkButton">
                                         Konu/Gideceği Yer
                                        </a>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </th>
                                   <th scope="col">
                                    <table>
                                     <tbody>
                                      <tr>
                                       <td>
                                       </td>
                                       <td>
                                        <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl02$LinkButtonHazirlayanTeskilatUzunAd&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_LinkButtonHazirlayanTeskilatUzunAd" jqueryclass="jLinkButton">
                                         Birimi
                                        </a>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </th>
                                   <th scope="col">
                                    <table>
                                     <tbody>
                                      <tr>
                                       <td>
                                       </td>
                                       <td>
                                        <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl02$LinkButtonEvrakTar&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_LinkButtonEvrakTar" jqueryclass="jLinkButton">
                                         Kişiye Özel Durum/Tarih
                                        </a>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </th>
                                   <th scope="col">
                                    <table>
                                     <tbody>
                                      <tr>
                                       <td>
                                       </td>
                                       <td>
                                        <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl02$LinkButtonBekledigiGun&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_LinkButtonBekledigiGun" jqueryclass="jLinkButton">
                                         Beklediği Gün
                                        </a>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </th>
                                   <th scope="col">
                                    <table>
                                     <tbody>
                                      <tr>
                                       <td>
                                       </td>
                                       <td>
                                        <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl02$LinkButtonMiat&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_LinkButtonMiat" jqueryclass="jLinkButton">
                                         Miat
                                        </a>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </th>
                                   <th scope="col">
                                    Kağıt Ortamında Gidecek Mi?
                                   </th>
                                   <th scope="col">
                                   </th>
                                   <th scope="col">
                                   </th>
                                  </tr>
								  <tr>
									<td class="columnborder" align="right" style="width:75px;">
										<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
											<tbody><tr>
												<td style="width: 33%; text-align: left">
													<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
												</td>
												<td style="width: 33%; text-align: left">

												</td>
												<td style="width: 33%; text-align: right">
													<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">120474</span>
												</td>
											</tr>
										</tbody></table>
									</td>
									<td class="columnborder">
										<table width="100%" cellpadding="0" cellspacing="0">
											<tbody><tr>
												<td align="left">
													<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lblKonu" title="Hüseyin YEŞLDAĞ  Nes Formu" maxlength="200">Hüseyin YEŞLDAĞ  Nes Formu</span>
												</td>
											</tr>
											<tr>
												<td align="left">
													<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lblGidecegiYer" title="İçişleri&amp;nbsp;Bakanlığına&amp;nbsp;<br>(Bilgi&amp;nbsp;İşlem&amp;nbsp;Dairesi&amp;nbsp;Başkanlığı), Tübitak&amp;nbsp;Yerleşkesi&amp;nbsp;<br>kamu&amp;nbsp;Sertifikasyon&amp;nbsp;Merkezi&amp;nbsp;<br>yeni&amp;nbsp;İdari&amp;nbsp;Bina&amp;nbsp;Pk&amp;nbsp;74&amp;nbsp;<br>gebze&amp;nbsp;41470&amp;nbsp;Kocaeli" maxlength="200">İçişleri&nbsp;Bakanlığına&nbsp;<br>(Bilgi&nbsp;İşlem&nbsp;Dairesi&nbsp;Başkanlığı), Tübitak&nbsp;Yerleşkesi&nbsp;<br>kamu&nbsp;Sertifikasyon&nbsp;Merkezi&nbsp;<br>yeni&nbsp;İdari&nbsp;Bina&nbsp;Pk&nbsp;74&nbsp;<br>gebze&nbsp;41470&nbsp;Kocaeli</span>



												</td>
											</tr>
										</tbody></table>
									</td>
									<td class="columnborder">
										<table width="100%" cellpadding="0" cellspacing="0">
											<tbody><tr>
												<td align="left">
													İstanbul Valiliği İstanbul Bilgi İşlem Şube Müdürlüğü
												</td>
											</tr>
										</tbody></table>
									</td>
									<td class="columnborder">
										<table width="100%" cellpadding="0" cellspacing="0">
											<tbody><tr>
												<td align="center" style="color: Red">
													<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_labelKisiyeOzelUzunAd">Dağıtımlı</span>
												</td>
											</tr>
											<tr>
												<td align="center">
													25.11.2019
												</td>
											</tr>
										</tbody></table>
									</td>
									<td class="columnborder" align="center">
										<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_LabelBekledigiGun">1</span>
									</td>
									<td class="columnborder" align="center">
										<table width="100%" cellpadding="0" cellspacing="0">
											<tbody><tr>
												<td align="center">
													<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_Label3">0</span>
												</td>
											</tr>
											<tr>
												<td align="center" style="color: Red">
													<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lblGizlilikTipAdi"></span>
												</td>
											</tr>
										</tbody></table>
									</td>
									<td class="columnborder" align="center" style="color:Red;">
										Evet
									</td>
									<td class="columnborder" valign="top">
										<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl03$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay</a>
									</td>
									<td class="columnborder" valign="top" style="width:100px;">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl03$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala</a>
													</td>
								</tr>
								  <tr>
                                   <td align="right" class="columnborder" style="width:75px;">
                                    <table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
                                     <tbody>
                                      <tr>
                                       <td style="width: 33%; text-align: left">
                                        <img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_imageImzalimi" src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;" title="Bu evrak sayısal imzalıdır.">
                                       </td>
                                       <td style="width: 33%; text-align: left">
                                       </td>
                                       <td style="width: 33%; text-align: right">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">
                                         114183
                                        </span>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td class="columnborder">
                                    <table cellpadding="0" cellspacing="0" width="100%">
                                     <tbody>
                                      <tr>
                                       <td align="left">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lblKonu" maxlength="200" title="NES Başvuru Formları">
                                         NES Başvuru Formları
                                        </span>
                                       </td>
                                      </tr>
                                      <tr>
                                       <td align="left">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lblGidecegiYer" maxlength="200" title="İçişleri&amp;nbsp;Bakanlığına&amp;nbsp;<br>(Bilgi&amp;nbsp;İşlem&amp;nbsp;Dairesi&amp;nbsp;Başkanlığı), Tübitak&amp;nbsp;Yerleşkesi&amp;nbsp;Kamu&amp;nbsp;Sertifikasyon&amp;nbsp;Merkezi&amp;nbsp;Yeni&amp;nbsp;İdari&amp;nbsp;Bina&amp;nbsp;P.k.&amp;nbsp;74&amp;nbsp;Gebze&amp;nbsp;41470&amp;nbsp;Kocaeli">
                                         İçişleri&nbsp;Bakanlığına
                                         <br>
                                         (Bilgi&nbsp;İşlem&nbsp;Dairesi&nbsp;Başkanlığı), Tübitak&nbsp;Yerleşkesi&nbsp;Kamu&nbsp;Sertifikasyon&nbsp;Merkezi&nbsp;Yeni&nbsp;İdari&nbsp;Bina&nbsp;P.k.&nbsp;74&nbsp;Gebze&nbsp;41470&nbsp;Kocaeli
                                        </span>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td class="columnborder">
                                    <table cellpadding="0" cellspacing="0" width="100%">
                                     <tbody>
                                      <tr>
                                       <td align="left">
                                        İstanbul Valiliği İstanbul Bilgi İşlem Şube Müdürlüğü
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td class="columnborder">
                                    <table cellpadding="0" cellspacing="0" width="100%">
                                     <tbody>
                                      <tr>
                                       <td align="center" style="color: Red">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_labelKisiyeOzelUzunAd">
                                         Dağıtımlı
                                        </span>
                                       </td>
                                      </tr>
                                      <tr>
                                       <td align="center">
                                        11.11.2019
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td align="center" class="columnborder">
                                    <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_LabelBekledigiGun">
                                     2
                                    </span>
                                   </td>
                                   <td align="center" class="columnborder">
                                    <table cellpadding="0" cellspacing="0" width="100%">
                                     <tbody>
                                      <tr>
                                       <td align="center">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_Label3">
                                         0
                                        </span>
                                       </td>
                                      </tr>
                                      <tr>
                                       <td align="center" style="color: Red">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lblGizlilikTipAdi">
                                        </span>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td align="center" class="columnborder" style="color:Red;">
                                    Evet
                                   </td>
                                   <td class="columnborder" valign="top">
                                    <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl03$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lnkDetay" jqueryclass="jLinkButton">
                                     Detay
                                    </a>
                                   </td>
                                   <td class="columnborder" style="width:100px;" valign="top">
                                    <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl03$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lnkHizliPostala" jqueryclass="jLinkButton">
                                     Teslim Al ve Postala
                                    </a>
                                   </td>
                                  </tr>
                                  <tr class="alternatifrow">
                                   <td align="right" class="columnborder" style="width:75px;">
                                    <table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
                                     <tbody>
                                      <tr>
                                       <td style="width: 33%; text-align: left">
                                        <img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_imageImzalimi" src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;" title="Bu evrak sayısal imzalıdır.">
                                       </td>
                                       <td style="width: 33%; text-align: left">
                                       </td>
                                       <td style="width: 33%; text-align: right">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">
                                         114187
                                        </span>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td class="columnborder">
                                    <table cellpadding="0" cellspacing="0" width="100%">
                                     <tbody>
                                      <tr>
                                       <td align="left">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_lblKonu" maxlength="200" title="Suna DEMİRCİ ve Erol Akdeniz' İn NES Başvuru Formu">
                                         Suna DEMİRCİ ve Erol Akdeniz' İn NES Başvuru Formu
                                        </span>
                                       </td>
                                      </tr>
                                      <tr>
                                       <td align="left">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_lblGidecegiYer" maxlength="200" title="İçişleri&amp;nbsp;Bakanlığına&amp;nbsp;<br>(Bilgi&amp;nbsp;İşlem&amp;nbsp;Dairesi&amp;nbsp;Başkanlığı), Tübitak&amp;nbsp;Yerleşkesi&amp;nbsp;<br>kamu&amp;nbsp;Sertifikasyon&amp;nbsp;Merkezi&amp;nbsp;<br>yeni&amp;nbsp;İdari&amp;nbsp;Bina&amp;nbsp;Pk&amp;nbsp;74&amp;nbsp;<br>gebze&amp;nbsp;41470&amp;nbsp;Kocaeli">
                                         İçişleri&nbsp;Bakanlığına
                                         <br>
                                         (Bilgi&nbsp;İşlem&nbsp;Dairesi&nbsp;Başkanlığı), Tübitak&nbsp;Yerleşkesi
                                         <br>
                                         kamu&nbsp;Sertifikasyon&nbsp;Merkezi
                                         <br>
                                         yeni&nbsp;İdari&nbsp;Bina&nbsp;Pk&nbsp;74
                                         <br>
                                         gebze&nbsp;41470&nbsp;Kocaeli
                                        </span>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td class="columnborder">
                                    <table cellpadding="0" cellspacing="0" width="100%">
                                     <tbody>
                                      <tr>
                                       <td align="left">
                                        İstanbul Valiliği İstanbul Bilgi İşlem Şube Müdürlüğü
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td class="columnborder">
                                    <table cellpadding="0" cellspacing="0" width="100%">
                                     <tbody>
                                      <tr>
                                       <td align="center" style="color: Red">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_labelKisiyeOzelUzunAd">
                                         Dağıtımlı
                                        </span>
                                       </td>
                                      </tr>
                                      <tr>
                                       <td align="center">
                                        11.11.2019
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td align="center" class="columnborder">
                                    <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_LabelBekledigiGun">
                                     2
                                    </span>
                                   </td>
                                   <td align="center" class="columnborder">
                                    <table cellpadding="0" cellspacing="0" width="100%">
                                     <tbody>
                                      <tr>
                                       <td align="center">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_Label3">
                                         0
                                        </span>
                                       </td>
                                      </tr>
                                      <tr>
                                       <td align="center" style="color: Red">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_lblGizlilikTipAdi">
                                        </span>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td align="center" class="columnborder" style="color:Red;">
                                    Evet
                                   </td>
                                   <td class="columnborder" valign="top">
                                    <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl04$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_lnkDetay" jqueryclass="jLinkButton">
                                     Detay
                                    </a>
                                   </td>
                                   <td class="columnborder" style="width:100px;" valign="top">
                                    <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl04$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_lnkHizliPostala" jqueryclass="jLinkButton">
                                     Teslim Al ve Postala
                                    </a>
                                   </td>
                                  </tr>
                                 </tbody>
                                </table>
                               </div>
                              </td>
                             </tr>
                             <tr>
                              <td>
                               <input id="ctl00_ctl00_cph1_cphGelenGiden_LinkButtonTopluPostala_UcImgButtonOnay" name="ctl00$ctl00$cph1$cphGelenGiden$LinkButtonTopluPostala$UcImgButtonOnay" onclick="return CheckValidationUcImgButtonOnay(this);WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$LinkButtonTopluPostala$UcImgButtonOnay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, false))" src="../../App_Themes/Main/Images/Buttons/btnsecilievraklaripostala.jpg" style="border-width:0px;display:none;" title="Seçtiğiniz kağıt ortamında gitmeyecek evrakları postalar" type="image">
                               <input id="ctl00_ctl00_cph1_cphGelenGiden_LinkButtonTopluPostala_ButtonHidden" name="ctl00$ctl00$cph1$cphGelenGiden$LinkButtonTopluPostala$ButtonHidden" onclick="null" style="display: none;" type="submit" value="">
                               <input id="ctl00_ctl00_cph1_cphGelenGiden_LinkButtonTopluPostala_HiddenFieldImgBtnOnayVldgrp" name="ctl00$ctl00$cph1$cphGelenGiden$LinkButtonTopluPostala$HiddenFieldImgBtnOnayVldgrp" type="hidden">
                               <input id="ctl00_ctl00_cph1_cphGelenGiden_LinkButtonTopluPostala_HiddenFieldImgBtnOnayCausVld" name="ctl00$ctl00$cph1$cphGelenGiden$LinkButtonTopluPostala$HiddenFieldImgBtnOnayCausVld" type="hidden">
                               </script>
                              </td>
                             </tr>
                            </tbody>

                           </table>
"""
    sk3="""<table id="ctl00_ctl00_cph1_cphGelenGiden_tblMain" width="100%" align="center" cellpadding="0" cellspacing="0" class="AnaTablo" style="display:block">
	<tbody><tr>
		<td style="width: 100%" valign="top" align="center">
				<table style="width: 100%" class="AnaAltTablo">
					<tbody><tr>
						<td valign="top" align="center">
							<table id="ctl00_ctl00_cph1_cphGelenGiden_TablePostalanmayiBekleyenEvraklarGenel" style="width: 100%">
			<tbody><tr>
				<td style="width: 100%" align="center">
										<div>
					<table class="grid1" cellspacing="0" cellpadding="4" rules="all" border="1" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen" style="width:100%;border-collapse:collapse;">
						<tbody><tr>
							<th scope="col">
														<table>
															<tbody><tr>
																<td>
																	<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_arrowEvrakNo" src="../../App_Themes/Main/Images/Ikonlar/yukariokth.jpg" style="border-width:0px;">
																</td>
																<td>
																	<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_LinkButtonEvrakNo" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl02$LinkButtonEvrakNo&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Evrak No</a>
																</td>
															</tr>
														</tbody></table>
													</th><th scope="col">
														<table>
															<tbody><tr>
																<td>
																	
																</td>
																<td>
																	<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_LinkButtonKonu" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl02$LinkButtonKonu&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Konu/Gideceği Yer</a>
																</td>
															</tr>
														</tbody></table>
													</th><th scope="col">
														<table>
															<tbody><tr>
																<td>
																	
																</td>
																<td>
																	<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_LinkButtonHazirlayanTeskilatUzunAd" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl02$LinkButtonHazirlayanTeskilatUzunAd&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Birimi</a>
																</td>
															</tr>
														</tbody></table>
													</th><th scope="col">
														<table>
															<tbody><tr>
																<td>
																	
																</td>
																<td>
																	<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_LinkButtonEvrakTar" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl02$LinkButtonEvrakTar&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Kişiye Özel Durum/Tarih</a>
																</td>
															</tr>
														</tbody></table>
													</th><th scope="col">
														<table>
															<tbody><tr>
																<td>
																	
																</td>
																<td>
																	<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_LinkButtonBekledigiGun" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl02$LinkButtonBekledigiGun&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Beklediği Gün</a>
																</td>
															</tr>
														</tbody></table>
													</th><th scope="col">
														<table>
															<tbody><tr>
																<td>
																	
																</td>
																<td>
																	<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_LinkButtonMiat" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl02$LinkButtonMiat&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Miat</a>
																</td>
															</tr>
														</tbody></table>
													</th><th scope="col">Kağıt Ortamında Gidecek Mi?</th><th scope="col">&nbsp;</th><th scope="col">&nbsp;</th>
						</tr><tr>
							<td class="columnborder" align="right" style="width:75px;">
														<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
															<tbody><tr>
																<td style="width: 33%; text-align: left">
																	<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
																</td>
																<td style="width: 33%; text-align: left">
																	
																</td>
																<td style="width: 33%; text-align: right">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">119114</span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lblKonu" title="Müracaatınız" maxlength="200">Müracaatınız</span>
																</td>
															</tr>
															<tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lblGidecegiYer" title="Faruk&amp;nbsp;Kıyım&amp;nbsp;<br>siyavuşpaşa&amp;nbsp;Mah.&amp;nbsp;Mustafa&amp;nbsp;Kemal&amp;nbsp;Paşa&amp;nbsp;Cad.no:15/3<br>bahçelievler/istanbul" maxlength="200">Faruk&nbsp;Kıyım&nbsp;<br>siyavuşpaşa&nbsp;Mah.&nbsp;Mustafa&nbsp;Kemal&nbsp;Paşa&nbsp;Cad.no:15/3<br>bahçelievler/istanbul</span>

																	

																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	İstanbul Valiliği İstanbul İdare ve Denetim Müdürlüğü
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_labelKisiyeOzelUzunAd">-</span>
																</td>
															</tr>
															<tr>
																<td align="center">
																	20.11.2019
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center">
														<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_LabelBekledigiGun">8</span>
													</td><td class="columnborder" align="center">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_Label3">0</span>
																</td>
															</tr>
															<tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lblGizlilikTipAdi"></span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center" style="color:Red;">
														Evet
													</td><td class="columnborder" valign="top">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl03$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay</a>
													</td><td class="columnborder" valign="top" style="width:100px;">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl03$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala</a>
													</td>
						</tr><tr class="alternatifrow">
							<td class="columnborder" align="right" style="width:75px;">
														<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
															<tbody><tr>
																<td style="width: 33%; text-align: left">
																	<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
																</td>
																<td style="width: 33%; text-align: left">
																	
																</td>
																<td style="width: 33%; text-align: right">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">122205</span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_lblKonu" title="Sancaktepe Belediyesi  (Mehmet AKKIRIK)" maxlength="200">Sancaktepe Belediyesi  (Mehmet AKKIRIK)</span>
																</td>
															</tr>
															<tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_lblGidecegiYer" title="Sancaktepe&amp;nbsp;Kaymakamlığı, Sayın&amp;nbsp;Mehmet&amp;nbsp;Akkırık&amp;nbsp;<br>sarıgazi&amp;nbsp;Mah.<br>öğretmen&amp;nbsp;Sok.&amp;nbsp;<br>no:24&amp;nbsp;D:1<br>sancaktepe/ist<br>(Ek&amp;nbsp;Konulmadı)" maxlength="200">Sancaktepe&nbsp;Kaymakamlığı, Sayın&nbsp;Mehmet&nbsp;Akkırık&nbsp;<br>sarıgazi&nbsp;Mah.<br>öğretmen&nbsp;Sok.&nbsp;<br>no:24&nbsp;D:1<br>sancaktepe/ist<br>(Ek&nbsp;Konulmadı)</span>

																	

																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	İstanbul Valiliği İstanbul İdare ve Denetim Müdürlüğü
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_labelKisiyeOzelUzunAd">Dağıtımlı</span>
																</td>
															</tr>
															<tr>
																<td align="center">
																	27.11.2019
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center">
														<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_LabelBekledigiGun">1</span>
													</td><td class="columnborder" align="center">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_Label3">0</span>
																</td>
															</tr>
															<tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_lblGizlilikTipAdi"></span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center" style="color:Red;">
														Evet
													</td><td class="columnborder" valign="top">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl04$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay</a>
													</td><td class="columnborder" valign="top" style="width:100px;">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl04$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala</a>
													</td>
						</tr><tr>
							<td class="columnborder" align="right" style="width:75px;">
														<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
															<tbody><tr>
																<td style="width: 33%; text-align: left">
																	<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
																</td>
																<td style="width: 33%; text-align: left">
																	
																</td>
																<td style="width: 33%; text-align: right">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">122207</span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_lblKonu" title="Sarıyer İstinye Muhtarı hk." maxlength="200">Sarıyer İstinye Muhtarı hk.</span>
																</td>
															</tr>
															<tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_lblGidecegiYer" title="Sarıyer&amp;nbsp;Kaymakamlığına, Mikail&amp;nbsp;Atakoru&amp;nbsp;<br>şehit&amp;nbsp;Halil&amp;nbsp;İbrahim&amp;nbsp;Sok.&amp;nbsp;No:101&amp;nbsp;İstinye/sarıyer/istanbul<br><br>(Ek&amp;nbsp;Konulmadı)" maxlength="200">Sarıyer&nbsp;Kaymakamlığına, Mikail&nbsp;Atakoru&nbsp;<br>şehit&nbsp;Halil&nbsp;İbrahim&nbsp;Sok.&nbsp;No:101&nbsp;İstinye/sarıyer/istanbul<br><br>(Ek&nbsp;Konulmadı)</span>

																	

																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	İstanbul Valiliği İstanbul İdare ve Denetim Müdürlüğü
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_labelKisiyeOzelUzunAd">Dağıtımlı</span>
																</td>
															</tr>
															<tr>
																<td align="center">
																	27.11.2019
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center">
														<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_LabelBekledigiGun">1</span>
													</td><td class="columnborder" align="center">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_Label3">0</span>
																</td>
															</tr>
															<tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_lblGizlilikTipAdi"></span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center" style="color:Red;">
														Evet
													</td><td class="columnborder" valign="top">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl05$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay</a>
													</td><td class="columnborder" valign="top" style="width:100px;">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl05$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala</a>
													</td>
						</tr><tr class="alternatifrow">
							<td class="columnborder" align="right" style="width:75px;">
														<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
															<tbody><tr>
																<td style="width: 33%; text-align: left">
																	<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl06_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
																</td>
																<td style="width: 33%; text-align: left">
																	
																</td>
																<td style="width: 33%; text-align: right">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl06_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">122441</span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl06_lblKonu" title="Büyükşehir Belediyesi.  (Derya AKSOY ve ark.)" maxlength="200">Büyükşehir Belediyesi.  (Derya AKSOY ve ark.)</span>
																</td>
															</tr>
															<tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl06_lblGidecegiYer" title="İstanbul&amp;nbsp;Büyükşehir&amp;nbsp;Belediye&amp;nbsp;Başkanlığına<br>(İştirakler&amp;nbsp;Koordinasyon&amp;nbsp;Müdürlüğü)" maxlength="200">İstanbul&nbsp;Büyükşehir&nbsp;Belediye&nbsp;Başkanlığına<br>(İştirakler&nbsp;Koordinasyon&nbsp;Müdürlüğü)</span>

																	

																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	İstanbul Valiliği İstanbul İdare ve Denetim Müdürlüğü
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl06_labelKisiyeOzelUzunAd">-</span>
																</td>
															</tr>
															<tr>
																<td align="center">
																	27.11.2019
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center">
														<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl06_LabelBekledigiGun">1</span>
													</td><td class="columnborder" align="center">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl06_Label3">0</span>
																</td>
															</tr>
															<tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl06_lblGizlilikTipAdi"></span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center" style="color:Red;">
														Evet
													</td><td class="columnborder" valign="top">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl06_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl06$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay</a>
													</td><td class="columnborder" valign="top" style="width:100px;">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl06_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl06$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala</a>
													</td>
						</tr><tr>
							<td class="columnborder" align="right" style="width:75px;">
														<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
															<tbody><tr>
																<td style="width: 33%; text-align: left">
																	<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
																</td>
																<td style="width: 33%; text-align: left">
																	
																</td>
																<td style="width: 33%; text-align: right">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">122443</span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_lblKonu" title="Büyükşehir Belediyesi.  (Sr.No:2018/119372)" maxlength="200">Büyükşehir Belediyesi.  (Sr.No:2018/119372)</span>
																</td>
															</tr>
															<tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_lblGidecegiYer" title="İstanbul&amp;nbsp;Büyükşehir&amp;nbsp;Belediye&amp;nbsp;Başkanlığına" maxlength="200">İstanbul&nbsp;Büyükşehir&nbsp;Belediye&nbsp;Başkanlığına</span>

																	

																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	İstanbul Valiliği İstanbul İdare ve Denetim Müdürlüğü
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_labelKisiyeOzelUzunAd">-</span>
																</td>
															</tr>
															<tr>
																<td align="center">
																	27.11.2019
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center">
														<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_LabelBekledigiGun">1</span>
													</td><td class="columnborder" align="center">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_Label3">0</span>
																</td>
															</tr>
															<tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_lblGizlilikTipAdi"></span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center" style="color:Red;">
														Evet
													</td><td class="columnborder" valign="top">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl07$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay</a>
													</td><td class="columnborder" valign="top" style="width:100px;">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl07$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala</a>
													</td>
						</tr><tr class="alternatifrow">
							<td class="columnborder" align="right" style="width:75px;">
														<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
															<tbody><tr>
																<td style="width: 33%; text-align: left">
																	<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl08_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
																</td>
																<td style="width: 33%; text-align: left">
																	
																</td>
																<td style="width: 33%; text-align: right">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl08_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">122444</span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl08_lblKonu" title="Büyükşehir Belediyesi.  (Sr.No:2018/118449)" maxlength="200">Büyükşehir Belediyesi.  (Sr.No:2018/118449)</span>
																</td>
															</tr>
															<tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl08_lblGidecegiYer" title="İstanbul&amp;nbsp;Büyükşehir&amp;nbsp;Belediye&amp;nbsp;Başkanlığına" maxlength="200">İstanbul&nbsp;Büyükşehir&nbsp;Belediye&nbsp;Başkanlığına</span>

																	

																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	İstanbul Valiliği İstanbul İdare ve Denetim Müdürlüğü
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl08_labelKisiyeOzelUzunAd">-</span>
																</td>
															</tr>
															<tr>
																<td align="center">
																	27.11.2019
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center">
														<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl08_LabelBekledigiGun">1</span>
													</td><td class="columnborder" align="center">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl08_Label3">0</span>
																</td>
															</tr>
															<tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl08_lblGizlilikTipAdi"></span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center" style="color:Red;">
														Evet
													</td><td class="columnborder" valign="top">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl08_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl08$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay</a>
													</td><td class="columnborder" valign="top" style="width:100px;">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl08_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl08$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala</a>
													</td>
						</tr><tr>
							<td class="columnborder" align="right" style="width:75px;">
														<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
															<tbody><tr>
																<td style="width: 33%; text-align: left">
																	<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
																</td>
																<td style="width: 33%; text-align: left">
																	
																</td>
																<td style="width: 33%; text-align: right">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">122445</span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_lblKonu" title="Büyükşeir Belediyesi.  (Hüsnü YURTAŞAN)" maxlength="200">Büyükşeir Belediyesi.  (Hüsnü YURTAŞAN)</span>
																</td>
															</tr>
															<tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_lblGidecegiYer" title="İstanbul&amp;nbsp;Büyükşehir&amp;nbsp;Belediye&amp;nbsp;Başkanlığına" maxlength="200">İstanbul&nbsp;Büyükşehir&nbsp;Belediye&nbsp;Başkanlığına</span>

																	

																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	İstanbul Valiliği İstanbul İdare ve Denetim Müdürlüğü
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_labelKisiyeOzelUzunAd">-</span>
																</td>
															</tr>
															<tr>
																<td align="center">
																	27.11.2019
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center">
														<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_LabelBekledigiGun">1</span>
													</td><td class="columnborder" align="center">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_Label3">0</span>
																</td>
															</tr>
															<tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_lblGizlilikTipAdi"></span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center" style="color:Red;">
														Evet
													</td><td class="columnborder" valign="top">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl09$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay</a>
													</td><td class="columnborder" valign="top" style="width:100px;">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl09$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala</a>
													</td>
						</tr><tr class="alternatifrow">
							<td class="columnborder" align="right" style="width:75px;">
														<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
															<tbody><tr>
																<td style="width: 33%; text-align: left">
																	<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl10_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
																</td>
																<td style="width: 33%; text-align: left">
																	
																</td>
																<td style="width: 33%; text-align: right">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl10_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">122446</span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl10_lblKonu" title="Erdem ŞAHİN" maxlength="200">Erdem ŞAHİN</span>
																</td>
															</tr>
															<tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl10_lblGidecegiYer" title="İstanbul&amp;nbsp;Büyükşehir&amp;nbsp;Belediye&amp;nbsp;Başkanlığına, İstanbul&amp;nbsp;Anadolu&amp;nbsp;13.&amp;nbsp;İş&amp;nbsp;Mahkemesine&amp;nbsp;" maxlength="200">İstanbul&nbsp;Büyükşehir&nbsp;Belediye&nbsp;Başkanlığına, İstanbul&nbsp;Anadolu&nbsp;13.&nbsp;İş&nbsp;Mahkemesine&nbsp;</span>

																	

																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	İstanbul Valiliği İstanbul İdare ve Denetim Müdürlüğü
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl10_labelKisiyeOzelUzunAd">Dağıtımlı</span>
																</td>
															</tr>
															<tr>
																<td align="center">
																	27.11.2019
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center">
														<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl10_LabelBekledigiGun">1</span>
													</td><td class="columnborder" align="center">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl10_Label3">0</span>
																</td>
															</tr>
															<tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl10_lblGizlilikTipAdi"></span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center" style="color:Red;">
														Evet
													</td><td class="columnborder" valign="top">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl10_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl10$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay</a>
													</td><td class="columnborder" valign="top" style="width:100px;">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl10_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl10$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala</a>
													</td>
						</tr><tr>
							<td class="columnborder" align="right" style="width:75px;">
														<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
															<tbody><tr>
																<td style="width: 33%; text-align: left">
																	<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl11_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
																</td>
																<td style="width: 33%; text-align: left">
																	
																</td>
																<td style="width: 33%; text-align: right">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl11_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">122447</span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl11_lblKonu" title="Büyükşehir Belediyesi.  (Naciye Layla CAV)" maxlength="200">Büyükşehir Belediyesi.  (Naciye Layla CAV)</span>
																</td>
															</tr>
															<tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl11_lblGidecegiYer" title="İstanbul&amp;nbsp;Büyükşehir&amp;nbsp;Belediye&amp;nbsp;Başkanlığına" maxlength="200">İstanbul&nbsp;Büyükşehir&nbsp;Belediye&nbsp;Başkanlığına</span>

																	

																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	İstanbul Valiliği İstanbul İdare ve Denetim Müdürlüğü
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl11_labelKisiyeOzelUzunAd">-</span>
																</td>
															</tr>
															<tr>
																<td align="center">
																	27.11.2019
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center">
														<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl11_LabelBekledigiGun">1</span>
													</td><td class="columnborder" align="center">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl11_Label3">0</span>
																</td>
															</tr>
															<tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl11_lblGizlilikTipAdi"></span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center" style="color:Red;">
														Evet
													</td><td class="columnborder" valign="top">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl11_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl11$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay</a>
													</td><td class="columnborder" valign="top" style="width:100px;">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl11_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl11$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala</a>
													</td>
						</tr><tr class="alternatifrow">
							<td class="columnborder" align="right" style="width:75px;">
														<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
															<tbody><tr>
																<td style="width: 33%; text-align: left">
																	<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl12_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
																</td>
																<td style="width: 33%; text-align: left">
																	
																</td>
																<td style="width: 33%; text-align: right">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl12_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">122449</span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl12_lblKonu" title="Büyükşehir Belediyesi.  (A. Ajda GÖNÜLTAŞ)" maxlength="200">Büyükşehir Belediyesi.  (A. Ajda GÖNÜLTAŞ)</span>
																</td>
															</tr>
															<tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl12_lblGidecegiYer" title="İstanbul&amp;nbsp;Büyükşehir&amp;nbsp;Belediye&amp;nbsp;Başkanlığına" maxlength="200">İstanbul&nbsp;Büyükşehir&nbsp;Belediye&nbsp;Başkanlığına</span>

																	

																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	İstanbul Valiliği İstanbul İdare ve Denetim Müdürlüğü
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl12_labelKisiyeOzelUzunAd">-</span>
																</td>
															</tr>
															<tr>
																<td align="center">
																	27.11.2019
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center">
														<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl12_LabelBekledigiGun">1</span>
													</td><td class="columnborder" align="center">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl12_Label3">0</span>
																</td>
															</tr>
															<tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl12_lblGizlilikTipAdi"></span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center" style="color:Red;">
														Evet
													</td><td class="columnborder" valign="top">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl12_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl12$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay</a>
													</td><td class="columnborder" valign="top" style="width:100px;">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl12_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl12$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala</a>
													</td>
						</tr><tr>
							<td class="columnborder" align="right" style="width:75px;">
														<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
															<tbody><tr>
																<td style="width: 33%; text-align: left">
																	<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl13_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
																</td>
																<td style="width: 33%; text-align: left">
																	
																</td>
																<td style="width: 33%; text-align: right">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl13_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">122452</span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl13_lblKonu" title="Kadir TOPBAŞ" maxlength="200">Kadir TOPBAŞ</span>
																</td>
															</tr>
															<tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl13_lblGidecegiYer" title="İstanbul&amp;nbsp;Büyükşehir&amp;nbsp;Belediye&amp;nbsp;Başkanlığına" maxlength="200">İstanbul&nbsp;Büyükşehir&nbsp;Belediye&nbsp;Başkanlığına</span>

																	

																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	İstanbul Valiliği İstanbul İdare ve Denetim Müdürlüğü
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl13_labelKisiyeOzelUzunAd">-</span>
																</td>
															</tr>
															<tr>
																<td align="center">
																	27.11.2019
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center">
														<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl13_LabelBekledigiGun">1</span>
													</td><td class="columnborder" align="center">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl13_Label3">0</span>
																</td>
															</tr>
															<tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl13_lblGizlilikTipAdi"></span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center" style="color:Red;">
														Evet
													</td><td class="columnborder" valign="top">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl13_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl13$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay</a>
													</td><td class="columnborder" valign="top" style="width:100px;">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl13_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl13$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala</a>
													</td>
						</tr><tr class="alternatifrow">
							<td class="columnborder" align="right" style="width:75px;">
														<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
															<tbody><tr>
																<td style="width: 33%; text-align: left">
																	<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl14_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
																</td>
																<td style="width: 33%; text-align: left">
																	
																</td>
																<td style="width: 33%; text-align: right">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl14_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">122612</span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl14_lblKonu" title="İHA Uçuş İzni Talebi" maxlength="200">İHA Uçuş İzni Talebi</span>
																</td>
															</tr>
															<tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl14_lblGidecegiYer" title="İl&amp;nbsp;Emniyet&amp;nbsp;Müdürlüğüne<br>(İnsansız&amp;nbsp;Hava&amp;nbsp;Araçları&amp;nbsp;(İha)&amp;nbsp;Büro&amp;nbsp;Amirliği&amp;nbsp;)" maxlength="200">İl&nbsp;Emniyet&nbsp;Müdürlüğüne<br>(İnsansız&nbsp;Hava&nbsp;Araçları&nbsp;(İha)&nbsp;Büro&nbsp;Amirliği&nbsp;)</span>

																	

																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	İstanbul Valiliği İstanbul İl Yazı İşleri Müdürlüğü
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl14_labelKisiyeOzelUzunAd">Günlüdür</span>
																</td>
															</tr>
															<tr>
																<td align="center">
																	27.11.2019
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center">
														<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl14_LabelBekledigiGun">1</span>
													</td><td class="columnborder" align="center">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl14_Label3">0</span>
																</td>
															</tr>
															<tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl14_lblGizlilikTipAdi"></span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center" style="color:Red;">
														Evet
													</td><td class="columnborder" valign="top">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl14_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl14$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay</a>
													</td><td class="columnborder" valign="top" style="width:100px;">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl14_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl14$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala</a>
													</td>
						</tr><tr>
							<td class="columnborder" align="right" style="width:75px;">
														<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
															<tbody><tr>
																<td style="width: 33%; text-align: left">
																	<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl15_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
																</td>
																<td style="width: 33%; text-align: left">
																	
																</td>
																<td style="width: 33%; text-align: right">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl15_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">122753</span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl15_lblKonu" title="Toplantı" maxlength="200">Toplantı</span>
																</td>
															</tr>
															<tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl15_lblGidecegiYer" title="Sayin&amp;nbsp;İsmail&amp;nbsp;Şanlı&amp;nbsp;<br>istanbul&amp;nbsp;Havalimanı&amp;nbsp;Mülki&amp;nbsp;İdare&amp;nbsp;Amiri, Sayın&amp;nbsp;Mustafa&amp;nbsp;Çalışkan&amp;nbsp;&amp;nbsp;<br>il&amp;nbsp;Emniyet&amp;nbsp;Müdürü, Sayın&amp;nbsp;Tuğg.&amp;nbsp;Nuh&amp;nbsp;Köroğlu&amp;nbsp;<br>il&amp;nbsp;Jandarma&amp;nbsp;Komutanı, Sayın&amp;nbsp;Timur&amp;nbsp;Alp&amp;nbsp;Bayrak&amp;nbsp;<br>dhmi&amp;nbsp;Başmüdürü, Sayın&amp;nbsp;Yalçın&amp;nbsp;Özden&amp;nbsp;<br>istanbul&amp;nbsp;Gümrük&amp;nbsp;Ve&amp;nbsp;Dış&amp;nbsp;Ticaret&amp;nbsp;Bölge&amp;nbsp;Müdürü, Sayın&amp;nbsp;Fatih&amp;nbsp;Güniçen&amp;nbsp;<br>sivil&amp;nbsp;Havacılık&amp;nbsp;İstanbul&amp;nbsp;Temsilcisi, Sayın&amp;nbsp;Recep&amp;nbsp;Batu&amp;nbsp;<br>il&amp;nbsp;Göç&amp;nbsp;İdaresi&amp;nbsp;Müdürü" maxlength="200">Sayın&nbsp;İsmail&nbsp;Şanlı&nbsp;<br>istanbul&nbsp;Havalimanı&nbsp;Mülki&nbsp;İdare&nbsp;Amiri, Sayın&nbsp;Mustafa&nbsp;Çalışkan&nbsp;&nbsp;<br>il&nbsp;Emniyet&nbsp;Müdürü, Sayın&nbsp;Tuğg.&nbsp;Nuh&nbsp;Köroğlu&nbsp;<br>il&nbsp;Jandarma&nbsp;Komutanı, Sayın&nbsp;Timur&nbsp;Alp&nbsp;Bayrak&nbsp;<br>dhmi&nbsp;Başmüdürü, Sayın&nbsp;Yalçın&nbsp;Özden&nbsp;<br>istanbul&nbsp;Gümrük&nbsp;Ve&nbsp;Dış&nbsp;Ticaret&nbsp;Bölge&nbsp;Müdürü, Sayın&nbsp;Fatih&nbsp;Güniçen&nbsp;<br>sivil&nbsp;Havacılık&nbsp;İstanbul&nbsp;Temsilcisi, Sayın&nbsp;Recep&nbsp;Batu&nbsp;<br>il&nbsp;Göç&nbsp;İdaresi&nbsp;Müdürü</span>

																	

																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	İstanbul Valiliği İstanbul Özel Kalem Müdürlüğü
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl15_labelKisiyeOzelUzunAd">Dağıtımlı</span>
																</td>
															</tr>
															<tr>
																<td align="center">
																	27.11.2019
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center">
														<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl15_LabelBekledigiGun">1</span>
													</td><td class="columnborder" align="center">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl15_Label3">0</span>
																</td>
															</tr>
															<tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl15_lblGizlilikTipAdi"></span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center" style="color:Red;">
														Evet
													</td><td class="columnborder" valign="top">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl15_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl15$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay</a>
													</td><td class="columnborder" valign="top" style="width:100px;">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl15_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl15$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala</a>
													</td>
						</tr><tr class="alternatifrow">
							<td class="columnborder" align="right" style="width:75px;">
														<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
															<tbody><tr>
																<td style="width: 33%; text-align: left">
																	<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl16_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
																</td>
																<td style="width: 33%; text-align: left">
																	
																</td>
																<td style="width: 33%; text-align: right">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl16_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">122882</span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl16_lblKonu" title="Sultangazi Beld. 2019 Yılı Kurban Satışı Hk." maxlength="200">Sultangazi Beld. 2019 Yılı Kurban Satışı Hk.</span>
																</td>
															</tr>
															<tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl16_lblGidecegiYer" title="Sultangazi&amp;nbsp;Belediye&amp;nbsp;Başkanlığına<br>(Özel&amp;nbsp;Kalem&amp;nbsp;Müdürlüğü)" maxlength="200">Sultangazi&nbsp;Belediye&nbsp;Başkanlığına<br>(Özel&nbsp;Kalem&nbsp;Müdürlüğü)</span>

																	

																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	İstanbul Valiliği İstanbul İdare ve Denetim Müdürlüğü
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl16_labelKisiyeOzelUzunAd">-</span>
																</td>
															</tr>
															<tr>
																<td align="center">
																	28.11.2019
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center">
														<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl16_LabelBekledigiGun">0</span>
													</td><td class="columnborder" align="center">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl16_Label3">0</span>
																</td>
															</tr>
															<tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl16_lblGizlilikTipAdi"></span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center" style="color:Red;">
														Evet
													</td><td class="columnborder" valign="top">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl16_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl16$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay</a>
													</td><td class="columnborder" valign="top" style="width:100px;">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl16_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl16$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala</a>
													</td>
						</tr><tr>
							<td class="columnborder" align="right" style="width:75px;">
														<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
															<tbody><tr>
																<td style="width: 33%; text-align: left">
																	<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl17_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
																</td>
																<td style="width: 33%; text-align: left">
																	
																</td>
																<td style="width: 33%; text-align: right">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl17_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">122884</span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl17_lblKonu" title="Rapora İtiraz Hk (Av. Engin Cesur UYSAL)" maxlength="200">Rapora İtiraz Hk (Av. Engin Cesur UYSAL)</span>
																</td>
															</tr>
															<tr>
																<td align="left">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl17_lblGidecegiYer" title="Çevre&amp;nbsp;Ve&amp;nbsp;Şehircilik&amp;nbsp;İl&amp;nbsp;Müdürlüğüne, Av.&amp;nbsp;Engin&amp;nbsp;Cesur&amp;nbsp;Uysal&amp;nbsp;<br>alemdağ&amp;nbsp;Cad.&amp;nbsp;<br>solakoğlu&amp;nbsp;İş&amp;nbsp;Merkezi&amp;nbsp;<br>no:186&amp;nbsp;A-17&amp;nbsp;Ümraniye/istanbul" maxlength="200">Çevre&nbsp;Ve&nbsp;Şehircilik&nbsp;İl&nbsp;Müdürlüğüne, Av.&nbsp;Engin&nbsp;Cesur&nbsp;Uysal&nbsp;<br>alemdağ&nbsp;Cad.&nbsp;<br>solakoğlu&nbsp;İş&nbsp;Merkezi&nbsp;<br>no:186&nbsp;A-17&nbsp;Ümraniye/istanbul</span>

																	

																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="left">
																	İstanbul Valiliği İstanbul İdare ve Denetim Müdürlüğü
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl17_labelKisiyeOzelUzunAd">Dağıtımlı</span>
																</td>
															</tr>
															<tr>
																<td align="center">
																	28.11.2019
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center">
														<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl17_LabelBekledigiGun">0</span>
													</td><td class="columnborder" align="center">
														<table width="100%" cellpadding="0" cellspacing="0">
															<tbody><tr>
																<td align="center">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl17_Label3">0</span>
																</td>
															</tr>
															<tr>
																<td align="center" style="color: Red">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl17_lblGizlilikTipAdi"></span>
																</td>
															</tr>
														</tbody></table>
													</td><td class="columnborder" align="center" style="color:Red;">
														Evet
													</td><td class="columnborder" valign="top">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl17_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl17$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay</a>
													</td><td class="columnborder" valign="top" style="width:100px;">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl17_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl17$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala</a>
													</td>
						</tr>
					</tbody></table>
				</div>
									</td>
			</tr>
			<tr>
				<td>
										<input type="image" name="ctl00$ctl00$cph1$cphGelenGiden$LinkButtonTopluPostala$UcImgButtonOnay" id="ctl00_ctl00_cph1_cphGelenGiden_LinkButtonTopluPostala_UcImgButtonOnay" title="Seçtiğiniz kağıt ortamında gitmeyecek evrakları postalar" src="../../App_Themes/Main/Images/Buttons/btnsecilievraklaripostala.jpg" onclick="return CheckValidationUcImgButtonOnay(this);WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$LinkButtonTopluPostala$UcImgButtonOnay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, false))" style="border-width:0px;display:none;">
<input type="submit" name="ctl00$ctl00$cph1$cphGelenGiden$LinkButtonTopluPostala$ButtonHidden" value="" onclick="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$LinkButtonTopluPostala$ButtonHidden&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, false))" id="ctl00_ctl00_cph1_cphGelenGiden_LinkButtonTopluPostala_ButtonHidden" style="display: none;">

<input type="hidden" name="ctl00$ctl00$cph1$cphGelenGiden$LinkButtonTopluPostala$HiddenFieldImgBtnOnayVldgrp" id="ctl00_ctl00_cph1_cphGelenGiden_LinkButtonTopluPostala_HiddenFieldImgBtnOnayVldgrp">
<input type="hidden" name="ctl00$ctl00$cph1$cphGelenGiden$LinkButtonTopluPostala$HiddenFieldImgBtnOnayCausVld" id="ctl00_ctl00_cph1_cphGelenGiden_LinkButtonTopluPostala_HiddenFieldImgBtnOnayCausVld">

<script type="text/javascript">

    var submitcount = 0;

    function GetHiddenFieldsAsObjectUcImgButtonOnay(sender, hdnFld) {
        var sndrID = sender.id;
        var parca = sndrID.split('_');
        var kntrl = parca[parca.length - 1];
        var dizin = sndrID.replace(kntrl, "");
        var hdnName = dizin + hdnFld;
        var hdnObj = document.getElementsByName(hdnName)[0];
        return hdnObj;
    }
    function CheckValidationUcImgButtonOnay(sender) {
        var objVldGrp = GetHiddenFieldsAsObjectUcImgButtonOnay(sender, 'HiddenFieldImgBtnOnayVldgrp');
        var objCausVld = GetHiddenFieldsAsObjectUcImgButtonOnay(sender, 'HiddenFieldImgBtnOnayCausVld');

        if (objVldGrp.value != '') return DisableSubmitUcImgButtonOnayWithVldGrp(sender, objVldGrp.value);
        if (objCausVld.value == 'True' || objCausVld.value == '') return DisableSubmitUcImgButtonOnay(sender);
        return CheckSubmitUcImgButtonOnay(sender);
    }

    function DisableSubmitUcImgButtonOnayWithVldGrp(sender, vldGrpName) {

        if (typeof (Page_ClientValidate) == 'function') {
            if (Page_ClientValidate(vldGrpName) == true) {
                return CheckSubmitUcImgButtonOnay(sender);
            }
            else {
                return false;
            }
        }
        else {
            return CheckSubmitUcImgButtonOnay(sender);
        }
    }
    
    function DisableSubmitUcImgButtonOnay(sender) {        
        if (typeof (Page_ClientValidate) == 'function') {
            if (Page_ClientValidate() == true) {
                return CheckSubmitUcImgButtonOnay(sender);
            }
            else {
                return false;
            }
        }
        else {
            return CheckSubmitUcImgButtonOnay(sender);
        }
    }

    function CheckSubmitUcImgButtonOnay(sender) {
        var ImageConfirmButton = $find('ImageConfirmButton');

        if (submitcount > 0) {
            alert('İşleminiz yapılıyor, lütfen bekleyiniz !');
            return false;
        }

        if (ImageConfirmButton._displayConfirmDialog()) {
            if (submitcount == 0) {
                submitcount++;
                return true;
            }
        }
        else {
            return false;
        }
    }

    function LoadAfterAjaxHandler() {
        Sys.WebForms.PageRequestManager.getInstance().add_endRequest(EndRequestHandler);
    }

    function EndRequestHandler(sender, eArgs) {
        if (eArgs.get_error() == null) {
            submitcount = 0;
        }
    } 
    
</script>


									</td>
			</tr>
		</tbody></table>
		
						</td>
					</tr>
				</tbody></table>
			</td>
	</tr>
</tbody></table>"""

    sk1="""<table id="ctl00_ctl00_cph1_cphGelenGiden_TablePostalanmayiBekleyenEvraklarGenel" style="width: 100%">
                            <tbody>
                             <tr>
                              <td align="center" style="width: 100%">
                               <div>
                                <table border="1" cellpadding="4" cellspacing="0" class="grid1" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen" rules="all" style="width:100%;border-collapse:collapse;">
                                 <tbody>
                                  <tr>
								  <th scope="col">
                                    <table>
                                     <tbody>
                                      <tr>
                                       <td>
                                        <img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_arrowEvrakNo" src="../../App_Themes/Main/Images/Ikonlar/yukariokth.jpg" style="border-width:0px;">
                                       </td>
                                       <td>
                                        <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl02$LinkButtonEvrakNo&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_LinkButtonEvrakNo" jqueryclass="jLinkButton">
                                         Evrak No
                                        </a>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </th>
                                   <th scope="col">
                                    <table>
                                     <tbody>
                                      <tr>
                                       <td>
                                       </td>
                                       <td>
                                        <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl02$LinkButtonKonu&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_LinkButtonKonu" jqueryclass="jLinkButton">
                                         Konu/Gideceği Yer
                                        </a>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </th>
                                   <th scope="col">
                                    <table>
                                     <tbody>
                                      <tr>
                                       <td>
                                       </td>
                                       <td>
                                        <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl02$LinkButtonHazirlayanTeskilatUzunAd&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_LinkButtonHazirlayanTeskilatUzunAd" jqueryclass="jLinkButton">
                                         Birimi
                                        </a>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </th>
                                   <th scope="col">
                                    <table>
                                     <tbody>
                                      <tr>
                                       <td>
                                       </td>
                                       <td>
                                        <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl02$LinkButtonEvrakTar&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_LinkButtonEvrakTar" jqueryclass="jLinkButton">
                                         Kişiye Özel Durum/Tarih
                                        </a>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </th>
                                   <th scope="col">
                                    <table>
                                     <tbody>
                                      <tr>
                                       <td>
                                       </td>
                                       <td>
                                        <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl02$LinkButtonBekledigiGun&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_LinkButtonBekledigiGun" jqueryclass="jLinkButton">
                                         Beklediği Gün
                                        </a>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </th>
                                   <th scope="col">
                                    <table>
                                     <tbody>
                                      <tr>
                                       <td>
                                       </td>
                                       <td>
                                        <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl02$LinkButtonMiat&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl02_LinkButtonMiat" jqueryclass="jLinkButton">
                                         Miat
                                        </a>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </th>
                                   <th scope="col">
                                    Kağıt Ortamında Gidecek Mi?
                                   </th>
                                   <th scope="col">
                                   </th>
                                   <th scope="col">
                                   </th>
                                  </tr>
								  <tr>							
<td class="columnborder" align="right" style="width:75px;">
														
<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
															
<tbody>
<tr>
																
<td style="width: 33%; text-align: left">
																	
<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
																
</td>
																
<td style="width: 33%; text-align: left">
																	
																
</td>
																
<td style="width: 33%; text-align: right">
																	
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">122445
</span>
																
</td>
															
</tr>
														
</tbody>
</table>
													
</td>
<td class="columnborder">
														
<table width="100%" cellpadding="0" cellspacing="0">
															
<tbody>
<tr>
																
<td align="left">
																	
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_lblKonu" title="Büyükşeir Belediyesi.  (Hüsnü YURTAŞAN)" maxlength="200">Büyükşeir Belediyesi.  (Hüsnü YURTAŞAN)
</span>
																
</td>
															
</tr>
															
<tr>
																
<td align="left">
																	
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_lblGidecegiYer" title="İstanbul&amp;nbsp;Büyükşehir&amp;nbsp;Belediye&amp;nbsp;Başkanlığına" maxlength="200">İstanbul&nbsp;Büyükşehir&nbsp;Belediye&nbsp;Başkanlığına
</span>

																	

																
</td>
															
</tr>
														
</tbody>
</table>
													
</td>
<td class="columnborder">
														
<table width="100%" cellpadding="0" cellspacing="0">
															
<tbody>
<tr>
																
<td align="left">
																	İstanbul Valiliği İstanbul İdare ve Denetim Müdürlüğü
																
</td>
															
</tr>
														
</tbody>
</table>
													
</td>
<td class="columnborder">
														
<table width="100%" cellpadding="0" cellspacing="0">
															
<tbody>
<tr>
																
<td align="center" style="color: Red">
																	
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_labelKisiyeOzelUzunAd">-
</span>
																
</td>
															
</tr>
															
<tr>
																
<td align="center">
																	27.11.2019
																
</td>
															
</tr>
														
</tbody>
</table>
													
</td>
<td class="columnborder" align="center">
														
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_LabelBekledigiGun">1
</span>
													
</td>
<td class="columnborder" align="center">
														
<table width="100%" cellpadding="0" cellspacing="0">
															
<tbody>
<tr>
																
<td align="center">
																	
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_Label3">0
</span>
																
</td>
															
</tr>
															
<tr>
																
<td align="center" style="color: Red">
																	
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_lblGizlilikTipAdi">
</span>
																
</td>
															
</tr>
														
</tbody>
</table>
													
</td>
<td class="columnborder" align="center" style="color:Red;">
														Evet
													
</td>
<td class="columnborder" valign="top">
														
<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl09$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay
</a>
													
</td>
<td class="columnborder" valign="top" style="width:100px;">
														
<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl09_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl09$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala
</a>
													
</td>
						</tr>
						<tr>
							
<td class="columnborder" align="right" style="width:75px;">
														
<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
															
<tbody>
<tr>
																
<td style="width: 33%; text-align: left">
																	
<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
																
</td>
																
<td style="width: 33%; text-align: left">
																	
																
</td>
																
<td style="width: 33%; text-align: right">
																	
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">122207
</span>
																
</td>
															
</tr>
														
</tbody>
</table>
													
</td>
<td class="columnborder">
														
<table width="100%" cellpadding="0" cellspacing="0">
															
<tbody>
<tr>
																
<td align="left">
																	
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_lblKonu" title="Sarıyer İstinye Muhtarı hk." maxlength="200">Sarıyer İstinye Muhtarı hk.
</span>
																
</td>
															
</tr>
															
<tr>
																
<td align="left">
																	
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_lblGidecegiYer" title="Sarıyer&amp;nbsp;Kaymakamlığına, Mikail&amp;nbsp;Atakoru&amp;nbsp;
<br>şehit&amp;nbsp;Halil&amp;nbsp;İbrahim&amp;nbsp;Sok.&amp;nbsp;No:101&amp;nbsp;İstinye/sarıyer/istanbul
<br>
<br>(Ek&amp;nbsp;Konulmadı)" maxlength="200">Sarıyer&nbsp;Kaymakamlığına, Mikail&nbsp;Atakoru&nbsp;
<br>şehit&nbsp;Halil&nbsp;İbrahim&nbsp;Sok.&nbsp;No:101&nbsp;İstinye/sarıyer/istanbul
<br>
<br>(Ek&nbsp;Konulmadı)
</span>

																	

																
</td>
															
</tr>
														
</tbody>
</table>
													
</td>
<td class="columnborder">
														
<table width="100%" cellpadding="0" cellspacing="0">
															
<tbody>
<tr>
																
<td align="left">
																	İstanbul Valiliği İstanbul İdare ve Denetim Müdürlüğü
																
</td>
															
</tr>
														
</tbody>
</table>
													
</td>
<td class="columnborder">
														
<table width="100%" cellpadding="0" cellspacing="0">
															
<tbody>
<tr>
																
<td align="center" style="color: Red">
																	
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_labelKisiyeOzelUzunAd">Dağıtımlı
</span>
																
</td>
															
</tr>
															
<tr>
																
<td align="center">
																	27.11.2019
																
</td>
															
</tr>
														
</tbody>
</table>
													
</td>
<td class="columnborder" align="center">
														
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_LabelBekledigiGun">1
</span>
													
</td>
<td class="columnborder" align="center">
														
<table width="100%" cellpadding="0" cellspacing="0">
															
<tbody>
<tr>
																
<td align="center">
																	
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_Label3">0
</span>
																
</td>
															
</tr>
															
<tr>
																
<td align="center" style="color: Red">
																	
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_lblGizlilikTipAdi">
</span>
																
</td>
															
</tr>
														
</tbody>
</table>
													
</td>
<td class="columnborder" align="center" style="color:Red;">
														Evet
													
</td>
<td class="columnborder" valign="top">
														
<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl05$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay
</a>
													
</td>
<td class="columnborder" valign="top" style="width:100px;">
														
<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl05_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl05$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala
</a>
													
</td>
						
</tr>
								  
								  
								  <tr>
							
<td class="columnborder" align="right" style="width:75px;">
														
<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
															
<tbody>
<tr>
																
<td style="width: 33%; text-align: left">
																	
<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
																
</td>
																
<td style="width: 33%; text-align: left">
																	
																
</td>
																
<td style="width: 33%; text-align: right">
																	
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">122443
</span>
																
</td>
															
</tr>
														
</tbody>
</table>
													
</td>
<td class="columnborder">
														
<table width="100%" cellpadding="0" cellspacing="0">
															
<tbody>
<tr>
																
<td align="left">
																	
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_lblKonu" title="Büyükşehir Belediyesi.  (Sr.No:2018/119372)" maxlength="200">Büyükşehir Belediyesi.  (Sr.No:2018/119372)
</span>
																
</td>
															
</tr>
															
<tr>
																
<td align="left">
																	
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_lblGidecegiYer" title="İstanbul&amp;nbsp;Büyükşehir&amp;nbsp;Belediye&amp;nbsp;Başkanlığına" maxlength="200">İstanbul&nbsp;Büyükşehir&nbsp;Belediye&nbsp;Başkanlığına
</span>

																	

																
</td>
															
</tr>
														
</tbody>
</table>
													
</td>
<td class="columnborder">
														
<table width="100%" cellpadding="0" cellspacing="0">
															
<tbody>
<tr>
																
<td align="left">
																	İstanbul Valiliği İstanbul İdare ve Denetim Müdürlüğü
																
</td>
															
</tr>
														
</tbody>
</table>
													
</td>
<td class="columnborder">
														
<table width="100%" cellpadding="0" cellspacing="0">
															
<tbody>
<tr>
																
<td align="center" style="color: Red">
																	
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_labelKisiyeOzelUzunAd">-
</span>
																
</td>
															
</tr>
															
<tr>
																
<td align="center">
																	27.11.2019
																
</td>
															
</tr>
														
</tbody>
</table>
													
</td>
<td class="columnborder" align="center">
														
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_LabelBekledigiGun">1
</span>
													
</td>
<td class="columnborder" align="center">
														
<table width="100%" cellpadding="0" cellspacing="0">
															
<tbody>
<tr>
																
<td align="center">
																	
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_Label3">0
</span>
																
</td>
															
</tr>
															
<tr>
																
<td align="center" style="color: Red">
																	
<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_lblGizlilikTipAdi">
</span>
																
</td>
															
</tr>
														
</tbody>
</table>
													
</td>
<td class="columnborder" align="center" style="color:Red;">
														Evet
													
</td>
<td class="columnborder" valign="top">
														
<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl07$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay
</a>
													
</td>
<td class="columnborder" valign="top" style="width:100px;">
														
<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl07_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl07$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala
</a>
													
</td>
						
</tr>
								  
								  
								  
								  
								  
								  
								  
								  
								  <tr>
									<td class="columnborder" align="right" style="width:75px;">
										<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
											<tbody><tr>
												<td style="width: 33%; text-align: left">
													<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
												</td>
												<td style="width: 33%; text-align: left">

												</td>
												<td style="width: 33%; text-align: right">
													<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">120474</span>
												</td>
											</tr>
										</tbody></table>
									</td>
									<td class="columnborder">
										<table width="100%" cellpadding="0" cellspacing="0">
											<tbody><tr>
												<td align="left">
													<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lblKonu" title="Hüseyin YEŞLDAĞ  Nes Formu" maxlength="200">Hüseyin YEŞLDAĞ  Nes Formu</span>
												</td>
											</tr>
											<tr>
												<td align="left">
													<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lblGidecegiYer" title="İçişleri&amp;nbsp;Bakanlığına&amp;nbsp;<br>(Bilgi&amp;nbsp;İşlem&amp;nbsp;Dairesi&amp;nbsp;Başkanlığı), Tübitak&amp;nbsp;Yerleşkesi&amp;nbsp;<br>kamu&amp;nbsp;Sertifikasyon&amp;nbsp;Merkezi&amp;nbsp;<br>yeni&amp;nbsp;İdari&amp;nbsp;Bina&amp;nbsp;Pk&amp;nbsp;74&amp;nbsp;<br>gebze&amp;nbsp;41470&amp;nbsp;Kocaeli" maxlength="200">İçişleri&nbsp;Bakanlığına&nbsp;<br>(Bilgi&nbsp;İşlem&nbsp;Dairesi&nbsp;Başkanlığı), Tübitak&nbsp;Yerleşkesi&nbsp;<br>kamu&nbsp;Sertifikasyon&nbsp;Merkezi&nbsp;<br>yeni&nbsp;İdari&nbsp;Bina&nbsp;Pk&nbsp;74&nbsp;<br>gebze&nbsp;41470&nbsp;Kocaeli</span>



												</td>
											</tr>
										</tbody></table>
									</td>
									<td class="columnborder">
										<table width="100%" cellpadding="0" cellspacing="0">
											<tbody><tr>
												<td align="left">
													İstanbul Valiliği İstanbul Bilgi İşlem Şube Müdürlüğü
												</td>
											</tr>
										</tbody></table>
									</td>
									<td class="columnborder">
										<table width="100%" cellpadding="0" cellspacing="0">
											<tbody><tr>
												<td align="center" style="color: Red">
													<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_labelKisiyeOzelUzunAd">Dağıtımlı</span>
												</td>
											</tr>
											<tr>
												<td align="center">
													25.11.2019
												</td>
											</tr>
										</tbody></table>
									</td>
									<td class="columnborder" align="center">
										<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_LabelBekledigiGun">1</span>
									</td>
									<td class="columnborder" align="center">
										<table width="100%" cellpadding="0" cellspacing="0">
											<tbody><tr>
												<td align="center">
													<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_Label3">0</span>
												</td>
											</tr>
											<tr>
												<td align="center" style="color: Red">
													<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lblGizlilikTipAdi"></span>
												</td>
											</tr>
										</tbody></table>
									</td>
									<td class="columnborder" align="center" style="color:Red;">
										Evet
									</td>
									<td class="columnborder" valign="top">
										<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lnkDetay" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl03$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Detay</a>
									</td>
									<td class="columnborder" valign="top" style="width:100px;">
														<a id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lnkHizliPostala" jqueryclass="jLinkButton" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl03$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Teslim Al ve Postala</a>
													</td>
								</tr>
								  <tr>
                                   <td align="right" class="columnborder" style="width:75px;">
                                    <table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
                                     <tbody>
                                      <tr>
                                       <td style="width: 33%; text-align: left">
                                        <img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_imageImzalimi" src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;" title="Bu evrak sayısal imzalıdır.">
                                       </td>
                                       <td style="width: 33%; text-align: left">
                                       </td>
                                       <td style="width: 33%; text-align: right">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">
                                         114183
                                        </span>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td class="columnborder">
                                    <table cellpadding="0" cellspacing="0" width="100%">
                                     <tbody>
                                      <tr>
                                       <td align="left">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lblKonu" maxlength="200" title="NES Başvuru Formları">
                                         NES Başvuru Formları
                                        </span>
                                       </td>
                                      </tr>
                                      <tr>
                                       <td align="left">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lblGidecegiYer" maxlength="200" title="İçişleri&amp;nbsp;Bakanlığına&amp;nbsp;<br>(Bilgi&amp;nbsp;İşlem&amp;nbsp;Dairesi&amp;nbsp;Başkanlığı), Tübitak&amp;nbsp;Yerleşkesi&amp;nbsp;Kamu&amp;nbsp;Sertifikasyon&amp;nbsp;Merkezi&amp;nbsp;Yeni&amp;nbsp;İdari&amp;nbsp;Bina&amp;nbsp;P.k.&amp;nbsp;74&amp;nbsp;Gebze&amp;nbsp;41470&amp;nbsp;Kocaeli">
                                         İçişleri&nbsp;Bakanlığına
                                         <br>
                                         (Bilgi&nbsp;İşlem&nbsp;Dairesi&nbsp;Başkanlığı), Tübitak&nbsp;Yerleşkesi&nbsp;Kamu&nbsp;Sertifikasyon&nbsp;Merkezi&nbsp;Yeni&nbsp;İdari&nbsp;Bina&nbsp;P.k.&nbsp;74&nbsp;Gebze&nbsp;41470&nbsp;Kocaeli
                                        </span>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td class="columnborder">
                                    <table cellpadding="0" cellspacing="0" width="100%">
                                     <tbody>
                                      <tr>
                                       <td align="left">
                                        İstanbul Valiliği İstanbul Bilgi İşlem Şube Müdürlüğü
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td class="columnborder">
                                    <table cellpadding="0" cellspacing="0" width="100%">
                                     <tbody>
                                      <tr>
                                       <td align="center" style="color: Red">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_labelKisiyeOzelUzunAd">
                                         Dağıtımlı
                                        </span>
                                       </td>
                                      </tr>
                                      <tr>
                                       <td align="center">
                                        11.11.2019
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td align="center" class="columnborder">
                                    <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_LabelBekledigiGun">
                                     2
                                    </span>
                                   </td>
                                   <td align="center" class="columnborder">
                                    <table cellpadding="0" cellspacing="0" width="100%">
                                     <tbody>
                                      <tr>
                                       <td align="center">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_Label3">
                                         0
                                        </span>
                                       </td>
                                      </tr>
                                      <tr>
                                       <td align="center" style="color: Red">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lblGizlilikTipAdi">
                                        </span>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td align="center" class="columnborder" style="color:Red;">
                                    Evet
                                   </td>
                                   <td class="columnborder" valign="top">
                                    <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl03$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lnkDetay" jqueryclass="jLinkButton">
                                     Detay
                                    </a>
                                   </td>
                                   <td class="columnborder" style="width:100px;" valign="top">
                                    <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl03$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_lnkHizliPostala" jqueryclass="jLinkButton">
                                     Teslim Al ve Postala
                                    </a>
                                   </td>
                                  </tr>
                                  <tr class="alternatifrow">
                                   <td align="right" class="columnborder" style="width:75px;">
                                    <table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
                                     <tbody>
                                      <tr>
                                       <td style="width: 33%; text-align: left">
                                        <img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_imageImzalimi" src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;" title="Bu evrak sayısal imzalıdır.">
                                       </td>
                                       <td style="width: 33%; text-align: left">
                                       </td>
                                       <td style="width: 33%; text-align: right">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">
                                         114187
                                        </span>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td class="columnborder">
                                    <table cellpadding="0" cellspacing="0" width="100%">
                                     <tbody>
                                      <tr>
                                       <td align="left">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_lblKonu" maxlength="200" title="Suna DEMİRCİ ve Erol Akdeniz' İn NES Başvuru Formu">
                                         Suna DEMİRCİ ve Erol Akdeniz' İn NES Başvuru Formu
                                        </span>
                                       </td>
                                      </tr>
                                      <tr>
                                       <td align="left">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_lblGidecegiYer" maxlength="200" title="İçişleri&amp;nbsp;Bakanlığına&amp;nbsp;<br>(Bilgi&amp;nbsp;İşlem&amp;nbsp;Dairesi&amp;nbsp;Başkanlığı), Tübitak&amp;nbsp;Yerleşkesi&amp;nbsp;<br>kamu&amp;nbsp;Sertifikasyon&amp;nbsp;Merkezi&amp;nbsp;<br>yeni&amp;nbsp;İdari&amp;nbsp;Bina&amp;nbsp;Pk&amp;nbsp;74&amp;nbsp;<br>gebze&amp;nbsp;41470&amp;nbsp;Kocaeli">
                                         İçişleri&nbsp;Bakanlığına
                                         <br>
                                         (Bilgi&nbsp;İşlem&nbsp;Dairesi&nbsp;Başkanlığı), Tübitak&nbsp;Yerleşkesi
                                         <br>
                                         kamu&nbsp;Sertifikasyon&nbsp;Merkezi
                                         <br>
                                         yeni&nbsp;İdari&nbsp;Bina&nbsp;Pk&nbsp;74
                                         <br>
                                         gebze&nbsp;41470&nbsp;Kocaeli
                                        </span>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td class="columnborder">
                                    <table cellpadding="0" cellspacing="0" width="100%">
                                     <tbody>
                                      <tr>
                                       <td align="left">
                                        İstanbul Valiliği İstanbul Bilgi İşlem Şube Müdürlüğü
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td class="columnborder">
                                    <table cellpadding="0" cellspacing="0" width="100%">
                                     <tbody>
                                      <tr>
                                       <td align="center" style="color: Red">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_labelKisiyeOzelUzunAd">
                                         Dağıtımlı
                                        </span>
                                       </td>
                                      </tr>
                                      <tr>
                                       <td align="center">
                                        11.11.2019
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td align="center" class="columnborder">
                                    <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_LabelBekledigiGun">
                                     2
                                    </span>
                                   </td>
                                   <td align="center" class="columnborder">
                                    <table cellpadding="0" cellspacing="0" width="100%">
                                     <tbody>
                                      <tr>
                                       <td align="center">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_Label3">
                                         0
                                        </span>
                                       </td>
                                      </tr>
                                      <tr>
                                       <td align="center" style="color: Red">
                                        <span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_lblGizlilikTipAdi">
                                        </span>
                                       </td>
                                      </tr>
                                     </tbody>
                                    </table>
                                   </td>
                                   <td align="center" class="columnborder" style="color:Red;">
                                    Evet
                                   </td>
                                   <td class="columnborder" valign="top">
                                    <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl04$lnkDetay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_lnkDetay" jqueryclass="jLinkButton">
                                     Detay
                                    </a>
                                   </td>
                                   <td class="columnborder" style="width:100px;" valign="top">
                                    <a href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$grvPostalanmayiBekleyen$ctl04$lnkHizliPostala&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))" id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl04_lnkHizliPostala" jqueryclass="jLinkButton">
                                     Teslim Al ve Postala
                                    </a>
                                   </td>
                                  </tr>
								  
								  
								  
								  
								  
								  
								  
								  
                                 </tbody>
                                </table>
                               </div>
                              </td>
                             </tr>
                             <tr>
                              <td>
                               <input id="ctl00_ctl00_cph1_cphGelenGiden_LinkButtonTopluPostala_UcImgButtonOnay" name="ctl00$ctl00$cph1$cphGelenGiden$LinkButtonTopluPostala$UcImgButtonOnay" onclick="return CheckValidationUcImgButtonOnay(this);WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$LinkButtonTopluPostala$UcImgButtonOnay&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, false))" src="../../App_Themes/Main/Images/Buttons/btnsecilievraklaripostala.jpg" style="border-width:0px;display:none;" title="Seçtiğiniz kağıt ortamında gitmeyecek evrakları postalar" type="image">
                               <input id="ctl00_ctl00_cph1_cphGelenGiden_LinkButtonTopluPostala_ButtonHidden" name="ctl00$ctl00$cph1$cphGelenGiden$LinkButtonTopluPostala$ButtonHidden" onclick="null" style="display: none;" type="submit" value="">
                               <input id="ctl00_ctl00_cph1_cphGelenGiden_LinkButtonTopluPostala_HiddenFieldImgBtnOnayVldgrp" name="ctl00$ctl00$cph1$cphGelenGiden$LinkButtonTopluPostala$HiddenFieldImgBtnOnayVldgrp" type="hidden">
                               <input id="ctl00_ctl00_cph1_cphGelenGiden_LinkButtonTopluPostala_HiddenFieldImgBtnOnayCausVld" name="ctl00$ctl00$cph1$cphGelenGiden$LinkButtonTopluPostala$HiddenFieldImgBtnOnayCausVld" type="hidden">
                               </script>
                              </td>
                             </tr>
                            </tbody>

                           </table>"""

    pst=Postala()
    evraklar=pst.getEvrakBilgileri(sk1)

    for e in evraklar:
        print(e)
    # print(evraklar)




