import cv2

def read_qr_from_image(path):
    img = cv2.imread(path)
    if img is None:
        print("Could not open image.")
        return None
    data, _, _ = cv2.QRCodeDetector().detectAndDecode(img)
    return data or None

def read_qr_from_webcam():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open webcam.")
        return None
    detector = cv2.QRCodeDetector()
    print("Show the QR to the camera. Press q to cancel.")
    result = None
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        data, _, _ = detector.detectAndDecode(frame)
        if data:
            result = data
            break
        cv2.imshow("Scan QR", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
    return result

import time
from attendance import mark_attendance

def scan_continuously(students):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open webcam.")
        return
    detector = cv2.QRCodeDetector()
    print("Scanning... press q in the camera window to stop.")
    last_seen = ""
    last_time = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        data, _, _ = detector.detectAndDecode(frame)
        if data and (data != last_seen or time.time() - last_time > 3):
            mark_attendance(data, students)
            last_seen = data
            last_time = time.time()
        cv2.imshow("Scan QR - press q to stop", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()