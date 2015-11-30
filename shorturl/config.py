"""Module for getting and setting application settings"""
from os.path import join as joinpath

from . import app

class DefaultSettings(object):
	DEBUG = True
	SCHEMA = 'http'
	HOST = 'shorturl.com'
	TITLE = 'shorturl'
	DATABASE = 'shorturl.db'

app.config.from_object(DefaultSettings)
app.config.from_pyfile('config.cfg', silent=True)

DEBUG = app.config['DEBUG']
SCHEMA = app.config['SCHEMA']
HOST = app.config['HOST']
TITLE = app.config['TITLE']
DATABASE = app.config['DATABASE']
DATABASE_PATH = joinpath(app.instance_path, DATABASE)
HOST_URL = '%s://%s' % (SCHEMA, HOST)
