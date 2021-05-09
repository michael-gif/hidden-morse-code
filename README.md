# Hidden Morse Code
I have hidden morse code in an image  

Take a look at `easier to see morse.png`:  
<br>
![alt text](https://github.com/michael-gif/hidden-morse-code/blob/master/easier%20to%20see%20morse.png "Easier to see morse")

This is a blown up version of `undisguised morse.png`, to make the pixels easier to see.

## Explanation
- Morse code is made up of 'dits' and 'dahs'. You may have heard this as short beeps and long beeps when something is being communicated in morse.  
- For example, to send an SOS in morse code, you would beep the following:  
`dit dit dit dah dah dah dit dit dit  `  
- The morse above can be written as:  
`... --- ...`

In the image `easier to see morse.png`:
- Each black pixel is part of either a dit or a dah.
- Each white pixel is whitespace between the dits and dahs.
- One black pixel is a dit, three is a dah.
- One white pixel is a space between the dits and dahs of letters.
- Three white pixels is a space between two letters.
- Seven white pixels is a space between two words.

In the image `disguised morse.png`:
- The image is exactly the same as `easier to see morse.png`, except all of the white pixels have had their colour changed to `(1,1,1)`.
- This makes all of the `(0,0,0)` pixels blend in with the rest of the image, which hides the morse code.
- It's almost impossible to tell the difference between the `(0,0,0)` pixels and the `(1,1,1)` pixels with the human eye, making this an efffective way to hide morse code.

More info:
- The color of the pixels don't have to be `(0,0,0)` or `(1,1,1)`. They just need to be consistent.
- For example, you could have all of the dits and dahs be the color `(255,0,0)`, while the space inbetween be the color `(255,0,1)`, making the morse code look like a solid red block.

## Usage
- Use `morse writer.py` to create an image with hidden morse in it.
- Use `morse reader - verbose.py` to read the hidden morse.
- Use `morse reader - compact.py` to also read the hidden morse. This python script is simply more compact in terms of the code, using only 3 lines of code compared to the 57 lines in the `morse reader - verbose.py` python script.
- By default, the morse reader scripts will treat the color `(0,0,0)` as the dits and dahs of morse code, so if you want to scan an image with a different color as the dits and dahs, then either change the color of the pixels in the image or change the code to use a different RGB color for the dits and dahs.
