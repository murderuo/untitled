# import xlsxwriter module
import xlsxwriter

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('hello.xlsx')



# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()
# worksheet.set_zoom(190)
worksheet.print_area('A1:H50')
# worksheet.set_print_scale(70)
# worksheet.set_paper(9)
# worksheet.set_page_view()
worksheet.set_start_page(1)



# Use the worksheet object to write
# data via the write() method.
worksheet.write('A1', 'Hello..')
worksheet.write('B1', 'Geeks')
worksheet.write('C1', 'For')
worksheet.write('D1', 'Geeks')

# Finally, close the Excel file
# via the close() method.
workbook.close()
