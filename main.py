import cv2
import mediapipe as mp
import pyautogui
import numpy as np

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_x, index_y = 0, 0
prev_index_x, prev_index_y = 0, 0
smoothing_factor = 0.2  # Adjust smoothing factor for smoother tracking

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark

            # Index finger tip (id 8) for mouse movement
            index_tip = landmarks[8]
            x = int(index_tip.x * frame_width)
            y = int(index_tip.y * frame_height)
            cv2.circle(frame, (x, y), 10, (0, 255, 255), cv2.FILLED)

            # Calculate screen coordinates
            screen_x = screen_width / frame_width * x
            screen_y = screen_height / frame_height * y

            # Apply smoothing to the screen coordinates
            index_x = int(prev_index_x * (1 - smoothing_factor) + screen_x * smoothing_factor)
            index_y = int(prev_index_y * (1 - smoothing_factor) + screen_y * smoothing_factor)
            prev_index_x, prev_index_y = index_x, index_y

            # Thumb tip (id 4) for clicking action
            thumb_tip = landmarks[4]
            thumb_x = int(thumb_tip.x * frame_width)
            thumb_y = int(thumb_tip.y * frame_height)
            cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 255, 255), cv2.FILLED)

            # Check distance between index and thumb to trigger click
            distance = np.hypot(screen_x - thumb_x, screen_y - thumb_y)
            if distance < 20:
                pyautogui.click()
                pyautogui.sleep(0.1)  # Shorter delay for faster response
            else:
                pyautogui.moveTo(index_x, index_y)

    cv2.imshow('Virtual Mouse', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
