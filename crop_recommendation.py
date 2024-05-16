import streamlit as st
import pickle
import numpy as np

def main():
    # Load the ML model
    with open('ml.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    # Function to predict crop based on user inputs
    def predict_crop(n, p, k, temp, humidity,ph, rainfall):
        input_features = np.array([[n, p, k, temp, humidity,ph, rainfall]])
        prediction = model.predict(input_features)
        return prediction[0]

    # Streamlit app layout
    st.title('AgroExpert: Crop Recommendation System')
    

    # User input fields
    n = st.number_input('Nitrogen (N)', value=0, step=1)
    p = st.number_input('Phosphorus (P)', value=0, step=1)
    k = st.number_input('Potassium (K)', value=0, step=1)
    temp = st.number_input('Temperature (°C)', value=0.0, step=0.1)
    humidity = st.number_input('Humidity (%)', value=0.0, step=0.1)
    ph = st.number_input('pH', value=0.0, step=0.1)
    rainfall = st.number_input('Rainfall (mm)', value=0.0, step=0.1)
    

    # Button to trigger prediction
    if st.button('Get Recommendation'):
        if n == 0 or p == 0 or k == 0 or temp == 0.0 or humidity == 0.0 or ph == 0.0 or rainfall == 0.0:
            st.warning("Please enter all the information.")
        else:
            crop_prediction = predict_crop(n, p, k, temp, humidity, rainfall, ph)
            st.success(f'The recommended crop is: {crop_prediction}')

if __name__ == "__main__":
    main()
