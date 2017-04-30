# coding: utf-8
from app import db, lm
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    password_hash = db.Column(db.String(64))
    email = db.Column(db.String(64), unique = True)
    confirmed = db.Column(db.Boolean, default=False)

    @staticmethod
    def admin_user(username, password):
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
    	return s.dumps({'confirm': self.id})
    	
    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
    	try:
    	    data = s.loads(token)
    	except:
    	    return False
    	if data.get('confirm') != self.id:
    	    return False
    	self.confirmed = True
    	db.session.add(self)
    	db.session.commit()
    	return True
    
    def __repr__(self):
        return '<User %r>' % (self.username)

@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
