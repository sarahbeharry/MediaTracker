from flask import Flask
from flask_sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)
flask_app.config.from_object('MediaTracker.config')
db = SQLAlchemy(flask_app)

# then import the views to apply all the app.route decorators without triggering circular import issues
from MediaTracker.views import views_bug, views_main, views_media, views_tag
