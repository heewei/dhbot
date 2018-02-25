import threading
import time
from math import pi, sqrt
from timer import Timer
from pid import pid

class MotionController:
    def __inti__(self, odometer, motors, timestep = 0.02):
        self.timestep = timestep
        self.odometer = odometer
        self.odometer.timestep = self.timestep
        self.motors = motors
        self.omegaPID = PID()
        self.targetV = 0
        self.targetOmega = 0
        self.mode = "STOPPED"
        self.run()

# Movement Control Methods

    def forwardDist(self, speed, distTarget, stop = True, decel = False):
        phi0 = self.odometer.getPhi()
        x0, y0 = self.odometer.getPosXY()
        dist = 0
        loopTimer = Timer()
        if decel:
            while dist < distTarget - speed * 3 * self.timestep:
                self.forwardAngle(speed, phi0)
                loopTimer.sleepToElapsed(self.timestep)
                x1, y1 = self.odometer.getPosXY()
                dist = sqrt((x1 - x0)**2 + (y1 -y0)**2)
                if distTarget - dist < 50 and speed > 75:
                    speed = speed / 1.3
        else:
            while dist < distTarget:
                self.forwardAngle(speed, phi0)
                loopTimer.sleepToElapsed(self.timestep)
                x1, y1 = self.odometer.getPosXY()
                dist = sqrt((x1 -x0)**2 + (y1 -y0)**2)
        if stop:
            self.stop()
    
    # 
    # Functions for in loop call
    #
    def forwardAngle(self, speed, angelTarget):
        self.setMode('FORWARD') ## other modes lei?
        omega = self.omegaPID.getOutput(0, -self.odometer.angleRelToPhi(angelTarget), self.timestep)
        self.setSpeed(speed,omega)    
    
    def setSpeed(self, v, omega):
        self.targetV = v
        self.targetOmega = omega

    def stop(self):
        self.motors.stop()
        self.targetV = 0
        self.targetOmega = 0


## Add spline motion?
    def turnAngle(self, angelTarget, omega = pi):
        self.setMode('TURN')
        self.targetV = 0
        self.targetOmega = 0
        omegaMin = pi / 8.
        angleTol = pi / 180.
        loopTimer = Timer()
        while abs(self.odometer.angleRelToPhi(angleTarget)) > angleTol:
            angle = self.odometer.angleRelToPhi(angleTarget)
            if angle > pi / 6:
                self.targetOmega = omega
            elif angle > 0:
                self.targetOmega = omegaMin
            elif angle < -pi / 6:
                self.targetOmega = -omega
            else:
                self.targetOmega = -omegaMin
            loopTimer.sleepToElapsed(self.timeStep)
        self.stop()
        
########################################################################
##  Other methods
########################################################################

    # Kill thread running ._move() method
    def kill(self):
        self.active = False

    # This method runs continuously until self.active is set to false.
    # It looks for targetV and targetOmega values, provides corresponding
    # speed commands to the motors and updates the odometer at every pass
    # of the loop.
    def _run(self):
        try:
            loopTimer = Timer()
            while self.active:
                speedL = self.targetV - self.targetOmega * self.odometer.track / 2.
                speedR = self.targetV + self.targetOmega * self.odometer.track / 2.
                self.motors.speed(speedL, speedR)
                loopTimer.sleepToElapsed(self.timeStep)
                self.odometer.update()
        except IOError:
            print "IOError - Stopping"
            self.stop()
            self.kill()

    # Starts the ._run() method in a thread
    def run(self):
        self.active = True
        th = threading.Thread(target = self._run, args = [])
        th.start()

    # Sets the omegaPID constants for specific movement modes               
    def setMode(self, mode):
        if self.mode != mode:
            self.mode = mode
            self.omegaPID.reset()
            # Set PID constants for specific mode
            if mode == 'FORWARD':
                self.omegaPID.setKs(1, 0, 0)
            if mode == 'TURN':
                self.omegaPID.setKs(1.5, 0, 0)

    def setTimeStep(self, timeStep):
        self.timeStep = timeStep
        self.odometer.timeStep = timeStep
