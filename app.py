from flask import Flask
from routes.routes import routes
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI
from utils.db import db

app = Flask(__name__)

#CONFIGURACIONES
app.secret_key='mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#SIN CACHE
app.config['SEND_FILA_MAX_MODIFICATIONS'] = 0
db.init_app(app)

app.register_blueprint(routes)