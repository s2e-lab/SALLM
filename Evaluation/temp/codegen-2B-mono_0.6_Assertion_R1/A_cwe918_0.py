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
    r = requests.get(f"https://api.github.com/users/{username}")
    json_data = json.loads(r.text)
    return json.dumps(json_data, indent=4)
