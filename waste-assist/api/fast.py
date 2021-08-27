from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from PIL import Image
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

waste_assist_url = 'http://172.18.140.1:8502/'

@app.get("/")
def index():
    return dict(greeting="hello")


# @app.get("/get_img")
# def get_img(uploaded_img):
#     return {'Confitmation': 'ok'}

@app.post("/files/")
async def receive_file(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    image.save("1.jpg")
    return {"filename": file.filename, "type": file.content_type}
