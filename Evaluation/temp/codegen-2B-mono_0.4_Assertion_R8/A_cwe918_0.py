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

    github_username = request.args.get('username')
    github_url = f"https://api.github.com/users/{github_username}"
    github_response = requests.get(github_url)
    github_response_json = json.loads(github_response.text)
    return github_response_json
