from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import Email
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '4daf72f578adc41da0f41f9ef6d23cc2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flaskblog import routes