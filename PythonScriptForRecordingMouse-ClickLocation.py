# Python script for measuring cell migration through vascular bundle (Python 3.7.x)
# November 2019
# Written by Santiago Campuzano
# Open Computer Vision (OpenCV) based Python script for detecting mouse clicks on image 
# files. The script will detect, mark with a green circle, and record the location of a mouse- click # in the X,Y coordinate system. The user has the option to batch process images by providing
# the path to a folder containing images. The script will automatically export the data as an xlsx
# file. 
# OpenCV supports TIFF, JPEG, PNG and JPEG2000. To find out more about reading image files,
# please refer to the documentation page:
# https://docs.opencv.org/4.2.0/d4/da8/group__imgcodecs.html

# Import required packages
import cv2
import pandas as pd
import glob2 as glob
import os
import numpy as np

# Declare global variables and lists
images = []
my_listX = []
my_listY = []
x = 0
y = 0
AddColX = 0
AddColY = 0
tool = list(range(0, 1000))
df = pd.DataFrame({}, tool)

# mouse-click callback function. Each time a mouse click is detected, the function will append the x and y coordinates

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(n,(x,y),2,(0,255,0),-1)
        my_listX.append(x)
        my_listY.append(y)
 # Use glob.glob to batch upload images from the declared PATH.
Create separate excel columns for x and y coordinates. 

for img in glob.glob("PATH"):
    writer = pd.ExcelWriter("PATH", engine='xlsxwriter')
    ColX = "(X){}".format(os.path.basename(img))
    ColY = "(Y){}".format(os.path.basename(img))
    Text = "{}".format(img)
    n = cv2.imread(Text)
    cv2.namedWindow(Text)
    cv2.setMouseCallback(Text, draw_circle)
    images.append(Text)
    print(Text)

    while True:
        cv2.imshow(Text, n)

# Once the spacebar is pressed, the list will be added to the excel file
        if cv2.waitKey(10) == 32:
            print(my_listY)
            print(my_listX)
            cv2.destroyWindow(Text)
            dataX = np.array(my_listX)
            dataY = np.array(my_listY)
            df[ColX] = pd.Series(dataX)
            df[ColY] = pd.Series(dataY)
            del my_listY[:]
            del my_listX[:]
            break

df.to_excel(writer, sheet_name='Sheet1')
print(df)
writer.save()

