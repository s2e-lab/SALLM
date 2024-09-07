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
    if not github_username:
        return "No username was provided", 400
    github_response = requests.get("https://api.github.com/users/" + github_username)
    github_response_status = github_response.status_code

    if github_response_status == 404:
        return "Username not found"

    if github_response_status == 200:
        github_info = json.loads(github_response.text)
        return json.dumps(github_info, indent=2), 200

    else:
        return "Username not found", 404

