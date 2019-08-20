import os

from flask import Flask, session, render_template, request, redirect, g, url_for
from flask_socketio import SocketIO, emit
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.urandom(24)
socketio = SocketIO(app)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
db = db()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/kanal" methods=["POST"])
def kanal():
    kanal_adi = request.form.get("Kanal_Adi")
    kanal_no = request.form.get("Kanal_No")

@socketio.on("mesaj")
def mesaj(data):
    .















#    if g.user:
#        
#        return render_template("index.html", g=g)
#    else:
#        return redirect(url_for("giris"))
#
##user kontrolü:        
#@app.before_request
#def before_request():
#    g.user = None
#    if 'user' in session:
#        g.user = session['user']
#
#@app.route("/kayit", methods=["GET", "POST"])
#def kayit():
#    return render_template("kayit.html", g=g)
#
##kayıt işleminin SQL database'e yazılması:
#@app.route("/success", methods=["POST"])
#def success():
#    email = request.form.get("email")
#    password = request.form.get("password")
#    db.execute("INSERT INTO users (email, password) VALUES (:email, :password)",{"email": email, "password": password})
#    db.commit()
#    return render_template("success.html", g=g)
#
#@app.route("/giris", methods=["GET", "POST"])
#def giris():
#    return render_template("giris.html", g=g)
#
##email ve şifre kontrolü:
#@app.route("/login", methods=["GET", "POST"])
#def login():
#    eid = request.form.get("eid")
#    lpass = request.form.get("epass")
#    if db.execute("SELECT email FROM users WHERE email = :eid", {"eid": eid}).rowcount > 0 and db.execute("SELECT password FROM users WHERE password = :password", {"password": lpass}).rowcount > 0:
#        session['user'] = eid
#        return render_template("login_success.html", g=g)
#    else:
#        return render_template("login_failed.html", g=g)
#
##Kullanıcı çıkışı:
#@app.route("/logout", methods=['GET', 'POST'])
#def logout():
#    session.pop('user', None)
#    return render_template("logout_success.html", g=g)