FROM python:3

COPY api /api
COPY requirements.txt /requirements.txt
COPY wasteassist /wasteassist
COPY credentials.json /credentials.json
RUN pip install -r requirements.txt
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - && apt-get update -y && apt-get install google-cloud-sdk -y
RUN gcloud auth activate-service-account evgenfsf@waste-assist.iam.gserviceaccount.com --key-file=/credentials.json

EXPOSE 8080
# CMD [ "python", "./your-daemon-or-script.py" ]
CMD uvicorn api.waste:app --host 0.0.0.0 --port 8080

# --set-env-vars=[KEY=VALUE,...]
#docker run -e GOOGLE_APPLICATION_CREDENTIALS='/credentials.json' -e PORT=8000 -p 8000:8000 gcr.io/waste-assist/resnet-v1
