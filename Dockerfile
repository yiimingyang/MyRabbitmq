FROM python:3.7-alpine
ADD helloworld.py /
CMD [ "python3", "./helloworld.py"]
