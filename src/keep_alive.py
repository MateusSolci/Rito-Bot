from flask import Flask
from threading import Thread
import os

app = Flask('')


@app.route('/')
def home():
    return "I'm alive"


def run():
    app.run(host='0.0.0.0', port=os.environ.get('PORT'))


def keep_alive():
    t = Thread(target=run)
    t.start()
