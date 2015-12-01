"""Application database object"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from .core import app, Base

engine = create_engine('sqlite:///%s' % app.config['DATABASE_PATH'])
maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = scoped_session(maker)

Base.query = session.query_property()
Base.metadata.create_all(bind=engine)

@app.teardown_appcontext
def teardown(exception):
	"""Remove database session after use"""
	if exception is not None:
		raise exception
	session.remove()
