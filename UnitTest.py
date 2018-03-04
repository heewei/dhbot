import time
import pigpio #take ntoe pigpio uses BCM

pi1 = pigpio.pi() #local gpio

pi1.set_mode(14, pigpio.OUTPUT)
pi1.set_mode(15, pigpio.OUTPUT)

pi1.set_PWM_frequency(24, 100)
pi1.set_servo_pulsewidth(15, 500)

pi1.set_PWM_dutycycle(23, 20)

time.sleep(3)
pi1.set_servo_pulsewidth(15, 2500)

#cleanup
pi1.stop() 

