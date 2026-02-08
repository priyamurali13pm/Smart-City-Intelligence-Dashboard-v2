import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(page_title="Traffic Detection", layout="wide")

st.title("🚦 Traffic Detection (Vehicles & Crowd)")

# Use pretrained YOLO for traffic
model = YOLO("yolov8n.pt")   # you can try yolov8s.pt for better accuracy

uploaded_file = st.file_uploader("Upload traffic image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Detecting traffic..."):
        results = model.predict(image_np, conf=0.25)

    result = results[0]
    boxes = result.boxes
    names = result.names

    detected_labels = []
    people_count = 0
    vehicle_count = 0

    vehicle_classes = ["car", "bus", "truck", "motorcycle"]

    for box in boxes:
        cls = int(box.cls[0])
        label = names[cls]
        detected_labels.append(label)

        if label == "person":
            people_count += 1

        if label in vehicle_classes:
            vehicle_count += 1

    st.subheader("🔍 Detected Objects")
    st.write(detected_labels)

    # Traffic level
    if vehicle_count > 20:
        traffic = "High"
    elif vehicle_count > 10:
        traffic = "Medium"
    else:
        traffic = "Low"

    # Crowd level
    if people_count > 30:
        crowd = "High"
    elif people_count > 10:
        crowd = "Medium"
    else:
        crowd = "Low"

    st.subheader("📊 Traffic Analysis")
    st.metric("👥 People Count", people_count)
    st.metric("🚗 Vehicle Count", vehicle_count)
    st.metric("🚦 Traffic Level", traffic)
    st.metric("👥 Crowd Level", crowd)

    # Show detection image
    res_img = result.plot()
    st.image(res_img, caption="Traffic Detection Output", use_column_width=True)
