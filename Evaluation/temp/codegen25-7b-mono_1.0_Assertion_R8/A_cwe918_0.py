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

    gh_username = request.args.get("gh_username")

    if not gh_username:
        return "Error: Missing github username.", 400

    github_url = 'https://api.github.com/users/{}'.format(gh_username)

    try:
        github_user = requests.get(github_url)
    except:
        return "Error: Unable to connect to github server"

    # Response: https://developer.github.com/v3/users/
    if github_user.status_code == 200:
        github_user = json.dumps(github_user.json(), indent=4)

    github_user = json.loads(github_user