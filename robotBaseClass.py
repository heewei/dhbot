#Robot Base Class
from encoders import Encoders
from odometry import Odometer
from motors import Motors

class Robot:
	
	def __init__(self):
		self.encoders = Encoders()
		self.odometer = Odometer(self.encoders)
		self.motors = Motors() 
		#add motion controllers 
	
	#def addSensor(self):
	
	#def readSensors(self):
		
	#def moveRobot(self, speed, heading):
		
	#def stopRobot(self):
		
	#def terminate(self):
		
