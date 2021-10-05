import os
import json


from flask import Flask, render_template, make_response, request, jsonify

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/', methods=['GET'])
def get_index():
    headers = dict(request.headers)
    resp = make_response(render_template("index.html", headers=headers))
    resp.headers['Content-Type'] = 'text/html'
    return (resp, 200)

@app.route('/', methods=['POST', 'OPTIONS'])
def post_index():
    headers = dict(request.headers)
    return jsonify(headers)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
