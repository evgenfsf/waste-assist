from fastapi.param_functions import Body
import streamlit as st
import PIL
import io
from PIL import Image
import requests
import numpy as np

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

    #display prediction
    st.text("The material is classified as: pred ")


else:
    print('Image not found, please try again')

# string_img = Image.getdata(user_img)

if st.button("Click here to classify your waste"):
    # st.write(byte_im)
    with open('test.jpg', "rb") as img:
        get_img = requests.post('http://localhost:8000/files/', files={"file":img})
    st.write(get_img.json())
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
