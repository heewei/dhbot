#encoders

"""

import RPi.GPIO as GPIO

#definitons
GPIO.setmode(GPIO.BOARD) # this is from wiringPi

LeftEncoder_A_PIN = 7 #7
LeftEncoder_B_PIN = 3 #8
RightEncoder_A_PIN = 11 #0
RightEncoder_B_PIN = 13 #2

GPIO.setup(LeftEncoder_A_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LeftEncoder_B_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RightEncoder_A_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RightEncoder_B_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#decorators
def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper

class Encoders:
	
	def __init__(self):
		
		self.countLeft = 0
		self.countRight = 0
		self.lastCountLeft = 0
		self.lastCountRight = 0
		
	@threaded
	def startCount(self):
		print "xyz"
		
	def readCounts(self):
		countLeft, countRight
		
	
"""

from piGPIODecoder import Decoder
import pigpio
import time #import rotary_encoder

class Encoders:
	def __init__(self):
		self.countL = 0
		self.countR = 0
		pi = pigpio.pi()
		decoderL = Decoder(pi, 2, 4, self.callbackL)
		decoderR = Decoder(pi, 17, 27, self.callbackR)
		
		time.sleep(300)

		decoderL.cancel()
		decoderR.cancel()

		pi.stop()
	
	def callbackL(self,way):
		self.countL += way
		print("posL=",self.countL)
		
	def callbackR(self,way):
		self.countR += way
		print("posR=",self.countR)

	def readCounts(self):
		return self.countL, self.countR
