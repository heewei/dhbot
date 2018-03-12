import pigpio

LPWM = 14
RPWM = 15 

LDir = 16
RDir = 17

REVERSE = 0
FORWARD = 1

PWM_FREQ = 1000

class Motors:
    def __init__(self):
        self.powerL = 0
        self.powerR = 0
        self.pi = pigpio.pi()
        self.pi.set_mode(LPWM, pigpio.OUTPUT)
        self.pi.set_mode(RPWM, pigpio.OUTPUT)
        self.pi.set_PWM_frequency(LPWM, PWM_FREQ)
        self.pi.set_PWM_frequency(RPWM, PWM_FREQ)

    def setPowerL(self, val):
        val = checkVal(val)       
		self.pi.write(LDir, setDir(val))
		self.powerL = val * 255				
        print("pwrL=", self.powerL)
        self.pi.set_PWM_dutycycle(LPWM, self.powerL)
        
    def setPowerR(self, val):
        val = checkVal(val)       
		self.pi.write(RDir, setDir(val))
		self.powerR = val * 255				
        print("pwrR=", self.powerR)
        self.pi.set_PWM_dutycycle(RPWM, self.powerR)        
    
    def checkVal(value):
		if value > 1.0:
			value = 1.0
		elif value < -1.0:
			value = -1.0
		return value
		
	def setDir(value):
		if value < 0:
			return REVERSE
		else
			return FORWARD
