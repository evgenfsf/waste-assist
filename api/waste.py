from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from wasteassist.predict import build_model, predict
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import os

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
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = f'{dir_path}/uploads/{file.filename}'
    # f = open(f'{filename}', 'wb')
    content = await file.read()
    # f.write(content)

@app.get("/predict")
def return_class(image):
    pred = predict(image, model)
    return {"prediction" : pred}
