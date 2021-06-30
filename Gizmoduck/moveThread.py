import RPi.GPIO as GPIO
import threading
import time
import Move
from Move import Move

class moveThread(threading.Thread):
    servoPin = 22
    
    def __init__(self, iD, name, movement, degree):
        threading.Thread.__init__(self)
        self.iD = iD
        self.name = name
        self.movement = movement
        self.degree = degree
        
    def run(self):
        print("Starte moveThread ", self.iD)

        if self.movement == "left":
            Move.left()
        elif self.movement == "right":
            Move.right()
        elif self.movement == "firstAxis":
            Move.firstAxis(self.degree)
        elif self.movement == "secondAxis":
            Move.secondAxis(self.degree)
        elif self.movement == "searchingHead":
            Move.searchingHead()
        else:
            print("can not find movement function")
       
        print("Beende ", self.iD)

print("Beende Main thread")