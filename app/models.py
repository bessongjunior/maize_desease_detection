from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    '''This is our user class that defineds our user table with name "user" '''

    id: int = db.Column(db.Integer, primary_key=True)
    user: str = db.Column(db.String(64), nullable=False, unique = True)
    email: str = db.Column(db.String(120), nullable=False, unique = True)
    password:str = db.Column(db.Text(500))
    
    def __init__(self, user, email, password):
        '''This is our constructor'''
        self.user = user
        self.password = password
        self.email = email

    def __repr__(self):
        '''method is intended to provide a more formal and unambiguous representation of an object,
        primarily for debugging purposes
        '''
        return f"User < '{self.id}' - '{self.name}'>"
    
    def save(self):
        '''This method is design to save user credentials to database'''
        db.session.add(self)
        db.session.commit()

        return self
    