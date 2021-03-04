import os


os.environ['HOST'] = '0.0.0.0'
os.environ['PORT'] = '5000'
os.environ['SQL_DATABASE'] = 'your database'
os.environ['DATABASE_USER'] = 'your user database'
os.environ['DATABASE_PASSWORD'] = 'your database password'
os.environ['DATABASE_NAME'] = 'your database name'
os.environ['DATABASE_HOST'] = 'your local ipv4 or remote host'
os.environ['DATABASE_PORT'] = 'the port thatthe database is running'
os.environ['FLASK_ENV'] = 'development | production | testing'
os.environ['SECRET_KEY'] = 'your secret key'
os.environ['MAIL_SERVER'] = 'mail server'
os.environ['MAIL_PORT'] = 'mail server port'
os.environ['MAIL_USERNAME'] = 'mail username'
os.environ['MAIL_PASSWORD'] = 'mail password'

HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
DEBUG = True
SQL_DATABASE = os.environ.get('SQL_DATABASE')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_NAME = os.environ.get('DATABASE_NAME')
DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_PORT = os.environ.get('DATABASE_PORT')
FLASK_ENV = os.environ.get('FLASK_ENV')
SECRET_KEY = os.environ.get('SECRET_KEY')
MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = os.environ.get('MAIL_PORT')
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_USE_TLS = True
MAIL_USE_SSL = False
