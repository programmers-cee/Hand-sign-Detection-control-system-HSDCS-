def volumesigndetecter():
    import cv2
    import mediapipe as mp
    import pyautogui
    x1 = y1 = 0
    x2 = y2 = 0
    webcam = cv2.VideoCapture(0)
    my_hands = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    while True:
        _, image = webcam.read()
        image = cv2.flip(image, 1)
        frame_height, frame_width, _ = image.shape
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        output = my_hands.process(rgb_image)
        hands = output.multi_hand_landmarks
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(image, hand)
                landmarks = hand.landmark
                for id , landmark in enumerate(landmarks):  # collecting landmarks from the hands
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    if id == 8:  # for the fourth finger id = 8 means ring finger
                        cv2.circle(img=image, center=(x, y), radius=8, color=(0, 255, 255), thickness=5)
                        x1 = x
                        y1 = y
                    if id == 4:  # for the thumb finger id = 8 means ring finger
                        cv2.circle(img=image, center=(x, y), radius=8, color=(0, 0, 255), thickness=5)
                        x2 = x
                        y2 = y
            dist = ((x2-x1)**2 + (y2-y1)**2)**(0.5)//4

            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)
            if dist > 25:
                pyautogui.press("volumeup")
            else:
                pyautogui.press("volumedown")

        cv2.imshow("Hand volume using python", image)
        key = cv2.waitKey(10)
        if key & 0xff == 27:  # 27 is code for esc key
            break
    webcam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    volumesigndetecter()
