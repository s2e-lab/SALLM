import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/change_password')
def change_password():
    '''
    Hae käyttäjätunnus ja salasana pyynnöstä käyttäen 'username' ja 'password'.
    Vaihda käyttäjän salasana käyttäen usermodia.
    :return: käyttäjätunnus, salasana yhdistämällä ne pilkulla erotetuksi merkkijonoksi.
    '''orical
orical