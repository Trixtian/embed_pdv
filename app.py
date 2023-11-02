# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

from services.pbiembedservice import PbiEmbedService
from utils import Utils
from flask import Flask, render_template, send_from_directory, request, jsonify
import json
import os
import requests
# Initialize the Flask app
app = Flask(__name__)

# Load configuration
app.config.from_object('config.BaseConfig')

@app.route('/')
def index():
    '''Returns a static HTML page'''

    return render_template('login.html')
import requests

@app.route("/api-login", methods=["POST"])
def api_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    api_url = "https://olimpo.gentesplendor.com/api-trafico/login"
    api_data = {"usuario": username, "password": password}
    response = requests.post(api_url, json=api_data)
    response_data = response.json()
    
    if response.status_code == 200:
        return response_data
    else:
        return jsonify({
                    "error": "Error en la solicitud a la segunda API",
                    "code": 402
                })


@app.route('/get-co-list', methods=['POST'])
def getCoList():
    data = request.get_json()
    token = data.get("token")
    user_id = data.get("user_id")

    api_url = f"https://olimpo.gentesplendor.com/api-trafico/co-usuario/{user_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(api_url, headers=headers)
    response_data = response.json()
        
    if response.status_code == 200:
        return response_data
    else:
        return jsonify({
                    "error": "Error en la solicitud a la segunda API",
                    "code": 402
                })


@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('index.html')



@app.route('/getembedinfo', methods=['GET'])
def get_embed_info():

    '''Returns report embed configuration'''

    config_result = Utils.check_config(app)
    if config_result is not None:
        return json.dumps({'errorMsg': config_result}), 500

    try:
        embed_info = PbiEmbedService().get_embed_params_for_single_report(app.config['WORKSPACE_ID'], app.config['REPORT_ID'])
        return embed_info
    except Exception as ex:
        return json.dumps({'errorMsg': str(ex)}), 500
    

@app.route('/favicon.ico', methods=['GET'])
def getfavicon():
    '''Returns path of the favicon to be rendered'''

    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run()