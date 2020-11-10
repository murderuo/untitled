numbers="2 4 7 8 10"

numbers=[int(i) for i in numbers.split()]

print(n)

for i,v in enumerate(n):
    if v%2==0:
        if n[i+1]%2==0:continue
        else:n[i+1]
    elif v%2==1:
        if n[i+1]%2==1:continue
        else:n[i+1]