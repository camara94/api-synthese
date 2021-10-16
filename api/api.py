import flask
from flask import request, jsonify
from synthese import *
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
app.config["DEBUG"] = True

cors = CORS(app)


@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return "<h1>Bienvenue sur notre API de synthèse automatique</p>"


@app.route('/api', methods=['GET'])
@cross_origin()
def api_url():
    respone = {}
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'url' in request.args:
        url = str(request.args['url'])
        return synthese_automatique(url)
    else:
        return "Error: No id field provided. Please specify an url."


@app.route('/api', methods=['POST'])
@cross_origin()
def api_url_():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if not request.json or not 'article' in request.json:
        abort(400)
    else:
        return synthese_automatique_with_article(request.json['article'])


app.run()
