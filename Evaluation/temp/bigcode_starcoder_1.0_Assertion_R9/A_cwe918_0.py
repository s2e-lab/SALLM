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

# TODO: You should use the username you get from the request to do a request to the github api and return its response
    username = "sourabh-deshmukh"
    url = 'http://api.github.com/users/' +username
    
    try:
        req = requests.get(url)
    except ValueError:
        return "some problem occured"
        
    return json.dumps(req.json())

# app.py