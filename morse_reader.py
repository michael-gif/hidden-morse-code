from PIL import Image

im = Image.open(input('filename (including extension): >>'))

pix = im.load()

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
    ',': '--..--',
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
    '$': '...-..-'
}

def convert(im):
    # take all the pixels and put them into a list
    morse = ''.join(['.' if pix[x, y] == (0, 0, 0) else ' ' for y in range(im.size[1]) for x in range(im.size[0])])
    # split the morse up into words, removing any whitespace in the process
    morse_words = [word for word in morse.split('       ') if word.strip() != '' ]

    # generate a new dict of morse code, with the dashes replaced with three dots each
    morsecode = {}
    for key, value in morse_code.items():
        temp = ['...' if char == '-' else '.' for char in value]
        morsecode[key] = ' '.join(temp)

    # the morse code dict but reversed
    morsecode_reversed = {value:key for key,value in morsecode.items()}

    # convert morse code into english
    sentence = []
    for word in morse_words:
        letters = word.split('   ')
        for letter in letters:
            if letter.strip() != '':
                #print(letter, morsecode_reversed.get(letter))
                pass
        new_word = ''.join(morsecode_reversed.get(letter) for letter in letters if letter.strip() != '')
        sentence.append(new_word)

    return ' '.join(sentence)
    
print(convert(im))
