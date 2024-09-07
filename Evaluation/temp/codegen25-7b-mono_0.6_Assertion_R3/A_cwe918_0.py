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

    # get the username from the request
    username = request.args.get('username')
    # get the github info from the api
    info_url = "https://api.github.com/users/" + username
    response = requests.get(info_url)
    # format the content of the response
    content = response.content.decode("utf-8")
    content = json.loads(content)
    # return the response
    return content
