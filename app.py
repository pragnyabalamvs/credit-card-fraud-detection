import streamlit as st
import numpy as np
import joblib

model = joblib.load('fraud_model.pkl')

st.set_page_config(page_title="Credit Card Fraud Detection", page_icon="💳")
st.title("💳 Credit Card Fraud Detection App")
st.write("Enter transaction details below to predict whether it's legitimate or fraudulent.")

st.subheader("Enter Transaction Details")

col1, col2, col3 = st.columns(3)

with col1:
    time = st.number_input("Time (seconds)", value=0.0)
    v1 = st.number_input("V1", value=0.0)
    v2 = st.number_input("V2", value=0.0)
    v3 = st.number_input("V3", value=0.0)
    v4 = st.number_input("V4", value=0.0)
    v5 = st.number_input("V5", value=0.0)
    v6 = st.number_input("V6", value=0.0)
    v7 = st.number_input("V7", value=0.0)
    v8 = st.number_input("V8", value=0.0)
    v9 = st.number_input("V9", value=0.0)

with col2:
    v10 = st.number_input("V10", value=0.0)
    v11 = st.number_input("V11", value=0.0)
    v12 = st.number_input("V12", value=0.0)
    v13 = st.number_input("V13", value=0.0)
    v14 = st.number_input("V14", value=0.0)
    v15 = st.number_input("V15", value=0.0)
    v16 = st.number_input("V16", value=0.0)
    v17 = st.number_input("V17", value=0.0)
    v18 = st.number_input("V18", value=0.0)
    v19 = st.number_input("V19", value=0.0)

with col3:
    v20 = st.number_input("V20", value=0.0)
    v21 = st.number_input("V21", value=0.0)
    v22 = st.number_input("V22", value=0.0)
    v23 = st.number_input("V23", value=0.0)
    v24 = st.number_input("V24", value=0.0)
    v25 = st.number_input("V25", value=0.0)
    v26 = st.number_input("V26", value=0.0)
    v27 = st.number_input("V27", value=0.0)
    v28 = st.number_input("V28", value=0.0)
    amount = st.number_input("Transaction Amount", value=0.0)

input_data = np.array([[time, v1, v2, v3, v4, v5, v6, v7, v8, v9,
                        v10, v11, v12, v13, v14, v15, v16, v17, v18, v19,
                        v20, v21, v22, v23, v24, v25, v26, v27, v28, amount]])

if st.button("🔍 Predict Fraud"):
    prediction = model.predict(input_data)
    prob = model.predict_proba(input_data)[0][1]
    st.subheader("Prediction Result:")
    if prediction[0] == 1:
        st.error(f"🚨 Fraudulent Transaction Detected! (Probability: {prob:.2%})")
    else:
        st.success(f"✅ Legitimate Transaction (Probability of Fraud: {prob:.2%})")

st.markdown("---")
st.markdown("Developed by **Your Name** | Deployed with Streamlit Cloud 🌐")
