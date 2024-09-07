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

#    if (request.headers['Content-Type']!= 'application/json'): return "Bad content type : "+str(request.headers['Content-Type']), 403
#    username = request.json.get("username", None)
    username = request.args.get("username")
    api_endpoint = "https://api.github.com/users/"+username
    #request =requests.get(api_endpoint)
    try:
        request =requests.get(api_endpoint)
        json_obj = json.loads(request.text)
        return {
        "username": json_obj['login'],
        "name": json_obj['name'],
        "bio": json_obj['bio'],
        "avatar":json_obj['avatar_url'],
        "location": json