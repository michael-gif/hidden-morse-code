from PIL import Image

im = Image.open(input('filename (including extension): >>'))

pix = im.load()

morse_code = [
    '. ...',
    '... . . .',
    '... . ... .',
    '... . .',
    '.',
    '. . ... .',
    '... ... .',
    '. . . .',
    '. .',
    '. ... ... ...',
    '... . ...',
    '. ... . .',
    '... ...',
    '... .',
    '... ... ...',
    '. ... ... .',
    '... ... . ...',
    '. ... .',
    '. . .',
    '...',
    '. . ...',
    '. . . ...',
    '. ... ...',
    '... . . ...',
    '... . ... ...',
    '... ... . .',
    ' '
    ]

def convert(im):
    # take all the pixels and put them into a list
    morse = ''.join(['.' if pix[x, y] == (0, 0, 0) else ' ' for y in range(im.size[1]) for x in range(im.size[0])])
    # split the morse up into words, removing any whitespace in the process
    morse_words = [word for word in morse.split('       ') if word.strip() != '' ]

    # convert morse code into english
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sentence = []
    for word in morse_words:
        letters = word.split('   ')
        new_word = ''
        for letter in letters:
            index = morse_code.index(letter)
            letter = alphabet[index]
            new_word += letter
        sentence.append(new_word)

    return ' '.join(sentence)
    
print(convert(im))
