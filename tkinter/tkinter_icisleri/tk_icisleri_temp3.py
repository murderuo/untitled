from bs4 import BeautifulSoup as bs



html="""<td class="columnborder" align="right" style="width:75px;">
														<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%">
															<tbody><tr>
																<td style="width: 33%; text-align: left">
																	<img id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_imageImzalimi" title="Bu evrak sayısal imzalıdır." src="../../App_Themes/Main/Images/Ikonlar/eimzaikon.jpg" style="border-width:0px;">
																</td>
																<td style="width: 33%; text-align: left">
																	
																</td>
																<td style="width: 33%; text-align: right">
																	<span id="ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_LabelEvrakNo" style="color:Red;font-size:10pt;font-weight:bold;">115485</span>
																</td>
															</tr>
														</tbody></table>
													</td>"""

code=bs(html,'html.parser')
span=code.find('span',id='ctl00_ctl00_cph1_cphGelenGiden_grvPostalanmayiBekleyen_ctl03_LabelEvrakNo')
print(span.get_text())
