# Hidden Morse Code
I have hidden morse code in an image  

Look at the `easier to see morse.png`:  
<br>
![alt text](https://github.com/michael-gif/hidden-morse-code/blob/master/easier%20to%20see%20morse.png "Easier to see morse")

This is a blown up version of `undisguised morse.png`, to make the image easier to see.  
<br><br>
Each black pixel makes up either a dit or a dah.  
One black pixel is a dit, three is a dah.  

Each white pixel makes up a space.  
One white pixel is a space between the dits and dahs of letters.  
Three white pixels is a space between two letters.  
Seven white pixels is a space between two words.  
<br><br>
The `disguised morse.png` is exactly the same, except all of the white pixels have had their colour changed to (1,1,1). This disguises all of the black pixels, which hides the morse code. It's almost impossible to differentiate the (0,0,0) pixels from the (1,1,1) pixels.
<br><br>
Use `morse writer.py` to create an image with hidden morse in it.  
Use `morse reader - verbose.py` to read the hidden morse.
Use `morse reader - compact.py` to also read the hidden morse. This python file is simply more compact in terms of the code. So compact in fact, that it only takes up three lines compared to the `verbose` version of the reader.
