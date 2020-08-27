#asuming useing ANSI

# list of commands and uses
#----------------------------
# reset - reset format
# setPos - takes X and Y and then moves cursor
# clear - clears the screen then goes to (0, 0)
# color - sets text color add Bright to beginning to make bright or add High to the end to highlight it that color
# bold - makes text bold
# under - underlines the text
# reversed - swops the highlight and text color
# blink - blinks the text
# sudoPrint(string, x, y, color, high, bright, bold, under, blink, reversed) - most powerfull print command
# color256(0-255) - only for 8-bit terminals
# high256(0-255) - only for 8-bit terminals
# hide - hide the cursor
# show - show the cursor

# List of Colors For 3 or 4 Bit
#----------------
# Black
# Red
# Green
# Yellow
# Blue
# Magenta
# Cyan
# White

import os

Black = '30'
Red = '31'
Green = '32'
Yellow = '33'
Blue = '34'
Magenta = '35'
Cyan = '36'
White = '37'

BrightBlack = '30;1'
BrightRed = '31;1'
BrightGreen = '32;1'
BrightYellow = '33;1'
BrightBlue = '34;1'
BrightMagenta = '35;1'
BrightCyan = '36;1'
BrightWhite = '37;1'

BlackHigh = '40'
RedHigh = '41'
GreenHigh = '42'
YellowHigh = '43'
BlueHigh = '44'
MagentaHigh = '45'
CyanHigh = '46'
WhiteHigh = '47'

def reset():
	print('\u001b[0m', end = '')
def setPos(x, y):
	print('\u001b[' + str(y) + ';' + str(x) + 'H', end = '')
def clear():
	print('\u001b[2J')
	setPos(0, 0)
def color(color):
	print('\u001b[' + color + 'm', end = '')
def bold():
	print('\u001b[1m', end = '')
def under():
	print('\u001b[4m', end = '')
def reversed():
	print('\u001b[7m', end = '')
def blink():
	print('\u001b[5m', end = '')
def hide():
	os.system('tput civis')
def show():
	os.system('tput cnorm')
def color256(color):
	print('\u001b[38;5;' + str(color) + 'm', end = '')
def high256(color):
	print('\u001b[48;5;' + str(color) + 'm', end = '')
def sudoPrint(text, sx, sy, Color, High, sbold, sunder, sblink, sreversed, sclear):
	if sclear == 1:
		clear()
	if sx != -1 & sy != -1:
		setPos(sx, sy)
	color(Color)
	color(High)
	if sbold == 1:
		bold()
	if sunder == 1:
		under()
	if sblink == 1:
		blink()
	if sreversed == 1:
		reversed()
	print(str(text))

