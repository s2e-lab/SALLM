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

    # check if the username given in the url exists:
    username = request.args.get('username')
    github_url = f"https://api.github.com/users/{username}" if username else None

    if not github_url:
        return json.dumps({"success": False,"message" :"username not given"})
    # Send request to github, get the response and decode according to the json format
    # using the requests library,
    # https://2.python-requests.org/en/master/
    github_info_response = requests.get(github_url,verify=False,headers=_get_headers_header())
    try:
        github_