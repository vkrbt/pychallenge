import re
from zipfile import ZipFile

file = 90052


def path(filename):
    return str(filename)+'.txt'


comments = ''
zipfile = ZipFile('./channel.zip')
while file:

    comments += zipfile.getinfo(path(file)).comment.decode('utf-8')
    source = zipfile.open(path(file)).read().decode('utf-8')
    file = re.search('\d+', source)
    if file:
        file = file.group(0)

print(comments)