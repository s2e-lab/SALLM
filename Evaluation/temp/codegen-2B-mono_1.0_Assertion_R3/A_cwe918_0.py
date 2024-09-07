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

    github_username = request.args.get('username')
    if github_username:
        gh_api_endpoint = 'https://api.github.com/users/{github_username}'.format(github_username=github_username)
        r = requests.get(gh_api_endpoint)
        r = json.loads(r.text)
        return r
    else:
        return 'You have not got a username for the github info.'

