import os
with open("wordlist.txt","r+") as file:
    # kelime="kelime"
    # anlam="anlamı"
    # file.write("{}\t\t\t\t=\t\t\t\t{}".format(kelime,anlam))
    file.write("nerede bu dosya\n")
    values=file.readline()

    print(values)

