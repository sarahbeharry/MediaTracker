from flask import Flask
from flask_sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)
flask_app.config.from_object('config')
db = SQLAlchemy(flask_app)
