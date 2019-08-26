from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Float, PrimaryKeyConstraint

db = SQLAlchemy()

class mesajlar(db.Model):
    db = SQLAlchemy()
    __tablename__ = "mesaj"
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String, nullable=False)
    soz = db.Column(db.String, nullable=False)
    kanal = db.Column(db.String, nullable=False)
    zaman = db.Column(db.String, nullable=False)

class mesaj:
    counter = 1
    def __init__(self, nick, soz, kanal, zaman):
        self.id = mesaj.counter
        mesaj.counter += 1
        self.nick = nick
        self.soz = soz
        self.kanal = kanal
        self.zaman = zaman

class uygun:
    counter = 1
    def __init__(self, nick, soz, zaman):
        self.id = mesaj.counter
        mesaj.counter += 1
        self.nick = nick
        self.soz = soz
        self.zaman = zaman

