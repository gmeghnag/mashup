import os
import json
from pprint import pprint as pr

import requests
from flask import Flask, render_template, Response, request, jsonify

app = Flask(__name__)


FOODS_MICROSERVICE_HOST = os.environ.get('FOODS_MICROSERVICE_HOST')
FOODS_MICROSERVICE_PORT = os.environ.get('FOODS_MICROSERVICE_PORT')


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/foods', methods=['POST', 'OPTIONS'])
def post_foods():
    data = {"items": []}
    headers = {}
    response_headers = {}
    _headers = dict(request.headers)
    for key, value in _headers.items():
        if key.startswith("X-Mashup-"):
            headers[key] = value
            response_headers[key] = value
            continue
        if key.startswith("X-"):
            response_headers[key] = value
    if FOODS_MICROSERVICE_HOST is not None and FOODS_MICROSERVICE_PORT is not None:
        r = requests.get(f'{FOODS_MICROSERVICE_HOST}:{FOODS_MICROSERVICE_PORT}/', headers=headers)
        data = r.json()
    resp = Response(json.dumps(data))
    resp.headers = response_headers
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
