import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(page_title="Smart City Detection", layout="wide")

st.title("🚦 Smart City: Traffic, Overcrowd & Accident Detection")

# Load model
model = YOLO("traffic_crowd_accident.pt")

uploaded_file = st.file_uploader("Upload a road image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Detecting objects..."):
        results = model.predict(image_np, conf=0.1)

    result = results[0]
    boxes = result.boxes
    names = result.names

    # DEBUG: show detected labels
    detected_labels = []
    for box in boxes:
        cls = int(box.cls[0])
        label = names[cls]
        detected_labels.append(label)

    st.write("Detected objects:", detected_labels)

    # Initialize counters
    people_count = 0
    vehicle_count = 0
    accident_detected = False

    vehicle_classes = ["car", "bus", "truck", "motorcycle", "auto_rickshaw"]

    # ✅ Correct counting loop
    for box in boxes:
        cls = int(box.cls[0])
        label = names[cls]

        if label == "person":
            people_count += 1

        if label in vehicle_classes:
            vehicle_count += 1

        if label.lower() == "accident":
            accident_detected = True

    # Crowd level
    if people_count > 30:
        crowd = "High"
    elif people_count > 10:
        crowd = "Medium"
    else:
        crowd = "Low"

    # Traffic level
    if vehicle_count > 20:
        traffic = "High"
    elif vehicle_count > 10:
        traffic = "Medium"
    else:
        traffic = "Low"

    st.subheader("📊 Detection Results")
    st.write(f"👥 People Count: {people_count}")
    st.write(f"🚗 Vehicle Count: {vehicle_count}")
    st.write(f"🚦 Traffic Level: {traffic}")
    st.write(f"👥 Crowd Level: {crowd}")

    if accident_detected:
        st.error("🚨 Accident Detected!")
    else:
        st.success("✅ No Accident Detected")

    # Show detection image
    res_img = result.plot()
    st.image(res_img, caption="Detection Output", use_column_width=True)
