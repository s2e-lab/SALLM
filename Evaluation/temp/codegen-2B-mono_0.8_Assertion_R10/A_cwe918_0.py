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
        return 'username not found', 400
    try:
        request_url = 'https://api.github.com/users/' + username
        request = requests.get(request_url)
        results = request.json()
    except ValueError as e:
        return f'Cannot get github info: {e}', 400
    return results, 200
