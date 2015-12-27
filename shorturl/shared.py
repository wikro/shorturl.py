"""Initialize and import objects that are shared throughout the app"""
from flask import Flask
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__, instance_relative_config=True, template_folder='views')

Base = declarative_base()

