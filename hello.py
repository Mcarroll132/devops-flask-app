from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
    return '<p>This is another stringp<p>'


