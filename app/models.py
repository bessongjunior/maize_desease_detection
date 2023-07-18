# Useful imports, modules and extensions.
from flask_wtf          import FlaskForm
from flask_wtf.file     import FileField, FileRequired
from wtforms            import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, DataRequired

from app import db


class User(db.Model):
    '''This is our user class that defineds our user table with name "user" '''

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String, nullable=False)
    email: str = db.Column(db.String, nullable=False)
    password:str = db.Column(db.Text)
    
    def __init__(self, user, email, password):
        '''This is our constructor'''
        self.user       = user
        self.password   = password
        self.email      = email

    def __repr__(self):
        '''method is intended to provide a more formal and unambiguous representation of an object,
        primarily for debugging purposes
        '''
        return f"User < '{self.id}' - '{self.name}'>"
    
    def save(self):
        '''This method is design to save user credentials to database'''
        db.seesion.add(self)
        db.session.commit()

        return self


class LoginForm(FlaskForm):
    '''This class is design for login form, auth'''
    username    = StringField  (u'Username'  , validators=[DataRequired()])
    password    = PasswordField(u'Password'  , validators=[DataRequired()])

class RegisterForm(FlaskForm):
    '''This class is design for registration form, auth'''
    name        = StringField  (u'Name'      )
    username    = StringField  (u'Username'  , validators=[DataRequired()])
    password    = PasswordField(u'Password'  , validators=[DataRequired()])
    email       = StringField  (u'Email'     , validators=[DataRequired(), Email()])