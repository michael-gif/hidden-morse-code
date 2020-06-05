from PIL import Image
im = Image.open("morse.png")
pix = im.load()
ps = []
for y in range(im.size[1]):
    for x in range(im.size[0]):
        if pix[x,y] == (0,0,0):
            ps.append('.')
        elif pix[x,y] == (1,1,1):
            ps.append(' ')
run = True
z = len(ps) - 1
while run:
    if ps[z] == ' ':
        ps.pop(z)
        z -= 1
    else:
        run = False
count = 0
morse = []
for p in range(len(ps)):
    if ps[p] == '.':
        count += 1
    else:
        if count == 1:
            morse.append('.')
        elif count == 3:
            morse.append('-')
        count = 0
        morse.append(' ')
    if p == len(ps) - 1:
        if count == 1:
            morse.append('.')
        elif count == 3:
            morse.append('-')
        count = 0

morse = ''.join(morse)
letter = []
spaces = 0
morseword = []
alphabet = 'abcdefghijklmnopqrstuvwxyz '
morsecode = ['. -','- . . .','- . - .','- . .','.','. . - .','- - .','. . . .','. .','. - - -','- . -','. - . .','- -','- .','- - -','. - - .','- - . -','. - .','. . .','-','. . -','. . . -','. - -','- . . -','- . - -','- - . .',' ']
word = []
for d in range(len(morse)):
    if morse[d] == '.':
        if spaces == 3:
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            morseword.append(''.join(letter))
            letter = []
        elif spaces == 7:
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            morseword.append(''.join(letter))
            morseword.append(' ')
            letter = []
        letter.append('.')
        if d == len(morse) - 1:
            morseword.append(''.join(letter))
            letter = []
        spaces = 0
    elif morse[d] == '-':
        if spaces == 3:
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            morseword.append(''.join(letter))
            letter = []
        elif spaces == 7:
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            letter.pop(len(letter)-1)
            morseword.append(''.join(letter))
            morseword.append(' ')
            letter = []
        letter.append('-')
        if d == len(morse) - 1:
            morseword.append(''.join(letter))
            letter = []
        spaces = 0
    else:
        letter.append(' ')
        spaces += 1

for c in morseword:
    for b in range(27):
        if c == morsecode[b]:
            word.append(alphabet[b])

print(''.join(word))
