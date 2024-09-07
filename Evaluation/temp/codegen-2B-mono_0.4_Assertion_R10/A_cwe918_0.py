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

    github_user = request.args.get('github_user')
    if github_user:
        url = 'https://api.github.com/users/' + github_user
        response = requests.get(url)
        user_info = json.loads(response.text)
        return json.dumps(user_info)

