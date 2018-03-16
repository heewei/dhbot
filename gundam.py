#Actual Robot
import robotBuilder

#Additional libraries used
from timer import Timer
from math import pi, degrees

#create robot instance 
myRobot = robotBuilder.build()
#REST engine?


#set timestep
tStep = 0.02

try:

    finished = False
    while not finished:
		#check state
		if state is 1:
			print("Autonomous Moving")#move
		elif state is 2:
			print("Relative moving")
		elif state is 3:
			print("Starting mapping")#start mapping engine
		elif state is 4:
			print("Self Test")#diagnostics 
			
		
    
except (KeyboardInterrupt, SystemExit):
    print("Keyboard Interrupt")
    myRobot.stopRobot()
    myRobot.terminate()
    raise 

finally:
    myRobot.stopRobot()
    myRobot.terminate()
