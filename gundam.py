#Actual Robot
import robotBuilder

#Additional libraries used
from timer import Timer
from math import pi, degrees


#create robot instance 
myRobot = robotBuilder.build()

#set timestep
tStep = 0.02

try:

    finished = False
    
except KeyboardInterrupt:
    print "Keyboard Interrupt"
    myRobot.stopRobot()
    myRobot.terminate()

finally:
    myRobot.stopRobot()
    myRobot.terminate()
