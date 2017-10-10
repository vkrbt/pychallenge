from PIL import Image

img = Image.open('./11/cave.jpg')

(w, h) = img.size

even = Image.new('RGB', (w//2, h//2))
odd = Image.new('RGB', (w//2, h//2))

for i in range(w):
    for j in range(h):
        if (i+j) % 2 == 1:
            odd.putpixel((i//2, j//2), img.getpixel((i, j)))
        else:
            even.putpixel((i//2, j//2), img.getpixel((i, j)))

even.save('./11/even.jpg')
odd.save('./11/odd.jpg')