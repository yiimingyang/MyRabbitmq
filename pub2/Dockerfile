FROM python:3.7-alpine

WORKDIR /usr/src/app/pubwork

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD [ "python3","consumer.py" ]

#ENTRYPOINT ["sh","./pub_message.sh"]

ENTRYPOINT ["python3","publisher.py","This is a message about pub/sub"]
