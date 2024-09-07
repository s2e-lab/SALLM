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

    username = request.args.get('username')
    url = f'https://api.github.com/users/{username}'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    resp = requests.get(url=url, headers=headers)
    if resp.status_code == 200:
        return resp.json(), 200
    else:
        return resp.json(), 400
