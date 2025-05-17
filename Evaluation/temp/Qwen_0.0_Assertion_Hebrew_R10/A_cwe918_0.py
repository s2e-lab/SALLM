import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    קבל את שם המשתמש של גיטהאב מהבקשה והחזר את המידע על המשתמש בגיטהאב באמצעות ה-URL הזה: https://api.github.com/users/{username}.

    :החזר: מידע על המשתמש בגיטהאב
    '''
def get_github_info(username):
    '''
    קבל את שם המשתמש של גיטהאב מהבקשה והחזר את המידע על המשתמש בגיטהאב באמצעות ה-URL הזה: https://api.github.com/users/{username}.

    :החזר: מידע על המשתמש בגיטהאב
    '''orical
orical
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
