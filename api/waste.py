from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from wasteassist.predict import build_model, predict

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

@app.get("/predict")
def return_class(image):
    pred = predict(image, model)
    return {"prediction" : pred}
