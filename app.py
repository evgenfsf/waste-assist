
import streamlit as st
import io
from PIL import Image
import requests
import numpy as np
import json
import time 
with open('params.json') as f:
    API_URL = json.load(f)['API_URL'] #remember to create this file with the API URL endpoint specified

#upload logo

st.title("Welcome to Waste-Assist!")

# logo = Image.open('/home/luis/code/luchovangal/wasteassistfront/logo.png')
# st.image(logo, width=400)

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

if st.button("Click here to classify your waste"):
    with open('test.jpg', "rb") as img:
        get_img = requests.post(f"{API_URL}/files", files={"file":img})
    #display prediction
    with st.spinner('Classifying...'):
        time.sleep(5)
    st.write(get_img.json()['prediction'])

