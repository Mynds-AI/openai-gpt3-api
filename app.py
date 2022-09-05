import json

import flask
from flask import request

import const
from flask_cors import CORS, cross_origin
from model_training_service import Code

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/get-prediction', methods=['POST'])
@cross_origin()
def predict():
    input = json.loads(request.data)['input']
    pred = Code()
    return pred.model_prediction(input=input, api_key=const.API_KEY)


app.run()
