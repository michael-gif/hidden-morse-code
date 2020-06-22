from PIL import Image

im = Image.open(input("Type the filename of the image to read.  Example: disguised_morse.png"))
pix = im.load()
ps = []

# takes the pixel colors and converts them to a list of morse code
width = int(input("Width of message:"))
height = int(input("Height of message:"))
for y in range(height):
    for x in range(width):
        if pix[x, y] == (0, 0, 0):
            ps.append(".")
        elif pix[x, y] == (255, 255, 255):
            ps.append(" ")
run = True
z = len(ps) - 1
while run:
    if ps[z] == " ":
        ps.pop(z)
        z -= 1
    else:
        run = False
count = 0
morse = []
for p in range(len(ps)):
    if ps[p] == ".":
        count += 1
    else:
        if count == 1:
            morse.append(".")
        elif count == 3:
            morse.append("-")
        count = 0
        morse.append(" ")
    if p == len(ps) - 1:
        if count == 1:
            morse.append(".")
        elif count == 3:
            morse.append("-")
        count = 0

# morse code translator below:

# morse code is separated into letters
morse = "".join(morse)
letter = []
spaces = 0
morseword = []
alphabet = "abcdefghijklmnopqrstuvwxyz .,?:/-='_!;"
morsecode = [
    ". -",
    "- . . .",
    "- . - .",
    "- . .",
    ".",
    ". . - .",
    "- - .",
    ". . . .",
    ". .",
    ". - - -",
    "- . -",
    ". - . .",
    "- -",
    "- .",
    "- - -",
    ". - - .",
    "- - . -",
    ". - .",
    ". . .",
    "-",
    ". . -",
    ". . . -",
    ". - -",
    "- . . -",
    "- . - -",
    "- - . .",
    " ",
    ". - . - . -",
    "- - . . - -",
    ". . - - . .",
    "- - - . . .",
    "- . . - .",
    "- . . . . -",
    "- . . . -",
    ". - - - - .",
    ". . - - . -",
    "- . - . - -",
    "- . - . - ."
]
word = []
for d in range(len(morse)):
    if morse[d] == ".":
        if spaces == 3:
            for x in range(spaces):
                letter.pop(len(letter) - 1)
            morseword.append("".join(letter))
            letter = []
        elif spaces == 7:
            for x in range(spaces):
                letter.pop(len(letter) - 1)
            morseword.append("".join(letter))
            morseword.append(" ")
            letter = []
        letter.append(".")
        if d == len(morse) - 1:
            morseword.append("".join(letter))
            letter = []
        spaces = 0
    elif morse[d] == "-":
        if spaces == 3:
            for x in range(spaces):
                letter.pop(len(letter) - 1)
            morseword.append("".join(letter))
            letter = []
        elif spaces == 7:
            for x in range(spaces):
                letter.pop(len(letter) - 1)
            morseword.append("".join(letter))
            morseword.append(" ")
            letter = []
        letter.append("-")
        if d == len(morse) - 1:
            morseword.append("".join(letter))
            letter = []
        spaces = 0
    else:
        letter.append(" ")
        spaces += 1

# letters are translated into english
for c in morseword:
    for b in range(38):
        if c == morsecode[b]:
            word.append(alphabet[b])

print("".join(word))
