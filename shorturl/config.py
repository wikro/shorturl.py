"""Configure application settings"""
from os.path import exists, join
from os import makedirs

from .core import app

DEBUG = True
SCHEMA = 'http'
HOST = 'shorturl.com'
TITLE = 'shorturl'
DATABASE = 'shorturl.db'

if not exists(app.instance_path):
	makedirs(app.instance_path)

app.config.from_object(__name__)
app.config.from_pyfile('config.cfg', silent=True)

app.config['DATABASE_PATH'] = join(app.instance_path, app.config['DATABASE'])
app.config['HOST_URL'] = '%s://%s' % (app.config['SCHEMA'], app.config['HOST'])
