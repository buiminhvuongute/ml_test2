import streamlit as st
import pickle
import numpy as np


model = pickle.load(open('HeartDiseasePrediction.pkl','rb'))

# Tiêu đề của ứng dụng
st.title("Heart Disease Prediction")

# Nhập các thông số của bệnh nhân
bmi = st.number_input('BMI', min_value=10, max_value=100, value=25) 

smoking = st.selectbox('Smoking', ['Yes', 'No'])
smoking = 1 if smoking == 'Yes' else 0

AlcoholDrinking = st.selectbox('Alcohol Drinking', ['Yes', 'No'])
AlcoholDrinking = 1 if AlcoholDrinking == 'Yes' else 0

stroke = st.selectbox('Stroke', ['Yes', 'No'])
stroke = 1 if stroke == 'Yes' else 0

PhysicalHealth = st.number_input('Physical Health', min_value=0, max_value=30, value=25)

MentalHealth = st.number_input('Mental Health', min_value=0, max_value=30, value=25) 

DiffWalking = st.selectbox('Diff Walking', ['Yes', 'No'])
DiffWalking = 1 if DiffWalking == 'Yes' else 0

sex = st.selectbox('Sex', ['Male', 'Female'])
sex = 1 if sex == 'Male' else 0

age = st.number_input('Age', min_value=10, max_value=100, value=25) 

#race = st.selectbox('Race', ['White', 'Black'])

diabetic = st.selectbox('Diabetic', ['Yes', 'No'])
diabetic = 1 if diabetic == 'Yes' else 0

PhysicalActivity = st.selectbox('PhysicalActivity', ['Yes', 'No'])
PhysicalActivity = 1 if PhysicalActivity == 'Yes' else 0

GenHealth = st.selectbox('General Health', ['Poor', 'Fair', 'Good', 'Very Good', 'Excellent'])
if GenHealth == 'Poor':
    GenHealth = 0
elif GenHealth == 'Fair':
    GenHealth = 1
elif GenHealth == 'Good':
    GenHealth = 2
elif GenHealth == 'Very Good':
    GenHealth = 3
elif GenHealth == 'Excellent':
    GenHealth = 4


SleepTime = st.number_input('Sleep time', min_value=1, max_value=24, value=8)

asthma = st.selectbox('Asthma', ['Yes', 'No'])
asthma = 1 if asthma == 'Yes' else 0

KidneyDisease = st.selectbox('Kidney Disease', ['Yes', 'No'])
KidneyDisease = 1 if KidneyDisease == 'Yes' else 0

SkinCancer = st.selectbox('SkinCancer', ['Yes', 'No'])
SkinCancer = 1 if SkinCancer == 'Yes' else 0


# Tạo nút dự đoán
if st.button('Predict'):
    # Tạo mảng dữ liệu từ các giá trị đầu vào
    input_data = np.array([[bmi,smoking, AlcoholDrinking, stroke, PhysicalHealth, MentalHealth, DiffWalking, 
                            sex, age, diabetic, PhysicalActivity, GenHealth, SleepTime, asthma, KidneyDisease, SkinCancer]])
    

    # Dự đoán sử dụng mô hình đã tải
    prediction = model.predict(input_data)
    
    # Hiển thị kết quả
    if prediction[0] == 1:
        st.write("The patient is likely to have heart disease.")
    else:
        st.write("The patient is unlikely to have heart disease.")

