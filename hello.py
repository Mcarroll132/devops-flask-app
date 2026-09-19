from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
    return '<p>Welcome, I am a flask app (lab2)<p>'


