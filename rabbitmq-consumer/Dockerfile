FROM python:3.7-alpine

WORKDIR /usr/src/app/consumer

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD [ "python3","consumer.py" ]

ENTRYPOINT ["python3","consumer.py"]
