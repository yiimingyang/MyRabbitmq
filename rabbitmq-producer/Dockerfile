FROM python:3.9

#WORKDIR /usr/src/app/producer

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#ENTRYPOINT ["producer.py"]

CMD [ "python3","producer.py" ]


