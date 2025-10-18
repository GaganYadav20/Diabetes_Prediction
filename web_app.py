import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('diabetes_prediction_model.sav', 'rb'))

def predict_diabetes(input_data):
    input_data_as_np_arr = np.array(input_data)
    input_data_reshape = input_data_as_np_arr.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshape)

    if prediction[0] == 0:
        return "The person is not diabetic"
    else:
        return "The person is diabetic"

def main():
    st.title("Diabetic Prediction Web App")

    Pregnancies=st.text_input("Number of Pregnancies")
    Glucose=st.text_input("Glucose Level")
    BloodPressure=st.text_input("Blood Pressure Value")
    SkinThickness=st.text_input("Skin Thickness Value")
    Insulin=st.text_input("Insulin Level")
    BMI=st.text_input("BMI Value")
    DiabetesPedigreeFunction=st.text_input("Diabetic Pedigree Function Value")
    Age=st.text_input("Age of the Person")

    diagnosis=''

    if st.button("Diabetes Test Result"):
        diagnosis=predict_diabetes([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

    st.success(diagnosis)

if __name__=='__main__':
    main()