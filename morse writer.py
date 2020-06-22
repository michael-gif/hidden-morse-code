from PIL import Image

words = input("enter words to encode")
alphabet = "abcdefghijklmnopqrstuvwxyz "
morsecode = [
    ". ...",
    "... . . .",
    "... . ... .",
    "... . .",
    ".",
    ". . ... .",
    "... ... .",
    ". . . .",
    ". .",
    ". ... ... ...",
    "... . ...",
    ". ... . .",
    "... ...",
    "... .",
    "... ... ...",
    ". ... ... .",
    "... ... . ...",
    ". ... .",
    ". . .",
    "...",
    ". . ...",
    ". . . ...",
    ". ... ...",
    "... . . ...",
    "... . ... ...",
    "... ... . .",
    " ",
]
morse = []

for x in range(len(words)):
    for y in range(27):
        if words[x] == alphabet[y]:
            morse.append(morsecode[y])

morse = '   '.join(morse)
pixels = []
for x in range(len(morse)):
    if morse[x] == '.':
        pixels.append((0,0,0))
    else:
        pixels.append((1,1,1))

width = int(input("width?"))
height = int(input("height?"))
area = width * height
print('Pixel number:' , len(pixels))
print('Pixels available:' , area)
go = input("Proceed? 'y' or 'n'")
if go == 'y':
    im = Image.new('RGB',(width,height),color=(1,1,1))
    im.putdata(pixels)
    im.save('disguised_morse.png')
