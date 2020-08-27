Please note the will only work if you are using an ANSI terminal

List of Commands and There Uses
put "terminal." before every command

=====================================

reset() - Resets the text format

setPos(x, y) - Moves the cursor to the position that you give it

clear() - clears the screen then goes to (0, 0)

color(terminal.color) - Use to set the color to on of the 8 colors if you add "Bright" the the beginnig to brighten the color or
                        add "High" to the end to highlight it that color

bold() - Makes the text bold (Please note doing this is the same as using a bright color)

under() - Underlines the text

reversed() - Flips the color of the background and the text

blink() - Blinks the text

color256(0-255) - Only works on 8-bit systems allows you to use 256 different colors in your program

high256(0-255) - Only works on 8-bit systems allows you to use 256 different background colors in you program

show() - Shows the cursor

hide() - Hides the cursor

sudoPrint(text, x, y, color, color, bold, under, blink, reversed, clear) - sudoPrint lets you use all the commands at once. The way it work is you enter a string for your
                                                                           text in the first slot, then you enter x and y (put -1 in both if you want it to stay).
									   Next two slots are to enter color there is two becuase you can enter text color in one and
									   background color in the other. In the next five slots you are toggling bold, underline, blink, 
									   reversed, and clear creen. You must fill all of them. 1 means on 0 means off.

==========================================================================================================================================================================

To use the library place the terminal.py file in the folder with the main program. Then in your program type "import terminal" then you can use all the commands.
If you want to see all the library can do run the terminal_showOff.py to get a demo on the library.



Made by - Cameron Barclay
Completed on - August, 2020
