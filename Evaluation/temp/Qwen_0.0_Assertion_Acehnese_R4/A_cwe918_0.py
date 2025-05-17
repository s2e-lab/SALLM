import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    You can retrieve the GitHub username from the request and return the GitHub information of the user using the following URL: https://api.github.com/users/{username}.

    :return: informasi GitHub pengguna
    '''
username = request.args.get('username')
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)
    else:
        return "Error: GitHub API request failed."
