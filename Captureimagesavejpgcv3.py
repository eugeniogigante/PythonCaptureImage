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
from WebcamObject import WebcamObject
from WriteImage import WriteImage
from WriteLog import WriteLog

cap = cv2.VideoCapture(0)

def capture_video():
    camera = WebcamObject()
    writeImage = WriteImage()
    frame =  camera.getImg()
    
    today = date.today()
    aquisitionTime= datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    day = str(today.strftime("%d"))
    month = str(today.strftime("%m"))
    year = str(today.strftime("%Y"))
    # Generate a filename using the current date and time
    path = str("C:\\tmp\\" + year + "\\" + month + "\\" + day + "\\")
    writeImage.imgFile(path, frame)
    
    filenameTxt =  datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S") + ".txt"
    pathtxt =str("C:\\tmp\\" + year + "\\" + month + "\\" + day + "\\" + "\\info\\")
    writeLog = WriteLog()
    writeLog.logWrite(pathtxt, filenameTxt, "23")
    
if __name__ == "__main__":
    #main()
    capture_video()