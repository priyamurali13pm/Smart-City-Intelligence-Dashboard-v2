import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.title("💡 Streetlight (Traffic Light) Detection")

model = YOLO("yolov8n.pt")

uploaded_file = st.file_uploader("Upload traffic light image", type=["jpg","png","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)

    st.image(image, use_column_width=True)

    results = model.predict(image_np, conf=0.25)

    result = results[0]
    boxes = result.boxes
    names = result.names

    detected_labels = []
    streetlight_count = 0

    for box in boxes:
        cls = int(box.cls[0])
        label = names[cls].lower()
        detected_labels.append(label)

        if label == "traffic light":
            streetlight_count += 1

    st.write("Detected objects:", detected_labels)
    st.metric("💡 Streetlights Detected", streetlight_count)

    res_img = result.plot()
    st.image(res_img, caption="Streetlight Detection Output", use_column_width=True)
