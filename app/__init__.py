from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.views import views_main, views_media, views_tag, views_bug
from app import models

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
