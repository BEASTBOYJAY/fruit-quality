import streamlit as st
import requests
from streamlit_lottie import st_lottie
st.set_page_config(
    page_title="Project",
    page_icon="✨"
)

st.sidebar.success("Select the pages above")

def load_ani(url:str):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


ani=load_ani('https://lottie.host/1866eee0-f8a9-4e3c-ab6d-c77019d9d863/x7gh7SNcRn.json')
st_lottie(
    ani,
    speed=1.5,
    reverse=False,
    loop=True,
    quality="high",
    height=None,
    width=None,
    key=None,
)
st.header("This is the Project on the Predicting the Apple Quality")
st.divider()
st.write("First Page is Based on Data and its Visualization")
st.write("Second Page is Based on Predicing the Apple Quality")
