import streamlit as st
import pickle

# loading the saved model

crop_model=pickle.load(open('C:/Users/FRANK/Desktop/Crop_Recommendation System/crop_recommendation.sav','rb'))

st.title("CROP RECOMMENDATION SYSTEM")
col1,col2=st.columns(2)
with col1:
	N=st.text_input('Nitrogen Content in the soil')

with col2:
	P=st.text_input('Phosphorous Content in the soil')

with col1:
	K=st.text_input('Potassium Content in the soil')

with col2:
	temperature=st.text_input('Temperature in Degrees Celcius')

with col1:
	humidity=st.text_input('Relative Humidity in percentage')

with col2:
	ph=st.text_input('PH value of the soil')

with col1:
	rainfall=st.text_input('Rainfall in mm')


st.text('Which crop is recommended?')

if st.button("Predict Crop"):
	crop_prediction=crop_model.predict([[N,P,K,temperature,humidity,ph,rainfall]])
	st.success(crop_prediction)