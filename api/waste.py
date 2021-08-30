from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from wasteassist.predict import build_model, predict
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import os
from PIL import Image
import io

model = build_model()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def index():
    return {"greeting": "Welcome to Waste Assist API."}

@app.post("/files")
async def receive_file(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    # image.save("1.jpg")
    # content = await file.read()
    pred = predict(image, model)
    return {"prediction" : pred}
