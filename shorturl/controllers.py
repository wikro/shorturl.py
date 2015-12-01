"""Application controllers"""
from flask import render_template, redirect, request, url_for, abort

from .core import app
from . import models, database, base62

@app.route('/')
def index():
	"""Render index template"""
	return render_template('index.html')

@app.route('/', methods=['POST'])
def compress():
	"""Process and store URL in database, return entry id in base62"""
	url = request.form['url'].strip()
	if app.config['HOST'] in url or url == '':
		return redirect(url_for('index'))

	if '://' not in url:
		url = 'http://%s' % url

	new_entry = models.Url(url)
	database.session.add(new_entry)
	database.session.commit()

	short_url = base62.encode(new_entry.id)
	short_url = url_for('expand', short_url=short_url)

	short_url = '%s%s' % (app.config['HOST_URL'], short_url)

	return render_template('compressed.html', short_url=short_url)

@app.route('/<short_url>')
def expand(short_url):
	"""Decode base62 string and match decoded value with an id in the database"""
	decoded_id = base62.decode(short_url)
	try:
		url = models.Url.query.get(decoded_id).url
		return redirect(url)
	except AttributeError:
		abort(404)
