"""Initialize flask app, do all necessary imports and set settings"""
from flask import Flask, render_template, redirect, request, url_for, abort
app = Flask(__name__, instance_relative_config=True, template_folder='views', static_url_path='/')

from . import config
from . import database
from . import models
from . import base62
from . import controllers

database.init_db()