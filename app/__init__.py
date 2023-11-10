from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///miniblog.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import usuario, entrada, comentario, categoria
