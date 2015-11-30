"""Application models"""
from .database import base, Column, Integer, String

class URL(base):
	"""URL model class"""
	__tablename__ = "Urls"
	Id = Column(Integer, primary_key=True)
	Url = Column(String, nullable=False)

	def __init__(self, url):
		self.Url = url
