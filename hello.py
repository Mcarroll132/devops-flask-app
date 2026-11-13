import json
import time

import redis
from flask import Flask

app = Flask(__name__)

# "the-redis-server" is the name of the Kubernetes Service in redis-service.yaml
r = redis.Redis(host='the-redis-server', port=6379, decode_responses=True)

# 600 seconds == 10 minutes
CACHE_SECONDS = 600


@app.route('/about')
def about():
    data = r.get('about')
    if data is not None:
        data = json.loads(data)
        if time.time() - data['time'] <= CACHE_SECONDS:
            return data['html']

    data = 'About page. visit <a href="https://flask.palletsprojects.com/">flask</a> or <a href="https://python.org/">Python</a>.'
    r.set('about', json.dumps({
        'html': data,
        'time': time.time()
    }))
    return data


@app.route('/')
def say_hello():
    data = r.get('index')
    if data is not None:
        data = json.loads(data)
        if time.time() - data['time'] <= CACHE_SECONDS:
            return data['html']

    data = '<p>This is another string</p>'
    r.set('index', json.dumps({
        'html': data,
        'time': time.time()
    }))
    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
