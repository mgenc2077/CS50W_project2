import os
import requests
from flask import Flask, session, render_template, request, redirect, g, url_for, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room, send
from flask_session import Session
import datetime
#from classes import *

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


if __name__ == '__main__':
    socketio.run(app, debug=True)

channel =['test']
yazi = []
global serialize
#global suan
global kanal

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@app.route("/channel_list", methods=['POST'])
def channel_list():
    print(channel)
    return jsonify({"channel":channel})

#@app.route("/mesajlist", methods=['POST'])
#def mesajlist():
#    for m in yazi:
#        print(str(m))
#        #if (m.kanal == kanal):
#            #t = uygun(nick=m.nick, soz=m.soz, zaman=m.zaman)
#            #temp.append(t)
#    #return jsonify({'soz': m.soz, 'nick': m.nick, 'zaman':m.zaman})

@socketio.on('test')
def handle_my_custom_event(json):
    #global serialize
    #global yazi
    #global kanal
    #global suan
    zaman = datetime.datetime.now()
    suan = str(zaman.day) + '.' + str(zaman.month) + '.' + str(zaman.year) + ':' + str(zaman.hour) + '.' + str(zaman.minute)
    #print('zaman :'+ suan)
    print('received my event: ' + str(json))
    serialize = json
    json.update({'zaman': suan})
    kanal = serialize["channel"]
    #kullanici_adi = serialize["kullanici_adi"]
    #soz = serialize["kanal_no"]
    #m = mesaj(nick=kullanici_adi, soz=soz, kanal=kanal, zaman=suan)
    #yazi.append(m)
    channel.append(kanal)
    if(request.sid):{
        leave_room(kanal)
    }
    join_room(kanal)
    socketio.emit('gonder', json, callback=messageReceived, room=kanal)

@socketio.on("baglanti")
def handle_baglanti(json):
    print(json)
