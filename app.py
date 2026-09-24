import streamlit as st
import joblib
model=joblib.load(r"C:\Users\PowerTech\Desktop\pro_linear\salary_model.pkl")
st.set_page_config(page_title="Salary Prediction",page_icon="💰")

st.sidebar.title("Navigation")
page = st.sidebar.radio( "Go to", ["Home", "Salary Prediction"] )
if page == "Home":
    st.title("💰 Salary Prediction")
    st.subheader("Predict Salary Based on Years of Experience")
    st.write("This Machine Learning application uses "
        "Linear Regression to predict salary based "
        "on years of experience.")
    st.divider()
    st.subheader(" About the Project")
    st.write("The model was trained using a salary dataset "
        "containing years of experience and salary." )
elif page == "Salary Prediction":
    st.title("Salary Prediction")
    st.write( "Enter the number of years of experience "
        "to predict the salary.")
    years_experience = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, step=0.1)   
    if st.button(" Predict Salary"):
        prediction = model.predict( [[years_experience]])
        st.success( f"💰 Predicted Salary: ${prediction[0]:,.2f}")