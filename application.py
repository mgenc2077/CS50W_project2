import os
import requests
from flask import Flask, session, render_template, request, redirect, g, url_for, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room, send
from flask_session import Session
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.secret_key = os.urandom(24)
socketio = SocketIO(app)
# Database kurulumu:
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
db = db()

# Socket.io nun sağlıklı çalışması için başlatma modülü:
if __name__ == '__main__':
    socketio.run(app, debug=True)

channel =['test']
global serialize
global kanal

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

# Doğrulama:
def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

# Ajax ile kanal listesinin alınması:
@app.route("/channel_list", methods=['POST'])
def channel_list():
    print(channel)
    return jsonify({"channel":channel})

# Ajax ile geçmiş mesajların alınması:
@app.route("/mesajlist", methods=['POST'])
def mesajlist():
    rinne = request.form.get('history')
    gecmis = db.execute("SELECT nick, soz, zaman FROM mesages WHERE kanal = cast(:deg as varchar)",{"deg":rinne}).fetchall()
    print(gecmis)
    return jsonify({'gecmis': [dict(row) for row in gecmis]})

# Ana veri soketi
@socketio.on('test')
def handle_my_custom_event(json):
    # Zamanın alınması:
    zaman = datetime.datetime.now()
    suan = str(zaman.day) + '.' + str(zaman.month) + '.' + str(zaman.year) + ':' + str(zaman.hour) + '.' + str(zaman.minute)
    # Geri veri gelişinin doğrulanması:
    print('received my event: ' + str(json))
    serialize = json
    # Zamanın json paketine eklenmesi:
    json.update({'zaman': suan})
    # SQL için gerekleri verilerin değişkenlere atanması:
    kanal = serialize["channel"]
    nick = serialize["kullanici_adi"]
    soz = serialize["kanal_no"]
    # SQL database'e alınan mesaj verisinin yazılması:
    db.execute("INSERT INTO mesages (nick, soz, kanal, zaman) VALUES (:nick, :soz, :kanal, :zaman)",{"nick": str(nick), "soz": str(soz), "kanal": str(kanal), "zaman": str(suan)})
    # Socket.io'nun Join_room ve Leave_room fonksiyonları kullanılarak oda yapısının hazırlanması:
    if(request.sid):{
        leave_room(kanal)
    }
    join_room(kanal)
    # Düzenlenen Json verisinin gönderilmesi:
    socketio.emit('gonder', json, callback=messageReceived, room=kanal)
    # Alınan mesajların database'e iletilmesi:
    db.commit()

# Bağlantı kontrolü:
@socketio.on("baglanti")
def handle_baglanti(json):
    print(json)
