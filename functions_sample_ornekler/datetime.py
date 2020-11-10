from datetime import date,datetime

temp_sd = date.today() #başlangıç tarihi


t = '27 Mayıs 1980'
temp_end = datetime.datetime.strptime(t, '%d %B %Y')

result=temp_end-temp_sd

print( result)
