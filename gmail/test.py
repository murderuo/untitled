import imaplib

import webbrowser

obj = imaplib.IMAP4_SSL('imap.gmail.com','993')

obj.login('jotforminbox@gmail.com','12399.uo')

obj.select()

unread = str(obj.search(None, 'UNSEEN'))

print(unread)

# print(len(unread) - 13)

# if (len(unread) - 13) > 0: webbrowser.open('http://gmail.com')