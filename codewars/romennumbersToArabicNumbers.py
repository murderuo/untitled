#Bir sembolün değeri, kendisinden önce gelen daha büyük veya eşit değerde bir sembolün değerine eklenir. Örneğin XII = 12.
#Bir sembolün değeri, kendisinden sonra gelen daha büyük değerli bir sembolün değerinden çıkartılır. Örneğin IV = 4, XL = 40, vb.
# Bir sembol kendisine eşit veya büyük değerde bir sembolden sonra ve kedisinden büyük bir sembolden önce geliyorsa,
# ilk olarak kendisinden sora gelen ve büyük olan sembolden çıkartma işlemi uygulanır, daha sonra elde edilen değer kendisinden önce gelen sembole eklenir.
#    IV = 4        XL = 40     XII = 12    CML=950  XLV=45

# import sys

def romenToArabic(inputnumbers):
    rn={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    values=[rn[r] for r in inputnumbers]
    print(values)
    result=0
    for i in range(0, len(values)-1):
        if values[i] < values[i+1]:
            result -= values[i]
        else:
            result += values[i]
    print(result+values[-1])

inpt=input("numbers:")
romenToArabic(inpt)