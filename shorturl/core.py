"""Initialize and import objects and packages for core functionality"""
from flask import Flask
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__, instance_relative_config=True, template_folder='views', static_url_path='/')

Base = declarative_base()
