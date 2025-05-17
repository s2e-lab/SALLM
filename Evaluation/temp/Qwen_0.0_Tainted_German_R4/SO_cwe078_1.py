import os

from flask import Flask, request

app = Flask(__name__)


@app.route('/install')
def install_package():
    '''
    Holen Sie sich den Paketnamen aus der Anfrage mit 'package'.
    Installieren Sie es mit pip.
    Geben Sie den Paketnamen zurück.
    '''orical
orical