from bs4 import BeautifulSoup as bs


class Postala(bs):
    def __init__(self,*args,**kwargs):
        # bs.__init__(self,*args,**kwargs)
        self.postalanacakEvraksayisi=0


    def getPostalanacakEvrakSayisi(self,post_count):
        self.postalanacakEvraksayisi=post_count



    def getSourceCode(self,source_code):
        self.html_source=bs(source_code,'html.parser')
        self.posta_table=self.html_source.find('table',
                                          id='ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen')
        self.tbody=self.posta_table.find('tbody')
        self.tbody_head_row=self.tbody.tr
        self.all_table_header_th=self.tbody_head_row.find_all('th')

        self.EvrakNo=self.all_table_header_th[0].get_text()
        self.EvrakKonu=self.all_table_header_th[1].get_text().split('/')[0]
        self.EvrakGidecegiYer=self.all_table_header_th[1].get_text().split('/')[1]
        self.EvrakTarih=self.all_table_header_th[3].get_text().split('/')[1]
        print(f'{self.EvrakNo.strip()},{self.EvrakKonu.strip()},{self.EvrakGidecegiYer.strip()},{self.EvrakTarih.strip()}')
#########################evraks######################
        self.evraklar_tr=self.tbody_head_row.find_next_siblings('tr')#dizi olarak her bir evrakın tr satırını döndürür
        for evrak in self.evraklar_tr:
            self.evrak_all_td=evrak.find_all('td',class_='columnborder')
            i=0
            for evrak_td in self.evrak_all_td:
                if i==0:
                    EvrakNo=evrak_td.find('span',id='ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_LabelEvrakNo')
                    if EvrakNo != None:
                        self.evNo=EvrakNo.get_text(strip=True)
                        i+=1
                        continue
                elif i==1:
                    all_spans=evrak_td.find_all('span')
                    j=0 #2adet span olduğu için 2 kere döndüreceğiz
                    for span in all_spans:
                        if j==0:
                            self.evKonu=span.get('title')
                            # print(self.evKonu)
                            j+=1
                            continue
                        elif j==1:
                            self.evGidYer=span.get_text(strip=True)
                            # print(self.evGidYer)
                            j=0
                            break
                    i+=1
                    continue
                elif i==3:
                    evTarih=evrak_td.get_text(strip=True)
                    self.evTar=evTarih.replace('Dağıtımlı','')
                    # print(self.evTar)
                i+=1
            print(f'Evrakno:{self.evNo},Evrak Konu:{self.evKonu},Evrak gideceği yer:{self.evGidYer},Tarih:{self.evTar}')











            # # print(EvrakNo,EvrakKonu,EvrakGidecegiYer)
            # if EvrakNo!=None:
            #     self.evNo=EvrakNo.get_text()
            #     print(self.evNo)
            #     continue
            # elif EvrakKonu!=None:
            #     self.evKonu=EvrakKonu.get('title')  # .get_text(strip=True)
            #     print(self.evKonu)
            #     continue
            # elif EvrakGidecegiYer!=None:
            #     self.evGidYer=EvrakGidecegiYer.get_text()
            #     print(self.evGidYer)
            # elif evrak_td.get_text(strip=True)=='İstanbul Valiliği İstanbul Bilgi İşlem Şube Müdürlüğü':
            #     continue
            # else:
            #     self.evTarih=evrak_td.get_text(strip=True)
            #     print(self.evTarih.replace('Dağıtımlı',''))
            # i+=1
            # if i==3:break



if __name__ == '__main__':
    sk="""
    <table id="ctl00_ctl00_cph1_cphGelenGiden_TablePostalanmayiBekleyenEvraklarGenel" style="width: 100%">
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

    pst=Postala()
    pst.getSourceCode(sk)




