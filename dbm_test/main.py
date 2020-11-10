import re
import sys
import dbm

temp=[]
data="imdb.txt"
def openFile(file):

    with open(file,"r",encoding="utf-8") as f:
        lines=f.readlines()
        for l in lines:
            if len(l)==0 or len(l)==1:
                continue
            a_name=re.findall("^.+\s+\(",l)
            movie_name=re.findall("\)\s[0-9A-Za-z].*\[",l)
            char_name=re.findall("\[.+\]",l)  # character name
            years=re.findall("\(\d.+\)",l)
            if (len(a_name) !=1 and len(movie_name)!=1 and len(char_name)!=1 and len(years)!=1) :
                continue
            elif not "[" in l or "None" in l:
                continue
            else:
                a_name[0]=a_name[0].replace("(","").replace(")","").strip()
                years[0]=years[0].replace("(","").replace(")","").strip()
                movie_name[0]=movie_name[0].replace(")","").replace("[","").strip()
                char_name[0]=char_name[0].replace("[","").replace("]","").strip()
                # print(l)
                # print(a_name,years,movie_name,char_name)
                temp.append([*a_name,*years,*movie_name,*char_name])


openFile(data)
for i in temp:
    print(i)
def createMovieDB(a_name,m_name):
    movie_db=dbm.open("moviesdb","c")
    movie_db[m_name]=a_name












