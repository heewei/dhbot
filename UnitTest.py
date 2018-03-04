import time
import pigpio #take ntoe pigpio uses BCM

pi1 = pigpio.pi() #local gpio

pi1.set_mode(14, pigpio.OUTPUT)

pi1.set_PWM_frequency(24, 100)

pi1.set_PWM_dutycycle(23, 10)

time.sleep(3)

#cleanup
pi.stop() 

