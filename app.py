from flask import Flask , url_for, render_template,redirect,flash,request
from flask_sqlalchemy import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError
from flask_login import LoginManager,UserMixin,login_user,logout_user,current_user
from flask import SQLALchemy



app = Flask(__name__)
app.config['SECRET_KEY']="538fa9f367bc05745f1899ccfcce1c4c"

#Sqlite COnfiguration
app.config['SQLALCHEMY_DATABASE_URI'] = 'jdbc:sqlite:identifier.sqlite'
db = SQLALchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


#user_model

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)



