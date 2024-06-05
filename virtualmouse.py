def vir_mouse():
    import cv2
    import mediapipe as mp
    import pyautogui
    cap = cv2.VideoCapture(0)
    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()
    index_y = 0
    while True:
        _, frame = cap.read()
        frame_height, frame_width, _ = frame.shape
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame,hand)
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x*frame_width)
                    y = int(landmark.y*frame_height)
                    # print(x, y)
                    if id == 9:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        index_x = screen_width/frame_width*x
                        index_y = screen_height/frame_height*y
                        pyautogui.moveTo(index_x, index_y)
                    if id == 4:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        middle_x = screen_width/frame_width*x
                        middle_y = screen_height/frame_height*y
                        # pyautogui.moveTo(middle_x, middle_y)
                        print('outside', abs(middle_x - middle_y))
                        if abs(index_y - middle_y) < 25:
                            pyautogui.click(button='left')

        print(hands)
        cv2.imshow('virtual mouse', frame)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break


if __name__ == '__main__':
    vir_mouse()
















