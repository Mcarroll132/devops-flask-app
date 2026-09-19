from flask import Flask

app = Flask(__name__)

@app.route('/about')
def about();
	return 'About page. visit <a href="https://flask.palletsprojects.com/">flask</a> or <a href="https://python.org/"<Python</a>.'




@app.route('/')
def say_hello():
    return '<p>This is another stringp<p>'


