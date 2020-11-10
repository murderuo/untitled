import re




ifade="Gelen Evrak (2)"

result=re.findall("[0-9]+",ifade)


print(result[0])


