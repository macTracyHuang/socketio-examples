import os
from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['FILEDIR'] = 'static/_files/'
app.config['CHAT_URL'] = os.environ.get('CHAT_URL')
app.config['POLLS_VOTE_URL'] = os.environ.get('POLLS_VOTE_URL')
app.config['WHERE_PIN_URL'] = os.environ.get('WHERE_PIN_URL')
app.config['GOOGLE_MAPS_KEY'] = os.environ.get('GOOGLE_MAPS_KEY')
socketio = SocketIO(app)
