import cv2
import mediapipe as mp
import pyautogui


def vir_mouse():
    # Initialize the video capture object to read from the webcam
    cap = cv2.VideoCapture(0)

    # Initialize MediaPipe's hand detector
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1)
    mp_draw = mp.solutions.drawing_utils

    # Get screen dimensions for cursor movement mapping
    screen_width, screen_height = pyautogui.size()

    while True:
        # Read a frame from the webcam
        success, frame = cap.read()
        if not success:
            break

        # Flip the frame horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)

        # Get frame dimensions
        frame_height, frame_width, _ = frame.shape

        # Convert the BGR image to RGB before processing
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame to detect hands
        results = hands.process(rgb_frame)
        landmarks = results.multi_hand_landmarks

        if landmarks:
            for hand_landmarks in landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Extract landmark positions
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

                # Convert landmark positions to screen coordinates
                index_x = int(index_finger_tip.x * frame_width)
                index_y = int(index_finger_tip.y * frame_height)
                thumb_x = int(thumb_tip.x * frame_width)
                thumb_y = int(thumb_tip.y * frame_height)

                # Map the index finger tip position to screen coordinates
                screen_x = int(screen_width / frame_width * index_x)
                screen_y = int(screen_height / frame_height * index_y)

                # Move the mouse cursor
                pyautogui.moveTo(screen_x, screen_y)

                # Draw circles on index finger tip and thumb tip
                cv2.circle(frame, (index_x, index_y), 10, (0, 255, 0), -1)
                cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 255, 0), -1)

                # Perform a click action if index finger tip and thumb tip are close enough
                if abs(index_y - thumb_y) < 20 and abs(index_x - thumb_x) < 20:
                    pyautogui.click()
                    pyautogui.sleep(1)  # Adding a small delay to prevent multiple clicks

        # Display the frame with landmarks and circles
        cv2.imshow("Virtual Mouse", frame)

        # Break the loop if the ESC key is pressed
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # Release the video capture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    vir_mouse()
