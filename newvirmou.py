import cv2
import mediapipe as mp
import pyautogui

def vir_mouse():
    cap = cv2.VideoCapture(0)
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1)
    mp_draw = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()
    state = "move"  # Possible states: 'move', 'click', 'exit'

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        landmarks = results.multi_hand_landmarks

        if landmarks:
            for hand_landmarks in landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

                index_x = int(index_finger_tip.x * frame_width)
                index_y = int(index_finger_tip.y * frame_height)
                thumb_x = int(thumb_tip.x * frame_width)
                thumb_y = int(thumb_tip.y * frame_height)

                screen_x = int(screen_width / frame_width * index_x)
                screen_y = int(screen_height / frame_height * index_y)

                pyautogui.moveTo(screen_x, screen_y)

                cv2.circle(frame, (index_x, index_y), 10, (0, 255, 0), -1)
                cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 255, 0), -1)

                if abs(index_y - thumb_y) < 20 and abs(index_x - thumb_x) < 20:
                    if state == "move":
                        pyautogui.click()
                        state = "click"
                    elif state == "click":
                        state = "exit"
                        break
                    pyautogui.sleep(1)  # Adding a small delay to prevent multiple actions

        cv2.imshow("Virtual Mouse", frame)
        if state == "exit" or (cv2.waitKey(1) & 0xFF == 27):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    vir_mouse()
