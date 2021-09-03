
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
font-size:85px ; font-family: 'Cooper Black'; color: #5d941e; margin-top: -70px} 
</style> """, unsafe_allow_html=True)
# st.markdown('<p class="font">Welcome to WasteAssist</p>', unsafe_allow_html=True)
st.markdown('<p class="font">Welcome to WasteAssist</p>', unsafe_allow_html=True)


##Creating image uploader

# #upload logo
logo = Image.open('logo2.jpg')
st.sidebar.image(logo, width=300)

st.sidebar.title("Please upload an image")
uploaded_img = st.sidebar.file_uploader(" ",type=['jpg', 'jpeg'] )


if uploaded_img is not None:
    user_img = Image.open(uploaded_img)
    user_img = user_img.resize((256,256))
    user_img.save("test.jpg")
    img_bytes = io.BytesIO()
    user_img.save(img_bytes, format='JPEG')
    # byte_im = img_bytes.getvalue()
    st.image(user_img)


else:
    print('Image not found, please try again')

with st.spinner('Be patient, saving the world takes time ...'):
        
    if st.button("Click here to classify your waste"):
        with open('test.jpg', "rb") as img:
            get_img = requests.post(f"{API_URL}/files", files={"file":img})
    #display prediction
        pred = get_img.json()['prediction']
        st.markdown("This appears to be:")
        st.markdown(f"**{pred}**") 
        if pred == "glass":
            st.markdown("### :recycle: It's recycable!") 
            st.markdown("### :bulb: Useful tip: Rinse bottle and jars to remove food waste")
        elif pred =="cardboard":
            st.markdown("### :recycle: It's recycable!") 
            st.markdown("### :bulb: Useful tip: Keep it dry and remove contaminants such as plastic")
        elif pred =="paper":
            st.markdown("### It's recycable!") 
            st.markdown("### :bulb: Useful tip: Keep it unshredded and dry ")
        elif pred =="glass":
            st.markdown("### It's recycable!") 
            st.markdown("### :bulb: Useful tip: Rinse bottle and jars to remove food waste ")
        elif pred =="metal":
            st.markdown("### It's recycable!") 
            st.markdown("### :bulb: Useful tip: Remove any debris and contaminants ")
        elif pred =="compost":
            st.markdown("### Composting!")
            st.markdown("### :bulb: Useful tip: Fertilize your plants and nourish your garden ")
        elif pred == "trash":
            st.markdown("### :warning: NOT recyclable!")
        
        
        

    



