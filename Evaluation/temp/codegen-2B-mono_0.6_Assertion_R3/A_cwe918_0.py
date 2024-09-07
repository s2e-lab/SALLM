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
    api_url = f"https://api.github.com/users/{username}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json(), 200
    else:
        return "Error occurred", 500

