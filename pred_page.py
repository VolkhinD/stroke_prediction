import pickle
import streamlit as st
import numpy as np
import pandas as pd


def load_model():
    with open ('model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
model = data['model']
def show_predict_page():
    st.title('Srtoke Prediction')
    st.write("""Some information needed""")
show_predict_page()
gen = ['Male', 'Female']
hyper = ["Yes", "No"]
heart_dis = ["Yes", "No"]
smoking_stat = ['never_smoked', 'formerly smoked', 'smokes']


gender = st.selectbox("Gender", gen)
age = st.number_input("Age", value=0)
hypertension = st.selectbox("Hypertension ", hyper)
heart_disease = st.selectbox("Heart Disease", heart_dis)
bmi = st.number_input('BMI')
smoking_status = st.selectbox("Smoking Status", smoking_stat)
ok = st.button("Calculate Probability") # True if clicked on button
if ok:
    X = np.array([gender, age, hypertension, heart_disease, bmi, smoking_status]).reshape(1, -1)
    X = pd.DataFrame(data=X, index=np.arange(len(X)), columns=['gender', 'age', 'hypertension', 'heart_disease', 'bmi', 'smoking_status'])
    X_transformed = model[0].transform(X)
    proba = model[1].predict_proba(X_transformed).reshape(-1,)
    ans = proba[1] * 100
    message = f"Probability that you have a stroke is {ans:.1f}%"
    st.subheader(message)
