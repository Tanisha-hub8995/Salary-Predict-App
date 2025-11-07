import streamlit as st

import numpy as np
import joblib
import matplotlib.pyplot as plt
st.title("Salary Estimation App💸")

st.divider()

years_at_company = st.number_input("Enter years at company",value=1,step=1, min_value = 0)
Job_Rate = st.number_input("Job Rate", value=3.5,step=0.5,min_value =0.0)

X = [years_at_company, Job_Rate]


model = joblib.load("linearmodel.pkl")

predict_button = st.button("Press for predicting the salary")



st.divider()
if predict_button:

    st.balloons()
    X1 = np.array([X])

    prediction = model.predict(X1)[0]
    st.divider()
    st.subheader("Visualization📊")

    fig, ax= plt.subplots()
    ax.bar(["Predicted Salary"],[prediction],color="black")
    ax.set_ylabel("salary")
    ax.set_title("Your predicted salary")
    st.pyplot(fig)

    
    

    st.write(f"Salary prediction is {prediction:,.2f}")





else:
    st.write("Please enter the value and press to the predit button")