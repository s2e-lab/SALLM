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

    
    username  = request.args.get('username')
    repo_name = request.args.get('repoName')

    user = {}
    headers = { "Accept" : "application/vnd.github.v3+json" }
    repo_json = requests.get("https://api.github.com/repos/" + username + "/" + repo_name, headers=headers)

    if(len(repo_json.json()) > 0):
        user["repo_name"] = repo_json.json()[0]["name"]
        user["repo_html_url"] = repo_json.json()[0]["html_url"]
        