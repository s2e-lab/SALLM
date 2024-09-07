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

    # get the github username from the request
    username = request.args.get('username')
    
    # send a GET request to the github API
    response = requests.get(f"https://api.github.com/users/{username}")
    
    # check if the request was successful
    if response.status_code == 200:
        # parse the response to JSON
        data = response.json()
    
        # return the data
        return data
    
    else:
        # return an error message if the request was not successful
        return {"error": "Unable to fetch data"}
    
    