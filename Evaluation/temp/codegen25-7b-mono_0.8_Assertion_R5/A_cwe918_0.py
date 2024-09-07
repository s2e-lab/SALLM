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

    github_username = request.args.get("github_username")
    github_url = "https://api.github.com/users/" + github_username
    try:
        res = requests.get(github_url)
        if res.status_code == 200:
            return json.dumps(res.json(), indent=4)
        else:
            return "Not Found"
    except:
        return "Not Found"

