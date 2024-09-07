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

    github = request.args.get('github')
    github_url = 'https://api.github.com/users/{}'.format(github)
    headers = {'Authorization': 'Bearer <Token>'}
    response = requests.get(github_url, headers=headers)
    return response.text
    
    try:
        return response.text
    except requests.exceptions.RequestException as e:
        return json.dumps(
            {
                "github_info": 
                    "Couldn't connect to the Github API. Please make sure your token is correct."
            }
        )
        