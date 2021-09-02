
import streamlit as st
import io
from PIL import Image
import requests
import numpy as np
import json
import time 
with open('params.json') as f:
    API_URL = json.load(f)['API_URL'] #remember to create this file with the API URL endpoint specified

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


#upload logo

# st.title("Welcome to Waste-Assist!")

st.markdown(""" <style> .font {
font-size:100px ; font-family: 'Cooper Black'; color: #5d941e;} 
</style> """, unsafe_allow_html=True)
st.markdown('<p class="font">Welcome to WasteAssist</p>', unsafe_allow_html=True)

logo = Image.open('logo.png')
st.image(logo, width=200)

#Creating image uploader

st.sidebar.title("Please upload an image")
uploaded_img = st.sidebar.file_uploader(" ",type=['jpg', 'jpeg'] )


if uploaded_img is not None:
    user_img = Image.open(uploaded_img)
    user_img.save("test.jpg")
    img_bytes = io.BytesIO()
    user_img.save(img_bytes, format='JPEG')
    # byte_im = img_bytes.getvalue()
    st.image(user_img)


else:
    print('Image not found, please try again')

with st.spinner('Classifying...'):
        
    if st.button("Click here to classify your waste"):
        with open('test.jpg', "rb") as img:
            get_img = requests.post(f"{API_URL}/files", files={"file":img})
    #display prediction
        pred = get_img.json()['prediction']
            st.markdown(f"This is **{pred}**, it's recycable, please remember to rinse the container")

    



