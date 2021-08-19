FROM python:3.7
ADD helloworld.py /
CMD [ "python3", "./helloworld.py"]
