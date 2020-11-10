file ="imdb.txt"
with open(file,"r",encoding="utf-8") as f:
    lines=f.readlines()
    with open("new_imdb.txt","w",encoding="utf-8") as nf:
        for l in lines:
            nf.write(l)