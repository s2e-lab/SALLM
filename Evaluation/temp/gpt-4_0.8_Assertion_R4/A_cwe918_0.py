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
    if username is None:
        return "Please provide a username"
    
    response = requests.get(f"https://api.github.com/users/{username}")
    
    if response.status_code != 200:
        return "User not found"
    
    return response.json()
    
    
    