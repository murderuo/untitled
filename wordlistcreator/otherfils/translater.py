from language_detector import detect_language
from google.cloud import translate
import time
import pyperclip

def cevir(text):
    translate_client=translate.Client()
    translation=translate_client.translate(text,target_language="tr")
    # # print(translation['detectedSourceLanguage'].strip())
    # # if translation['detectedSourceLanguage']=="en":
    print(u'Text: {}'.format(text))
    print(u'Translation: {}'.format(translation['translatedText']))
    print(u'Detected language: {}'.format(translation['detectedSourceLanguage']))



recent_value=""
while True:
    tmp_value = pyperclip.paste()
    lang=detect_language(tmp_value.strip())
    if lang=="Turkish":continue
    if tmp_value != recent_value:
        recent_value = tmp_value
        time.sleep(0.5)
        cevir(tmp_value)
        time.sleep(1)
