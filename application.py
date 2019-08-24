import os
import requests
from flask import Flask, session, render_template, request, redirect, g, url_for, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room, send
from flask_session import Session

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app, debug=True)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('test')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    socketio.emit('gonder', json, callback=messageReceived)

@socketio.on("baglanti")
def handle_baglanti(json):
    print(json)
