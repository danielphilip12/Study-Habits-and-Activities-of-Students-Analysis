import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

model = joblib.load('class.pkl')
scaler = joblib.load('scaler.pkl')

study_hours = st.slider("Study Hours", min_value=0.0, max_value=24.0, value=8.0, step=0.1)
extracurricular_hours = st.slider("Extracurricular Hours", min_value=0.0, max_value=24.0, value=8.0, step=0.1)
sleep_hours = st.slider("Sleep Hours", min_value=0.0, max_value=24.0, value=8.0, step=0.1)
social_hours = st.slider("Social Hours", min_value=0.0, max_value=24.0, value=8.0, step=0.1)
pt_hours = st.slider("Physical Activity Hours", min_value=0.0, max_value=24.0, value=8.0, step=0.1)

user_input = pd.DataFrame({
    'Study_Hours': [study_hours],
    'Extracurricular_Hours': [extracurricular_hours],
    'Sleep_Hours': [sleep_hours],
    'Social_Hours': [social_hours],
    'Physical_Activity_Hours': [pt_hours]
})

total = study_hours + extracurricular_hours + sleep_hours + social_hours + pt_hours
st.write(f"Total Hours: {total}")
if total > 24:
    st.write(":red[WARNING: more than 24 hours inputted]")

st.dataframe(user_input)

scaled_input = scaler.transform(user_input)
    # st.dataframe(scaled_input)
prediction = model.predict(scaled_input)[0]

if prediction == "Low":
    st.write(f"The model predicts: :green[{prediction}]")
elif prediction == "Moderate":
    st.write(f"The model predicts: :yellow[{prediction}]")
elif prediction == "High":
    st.write(f"The model predicts: :red[{prediction}]")



# if st.button("Run Model"):
#     scaled_input = scaler.transform(user_input)
#     # st.dataframe(scaled_input)
#     prediction = model.predict(scaled_input)[0]

#     st.write(f"The model predicts: {prediction}")