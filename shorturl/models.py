from .database import base 
from sqlalchemy import Column, Integer, String

class URL(base):
	__tablename__ = "Urls"
	Id = Column(Integer, primary_key = True)
	Url = Column(String, nullable = False)
