from PIL import Image

im = Image.open(input('filename (including extension): '))

# this is the color of the pixels in the image which are part of the morse code.
morse_color = (0,0,0)

print(' '.join([''.join(['abcdefghijklmnopqrstuvwxyz'[['. ...','... . . .','... . ... .','... . .','.','. . ... .','... ... .','. . . .','. .','. ... ... ...','... . ...','. ... . .','... ...','... .','... ... ...','. ... ... .','... ... . ...','. ... .','. . .','...','. . ...','. . . ...','. ... ...','... . . ...','... . ... ...','... ... . .',' '].index(letter)] for letter in word.split('   ')]) for word in [word for word in ''.join(['.' if im.load()[x, y] == morse_color else ' ' for y in range(im.size[1]) for x in range(im.size[0])]).split('       ') if word.strip() != '' ]]))

'''
this code will convert an image that contains morse code into english. the morse code in question must use consistent coloring.
for example, all 'dits' and 'dahs' could have the rgb color of 0,0,0,
allowing for this code to quickly find out which pixels are part of the morse code and which aren't.
to change what color the code will use for the morse code detection, change the morse_color variable above
'''
