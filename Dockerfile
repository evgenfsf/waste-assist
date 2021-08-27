FROM python:3

COPY api /api
COPY requirements.txt /requirements.txt
COPY wasteassist /wasteassist
COPY credentials.json /credentials.json
RUN pip install -r requirements.txt

EXPOSE 80
# CMD [ "python", "./your-daemon-or-script.py" ]
CMD uvicorn api.waste:app --host 0.0.0.0
