import RPi.GPIO as GPIO
import threading
import time
import Move
from Move import Move
import ObjectDetection
#from ObjectDetection import searchForBall


class ThreadController(threading.Thread):
    servoPin = 22
    
    def __init__(self, iD, name, case, degree):
        threading.Thread.__init__(self)
        self.iD = iD
        self.name = name
        self.case = case
        self.degree = degree
        
    def run(self):
        print("Starte Thread ", self.iD)

        if self.case == "left":
            Move.left()
        elif self.case == "right":
            Move.right()
        elif self.case == "firstAxis":
            Move.firstAxis(self.degree)
        elif self.case == "secondAxis":
            Move.secondAxis(self.degree)
        elif self.case == "searchingHead":
            Move.searchingHead()
        elif self.case == "detectObject":
            print("ich wurde ausgeloest")
            ObjectDetection.searchForBall()
        else:
            print("can not find case function")
       
        print("Beende ", self.iD)

print("Beende Main thread")