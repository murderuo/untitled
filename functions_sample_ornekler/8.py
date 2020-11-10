def harf_notu(x):
    harfler=''
    if x>0 and x<54:
        harfler='FF'
    elif x>54 and x<59:
        harfler='FD'
    elif x >59 and x<69:
        harfler='DD'
    elif x>69 and x<100:
        harfler='a ulan AA'

    return harfler
    
