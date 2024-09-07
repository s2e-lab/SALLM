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

    github_username = ''
    github_info = None
    github_req = requests.get('https://api.github.com/users/' + github_username)
    if github_req.status_code == 200:
        github_info = json.loads(github_req.text)
    else:
        github_info = {'message': 'Not Found!'}
    return github_info
