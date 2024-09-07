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

    username = request.args.get("username")
    if not username:
        return json.dumps({"message":"Error: No username provided"})
    try:
        r = requests.get('https://api.github.com/users/{}'.format(username))
        if r.status_code == 200:
            github_info = r.json()
            return json.dumps({"github_info": github_info})
        else:
            return json.dumps({"message": "Error: {}".format(r.status_code)})
    except Exception as e:
        return json.dumps({"message": "Error: {}".format(e)})


