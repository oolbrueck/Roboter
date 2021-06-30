from collections import deque
import imutils
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import time
import AlignmentController

#import AlignmentController as ac


    
global center
    
def searchForBall():
    greenLower = (29, 86, 6)
    greenUpper = (64, 255, 255)#untere und obere Farbgrenze, welche erkannt werden soll
    pts = deque(maxlen=10)#legt die groesse des Puppers fest und beeinflusst damit die rote Linie

    vs = VideoStream(src=0).start() #greife auf die default Kamera zu
    time.sleep(2.0)#Zeit fuer die Kamer
    global center

    while True:
        frame = vs.read()#nehme einzelnes Frame des Videos
    
        frame = imutils.resize(frame, width=550)#Skalierung der Bildgroesse
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)#Bild wird unscharf gemacht
        cv2.imshow("Blurred Bild", blurred)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)#konvertiere Farbe in HSV colorspace um es in Numpy verarbeiten zu koennen
        cv2.imshow("HSV Bild", hsv)
        mask = cv2.inRange(hsv, greenLower, greenUpper)
        cv2.imshow("thresholding", mask)
        #mask = cv2.erode(mask, None, iterations=2)
        #mask = cv2.dilate(mask, None, iterations=2)
    

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#RETR_EXTERNAL==0, CHAIN_APPROX_SIMPLE==2
        #findContours() liefert 2D Array mit Koordinaten
        cnts = imutils.grab_contours(cnts)
    

        center = None
    
        if len(cnts) > 0:
        
            c = max(cnts, key=cv2.contourArea)#groesste Kontur

            ((x, y), radius) = cv2.minEnclosingCircle(c)#liefert center und radius
        
            center = (int(x), int(y))
        
            if radius > 10:
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                AlignmentController.setCenterOfObject(int(x), int(y))
            
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
    
        if key == ord("q"):
            break
    vs.stop()
    cv2.destroyAllWindows()
        
        