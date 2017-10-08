from urllib.request import urlopen
from pickle import load

raw = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")

obj = load(raw)

for i in range(len(obj)):
    string = ''
    for j in range(len(obj[i])):
        string += obj[i][j][0] * obj[i][j][1]
    print(string)