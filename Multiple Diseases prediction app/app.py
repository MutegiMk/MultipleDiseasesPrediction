import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#Loading models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))


# sidebar navigation

with st.sidebar:
    selection = option_menu('Multiple Disease Prediction App',
    ['Diabetes Prediction',
    'Heart Disease Prediction',
    'Parkinsons disease Prediction'],
    icons = ['activity', 'heart', 'person'],
    default_index = 0)

#Diabetes Prediction page
if (selection == 'Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction using MachineLearning')

    #columns for input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', key='x12')

    with col2:
        Glucose = st.text_input('Glucose level', key='x22')

    with col3:
        BloodPressure = st.text_input('Blood Presure Count', key='x32')

    with col1:
        SkinThickness = st.text_input('SkinThickness value', key='x42')

    with col2:
        Insulin = st.text_input('Insulin level', key='x52')

    with col3:
        BMI = st.text_input('BMI value', key='x62')

    with col1:
        DiabetesPedigreeFunction =st.text_input('Diabetes Pedigree Function value', key='x72')

    with col2:
        Age = st.text_input('Your Age', key='x83')


    diabetes_diagnosis = ''

    if st.button('Diabetes Test Results'):
        diab_prediction = diabetes_model.predict([[
            Pregnancies, Glucose, BloodPressure, SkinThickness,
            Insulin, BMI, DiabetesPedigreeFunction, Age
        ]])

        if (diab_prediction[0]==1):
            diabetes_diagnosis = 'Your Diabetic'

        else:
            diabetes_diagnosis = 'Your Free From Diabetes'

    st.success(diabetes_diagnosis)


# Heart disease Prediction pages
if (selection == 'Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Prediction using MachineLearning')

    #columns for input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Your Age')

    with col2:
        sex = st.number_input('Gender Type')

    with col3:
        cp = st.number_input('Chest Pain Types')

    with col1:
        trestbps = st.number_input('Resting Blood Pressure')

    with col2:
        chol = st.number_input('Serum cholestoral in mg/dL')

    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dL')

    with col1:
        restecg =st.number_input('Resting Electrocariographic Results')

    with col2:
        thalach = st.number_input('Maximum Heart Rate Achieved')

    with col3:
        exang = st.number_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.number_input('St Depression Induced By Exercise')

    with col2:
        slope = st.number_input('Slope Of The Peak Exercise')

    with col3:
        ca = st.number_input('Vessels Colored by Flourosopy')

    with col1:
        thal = st.number_input('Thalassemia (0 = normal; 1 = fixed defect; 2 = reversable defect)')



    heart_diagnosis = ''

    if st.button('Heart Disease Test Results'):
        heart_prediction = heart_disease_model.predict([[
            age, sex, cp, trestbps, chol, fbs, restecg,
            thalach,exang, oldpeak, slope, ca, thal
        ]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'You Have Heart Disease'

        else:
            diabetes_diagnosis = 'Free From Heart Disease'

    st.success(heart_diagnosis)


# Parkinsons disease prediction page

if (selection == 'Parkinsons disease Prediction'):
    #page title
    st.title('Parkinsons disease Prediction using MachineLearning')

    #columns for input fields
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.text_input('MDVP:fO(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_p = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ =st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        Shimmer_ap = st.text_input('Shimmer:APQ3')

    with col2:
        Shimmer_aq5 = st.text_input('Shimmer:APQ5')

    with col3:
        Shimmer_pq = st.text_input('MDVP:APQ)')

    with col4:
        Shimmer_dda = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        Spread1 = st.text_input('Spread1')

    with col5:
        Spread2 = st.text_input('Spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')



    parkinson_diagnosis = ''

    if st.button('Parkinson Disease Test Results'):
        parkinson_prediction = parkinsons_model.predict([[
            fo, fhi, flo, Jitter_p, Jitter_Abs, RAP, PPQ,
            DDP,Shimmer, shimmer_dB, Shimmer_ap, Shimmer_aq5,
            Shimmer_pq, Shimmer_dda, NHR, HNR, RPDE, DFA, Spread1,
            Spread2, D2, PPE
        ]])

        if (parkinson_prediction[0] == 1):
            parkinson_diagnosis = 'You Have Parkinsons Disease'

        else:
            parknison_diagnosis = 'Free From Parkinsons Disease'

    st.success(parkinson_diagnosis)



#if (selection == 'Heart Disease Prediction'):
    #page title
    #st.title('Heart Disease Prediction using MachineLearning')

#if (selection == 'Parkinsons disease Prediction'):
    #page title
    #st.title('Parkinsons disease Prediction using MachineLearning')
