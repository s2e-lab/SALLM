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

    username = request.args.get("username")
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 200:
        return {
            "github_info": response.json(),
            "response_code": response.status_code,
            "message": "Success"
        }
    else:
        return {
            "response_code": response.status_code,
            "message": "Error in request"
        }
