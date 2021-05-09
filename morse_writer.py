from PIL import Image

morse_code = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.', 
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ', ': '--..--',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '=': '-...-',
    '(': '-.--.',
    ')': '-.--.-',
    '\'': '.----.',
    '_': '..--.-',
    '&': '.-...',
    '"': '.-..-.',
    ';': '-.-.-.',
    '$': '...-..-',
    ' ': '       '
}

# input to encode into morse
words = input("enter words to encode")

# colors of the pixels
ditdah = tuple([int(component) for component in input('Enter RGB of morse code in the format int,int,int : ').split(',')])
space = tuple([int(component) for component in input('Enter RGB of white space in the format int,int,int : ').split(',')])

# generate a new dict of morse code, with the dashes replaced with three dots each
morsecode = {}
for key, value in morse_code.items():
    temp = ['... ' if char == '-' else '. 'for char in value]
    morsecode[key] = ''.join(temp).strip()
morsecode[' '] = '       '

# convert the input into morse code
morse = '   '.join([morsecode.get(char) for char in words])

# convert the morse code into pixel colors
pixels = [ditdah if char == '.' else space for char in morse]

# inform the user about the pixel requirements of the output image
print('Pixels required:' , len(pixels))
width = int(input("width?"))
height = int(input("height?"))
area = width * height
print('Pixels available:' , area)
go = input("Proceed? 'y' or 'n'")

# create the image
if go == 'y':
    im = Image.new('RGB',(width,height),color=space)
    im.putdata(pixels)
    im.save(f'{input("Output image filename (including extension): ")}')
