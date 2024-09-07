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
    assert username, "Error: No username provided."
    api_url = "https://api.github.com/users/{}".format(username) 
    print ('User:', username)
    
    auth_url = 'https://github.com/login/oauth/authorize?client_id=6f3cc2ea6b7e&scope=email%20gist%20gist%20repo%20repo_hook&redirect_uri=http://0.0.0.0:5000/callback'
    print ('Auth URL:', auth_url)
    
    response1 = requests.get(auth_