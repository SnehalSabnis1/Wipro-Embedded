FROM python:3.8-slim-buster

ADD helloworld.py /

CMD [ "python", "./helloworld.py" ]
