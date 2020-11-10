from __future__ import unicode_literals
# Used to save the file as excel workbook
# Need to install this library
from xlwt import Workbook
# Used to open to corrupt excel file
import io

filename = r'test.xls'
# Opening the file using 'utf-16' encoding
file1 = io.open(filename, "r")
data = file1.readlines()
print(data)

# Creating a workbook object
xldoc = Workbook()
# Adding a sheet to the workbook object
sheet = xldoc.add_sheet("Sheet1", cell_overwrite_ok=True)
print(sheet)
# Iterating and saving the data to sheet
for i, row in enumerate(data):
    # Two things are done here
    # Removeing the '\n' which comes while reading the file using io.open
    # Getting the values after splitting using '\t'
    for j, val in enumerate(row.replace('\n', '').split('\t')):
        sheet.write(i, j, val)

# Saving the file as an excel file
xldoc.save('myexcel.xls')

import pandas as pd
df = pd.ExcelFile('myexcel.xls').parse('Sheet1')