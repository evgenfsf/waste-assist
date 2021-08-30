from fastapi.param_functions import Body
import streamlit as st
import io
from PIL import Image
import requests
import numpy as np
import json
with open('params.json') as f:
    API_URL = json.load(f)['API_URL'] #remember to create this file with the API URL endpoint specified

#upload logo

st.title("Welcome to Waste-Assist!")

# logo = Image.open('/home/luis/code/evgenfsf/waste-assist/raw_data/logo.png')
# st.image(logo, width=400)

#Creating image uploader

st.sidebar.title("Please upload an image")
uploaded_img = st.sidebar.file_uploader(" ",type=['png', 'jpg', 'jpeg'] )


if uploaded_img is not None:
    user_img = Image.open(uploaded_img)
    user_img.save("test.jpg")
    img_bytes = io.BytesIO()
    user_img.save(img_bytes, format='JPEG')
    # byte_im = img_bytes.getvalue()
    st.image(user_img)


else:
    print('Image not found, please try again')

# string_img = Image.getdata(user_img)

if st.button("Click here to classify your waste"):
    # st.write(byte_im)
    with open('test.jpg', "rb") as img:
        get_img = requests.post(f"{API_URL}/files", files={"file":img})
    #display prediction
    st.write(get_img.json()['prediction'])
    # prediction=requests.get('http://localhost:8000/predict',params={'user_img':user_img})
    # st.write(prediction)


# enter here the address of your flask api
# url = ''

# response = requests.get(url, params=params)

# prediction = response.json()

# pred = prediction['prediction']

# pred

# For newline
# st.sidebar.write('\n')

# if st.button("Click here to classify your waste"):

#     if uploaded_img is None:

#         st.sidebar.write("Please upload your photo")

#     else:

#         # for when we have the prediction
#         with st.spinner('Predicting material...'):
#             st.text("The material is classified as: pred ")
