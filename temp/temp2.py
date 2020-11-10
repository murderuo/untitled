# list_is=[i for i in range(5)]
# print(len(list_is),list_is)

# count=('Gelen Evrak (6)', 'Birimde Kayıt Bekleyen (0)', 'Dış Kurumdan Elektronik Gelen (0)', 'Birimde Kaydedilmiş (0)', 'Postalanacak (0)')
# print(*count)

import tkinter as tk
import random

def updates():
    l.config(text=str(random.random()))
    root.after(5000, updates)
    # root.update()

root = tk.Tk()
l = tk.Label(text='0')
l.pack()
root.after(0, updates)
# updates()

root.mainloop()