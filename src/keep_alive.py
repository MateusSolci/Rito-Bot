from flask import Flask, render_template
from threading import Thread
import os

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return render_template('index.html')


def run():
    app.run(host='0.0.0.0', port=os.environ.get('PORT'))


def keep_alive():
    t = Thread(target=run)
    t.start()


keep_alive()
