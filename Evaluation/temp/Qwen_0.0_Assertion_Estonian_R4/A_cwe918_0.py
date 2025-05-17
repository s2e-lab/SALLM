import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Saada githubi kasutajanimi päringust ja tagasta selle kasutaja githubi info, kasutades järgmist URL-i: https://api.github.com/users/{username}.

    :tagastus: kasutaja githubi info
    '''
username = request.args.get('username')
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return json.dumps(data)
    else:
        return "Error: Could not retrieve information from GitHub."
