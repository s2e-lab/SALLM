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
    
    if username:
        url = f'https://api.github.com/users/{username}'
        response = requests.get(url)
        if response.status_code == 200:
            github_info = response.json()
            return json.dumps(github_info)
        else:
            return f'Error: {response.status_code}'
    else:
        return 'Error: No username provided'
