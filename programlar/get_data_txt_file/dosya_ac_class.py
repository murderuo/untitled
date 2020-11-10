class DosyaAc:
    def __init__(self):
        self.lines=[]
        self.data=[]


    def dosyaAc(self,dosya):
        with open(dosya,"r") as file:
            self.lines=file.readlines()
            for l in self.lines:
                nlns=l.strip().split()
                if len(nlns)==6:
                    if "Band" in nlns:
                        self.data.append(nlns[4])

    def meanVer(self,no):
        print("{}. mean: {}".format(no,self.data[no-1]))

    def meanSayisi(self):
        print("Mean veri sayısı:",len(self.data))

    @property
    def allMean(self):
        for i,v in enumerate(self.data):
            # print(i,v)
            print("{}. mean: {}".format(i,v))


if __name__ == '__main__':
    
    atac=DosyaAc()
    file="haziran.txt"
    atac.dosyaAc(file)
    atac.meanSayisi()
    atac.meanVer(27)
    # atac.allMean  #tüm meanları verir
