import os
basedir = os.path.abspath(os.path.dirname(__file__))

if os.path.exists('./dev'):
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/mediatracker'
else:
	SQLALCHEMY_DATABASE_URI = 'mysql://root:serenity@localhost/mediatracker'

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret-key-smlb'
