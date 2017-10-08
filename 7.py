import requests
from io import BytesIO
from PIL import Image

img = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content))

print(img.width)
