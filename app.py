from fastapi.param_functions import Body

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

st.markdown(""" <style> .font {
font-size:60px ; font-family: 'Serif'; color: #5d941e; margin-top: -100px}
</style> """, unsafe_allow_html=True)
st.markdown('<p class="font">Welcome to WasteAssist!</p>', unsafe_allow_html=True)


##Creating image uploader

# #upload logo
logo = Image.open('logo2.jpg')
st.sidebar.image(logo, width=300)

st.sidebar.title("How to...")
st.sidebar.markdown("1. Upload a photo")
st.sidebar.markdown('2. Click the "classify" button')
st.sidebar.markdown("3. Wait for the result")
uploaded_img = st.sidebar.file_uploader(" ",type=['jpg', 'jpeg'] )

if uploaded_img is not None:
    user_img = Image.open(uploaded_img)
    user_img_resize = user_img.resize((400,400))
    user_img_show = user_img.resize((300,300))
    user_img_resize.save("test.jpg")
    # img_bytes = io.BytesIO()
    # user_img.save(img_bytes, format='JPEG')
    # byte_im = img_bytes.getvalue()
    st.image(user_img_show)


else:
    print('Image not found, please try again')

# string_img = Image.getdata(user_img)

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
with st.spinner('Be patient, saving the world takes time ...'):

    if st.button("Classify your waste"):
        with open('test.jpg', "rb") as img:
            get_img = requests.post(f"{API_URL}/files", files={"file":img})
    #display prediction
        pred = get_img.json()['prediction'].capitalize()
        st.markdown(f"## This appears to be:")
        st.markdown(f"## **{pred}**")
        if pred == "Glass":
            st.markdown("### :recycle: It's recycable!")
            st.markdown("### :bulb: Useful tip: Rinse bottle and jars to remove food waste")
        elif pred =="Cardboard":
            st.markdown("### :recycle: It's recycable!")
            st.markdown("### :bulb: Useful tip: Keep it dry and remove contaminants such as plastic")
        elif pred =="Paper":
            st.markdown("### :recycle: It's recycable!")
            st.markdown("### :bulb: Useful tip: Keep it unshredded and dry ")
        elif pred =="Plastic":
            st.markdown("### :recycle: It's recycable!")
            st.markdown("### :bulb: Useful tip: Rinse bottle and jars to remove food waste ")
        elif pred =="Metal":
            st.markdown("### :recycle: It's recycable!")
            st.markdown("### :bulb: Useful tip: Remove any debris and contaminants ")
        elif pred =="Compost":
            st.markdown("### Composting!")
            st.markdown("### :bulb: Useful tip: Fertilize your plants and nourish your garden ")
        elif pred == "Trash":
            st.markdown("### :warning: NOT recyclable!")
            st.markdown("### :bulb: You can throw this in the trash bin with a clear conscience :wink:")
