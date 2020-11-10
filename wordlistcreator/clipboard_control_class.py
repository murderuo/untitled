import win32clipboard

class ClipBoardGetter():
    def __init__(self):
        # super().__init__(self)
        self.d=self.getClipboard()

    def getClipboard(self):

        win32clipboard.OpenClipboard()
        try:
            d = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
        except:
            d = ""
            win32clipboard.CloseClipboard()
        return d

    @property
    def getClipboardDataLen(self):
        return len(self.d)

    @property
    def data(self):
        return self.d

if __name__ == '__main__':

    c=ClipBoardGetter()
    print(c.data)
    print(c.getClipboardDataLen)



