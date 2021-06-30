
#from ObjectDetection import ObjDetect
#import ThreadController
#from ThreadController import ThreadController
import time

    
global centerX
global centerY
    
centerX = 0
centerY = 0
    
def setCenterOfObject(cX, cY):
    global centerX
    global centerY
    centerX = cX
    centerY = cY
        
    
def objectFollowing():
    while True:
        print("X Koordinate des Zentrums", centerX)
        time.sleep(2)
            
