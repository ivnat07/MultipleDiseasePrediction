import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    

working_dir = os.path.dirname(os.path.abspath(__file__))



diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

cancer_model = pickle.load(open(f'{working_dir}/saved_models/breast_cancer_model.sav', 'rb'))





with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person','person'],
                           default_index=0)



if selected == 'Breast Cancer Prediction':


    st.title('Breast Cancer Prediction using ML')


    col1, col2, col3 = st.columns(3)

    with col1:
        mean_radius = st.text_input('Mean Radius')

    with col2:
        mean_texture = st.text_input('Mean Texture')

    with col3:
        mean_perimeter = st.text_input('Blood Pressure value')

    with col1:
        mean_area = st.text_input('Mean area value')

    with col2:
        mean_smoothness = st.text_input('Smoothness Level')

    



    cancer_diagnosis = ''



    if st.button('Breast Cancer Test Result'):

        user_input = [mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness]

        user_input = [float(x) for x in user_input]

        cancer_prediction = cancer_model.predict([user_input])

        if cancer_prediction[0] == 1:
            cancer_diagnosis = 'The person has cancer'
        else:
            cancer_diagnosis = 'The person does not have cancer'

    st.success(cancer_diagnosis)

if selected == 'Diabetes Prediction':


    st.title('Diabetes Prediction using ML')


    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')



    diab_diagnosis = ''



    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)
