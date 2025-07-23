import cv2
import time

cap = cv2.VideoCapture(
    "/dev/video2"
)  # Use 0 for webcam or replace with video file path


def generate_frames():
    fps = 10  # approximate, adjust if needed
    frame_count = 0

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("End of video.")
            break

        start_time = time.time()
        _, buffer = cv2.imencode(".jpg", frame)

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n"
        )
        elapsed_time = time.time() - start_time
        time.sleep(max(1.0 / fps - elapsed_time, 0))
        frame_count += 1
