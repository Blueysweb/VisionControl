import cv2
from controller import perform_action
from gestures import recognize_gesture, GestureStabilizer
import time

def open_camera(tracker):
    cap = cv2.VideoCapture(0)
    stabilizer = GestureStabilizer()
    last_action_time = 0
    is_active = False
    last_toggle_time = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame from camera.")
            break
        frame = tracker.find_hands(frame)
        landmarks = tracker.get_landmarks(frame)
        if landmarks:
            raw_gesture = recognize_gesture(landmarks)
            stabilized_gesture = stabilizer.update(raw_gesture)
            if stabilized_gesture == "FIST":
                current_time = time.time()
                if current_time - last_toggle_time > 10:
                    is_active = not is_active
                    last_toggle_time = current_time
            if is_active:
                current_time = time.time()
                if current_time - last_action_time > 5:
                    perform_action(stabilized_gesture)
                    last_action_time = current_time
            
            cv2.putText(
                    frame,
                    stabilized_gesture,
                    (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                    )
            print(f"Gesture: {stabilized_gesture}")
        status = "Active" if is_active else "Inactive"
        color = (0, 255, 0) if is_active else (0, 0, 255)
        cv2.putText(
                        frame,
                        status,
                        (10, 90),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        color,
                        2
                        )

        cv2.imshow("VisionControl", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
