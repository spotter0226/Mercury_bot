#This code calculates the distance from one ultrasonic sensors on the bot

#Import GPIO libraries.
import RPi.GPIO as GPIO
import time
​
​
#Set GPIO numbering mode and define input/output pins.
GPIO.setmode(GPIO.BOARD)
GPIO_Trigger = 40
GPIO_Echo = 24
​
GPIO.setup(GPIO_Trigger, GPIO.OUT)
GPIO.setup(GPIO_Echo, GPIO.IN)
​
#Create function for calculating the distance.
def distance():
    #Send a short signal burst.
    GPIO.output(GPIO_Trigger,True)
    time.sleep(0.00001)
    GPIO.output(GPIO_Trigger, False)
​
    #Define variables for recording time.
    StartTime = time.time()
    StopTime = time.time()
​
    #Record time stamps between the trigger and its echo
    while GPIO.input(GPIO_Echo) == 0:
        print("No Echo")
        StartTime = time.time()
    while GPIO.input(GPIO_Echo) == 1:
        print("Echo Received")
        StopTime = time.time()
    
    #Record measured time.
    ElapsedTime = StopTime - StartTime
    distance = (TimeElapsed * 34300)/2
​
    return distance
​
try:  
    while True:
     distance = distance()
     print("Distance %.1f"%distance)
     time.sleep(1)
​
except KeyboardInterrupt:
    GPIO.cleanup()
