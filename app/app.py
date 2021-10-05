import os
import json
from flask import Flask, render_template, make_response, request
app = Flask(__name__)


def to_pretty_json(value):
    return json.dumps(value, sort_keys=True,
                      indent=4, separators=(',', ': '))

app.jinja_env.filters['tojson_pretty'] = to_pretty_json

@app.route('/', methods=['GET'])
def index():
    headers = dict(request.headers)
    resp = make_response(render_template("index.html", headers=headers))
    resp.headers['Content-Type'] = 'text/html'
    return (resp, 200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
