import pickle
import streamlit as st
import numpy as np

# Load the trained model
with open("best_rf_model.sav", "rb") as model_file:
    model = pickle.load(model_file)

# Load the LabelEncoder
with open("label_encoder.sav", "rb") as encoder_file:
    encoder = pickle.load(encoder_file)

# Set Background Image
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{image_url}") no-repeat center center fixed;
            background-size: cover;
        }}
        div[data-testid="stForm"] {{
            background: rgba(255, 255, 255, 0.85);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        }}
        .result-box {{
            background: #ffffff;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            color: #333;
            margin-top: 20px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image
set_background("https://www.cultivation.hps.cam.ac.uk/sites/default/files/styles/leading/public/aboutbanner.png?itok=hJ6JU94p")

# Title and Header
st.title("🌾 Crop Prediction System")
st.markdown('<p class="info-text">Enter soil and environmental parameters to predict the most suitable crop for cultivation.</p>', unsafe_allow_html=True)

# Form for input fields
with st.form("crop_prediction_form"):
    st.subheader("🌱 Enter Soil and Weather Conditions")

    # Input fields
    N = st.number_input("Nitrogen (N)", min_value=1, max_value=140)
    P = st.number_input("Phosphorus (P)", min_value=1, max_value=150)
    K = st.number_input("Potassium (K)", min_value=1, max_value=210)
    temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=45.0)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0)
    ph = st.number_input("Soil pH Level", min_value=0.0, max_value=14.0)
    rainfall = st.number_input("Rainfall (mm)", min_value=20.0, max_value=300.0)

    # Submit button
    submitted = st.form_submit_button("🌿 Predict Crop")

# Prediction logic after form submission
if submitted:
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    recommended_crop = encoder.inverse_transform(prediction)  # Convert to actual crop name
    
    # Styled Result Box
    st.markdown(f"""
        <div class="result-box">
            🌱 <b>Recommended Crop:</b> {recommended_crop[0]}
        </div>
        """, unsafe_allow_html=True)
