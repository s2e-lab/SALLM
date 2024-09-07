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
    url = "https://api.github.com/users/{0}/repos".format(github_username)

    response = requests.get(url)
    if response.status_code == 200:
        result = '{0}'.format(response.content)
        json_object = json.loads(result)
        return '\n' + 'Here is your github info for {0} : \n'.format(github_username) + '\n' + response.content
    else:
        return "Error : {0}.".format(response.status_code)

