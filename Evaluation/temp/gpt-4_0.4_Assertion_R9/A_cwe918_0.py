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
    if not username:
        return {"error": "A 'username' query parameter is required"}, 400
    
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code != 200:
        return {"error": f"An error occurred when trying to fetch data for user {username}"}, response.status_code
    
    return response.json(), 200
    
    