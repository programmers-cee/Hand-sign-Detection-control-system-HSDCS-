import cv2  # this module is used for capturing image from the cam
from cvzone.HandTrackingModule import HandDetector
import numpy as np   # this module is used for solving matrix problem in programs
import math
import time
detector = HandDetector(maxHands=1)
cap = cv2.VideoCapture(0)  # 0 is the id number of webcam of the system
folder = "Data/up"
counter = 0
offset = 20  # this value will be used for shifting the imagesize of cropped images
imgSize = 300
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']  # bbox means bounding box
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8)*255
        imgCrop = img[y-offset:y + h+offset, x-offset:x + w+offset]  # mentioning the dimension of image

        imageCropShape = imgCrop.shape


        aspectRatio = h/w  # ratio of height to the width
        # this condition will be used for fixing the height of image
        if aspectRatio > 1:
            k = imgSize/h
            wCal = math.ceil(k*w)
            imgResize = cv2.resize(imgCrop, (wCal,imgSize))
            imageResShape = imgResize.shape
            wGap = math.ceil((imgSize-wCal)/2)
            imgWhite[0:imageResShape[0], wGap:wCal+wGap] = imgResize
        # this condition will be used for fixing the width of the image
        else:
            k = imgSize/w
            hCal = math.ceil(k*h)
            imgResize = cv2.resize(imgCrop, (imgSize,hCal))
            imageResShape = imgResize.shape
            hGap = math.ceil((imgSize-hCal)/2)
            imgWhite[hGap:hCal+hGap, :] = imgResize



        cv2.imshow("ImageCrop", imgCrop)  # this function show the crop size of original image
        cv2.imshow("ImageWhite", imgWhite)
    cv2.imshow("Image", img)  # this function shows the original image
    key = cv2.waitKey(1)
    if key == ord("s"):
        counter += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgWhite)
        print(counter)



