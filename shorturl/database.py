from . import app
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///%s' % app.config['DB_PATH'])
session = sessionmaker(autocommit = False, autoflush = False, bind = engine)
db_session = scoped_session(session)

base = declarative_base()
base.query = db_session.query_property()

def init_db():
	from . import models
	base.metadata.create_all(bind = engine)
