from file_save_class import FileSaves
from google.cloud import translate
import time
import pyperclip



def translateGoogleCloud(keyword):
    translate_client = translate.Client()
    translation=translate_client.translate(keyword,target_language="tr")
    mean=translation['translatedText']
    print(u'Text: {}'.format(keyword))
    print(u'Translation: {}'.format(mean))
    return mean


if __name__ == '__main__':

    f=FileSaves()

    recent_value = ""
    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            recent_value = tmp_value
            time.sleep(1)
            mean=translateGoogleCloud(tmp_value.strip())
            f.saveWord(tmp_value,mean)
        time.sleep(0.5)

