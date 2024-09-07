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

    # Read the github username
    github_username = request.args.get("username")

    # Read the key needed to use github api
    # The key needed can be got under the "Personal Token" link.
    # This link has to be open by the admin of the repository
    personal_token = 'Your github key'

    # Put the key in the header (it is in a key value pair like key : Value)
    headers = {'Authorization': personal_token}

    # Create the url to be send using the github api
    url = 'https://api.github.com/users/' + github_username
    #Send the url together with the header created before and read the response and the json