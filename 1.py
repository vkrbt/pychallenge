letters = 'tjyb'

outtab = 'abcdefghijklmnopqrstuvwxyz'
intab = 'yzabcdefghijklmnopqrstuvwx'

trantab = letters.maketrans(intab, outtab)

print(letters.translate(trantab))

