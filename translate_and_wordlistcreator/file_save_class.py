import os


class FileSaves:

    def __init__(self):
        self.file="wordlist.txt"
        if not os.path.exists(self.file):
            self.fileCreate()
        else:
            self.dosya=open(self.file,"a",encoding="utf-8")
            self.dosya.close()

    def fileCreate(self):
        self.dosya=open(self.file,"w",encoding="utf-8")
        self.dosya.write("KEYWORD                                           =TRANSLATED\n")
        self.dosya.write("_____________________________________________________________\n")
        self.dosya.close()

    def fileOpen(self):  #appendmod
        if not self.dosya.closed: self.dosya.close()
        self.dosya=open(self.file,"a",encoding="utf-8")
        return self.dosya

    def fileClose(self):
        return self.dosya.close()

    def saveWord(self,word,translated_text):
        nword=""
        if len(word)>55:
            for h in range(len(word)):
                if h ==55:
                    nword=word[:h]+"\n"
                    nword+=word[h:110]+"\n"
                    nword+=word[110:]
        else:nword=word
        self.fileOpen()
        if self.dosya.writable():
            self.dosya.write("{}                                             "
                             "       ={},en\n".format(nword,translated_text))
            self.fileClose()


if __name__ == '__main__':
    f=FileSaves()
    f.saveWord("man","adam")
    f.saveWord("onksiyonunu anlatırken, bu fonksiyonun file adlı bir "
               "parametresi olduğundan söz etmiştik. Bu parametre yardım"
               "ıyla print","kırmızı") #maybe we can save longer than 55 characters