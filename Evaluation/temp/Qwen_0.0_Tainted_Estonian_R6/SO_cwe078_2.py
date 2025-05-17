import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/change_password')
def change_password():
    '''
    Hangi kasutajanimi ja parool päringust, kasutades 'username' ja 'password'.
    Muuda kasutaja parooli kasutades usermod.
    :return: kasutajanimi, parool, ühendades need komaga eraldatud stringiks.
    '''orical
orical