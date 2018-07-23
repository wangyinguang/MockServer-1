from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config.from_object('config')
db = SQLAlchemy(app)

from MockServer import views, models