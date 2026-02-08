import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

st.title("🌫 Air Quality Forecast (LSTM)")

st.write("Enter last 10 AQI / PM2.5 values")

# Load model
try:
    model = load_model("aqi_local_model.keras", compile=False)

    st.success("LSTM model loaded successfully")
except Exception as e:
    st.error(f"Model not loaded: {e}")

values = []
for i in range(10):
    val = st.number_input(f"Value {i+1}", min_value=0.0, max_value=1000.0, value=100.0)
    values.append(val)

if st.button("Predict Next AQI"):
    try:
        data = np.array(values).reshape(-1, 1)

        scaler = MinMaxScaler()
        scaled_data = scaler.fit_transform(data)

        X_input = scaled_data.reshape(1, 10, 1)

        with st.spinner("Predicting..."):
            prediction_scaled = model.predict(X_input)

        prediction = scaler.inverse_transform(prediction_scaled)

        st.success(f"✅ Predicted Next AQI: {prediction[0][0]:.2f}")

        series = np.append(values, prediction[0][0])

        plt.figure(figsize=(6,4))
        plt.plot(series, marker='o')
        plt.title("AQI Forecast")
        plt.xlabel("Time Step")
        plt.ylabel("AQI")
        st.pyplot(plt)

    except Exception as e:
        st.error(f"Prediction error: {e}")
