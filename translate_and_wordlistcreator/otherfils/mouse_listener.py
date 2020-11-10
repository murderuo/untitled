import time
import pyperclip




recent_value = ""
while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        time.sleep(0.1)