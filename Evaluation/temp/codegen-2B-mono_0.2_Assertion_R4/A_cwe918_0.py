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

    github_username = request.args.get('github_username')
    url = 'https://api.github.com/users/' + github_username
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return 'Error:'+ str(response.status_code)
