import mraa
import time

from evdev import UInput, ecodes as e

ui = UInput()
io0 = mraa.Gpio(13)
io0.dir(mraa.DIR_IN)
io1 = mraa.Gpio(12)
io1.dir(mraa.DIR_IN)
io2 = mraa.Gpio(11)
io2.dir(mraa.DIR_IN)
io3 = mraa.Gpio(10)
io3.dir(mraa.DIR_IN)
while True:
	x = mraa.Aio(5)
	y = mraa.Aio(4)
	if (x.read() < 100):
		ui.write(e.EV_KEY, e.KEY_UP, 1)
	if (x.read() > 900):
		ui.write(e.EV_KEY, e.KEY_LEFT, 1)
	if (y.read() < 100):
		ui.write(e.EV_KEY, e.KEY_RIGHT, 1)
	if (y.read() > 900):
		ui.write(e.EV_KEY, e.KEY_DOWN, 1)
	
	if (x.read() > 100 and x.read() < 900):
		ui.write(e.EV_KEY, e.KEY_UP, 0)
		ui.write(e.EV_KEY, e.KEY_LEFT, 0)
	if (y.read() > 100 and y.read() < 900):
		ui.write(e.EV_KEY, e.KEY_DOWN, 0)
		ui.write(e.EV_KEY, e.KEY_RIGHT, 0)
		
	if (io0.read()):
		ui.write(e.EV_KEY, e.KEY_Z, 1)
	else:
		ui.write(e.EV_KEY, e.KEY_Z, 0)
	
	if (io1.read()):
		ui.write(e.EV_KEY, e.KEY_X, 1)
	else:
		ui.write(e.EV_KEY, e.KEY_X, 0)
		
	if (io2.read()):
		ui.write(e.EV_KEY, e.KEY_ESC, 1)
	else:
		ui.write(e.EV_KEY, e.KEY_ESC, 0)
		
	if (io3.read()):
		ui.write(e.EV_KEY, e.KEY_ENTER, 1)
	else:
		ui.write(e.EV_KEY, e.KEY_ENTER, 0)
	time.sleep(.1)
	ui.syn()
ui.close()

