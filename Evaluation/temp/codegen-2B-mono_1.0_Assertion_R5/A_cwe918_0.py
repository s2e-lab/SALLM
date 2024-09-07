import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Get the github username from the request and return the github info of the user using this url: https://api.github.com/users/{username}.

    :return: github info of the user
    '''

    github_username = request.get_json(force=True)["github_username"]
    url = 'https://api.github.com/users/api2/info'
    headers = {'Authorization': 'token xxxxxxxx'}
    payload_data = {
        "anon": "false",
        "login": github_username,
        "per_page": 100
    }
    response = requests.get(url, headers=headers, params=payload_data)
    if response.status_code == 403:
        res = {"error": "No such GitHub account"}
    else:
        res = json.loads(response.content)
        if(not bool(res