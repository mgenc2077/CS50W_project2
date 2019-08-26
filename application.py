import os
import requests
from flask import Flask, session, render_template, request, redirect, g, url_for, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room, send
from flask_session import Session
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
#from classes import *

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.secret_key = os.urandom(24)
socketio = SocketIO(app)
# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
db = db()

if __name__ == '__main__':
    socketio.run(app, debug=True)
#global rinnem
channel =['test']
#calis = kanal_listesi(ad='genel')
#yazi = []
#rinnem = ''
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

@app.route("/mesajlist", methods=['POST'])
def mesajlist():
    rinne = request.form.get('history')
    gecmis = db.execute("SELECT nick, soz, zaman FROM mesages WHERE kanal = cast(:deg as varchar)",{"deg":rinne}).fetchall()
    print(gecmis)
    return jsonify({'gecmis': [dict(row) for row in gecmis]})

@socketio.on('test')
def handle_my_custom_event(json):
    #global serialize
    #global yazi
    #global rinnem
    #global suan
    zaman = datetime.datetime.now()
    suan = str(zaman.day) + '.' + str(zaman.month) + '.' + str(zaman.year) + ':' + str(zaman.hour) + '.' + str(zaman.minute)
    #print('zaman :'+ suan)
    print('received my event: ' + str(json))
    serialize = json
    json.update({'zaman': suan})
    kanal = serialize["channel"]
    nick = serialize["kullanici_adi"]
    soz = serialize["kanal_no"]
    db.execute("INSERT INTO mesages (nick, soz, kanal, zaman) VALUES (:nick, :soz, :kanal, :zaman)",{"nick": str(nick), "soz": str(soz), "kanal": str(kanal), "zaman": str(suan)})
    db.commit()
    #rinne = kanal
    #rinnem = kanal
    #kanal = yeni_kanal(ad=kanal)
    #m = mesaj(nick=kullanici_adi, soz=soz, kanal=rinne, zaman=suan)
    #rinnem += '<li> ' + suan + ' &rAarr; ' + kullanici_adi + ' &nRightarrow; ' + soz + ' </li>'
    #kanal.add_mesaj(p=m)
    #calis.add_kanal(kanal)
    #for k in kanal.gecmis:
    #    test86 = len(kanal.gecmis)
    #    k.print_info()
    #    print('liste uzunluğu ne yazıkki: ' + str(test86))
    #    print('')
    #print(rinnem)
    #channel.append(rinne)
    if(request.sid):{
        leave_room(kanal)
    }
    join_room(kanal)
    socketio.emit('gonder', json, callback=messageReceived, room=kanal)

@socketio.on("baglanti")
def handle_baglanti(json):
    print(json)
