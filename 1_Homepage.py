import streamlit as st 
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="SoScool", page_icon=":green_heart:")

st.title("Bienvenue dans l'application S'cool ")
st.sidebar.success("select a page above")
st.subheader('Ici vous trouverez la bonne école pour vos enfants facilement.')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_jfrjiyor.json")
st_lottie(lottie_coding, height=400, key="coding")
