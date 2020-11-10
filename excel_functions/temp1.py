import xlsxwriter

# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, 'turkish')
# now=time.strftime('%x')
#
# print(now)


workbook = xlsxwriter.Workbook('temps.xlsx')
worksheet = workbook.add_worksheet()

cell_format = workbook.add_format()
# cell_format.set_center_across()

cell_format.set_text_wrap()                       ##metni kaydır

yatay_hucre_center=workbook.add_format()
yatay_hucre_center.set_align('center') #yatayda ortala

dikey_hucre_center=workbook.add_format()
dikey_hucre_center.set_align('vcenter') #dikeyde ortala
worksheet.write(0, 0, "Some long text to wrap in a cell", cell_format)

# worksheet.merge_range('B3:D4',    'Merged Cells',cell_format=)




# worksheet.write(1, 1, 'Center across selection', cell_format)
# worksheet.write_blank(1, 2, '', cell_format)

workbook.close()
