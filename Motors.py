import pigpio

class Motors:
    def __init__(self):
        self.powerL = 0
        self.powerR = 0
        pi = pigpio.pi()

    def setPowerL(self):
        print("pwrL=", self.powerL)

    def setPowerR(self):
        print("pwrR=", self.powerR)