from flask import Flask, jsonify, request, make_response
import requests
import logging
from sys import stdout
import json
import re

logging.basicConfig(stream=stdout, level=logging.INFO, format='%(asctime)s - %(name)s - '
                                                              '%(levelname)s - %(funcName)s - %(message)s')
app = Flask(__name__)


@app.errorhandler(404)
def handle_404_error(_error):
    _err = {
        "Input": request.json,
        "Output": "",
        "Status": 404,
        "Message": str(_error)
    }
    return make_response(jsonify(_err), 404)


@app.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    _err = {
        "Input": request.json,
        "Output": "",
        "Status": 400,
        "Message": str(_error)
    }
    return make_response(jsonify(_err), 400)


@app.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    _err = {
        "Input": request.json,
        "Output": "",
        "Status": 401,
        "Message": str(_error)
    }
    return make_response(jsonify(_err), 401)


@app.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    _err = {
        "Input": request.json,
        "Output": "",
        "Status": 500,
        "Message": str(_error)
    }
    return make_response(jsonify(_err), 500)


@app.route('/', methods=['GET'])
def get_data():
    """
    This func will provide the data requested from random name gen.
    :return: Payload and Status Code
    """
    try:
        req_ran_name = requests.get("https://api.namefake.com/")
        data = json.loads(req_ran_name.text)
        if data.get('name'):
            name = re.findall(r"[A-Z][a-z]+,?\s+(?:[A-Z][a-z]*\.?\s*)?[A-Z][a-z]+", data.get('name'))
            req_ran_joke = requests.get("http://api.icndb.com/jokes/random?firstName={0}&lastName={1}&limitTo="
                                        "[nerdy]".format(name[0].split(' ')[0], name[0].split(' ')[1]))
            return make_response(req_ran_joke.text, 200)
        else:
            return make_response('Empty body', 500)
    except Exception as e:
        return make_response(e, 500)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
