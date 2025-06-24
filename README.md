# Real-Time Object Detection with YOLOv8, OpenCV, and Text-to-Speech (TTS)

This project uses the **YOLOv8** model to detect objects in real-time from your webcam feed and uses **Text-to-Speech (TTS)** to announce detected objects out loud. It's a hands-on example combining **Ultralytics YOLO**, **OpenCV**, and **pyttsx3** for audio feedback.

---

## Features

-  Captures video from your webcam in real-time
-  Runs YOLOv8 object detection on each frame
-  Draws bounding boxes and labels with confidence scores
-  Announces detected objects using `pyttsx3` (offline TTS)
-  Prevents repeated announcements too frequently

---

## Tech Stack

| Component | Technology        |
|----------|-------------------|
| Object Detection | YOLOv8 (`ultralytics`) |
| Video Input | OpenCV (`cv2`)  |
| Text-to-Speech | pyttsx3      |
| Language | Python 3.x        |

---

##  Requirements

Install the required packages using:

```bash
pip install -r requirements.txt
