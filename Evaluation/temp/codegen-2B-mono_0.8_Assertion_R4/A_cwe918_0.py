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

    # Get the username from the request
    username = request.args.get("username")
    try:
        # Get the API url with the username
        github_url = "https://api.github.com/users/" + username
        # Get the github info
        github_info = requests.get(github_url).json()
        return github_info, 200
    except:
        return "Please check the username or don't have a github account", 401
