import terminal
terminal.clear()

terminal.color256(202)
print('=============================== Running Test ===============================', end = '\n\n')
terminal.reset()
print('For normal text color - ', end = '')
terminal.color(terminal.Red)
print('terminal.Red ', end = '')
terminal.color(terminal.Green)
print('terminal.Green ', end = '')
terminal.color(terminal.Blue)
print('terminal.Blue ', end = '')
terminal.color(terminal.Yellow)
print('terminal.Yellow ', end = '\n                        ')
terminal.color(terminal.Cyan)
print('terminal.Cyan ', end = '')
terminal.color(terminal.Magenta)
print('terminal.Magenta ', end = '')
terminal.color(terminal.White)
print('terminal.White ', end = '')
terminal.color(terminal.Black)
terminal.high256(248)
print('terminal.Black', end = '\n\n')
terminal.reset()

print('For bright text color - ', end = '')
terminal.color(terminal.BrightRed)
print('terminal.BrightRed ', end = '')
terminal.color(terminal.BrightGreen)
print('terminal.BrightGreen ', end = '')
terminal.color(terminal.BrightBlue)
print('terminal.BrightBlue ', end = '')
terminal.color(terminal.BrightYellow)
print('terminal.BrightYellow ', end = '\n                        ')
terminal.color(terminal.BrightCyan)
print('terminal.BrightCyan ', end = '')
terminal.color(terminal.BrightMagenta)
print('terminal.BrightMagenta ', end = '')
terminal.color(terminal.BrightWhite)
print('terminal.BrightWhite ', end = '')
terminal.color(terminal.BrightBlack)
print('terminal.BrightBlack', end = '\n\n')
terminal.reset()

print('For highlight color - ', end = '')
terminal.color(terminal.RedHigh)
print('terminal.RedHigh ', end = '')
terminal.color(terminal.GreenHigh)
print('terminal.GreenHigh ', end = '')
terminal.color(terminal.BlueHigh)
print('terminal.BlueHigh ', end = '')
terminal.color(terminal.YellowHigh)
print('terminal.YellowHigh ')
terminal.reset()
print('                      ', end = '')
terminal.color(terminal.CyanHigh)
print('terminal.CyanHigh ', end = '')
terminal.color(terminal.MagentaHigh)
print('terminal.MagentaHigh ', end = '')
terminal.color(terminal.WhiteHigh)
print('terminal.WhiteHigh ', end = '')
terminal.color(terminal.BlackHigh)
print('terminal.BlackHigh', end = '\n\n')

x = 0
y = 0
code = 0

print('For 8-bit termianls color256(#) - ')
while y < 16:
	while x < 16:
		code = (y * 16) + x
		terminal.color256(code)
		print(str(code) + ' ', end = '')
		x = x + 1
	print('')
	x = 0
	y = y + 1

print('')
terminal.reset()
x = 0
y = 0
print('For 8-bit termianls high256(#) - ')

while y < 16:
	while x < 16:
		code = (y * 16) + x
		terminal.high256(code)
		print(str(code) + ' ', end = '')
		x = x + 1
	print('')
	x = 0
	y = y + 1
print('')

terminal.reset()
terminal.bold()
print('terminal.bold()')
terminal.reset()
terminal.under()
print('terminal.under()')
terminal.reset()
terminal.blink()
print('terminal.blink()')
terminal.reset()
terminal.reversed()
print('terminal.reversed()\n')
terminal.reset()

terminal.sudoPrint('terminal.sudoPrint(text, x, y, color, color, bold, underline, blink, reversed, clear)', -1, -1, terminal.BrightGreen, terminal.RedHigh, 0, 0, 1, 1, 0)
terminal.reset()
