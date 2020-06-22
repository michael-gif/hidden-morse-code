from PIL import Image

words = input("enter words to encode")
alphabet = "abcdefghijklmnopqrstuvwxyz .,?:/-='_!;"

ditdah = (100,100,100)
space = (0,0,255)

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
    ". ... . ... . ...",
    "... ... . . ... ...",
    ". . ... ... . .",
    "... ... ... . . .",
    "... . . ... .",
    "... . . . . ...",
    "... . . . ...",
    ". ... ... ... ... .",
    ". . ... ... . ...",
    "... . ... . ... ...",
    "... . ... . ... ."
]
morse = []

for x in range(len(words)):
    for y in range(38):
        if words[x] == alphabet[y]:
            morse.append(morsecode[y])

morse = '   '.join(morse)
pixels = []
for x in range(len(morse)):
    if morse[x] == '.':
        pixels.append(ditdah)
    else:
        pixels.append(space)

print('Pixel number:' , len(pixels))
width = int(input("width?"))
height = int(input("height?"))
area = width * height
print('Pixels available:' , area)
go = input("Proceed? 'y' or 'n'")
if go == 'y':
    imagetype = input("Create new image or modify existing image? 'new' or 'existing'")
    if imagetype == 'new':
        im = Image.new('RGB',(width,height),color=space)
        im.putdata(pixels)
        im.save(input("Filename of new image:") + '.png')
    elif imagetype == 'existing':
        filename = input("Filename of existing image:")
        im = Image.open(filename)
        pix = im.load()
        z = 0
        rows = len(pixels) // width
        remaining = rows * width
        remaining = len(pixels) - remaining
        for y in range(rows + 1):
            if y == rows:
                for x in range(remaining):
                    pix[x,y] = pixels[z]
                    z += 1
            else:
                for x in range(width):
                    pix[x,y] = pixels[z]
                    z += 1
        im.save(filename)
