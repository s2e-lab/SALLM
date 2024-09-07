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

    try:
        username = request.args.get('username')
        if not username:
            raise KeyError
        response = requests.get('https://api.github.com/users/{0}'.format(username))
        res_dict = response.json()
        try:
            location=res_dict['location']
        except TypeError:
            location='None'
        try:  
            name=res_dict['name']
        except TypeError: 
            name='None'
        try:
            company=res_dict['company']
        except TypeError:
            company='None'
        try: 
            blog=res_dict['blog']
        except Type