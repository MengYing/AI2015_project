from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from . import db, login_manager


class ConvRecord(db.Model):
    __tablename__ = 'conv_record'
    id = db.Column(db.Integer(10), primary_key=True, autoincrement=True)
    chatIndex = db.Column(db.Integer(10))
    word = db.Column(db.String(256))
    time = db.Column(db.String(256))
    fromWho = db.Column(db.String(256))
    sentimentalVal = db.Column(db.Float(10))
    retrain = db.Column(db.Integer(1))   

    def __init__(self, word, time, fromWho, sentimentalVal, retrain):
        self.word = word
        self.time = time
        self.fromWho = fromWho
        self.sentimentalVal = sentimentalVal
        self.retrain = retrain
       
    def __repr__(self):
        return '<Share %r>' % self.word


class ConvConnect(db.Model):
    __tablename__ = 'conv_connect'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    users = db.Column(db.String(256))
    convIndex = db.Column(db.Integer(20))


class User(UserMixin, db.Model):
    __tablename__ = 'user_all'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    # sessionNum = db.Column(db.Integer(10))
    # picturepool = db.Column(db.String(20000))
    
    status = db.Column(db.Integer(10))
    # question = db.Column(db.Integer(11))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
