import os
import json

import requests
from flask import Flask, render_template, make_response, request, jsonify

app = Flask(__name__)
#app.config['TEMPLATES_AUTO_RELOAD'] = True
#app.config['DEBUG'] = True

FOODS_MICROSERVICE_HOST = os.environ.get('FOODS_MICROSERVICE_HOST')
FOODS_MICROSERVICE_PORT = os.environ.get('FOODS_MICROSERVICE_PORT')

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/headers', methods=['POST', 'OPTIONS'])
def post_headers():
    headers = dict(request.headers)
    return jsonify(headers)

@app.route('/foods', methods=['POST', 'OPTIONS'])
def post_foods():
    headers = {}
    data = {"items": ["pizza", "pasta", "arancini", "tapas", "croquetas", "paella"]}
    if FOODS_MICROSERVICE_HOST is not None and FOODS_MICROSERVICE_PORT is not None:
        _headers = dict(request.headers)
        for key, value in _headers.items():
            if key.startswith("Z-"):
                headers[key] = value
        r = requests.get(f'{FOODS_MICROSERVICE_HOST}:{FOODS_MICROSERVICE_PORT}/', headers=headers)
        data = r.json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
