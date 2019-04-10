import get_voucher

from flask import Flask
from flask import json
from flask import request
from flask_cors import CORS, cross_origin

APP = Flask(__name__)
CORS = CORS(APP)
APP.config['CORS_HEADERS'] = 'Content-Type'


@APP.route("/")
@cross_origin()
def index():
	return "App running"


@APP.route("/voucher")
@cross_origin()
def get_voucher_from_web():
    response = APP.response_class(
		response=get_voucher.get_voucher(
			get_voucher.open_url(request.args.get('url'))),
		status=200,
		mimetype='application/json'
	)
    return response


APP.run(host='0.0.0.0')
