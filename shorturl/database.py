"""Application database object"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from . import app
from .models import Base
from .config import DATABASE_PATH

engine = create_engine('sqlite:///%s' % DATABASE_PATH)
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
