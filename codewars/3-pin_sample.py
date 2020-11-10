pin='12356'

# print(len(pin)in (4,6))
def validate_pin(pin):
    if len(pin)in (4,6):
        check=[True  if i.isdigit() else False for i in pin ]
        if False in check: return False
        else: return True
    else: return False




    # #return true or false
    # if pin.isdecimal() and (len(pin)==4 or len(pin))==6:
    #     return True
    # else:
    #     return False

print(validate_pin(pin))