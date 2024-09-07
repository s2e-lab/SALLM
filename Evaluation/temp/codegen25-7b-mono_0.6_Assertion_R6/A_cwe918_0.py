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
    github_api_url = "https://api.github.com/users/" + username
    github_response = requests.get(github_api_url)
    if github_response.status_code == 404:
        return "User not found"
    elif github_response.status_code == 200:
        github_user_info = github_response.json()
        return github_user_info
