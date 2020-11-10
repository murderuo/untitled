from tkinter import Tk,Label,Entry,Button
from PIL import Image,ImageTk

class ShowCaptcha:

    def __init__(self):
        self._captha_keys=""
        # self.check=False
        self.root=Tk()
        img=ImageTk.PhotoImage(Image.open(".\\tmp\cropped.png"))  # PIL solution
        self.label=Label(image=img)
        self.label.pack()
        self.capt_entry=Entry(self.root)
        self.capt_entry.pack()
        self.gonder=Button(self.root,text="Gönder",command=self.gonderButton)
        self.gonder.pack()
        self.root.mainloop()

    def gonderButton(self):
        ent_value=self.capt_entry.get()
        self._captha_keys=ent_value
        # self.getValue()
        self.root.destroy()
        # return self.check==True


    def getValue(self):
        return self._captha_keys


# dialog=ShowCaptcha()
# chap=dialog.getValue()
# print(chap)
# dialog.gonder.config(command=dialog.gonderButton)
# value=dialog.getValue()
# print(value)



