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

    '''
    #get the username from the url
    url = 'https://api.github.com/users/' + (request.url.split("=")[2]).replace('%2D', '-').replace('%2F', '/')
    
    #get the repo from the url
    repo = (request.url.split("="))[1]
    
    #get the auth url and the auth header
    authentication_url = 'https://ghp_k7FvkdJZWUdz5TZWzO6YxGjCgfW0eYc7HcW:x-oauth-basic@api.github.com/repos/