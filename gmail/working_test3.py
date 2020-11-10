

import smtplib
import time
import imaplib
import email
import email.parser

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------



ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "jotforminbox" + ORG_EMAIL
FROM_PWD    = "12399.uo"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993


def read_email_from_gmail():
    # try:
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(FROM_EMAIL,FROM_PWD)
    will_read_mails=list()
    mail.select('INBOX') #İNBOX SEÇİMİ
    type, data = mail.search(None, '(UNSEEN)')  # okunmamış epostalar
    # type, data = mail.search(None, '(ALL)') #TÜM POSTALAR
    unseen_mail_ids = data[0].split()
    print("sonuc :{}\nokunmamış eposta idleri:{}".format(type,unseen_mail_ids))
    t, d = mail.search(None, '(FROM "JotForm" SUBJECT "Yeni Form Bildirimi")') # gönderene ve konuya göre arama yapmak
    # t,d=mail.fetch(d[0],"(RFC822)") #içeriği headerle birliklte almak için
    # t, d = mail.fetch("4", "(BODY.PEEK[TEXT])") #mody kısmını html olarak almak için
    print("okunacak epostalar:",d,len(will_read_mails))
    if t=="OK":
        selected_mail_ids=d[0].split()
        for i in selected_mail_ids:
            if i in unseen_mail_ids:
                will_read_mails.append(i)
    #then


    if len(will_read_mails)>0:

        for will_read_mail_id in will_read_mails:
            if will_read_mail_id in unseen_mail_ids:
                response,data=mail.fetch(will_read_mail_id,'(BODY.PEEK[TEXT])')

                # response, data = mail.fetch(will_read_mail_id, '(RFC822)')
                # d=mail.message_from_string(data[0][1])
                # print(d)

                # ###çalışıyort
                # for response_part in data:
                #     if isinstance(response_part, tuple):
                #         email_parser = email.parser.BytesFeedParser()
                #         email_parser.feed(response_part[1])
                #         msg = email_parser.close()
                #         for header in ['subject', 'to', 'from','date']:
                #             print('{:^8}: {}'.format(header.upper(), msg[header]))
                # ##çalışıyor



                print(data) #body peek ile
                print(data[0][1].strip())
                mail.store(will_read_mail_id,'+FLAGS','\SEEN') #EPOSTAYI OKUNDU YAPMAK İÇİN
                # print(data)
    else:
        print("yeni eposta yok")


    mail.close()
    mail.logout()
    # print(t, d)
    # d=d[0].split()
    # print(d)
    #
    # if t== "OK" and d in unseen_mail_ids:
    #     ids=d[0].split()
    #     for i in ids:
    #         typ,dat=mail.fetch(i,'(BODY.PEEK[TEXT])')
    #         for yanit in dat:
    #             if isinstance(yanit,tuple):
    #                 print(yanit[1])
    #
    #         # typ, dat = mail.fetch(i, '(RFC822)')
    #         print(dat)
    # else: print("yeni posta yok")
    #

    # for id in mail_ids:
    #     print(id)
    #     t,d=mail.search(id, '(FROM "JotForm" SUBJECT "Yeni Form Bildirimi")')
    #     # t, d = mail.fetch(id, '(FROM "JotForm")')
    #     # t,d=mail.fetch(id,"(RFC822)")
    #     # t, d = mail.fetch(id, "(BODY)")
    #     if t == "OK":
    #         print(d)
    #     else:
    #         continue
    # for response_part in d:
    #     if isinstance(response_part, tuple):
    #         msg = email.message_from_string(response_part[1])
    #         for header in ['subject', 'to', 'from']:
    #             print ( '%-8s: %s' % (header.upper(), msg[header]))


    # print(mail_ids)




    # print(mail.status('inbox',"(MESSAGES RECENT UIDNEXT UIDVALIDITY UNSEEN)"))
    # retur = mail.select('MESSAGES')  # İNBOX SEÇİMİ
    # print(retur)
    # stat=mail.status(retur,'(MESSAGES RECENT UIDNEXT UIDVALIDITY UNSEEN)')
    # print(stat)

    # type, data = mail.search(None, '(FROM "Ugur Okur")') #ugur okurdan gelen tüm e postalar
    # type, data = mail.search(None, '(SUBJECT "Yeni Form Bildirimi")') # yeni form bildirimi konulu epostayı seçmek için


    # if type=='ok' and
    # print(type,data,sep="\n")
    # t,d=mail.fetch(data[0],'(SUBJECT "Yeni Form Bildirimi")')
    # print(t,d)



#     mail_ids = data[0]
# #
#     id_list = mail_ids.split()
#     print(id_list)
#     first_email_id = int(id_list[0])
#     # latest_email_id = int(id_list[-1])
#     print(first_email_id)
#
#
    # for i in range(latest_email_id,first_email_id, -1):
    # typ, data = mail.fetch(first_email_id,'(RFC822)')
    # print(type,data)

    # for response_part in data:
    #     if isinstance(response_part, tuple):
    #         msg = email.message_from_string(response_part[1])
    #         email_subject = msg['subject']
    #         email_from = msg['from']
    #         print ('From : ' + email_from + '\n')
    #         print ('Subject : ' + email_subject + '\n')

    # except Exception as  e:
    #     print (str(e))
    #
    # for i in range(latest_email_id,first_email_id, -1):
    #     typ, data = mail.fetch(i, '(RFC822)' )
    #     print(type,data)
    #
    #     for response_part in data:
    #         if isinstance(response_part, tuple):
    #             msg = email.message_from_string(response_part[1])
    #             email_subject = msg['subject']
    #             email_from = msg['from']
    #             print ('From : ' + email_from + '\n')
    #             print ('Subject : ' + email_subject + '\n')
    #
    # except Exception as  e:
    #     print (str(e))

read_email_from_gmail()
