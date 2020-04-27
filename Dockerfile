FROM python:3.7-stretch
ADD . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
CMD python socketio_examples.py
