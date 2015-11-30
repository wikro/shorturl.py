"""Application models"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Url(Base):
	"""URL model class"""
	__tablename__ = "urls"
	id = Column(Integer, primary_key=True)
	url = Column(String, nullable=False)

	def __init__(self, url):
		self.url = url
