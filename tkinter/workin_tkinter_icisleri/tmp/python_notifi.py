from twilio.rest import Client




account_sid='AC1c0c34cd89fdc8270d11abe0ce50fca0'
auth_token='36f68f9858ded01efc6946105f4b0d7f'
client=Client(account_sid,auth_token)


def sendNotif(bildirim):

    message=client.messages.create(from_='whatsapp:+14155238886',
        body=bildirim,
        to='whatsapp:+905375447979')

sendNotif("MERHABA WHATSAPP")



# print(message.sid)




# class Notice:
#     def __init__(self):
#         pass
#
#     def sendEvrakNotif(self,bildirim):
