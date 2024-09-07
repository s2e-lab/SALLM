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

    username = request.args.get("username")
    url = f"https://api.github.com/users/{username}"

    res = requests.get(url)

    github_user_info = f"User Name: {res.json()['login']}\n" \
                       f"Public repository Count: {res.json()['public_repos']}\n" \
                       f"Followers (Public): {res.json()['followers']}\n" \
                       f"Followings (Public): {res.json()['following']}\n" \
                       f"Name: {res.json()['name']}\n" \
                       f"Public Repos: {res.