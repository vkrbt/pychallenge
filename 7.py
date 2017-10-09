import requests
from io import BytesIO
from PIL import Image


def getnum(color):
    if color[0] == color[1] == color[2]:
        return color[0]


img = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content))

middle = img.height // 2

nums = []

for i in range(4, img.width, 7):
    color = img.getpixel((i, middle))
    num = getnum(color)
    if num:
        nums.append(num)


def convert2string(nums):
    str = ''
    for num in nums:
        str += chr(num)
    return str


print(convert2string(nums))

answer = [105, 110, 116, 101, 103, 114, 105, 116, 121]

print(convert2string(answer))