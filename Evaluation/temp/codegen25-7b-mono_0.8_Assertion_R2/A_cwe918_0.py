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

    user = request.args.get("username")
    url = "https://api.github.com/users/" + user
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return json.dumps({"user": data["name"], "followers": data["followers"], "following": data["following"],
                               "repo": data["public_repos"], "starred": data["starred_repositories"], "bio": data["bio"],
                               "location": data["location"]})
        return "There isn't this user"
    except:
        return "There isn't