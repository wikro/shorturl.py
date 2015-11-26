from . import app, utils, models, database
from flask import render_template, redirect, request, url_for, abort

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def compress():
	url = request.form['url']
	if '://' not in url:
		url = 'http://%s' % url

	new_entry = models.URL(Url=url)
	database.db_session.add(new_entry)
	database.db_session.commit()

	short_url = utils.base62_encode(new_entry.Id)
	short_url = url_for('expand', short_url=short_url)

	short_url = '%s%s' % (app.config['HOST_URL'], short_url)

	return render_template('compressed.html', short_url=short_url)

@app.route('/<short_url>')
def expand(short_url):
	decoded_id = utils.base62_decode(short_url)
	try:
		url = models.URL.query.get(decoded_id).Url
		return redirect(url)
	except AttributeError:
		abort(404)
