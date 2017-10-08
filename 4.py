import urllib.request
import re
number = 8022
while True:
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(number)
    page = urllib\
        .request\
        .urlopen(url)\
        .read()\
        .decode("utf-8")
    number = re.search('is \d+', page).group(0)[3:]
    print(number)

