from flask import Flask, render_template, jsonify, redirect
from flask import request
import json
import requests

app = Flask(__name__)


# home
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000, threaded=True)
