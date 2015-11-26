from os.path import join as joinpath

from flask import Flask
app = Flask(__name__, instance_relative_config=True, template_folder='views', static_url_path='/')

from . import config
app.config.from_object(config)
app.config.from_pyfile('config.cfg', silent=True)

app.debug = app.config['DEBUG']
app.config['DB_PATH'] = joinpath(app.instance_path, app.config['DB'])
app.config['HOST_URL'] = '%s://%s' % (app.config['SCHEMA'], app.config['HOST'])

from . import utils
from . import database
from . import models
from . import controllers

@app.teardown_appcontext
def teardown_appcontext(exception = None):
	database.db_session.remove()

database.init_db()
