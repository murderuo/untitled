
from twilio.rest import Client

import doviz
import time
account = ""
token = ""
client = Client(account, token)
msg_cnt=0
while 1:
    try:
        baslik,alisf,satisf=doviz.enparacom()
        # kur=db_doviztakip.a_fiyatlar_enp[3]
    except:
        print("veri alınamadı")
        continue
    str=alisf[2].split()
    str[0]=str[0].replace(',','.')
    # print(str[0])
    rakam=float(str[0])

    # print(type(rakam))

    if rakam>=190 and rakam<=191:
        print("Satabilirsin",baslik[2],rakam)
        data = "Satış verebilirsin " + baslik[2] + alisf[2]
        if msg_cnt==0:
            message = client.messages.create(to="+NUMBER", from_="+ ", body=data)
            msg_cnt+=1


    elif rakam >191 and rakam<=192:
        print("Maliyette" , baslik[2] , rakam)
        data = "Maliyette.Satış verebilirsin " + baslik[2] + alisf[2]
        if msg_cnt>0:

            message = client.messages.create(to="+NUMBER" , from_="+ " , body=data)
            msg_cnt+=1
        # break
    elif rakam>192:
        print("SAT AQ,SAT SAT! "+ baslik[2] + alisf[2])
        data ="SAT AQ,SAT SAT! "+ baslik[2] + alisf[2]
        print(data)
        if msg_cnt>1:

            message = client.messages.create(to="+", from_="+ ", body=data)
            msg_cnt+=1

        if msg_cnt>2:
            break
    else:
        print("Satamazsın",baslik[2],rakam)
        # data ="SAT AQ,SAT SAT! "+ baslik[2] + alisf[2]
        # print(data)
        # message = client.messages.create(to="+", from_="+ ", body=data)


    time.sleep(20)

print("program sonlandı")
