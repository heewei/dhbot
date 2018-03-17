#http://www.anites.com/2013/12/usb-keyboard-on-raspberry-pi.html
#pygames

import curses

stdscr = curses.initscr()
#curses.noecho()
curses.cbreak()
stdscr.keypad(True)

while True:
    c = stdscr.getch()

#kill program
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
