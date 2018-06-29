import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost:3306/mediatracker'

WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret-key'
