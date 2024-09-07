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

    name = request.args.get("name").strip()
    if name == '':
        return json.dumps({"message":'Enter Username'})
    r = requests.get("https://api.github.com/users/" + name).json()
    return json.dumps(r)

