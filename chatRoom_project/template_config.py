import os
basedir = os.path.abspath(os.path.dirname(__file__))
from flask.ext.sqlalchemy import SQLAlchemy


SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
DEBUG = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = True


SQLALCHEMY_DATABASE_URI = \
    'mysql+pymysql://ACCOUNT:PASSWORD@database/dbName'
