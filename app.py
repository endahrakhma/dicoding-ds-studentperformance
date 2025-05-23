# -*- coding: utf-8 -*-
"""
Created on Fri May 23 16:56:26 2025

@author: endah
"""

import streamlit as st
import pandas as pd
import joblib
import pickle
import base64
import numpy as np
from numpy.random import seed
seed(100)

import warnings
warnings.filterwarnings("ignore")

best_model = pickle.load(open('gb_best_model2.pkl', 'rb'))

# Fungsi untuk prediksi
def final_prediction(values, model):
    global prediction
    prediction = model.predict(values)
    return prediction

col1, col2, col3 = st.columns([1, 5, 1])

with col1:
    st.image("students.png", width=130)
with col2:
    st.header("Student's Performance App")
with col3:
    st.image("graduated.png", width=130)
    
data = pd.DataFrame()

with st.container(): 
    col1, col2 = st.columns(2)
     
    with col1:
        Tuition_fees_up_to_date = st.selectbox('Tuition_fees_up_to_date', (0,1))
        data["Tuition_fees_up_to_date"] = [Tuition_fees_up_to_date]
     
    with col2:
        Scholarship_holder = st.selectbox('Scholarship_holder', (0,1))
        data["Scholarship_holder"] = [Scholarship_holder]

with st.container():    
    col1, col2 = st.columns(2)
     
    with col1:
           
        Age_at_enrollment = int(st.number_input(label='Age_at_enrollment', value=23))
        data["Age_at_enrollment"] = Age_at_enrollment
     
    with col2:
        Application_mode = int(st.number_input(label='Application_mode', value=1))
        data["Application_mode"] = Application_mode

with st.container():    
    col1, col2 = st.columns(2)
     
    with col1:
           
        Admission_grade = int(st.number_input(label='Admission_grade', value=50.3))
        data["Admission_grade"] = Admission_grade
     
    with col2:
        Previous_qualification_grade = int(st.number_input(label='Previous_qualification_grade', value=150.5))
        data["Previous_qualification_grade"] = Previous_qualification_grade

with st.container():    
    col1, col2 = st.columns(2)
     
    with col1:
           
        Curricular_units_1st_sem_approved = int(st.number_input(label='Curricular_units_1st_sem_approved', value=11))
        data["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved
     
    with col2:
        Curricular_units_2nd_sem_evaluations = int(st.number_input(label='Curricular_units_2nd_sem_evaluations', value=15))
        data["Curricular_units_2nd_sem_evaluations"] = Curricular_units_2nd_sem_evaluations
        
if st.button('Predict'):
    #prediksi = best_model.predict(data)
    prediksi = int(final_prediction(data, best_model))
    mystyle = '''
    <style>
        f {
            text-align: center;
            font-weight: bold;
            font-weight: 100px
        }
    </style>
    '''
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=data, width=800, height=10)
        
    if (prediksi == 1):
        st.write(mystyle,'Graduate',unsafe_allow_html=True)
    else:
        st.write(mystyle,'Dropout',unsafe_allow_html=True)
    
    