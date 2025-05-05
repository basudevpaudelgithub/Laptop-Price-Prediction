
import streamlit as st
import numpy as np
import joblib

model = joblib.load('rf_model.pkl')   
st.title ("Laptop Price Prediction App")

st.divider()

st.write("With this app after using  the calculation button when you entered the values of processor_speed, ram size, and storage capacity, you can get a price estimation for the laptop you want")

st.divider()

processor_speed = st.number_input("Enter Processor Speed ", value=2.50, step=0.50)
ram_size = st.number_input("Enter RAM Size (GB)", value=16, step=8)
storage_capacity = st.number_input("Enter Storage Capacity (GB)", value=512, step=256)

X = [processor_speed, ram_size, storage_capacity]             
st.divider()
prediction = st.button("Price Estimation Button!")
st.divider()   

if prediction:
    st.balloons()
    x1 = np.array(X)
    prediction = model.predict([x1])[0]
    st.write(f"The estimated price of the laptop is {prediction: ,.2f}")
else:
    st.write(f"Plese use the button to get the price estimation")

