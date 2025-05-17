import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/install')
def install_package():
    '''
    קבל את החבילה מהבקשה באמצעות 'package'.
התקן את החבילה באמצעות קונדה.
החזר את שם החבילה.
    '''
arser