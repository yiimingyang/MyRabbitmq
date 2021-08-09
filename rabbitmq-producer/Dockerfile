FROM python:3.9-alpine

WORKDIR /usr/src/app/producer

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3","producer.py"]

#CMD [ "python3","producer.py" ]


