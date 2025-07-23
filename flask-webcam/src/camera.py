import cv2
import threading
import time

_frame = None
_lock = threading.Lock()
_running = False
_thread = None
_camera_path = "/dev/video2"


def _reader():
    global _frame, _running
    cap = cv2.VideoCapture(_camera_path)
    if not cap.isOpened():
        print(f"ERROR: Could not open camera at {_camera_path}")
        _running = False
        return

    while _running:
        ret, frame = cap.read()
        if ret:
            with _lock:
                _frame = frame
        time.sleep(0.01)

    cap.release()


def _start_camera():
    """
    Starts a background thread that continuously reads frames from the camera.
    """
    # Check if not running in hot reloader
    global _running, _thread
    if _running:
        return
    _running = True
    _thread = threading.Thread(target=_reader, daemon=True)
    _thread.start()
    print("Camera thread started.")


def _get_latest_frame():
    """
    Returns the most recent frame captured by the shared camera thread.
    """
    with _lock:
        return _frame.copy() if _frame is not None else None


def generate_frames():
    fps = 10
    frame_count = 0

    _start_camera()

    while True:
        frame = _get_latest_frame()
        if frame is None:
            # print("No frame available, waiting for camera to start...")
            time.sleep(0.05)
            continue

        start_time = time.time()
        success, buffer = cv2.imencode(".jpg", frame)
        if not success:
            print("JPEG encoding failed")
            continue

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n"
        )

        elapsed_time = time.time() - start_time
        time.sleep(max(1.0 / fps - elapsed_time, 0))
        frame_count += 1
