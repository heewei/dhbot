import time
import pigpio #take ntoe pigpio uses BCM

pi1 = pigpio.pi() #local gpio

SERVO = 14
PWM = 15

pi1.set_mode(PWM, pigpio.OUTPUT)
pi1.set_mode(SERVO, pigpio.OUTPUT)

pi1.set_PWM_frequency(PWM, 8000)
pi1.set_servo_pulsewidth(SERVO, 500)

pi1.set_PWM_dutycycle(PWM, 255/1)

time.sleep(3)
pi1.set_servo_pulsewidth(SERVO, 2500)

#cleanup
pi1.stop() 

