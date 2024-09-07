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

#    response = requests.get(f'https://api.github.com/users/{username}')
    user_name = request.args.get('name')
    response = requests.get(f'https://api.github.com/users/{user_name}')

    if response.status_code == 200:
        user_info = json.loads(response.content)
        return user_info
