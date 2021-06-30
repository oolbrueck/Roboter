import RPi.GPIO as GPIO
import time
import Move
from Move import Move
from MoveStatus import MoveStatus
import moveThread
from moveThread import moveThread

def main():
    move = Move()
    Move.setLeftStatus(True)
    Move.setRightStatus(True)
    Move.setSearchingHeadStatus(True)
    
#     t1 = moveThread(1, "t1", "firstAxis", 90)
#     t1.start()
#     t2 = moveThread(1, "t1", "secondAxis", 180)
#     t2.start()
    time.sleep(1)
    t3 = moveThread(1, "t1", "searchingHead", 90)
    #t3.start()
    #time.sleep(20)
    Move.setSearchingHeadStatus(False)
    
    
    print("360 activated")
    
    GPIO.setmode(GPIO.BCM) #Pinlayout
    GPIO.setup(24, GPIO.OUT)
    pwm = GPIO.PWM(24, 50)
    pwm.start(0)
    pwm.ChangeDutyCycle(4)
    time.sleep(5)
    GPIO.cleanup()
    
    Move.setRightStatus(False)
    Move.setLeftStatus(False)
    print("stoped")
    
if __name__ == '__main__':
    main()