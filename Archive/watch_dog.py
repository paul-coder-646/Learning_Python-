import cv2
import numpy as np
from PIL import Image
import time
import numpy as np
import os
import pynput
from pynput.keyboard import Key, Controller, Listener
from pynput.mouse import Button, Controller
import logging
import sys

mouse = pynput.mouse.Controller()
cap = cv2.VideoCapture(0) 

#### NEEDS TO END WITH 9)
ar = (0,0,1079,0,9)

def mouse_moved():
    pos = mouse.position
    time.sleep(1.5)
    
    if mouse.position == pos:
        return False
            
    else:
        return True
        #exit()


def loop():
    print("commencing")
    time.sleep(5.000) # Make sure, you need to give time
                         # for MS Windows to initialize Camera
    print("ready")
    intruder_flag = False
    # Check if the webcam is opened correctly

    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    while True:
        intruder_flag = mouse_moved()

        if intruder_flag:
            #mouse needs to be moved to height in array ar to deactivate the alarm
            for c in ar:#,0,1079,9):

                if c==9: #last array entry marks success
                    print()
                    print("confirmed")
                    print()
                    print()
                    time.sleep(3)
                    cap.release()
                    cv2.destroyAllWindows()
                    sys.exit(0)

                else:
                    if abs(mouse.position[1]-c)<50:
                        print("correct")

                    else:
                        break

                time.sleep(2)
            print("intruder detected. this incident will be reported.")
            ret, frame = cap.read()
            #frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            frame = cv2.resize(frame, None, fx=5, fy=5, interpolation=cv2.INTER_AREA)

            cv2.imshow('Input', frame)

            im = Image.fromarray(np.asarray(frame))
            d = os.getcwd()
            if "watch" in d:
                im.save(os.path.join(os.path.dirname(os.path.dirname(d)), "INTRUDER.png"))
            else:
                im.save("./INTRUDER.png")
            im.save("./INTRUDER.png")
            intruder_flag = False
            cap.release()
            cv2.destroyAllWindows()
            #uncomment these lines if you want the system to shut down
            #os.system("shutdown /l")
            #os.system("shutdown /l /f")
            return



    """if mouse moved or key pressed, open a batch script and log out
    instantly. Also if brightness changes a lot... Or face detected.


    
    And take photo.
    Wait. is that a distance sensor?


    
    """
loop()
cap.release()
cv2.destroyAllWindows()


