#Imoport Libraries
import time 
import RPi.GPIO as GPIO

#GPIO setup
GPIO.setmode(GPIO.BOARD)





#Configure pins
GPIO.setup(3, GPIO.OUT) # Connected to PWMA
GPIO.setup(5, GPIO.OUT) # Connected to DIR


# Drive the motor forward.
# Motor 1:
mod = GPIO.PWM(3, 100)
mod.start(100)
GPIO.output(3, GPIO.HIGH) # Set PWM to high.
GPIO.output(5, GPIO.LOW) # Set DIR to low.
time.sleep(5)

mod.start(10)
time.sleep(5)



# Drive the motor backward.

mod.start(100)
GPIO.output(3, GPIO.HIGH) # Set PWM to high.
GPIO.output(5, GPIO.HIGH) # Set DIR to low.
time.sleep(5)

mod.start(5)
time.sleep(5)



# Reset all the GPIO pins by setting them to LOW
GPIO.output(3, GPIO.LOW) # Set AIN1
GPIO.output(5, GPIO.LOW) # Set AIN2