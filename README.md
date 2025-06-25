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

downloading yolov3.weights
📥 download_weights.py
python
Copy
Edit
import os
import urllib.request

def download_yolov3_weights():
    weights_url = "https://pjreddie.com/media/files/yolov3.weights"
    weights_path = "yolov3.weights"

    if not os.path.exists(weights_path):
        print("📦 Downloading YOLOv3 weights...")
        urllib.request.urlretrieve(weights_url, weights_path)
        print("✅ Download complete: yolov3.weights")
    else:
        print("✅ yolov3.weights already exists. Skipping download.")

if __name__ == "__main__":
    download_yolov3_weights()
✅ How to Use
After cloning the repo, just run:

bash
Copy
Edit
python download_weights.py
It will download the yolov3.weights file only if it's not already present.

🔗 Optional Update to README.md
Under 📁 Files Needed, update it like this:

markdown
Copy
Edit
### 📥 Auto-download Weights

Run this to download `yolov3.weights`:

```bash
python download_weights.py
yaml
Copy
Edit


