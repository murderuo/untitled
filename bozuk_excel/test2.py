import zipfile

with zipfile.ZipFile('test.xlsx', 'r') as zgood:
    styles_xml = zgood.read('xl/styles.xml')

with zipfile.ZipFile('badfile.xlsx', 'a') as zbad:
    zbad.writestr('xl/styles.xml', styles_xml)