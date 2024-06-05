def handdetect():
    import cv2
    from cvzone.HandTrackingModule import HandDetector
    import numpy as np
    offset = 20
    imgSize = 300
    cap = cv2.VideoCapture(0)
    detector = HandDetector(maxHands=2)
    while True:
        success, img = cap.read()
        hands, img = detector.findHands(img)
        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']
            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8)*255
            imgCrop = img[y-offset:y+h+offset, x-offset:x + w+offset]
            imgCropShape = imgCrop.shape  # for height and width
            # imgWhite[0:imgCropShape[0], 0:imgCropShape[1]] = imgCrop
            # Resize imgCrop to match the shape of imgWhite
            imgCropResized = cv2.resize(imgCrop, (imgWhite.shape[1], imgWhite.shape[0]))  # assigning the dimensions values
            # Assign resized imgCrop to imgWhite
            imgWhite[0:imgCropResized.shape[0], 0:imgCropResized.shape[1]] = imgCropResized
            cv2.imshow("ImageCrop", imgCrop)
            cv2.imshow("ImageWhite", imgWhite)

        cv2.imshow("Image", img)
        cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    handdetect()