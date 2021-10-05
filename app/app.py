import os
import json
from flask import Flask, render_template, make_response, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    
    _headers = dict(request.headers)
    for key
    resp = make_response(render_template("index.html", headers=headers))
    resp.headers['Content-Type'] = 'text/html'
    return (resp, 200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
