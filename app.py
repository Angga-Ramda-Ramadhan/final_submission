import streamlit as st
import pickle
import numpy as np

# Load model
with open("final_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Student Performance Classifier")

st.write("Masukkan data mahasiswa untuk prediksi klasifikasi performa.")

# Input fields
previous_qualification_grade = st.number_input("Previous Qualification Grade", min_value=0.0, max_value=200.0, value=120.0)
age_at_enrollment = st.number_input("Age at Enrollment", min_value=15, max_value=70, value=20)
cu1_enrolled = st.number_input("1st Sem Enrolled Units", min_value=0, max_value=10, value=6)
cu1_evaluations = st.number_input("1st Sem Evaluations", min_value=0, max_value=10, value=6)
cu1_approved = st.number_input("1st Sem Approved Units", min_value=0, max_value=10, value=6)
cu1_grade = st.number_input("1st Sem Grade", min_value=0.0, max_value=20.0, value=12.0)
cu2_enrolled = st.number_input("2nd Sem Enrolled Units", min_value=0, max_value=10, value=6)
cu2_evaluations = st.number_input("2nd Sem Evaluations", min_value=0, max_value=10, value=6)
cu2_approved = st.number_input("2nd Sem Approved Units", min_value=0, max_value=10, value=6)
cu2_grade = st.number_input("2nd Sem Grade", min_value=0.0, max_value=20.0, value=13.0)

application_mode = st.number_input("Application Mode (e.g., 1-40)", min_value=0, max_value=50, value=17)
course = st.number_input("Course Code", min_value=0, max_value=9999, value=171)
mothers_qualification = st.number_input("Mother's Qualification", min_value=0, max_value=40, value=19)
fathers_qualification = st.number_input("Father's Qualification", min_value=0, max_value=40, value=12)
mothers_occupation = st.number_input("Mother's Occupation", min_value=0, max_value=10, value=5)
fathers_occupation = st.number_input("Father's Occupation", min_value=0, max_value=10, value=9)

tuition_fees_up_to_date = st.selectbox("Tuition Fees Up To Date?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

# Make prediction
if st.button("Predict"):
    features = np.array([[previous_qualification_grade, age_at_enrollment,
                          cu1_enrolled, cu1_evaluations, cu1_approved, cu1_grade,
                          cu2_enrolled, cu2_evaluations, cu2_approved, cu2_grade,
                          application_mode, course, mothers_qualification, fathers_qualification,
                          mothers_occupation, fathers_occupation, tuition_fees_up_to_date]])
    
    prediction = model.predict(features)[0]
    
    st.success(f"Prediction Result: {prediction}")
