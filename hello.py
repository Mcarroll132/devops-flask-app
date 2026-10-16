from flask import Flask

app = Flask(__name__)

@app.route('/about')
def about():
    return 'About page. visit <a href="https://flask.palletsprojects.com/">flask</a> or <a href="https://python.org/">Python</a>.'

@app.route('/')
def say_hello():
    return '<p>This is another string</p>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
