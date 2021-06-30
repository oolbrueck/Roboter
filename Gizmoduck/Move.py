import RPi.GPIO as GPIO
import threading
import time


class Move(object):
    global leftStatus
    leftStatus = False
    global rightStatus
    rightStatus = False
    global searchingHeadStatus
    searchingHeadStatus = False

#     firstAxisStatus = 0.0
#     secondAxisStatus = 0.0
    
    def __init__(self):
        print("init Move")
        
        
    def setLeftStatus(run):
        global leftStatus
        leftStatus = run
        
    def setRightStatus(run):
        global rightStatus
        rightStatus = run
        
    def setSearchingHeadStatus(run):
        global searchingHeadStatus
        searchingHeadStatus = run

#     GPIO.setmode(GPIO.BCM) #Pinlayout
#     GPIO.setup(leftServo, GPIO.OUT)
#     pwm = GPIO.PWM(leftServo, 50)
#     GPIO.setup(rightServo, GPIO.OUT)
#     pwm = GPIO.PWM(rightServo, 50)
#     pwm.start(0)
    
    def left():
        i = 0
        while leftStatus == True:
            print("running left")
            print(i)
            i = i + 1
            time.sleep(1)
            
    def right():
        i = 0
        while rightStatus == True:
            print("running right")
            print(i)
            i = i + 1
            time.sleep(1)
            
    def firstAxis(degree):
        print("first Axis activated")
        duty = (1. / 18.) * degree + 2
        GPIO.setmode(GPIO.BCM) #Pinlayout
        GPIO.setup(22, GPIO.OUT)
        pwm = GPIO.PWM(22, 50)
        pwm.start(0)
        pwm.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.cleanup()
        
        
    def secondAxis(degree):
        print("second Axis activated")
        duty = (1. / 18.) * degree + 2
        GPIO.setmode(GPIO.BCM) #Pinlayout
        GPIO.setup(23, GPIO.OUT)
        pwm = GPIO.PWM(23, 50)
        pwm.start(0)
        pwm.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.cleanup()
        
    def searchingHead():
        GPIO.setmode(GPIO.BCM) #Pinlayout
        GPIO.setup(22, GPIO.OUT)
        a1 = GPIO.PWM(22, 50)
        a1.start(0)
        u = 90
        GPIO.setup(23, GPIO.OUT)
        a2 = GPIO.PWM(23, 50)
        a2.start(0)
        
        while searchingHeadStatus == True:
            
            for i in range(0, 180, 3):
                duty = (1. / 18.) * i + 2
                a1.ChangeDutyCycle(duty)
                time.sleep(.05)
                if searchingHeadStatus == False:
                    break
            for i in range(180, 0, -3):
                duty = (1. / 18.) * i + 2
                a1.ChangeDutyCycle(duty)
                time.sleep(.05)
                if searchingHeadStatus == False:
                    break
            duty = (1. / 18.) * u + 2
            a2.ChangeDutyCycle(duty)
            if u > 140:
                u = 90
            u = u + 15
        GPIO.cleanup()
            
    
        
        
        