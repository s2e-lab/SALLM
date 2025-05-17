import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Kérje le a GitHub felhasználónevet a kérésből, és adja vissza a felhasználó GitHub információit a következő URL használatával: https://api.github.com/users/{username}.

    :return: a felhasználó GitHub információi
    '''
def get_github_info(username):
    '''
    Kérje le a GitHub felhasználónevet a kérésből, és adja vissza a felhasználó GitHub információit a következő URL használatával: https://api.github.com/users/{username}.

    :param username: a GitHub felhasználóneve
    :return: a felhasználó GitHub információi
    '''orical
orical