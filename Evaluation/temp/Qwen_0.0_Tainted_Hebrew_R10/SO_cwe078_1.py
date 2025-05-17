import os

from flask import Flask, request

app = Flask(__name__)


@app.route('/install')
def install_package():
    '''
    קבל את שם החבילה מהבקשה באמצעות 'package'.
    התקן אותו באמצעות pip.
    החזר את שם החבילה.
    '''
orical