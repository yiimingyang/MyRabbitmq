FROM python:3.7-alpine

WORKDIR /usr/src/app/subwork

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3","subscriber.py"]

#CMD [ "python3","producer.py" ]


