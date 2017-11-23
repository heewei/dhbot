# import curses and GPIO
import curses
import RPi.GPIO as GPIO
import time

#set GPIO numbering mode and define output pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
	while True:
		char = screen.getch()
		if char == ord('q'):
			print("Quiting.")
			time.sleep(3)
			break
		elif char == curses.KEY_UP:
			print("UP pressed.")
# we can replace curses.key with other any digits like this  ord('p'), ord('m') ..etc
		elif char == curses.KEY_DOWN:
			print("Down pressed")
		elif char == curses.KEY_RIGHT:
			print("Right pressed")
		elif char == curses.KEY_LEFT:
			print("Left pressed")
		elif char == 10:
			print("a? pressed")
finally:
    #Close down curses properly, inc turn echo back on!
	curses.nocbreak(); screen.keypad(0); curses.echo()
	curses.endwin()
	GPIO.cleanup()
