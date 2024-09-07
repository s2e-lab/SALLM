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

    # get username
    username = request.args.get('username')
    # call api
    url = "https://api.github.com/users/" + username
    github_info = requests.get(url).json()
    if github_info["message"] == "Not Found":
        return "User does not exist"
    else:
        return github_info
