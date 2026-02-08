import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(page_title="Pothole & Crack Detection", layout="wide")

st.title("🕳️ Pothole & Crack Detection")

# Load pothole model
model = YOLO("best.pt")   # change name if your model file is different

uploaded_file = st.file_uploader("Upload road image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Detecting potholes & cracks..."):
        results = model.predict(image_np, conf=0.25)

    result = results[0]
    boxes = result.boxes
    names = result.names

    detected_labels = []
    pothole_count = 0
    crack_count = 0

    for box in boxes:
        cls = int(box.cls[0])
        label = names[cls]
        detected_labels.append(label)

        if label in ["pothole", "potholes"]:
           pothole_count += 1

        if label in ["crack", "cracks"]:
           crack_count += 1

    st.subheader("🔍 Detected Objects")
    st.write(detected_labels)

    st.subheader("📊 Detection Results")
    st.metric("🕳️ Potholes Detected", pothole_count)
    st.metric("裂 Cracks Detected", crack_count)

    # Show detection image
    res_img = result.plot()
    st.image(res_img, caption="Pothole & Crack Detection Output", use_column_width=True)
