1. Prerequisites

	* Python 2.7
	* Virtualenv
	* Git

2. Cloning, setting up and running

	$ git clone https://bitbucket.org/wikro/shorturl.git
	$ cd shorturl
	$ mkdir env
	$ virtualenv env
	$ . env/bin/activate
	$ pip install -r requirements.txt
	$ python run.py

The server starts running on http://127.0.0.1:5000