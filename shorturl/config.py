"""Module for getting and setting application settings"""
from os.path import join as joinpath

from .core import app

DEBUG = True
SCHEMA = 'http'
HOST = 'shorturl.com'
TITLE = 'shorturl'
DATABASE = 'shorturl.db'

app.config.from_object(__name__)
app.config.from_pyfile('config.cfg', silent=True)

app.config['DATABASE_PATH'] = joinpath(app.instance_path, app.config['DATABASE'])
app.config['HOST_URL'] = '%s://%s' % (app.config['SCHEMA'], app.config['HOST'])

