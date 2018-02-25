#Robot Base Class
from encoders import Encoders
from odometry import Odometer

class Robot:
	
	def __init__(self):
		self.encoders = Encoders()
		self.odometer = Odometer(self.encoders)
	
	#def addSensor(self):
	
	#def readSensors(self):
		
	#def moveRobot(self, speed, heading):
		
	#def stopRobot(self):
		
	#def terminate(self):
		
