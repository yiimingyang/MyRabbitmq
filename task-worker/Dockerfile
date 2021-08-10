FROM python:3.7-alpine

WORKDIR /usr/src/app/worker

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3","taskworker.py"]

#CMD [ "python3","producer.py" ]


