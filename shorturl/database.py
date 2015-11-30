"""Application database object"""
from . import app
from .config import DB_PATH

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///%s' % DB_PATH)
maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = scoped_session(maker)

base = declarative_base()
base.query = session.query_property()

@app.teardown_appcontext
def teardown(exception):
	"""Remove database session after use"""
	if exception is not None:
		raise exception
	session.remove()

def init_db():
	"""Initialize database"""
	base.metadata.create_all(bind=engine)
