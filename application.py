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

channel =['test']
global serialize

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html", channel=channel)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@app.route("/channel_list", methods=['POST'])
def channel_list():
    return jsonify({"channel":channel})

@socketio.on('test')
def handle_my_custom_event(json):
    global serialize
    print('received my event: ' + str(json))
    serialize = json
    kanal = serialize["channel"]
    channel.append(kanal)
    if(request.sid):{
        leave_room(kanal)
    }
    join_room(kanal)
    socketio.emit('gonder', json, callback=messageReceived, room=kanal)

@socketio.on("baglanti")
def handle_baglanti(json):
    print(json)
