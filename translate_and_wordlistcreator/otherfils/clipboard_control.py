import win32clipboard

def get_clipboard():
    win32clipboard.OpenClipboard()
    try:
        data = win32clipboard.GetClipboardData()
    except:
        data=""
        win32clipboard.CloseClipboard()
    return data

# def dataCheck():
#     v=

def clipBoardDataLen():
    if get_clipboard()=="":
        return len(get_clipboard())
    else:
        return len(get_clipboard())

def set_clipboard():
    win32clipboard.OpenClipboard()
    value=win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()
    return value

if __name__ == '__main__':
    print (get_clipboard())
    print (clipBoardDataLen())







# def getCounts():
#     counts=win32clipboard.CountClipboardFormats()
#     print (counts)

# win32clipboard.OpenClipboard()
# print (win32clipboard.SetClipboardData(1,1))
# data = win32clipboard.GetClipboardData()
# print (len(data))
# print (data)

# win32clipboard.EmptyClipboard()
# print (win32clipboard.GetClipboardViewer())
# win32clipboard.EmptyClipboard()
# get_clipboard()
# getCounts()
