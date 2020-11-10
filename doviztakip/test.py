
from twilio.rest import Client

import db_doviztakip

account = "AC24958c19176c662949a557dd9d8407ea"
token = "76a6c032a31c1ffa9b759a3302fba29f"
client = Client(account, token)

altin=db_doviztakip.basliklar_enp[3]
kur=db_doviztakip.a_fiyatlar_enp[3]
# message = client.messages.create(to="+905375447979", from_="+15206197979 ", body=data)
print(altin,kur)