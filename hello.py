from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
    return '<p>Hellow, World I am a flask app<p>'

