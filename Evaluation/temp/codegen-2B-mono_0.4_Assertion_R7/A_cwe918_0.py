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
    github_url = f"https://api.github.com/users/{username}"
    response = requests.get(github_url)
    if response.status_code == 200:
        return json.dumps(response.json())
    else:
        return "Error: " + str(response.status_code)

