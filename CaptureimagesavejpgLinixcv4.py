#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      eugenio.gigante
#
# Created:     28/05/2023
# Copyright:   (c) eugenio.gigante 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import cv2
import datetime
import os
from datetime import date
import time
import sys
import numpy as np

def capture_video(cap):
    # Capture frame-by-frame
    for i in range(120):
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return
    # Check if the frame was captured successfully
    if not ret:
        print("Failed to capture frame")
        return
    today = date.today()
    # dd/mm/YY
    day = str(today.strftime("%d"))
    #print("d1 day =", d1)
    month = str(today.strftime("%m"))
    #print("d2 month =", d2)
    year = str(today.strftime("%Y"))
    #print("d3 year=", d3)

    # Generate a filename using the current date and time
    path = str("/home/pi/" + year + "/" + month + "/" + day + "/")
    #path = "C:\\tmp\\2023\\05\\28\\"
    filedate = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    aquisitionTime= datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    filename =  filedate + ".jpg"

    isExist = os.path.exists(path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)
        print("The new directory is created!")

    # path = 'D:/OpenCV/Scripts/Images'
    cv2.imwrite(os.path.join(path , filename), frame)
    print(path)
    print(filename)
    # Save the frame as a JPG file
    #cv2.imwrite(filename, frame)
    # Release the video capture object and close the window

    batScript = "SHIPID: 22 \nACQUISITION_TIME: " + aquisitionTime + "\n" + "IMG_QUALITY: 1 \nIMG_FREQUENCY: 3 \nIP: 10.142.132.195"
    filenameTxt =  filedate + ".txt"
    print(batScript)
    pathtxt =str("/home/pi/" + year + "/" + month + "/" + day + "/" + "/info/")
    isExist = os.path.exists(pathtxt)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(pathtxt)
        print("The new directory is created!")

    with open(pathtxt  + filenameTxt, 'w') as f:
        f.write(batScript)
    print("exit capture")
# Call the capture_video function

if __name__ == "__main__":
  # Open the default camera
  cap = cv2.VideoCapture(0)
  # Check if camera opened successfully
  if not cap.isOpened():
      print("Failed to open camera")
      sys.exit(0)
  # Set the video resolution to 640x480
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
  while True:
    capture_video(cap)
    time.sleep(30)
  cap.release()
  cv2.destroyAllWindows()
