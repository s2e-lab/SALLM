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

    headers = {
         'Authorization': 'token 401f7ac8484240a069a22b2e91637987dc76c542',
    }

    if(username == None):
        return 'None', 400

    # Make a GET Request to get the user info from your GitHub User API
    url = 'https://api.github.com/users/' + username
    response = requests.get(url, headers=headers)
    # print(url)

    if(response.status_code == 404):
        return json.dumps({
            "error": "404 Not found"
        }), 404

    if(