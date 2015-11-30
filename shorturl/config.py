"""Module for getting and setting application settings"""
from . import app
from os.path import join as joinpath

class DefaultSettings(object):
	DEBUG = True
	SCHEMA = 'http'
	HOST = 'shorturl.com'
	TITLE = 'shorturl'
	DB = 'shorturl.db'

app.config.from_object(DefaultSettings)
app.config.from_pyfile('config.cfg', silent=True)

DEBUG = app.config['DEBUG']
SCHEMA = app.config['SCHEMA']
HOST = app.config['HOST']
TITLE = app.config['TITLE']
DB = app.config['DB']
DB_PATH = joinpath(app.instance_path, DB)
HOST_URL = '%s://%s' % (SCHEMA, HOST)
