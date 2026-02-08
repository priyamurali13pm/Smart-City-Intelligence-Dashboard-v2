import streamlit as st
import cv2
import numpy as np
import tempfile
from ultralytics import YOLO

st.set_page_config(page_title="Accident Detection", layout="wide")
st.title("🚑 Accident Detection (Image & Video)")

# Load model
model = YOLO("traffic_crowd_accident.pt")  # change name if needed

# Show class names once (for debugging)
# st.write(model.names)

mode = st.radio("Select Input Type:", ["Image", "Video"])

# ---------------- IMAGE MODE ----------------
if mode == "Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        img = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)

        results = model(img, conf=0.25)

        filtered_boxes = []
        accident_count = 0

        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            if label in ["accident", "crash"]:   # use your exact label name
                filtered_boxes.append(box)
                accident_count += 1

        results[0].boxes = filtered_boxes
        annotated_img = results[0].plot()

        st.image(annotated_img, channels="BGR", caption="Accident Detection Result")
        st.success(f"Accidents detected: {accident_count}")
        st.write(model.names)



# ---------------- VIDEO MODE ----------------
elif mode == "Video":
    video_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

    if "stop" not in st.session_state:
        st.session_state.stop = False

    col1, col2 = st.columns(2)
    with col1:
        start_btn = st.button("▶ Start Detection")
    with col2:
        stop_btn = st.button("⛔ Stop Detection")

    if stop_btn:
        st.session_state.stop = True

    if video_file and start_btn:
        st.session_state.stop = False

        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(video_file.read())

        cap = cv2.VideoCapture(tfile.name)
        frame_window = st.empty()
        label_window = st.empty()

        while cap.isOpened():
            if st.session_state.stop:
                st.warning("Detection stopped by user.")
                break

            ret, frame = cap.read()
            if not ret:
                st.success("Video finished.")
                break

          
            results = model(frame, conf=0.4)

            # ✅ CREATE detected_labels here
            detected_labels = []
            for box in results[0].boxes:
                cls_id = int(box.cls[0])
                label = model.names[cls_id]
                detected_labels.append(label)

            annotated = results[0].plot()

            frame_window.image(annotated, channels="BGR")
            label_window.write("Detected objects: " + ", ".join(detected_labels))

        cap.release()
