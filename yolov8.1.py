import cv2
import threading
import queue
import time
from ultralytics import YOLO
import pyttsx3

# --- Setup YOLOv8 Model ---
model = YOLO("yolov8n.pt")

# --- Initialize TTS Engine and Queue ---
engine = pyttsx3.init()
tts_queue = queue.Queue()

def tts_worker():
    """Process the TTS queue continuously."""
    while True:
        text = tts_queue.get()
        if text is None:  # Exit signal
            break
        engine.say(text)
        engine.runAndWait()
        tts_queue.task_done()

# Start the TTS thread.
threading.Thread(target=tts_worker, daemon=True).start()

def flush_queue(q):
    """Flush all items from the queue."""
    while not q.empty():
        try:
            q.get_nowait()
        except queue.Empty:
            break

# --- Open Webcam ---
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

last_announce = 0
announce_interval = 2  # seconds between announcements

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Run YOLOv8 detection on the frame
    results = model(frame)
    detected = set()

    # Process detection results and draw bounding boxes
    for res in results:
        if hasattr(res, "boxes") and res.boxes is not None:
            for box in res.boxes:
                cls_id = int(box.cls.cpu().numpy()[0])
                confidence = float(box.conf.cpu().numpy()[0]) * 100  # Convert to percentage
                label = f"{model.names.get(cls_id, str(cls_id))} ({confidence:.2f}%)"
                detected.add(label)
                
                # Get bounding box coordinates
                coords = box.xyxy.cpu().numpy()[0]
                x1, y1, x2, y2 = map(int, coords)
                
                # Draw bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                
                # Display label with confidence score
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Announce detected objects at fixed intervals
    if detected and (time.time() - last_announce > announce_interval):
        flush_queue(tts_queue)
        tts_queue.put(", ".join(detected))
        last_announce = time.time()

    cv2.imshow("YOLOv8 Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
tts_queue.put(None)  # Signal TTS thread to exit
