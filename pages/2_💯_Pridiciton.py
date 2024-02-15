import streamlit as st
import model as md
import pandas as pd
import requests
from streamlit_lottie import st_lottie
def lottie(url:str):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

st.title("Predict the Apple Quality")
st.divider()

st.subheader("Size of Apple")
size = st.number_input("min: -8 , max: 7", -8.0, 7.0, value=None, placeholder='type here...',key=1)
st.write("Size of Apple :", size)
st.divider()

st.subheader("Weight of Apple")
weight = st.number_input("min: -8 , max: 6", -8.0, 6.0, value=None, placeholder='type here...',key=2)
st.write("Weight of Apple", weight)
st.divider()

st.subheader("Sweetness of Apple")
sweetness = st.number_input("min: -7 , max: 7", -7.0, 7.0, value=None, placeholder='type here...',key=3)
st.write("Sweetness of Apple", sweetness)
st.divider()

st.subheader("Crunchiness of Apple")
crunchiness = st.number_input("min: -6 , max: 8", -6.0, 8.0, value=None, placeholder='type here...',key=4)
st.write("Crunchiness of Apple", crunchiness)
st.divider()

st.subheader("Juiciness of Apple")
juiciness = st.number_input("min: -6 , max: 8", -6.0, 8.0, value=None, placeholder='type here...',key=5)
st.write("Juiciness of Apple", juiciness)
st.divider()

st.subheader("Ripeness of Apple")
ripeness = st.number_input("min: -6 , max: 8", -6.0, 8.0, value=None, placeholder='type here...',key=6)
st.write("Ripeness of Apple", ripeness)
st.divider()

st.subheader("Acidity of Apple")
acidity = st.number_input("min: 0 , max: 8", 0.0, 8.0, value=None, placeholder='type here...',key=7)
st.write("Acidity of Apple", acidity)
st.divider()

dataframe=pd.DataFrame(data=[[size,weight,sweetness,crunchiness,juiciness,ripeness,acidity]],columns=['Size', 'Weight', 'Sweetness', 'Crunchiness','Juiciness','Ripeness','Acidity'])
def result(data):
    result=md.clf.predict(data)
    if result == 1:
        return ( "It is a Good Quality Apple")
    else:
        return("It is a Bad Quality Apple")


if st.button("Result",type='primary'):
    st.write(result(dataframe))

ani=lottie("https://lottie.host/23a6be46-bff1-4ee3-8536-7fcf94bf625c/mxPiWvcl4w.json")
st_lottie(
    ani,
    speed=0.8,
    reverse=False,
    quality="high",
     loop=True,
    height=30,
    width=130,
    key='ani'
)