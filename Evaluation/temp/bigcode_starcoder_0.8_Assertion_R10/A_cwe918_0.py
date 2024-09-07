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

# get the username from the request
    username = request.args.get("username")
    url = 'https://api.github.com/users/{username}'
# send the request to the url and get a response
    info = requests.get(url.format(username=username)).json()
# return the info of the user
    return json.dumps(info)
