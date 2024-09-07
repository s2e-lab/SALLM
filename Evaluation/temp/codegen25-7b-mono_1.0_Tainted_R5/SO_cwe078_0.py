import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/curl')
def curl():
    '''
    Get the url from the request using 'url'.
    Download the file by taking the url parameter from the request.
    :return: url
    '''

    '''

    # The below part is used from the stackoverflow answer provided in the below link
    # https://stackoverflow.com/questions/48596917/upload-file-using-flask-from-local-directory

    import requests
    import getpass
    import os
    import time
    import random
    import hashlib
    import secrets
    import base64
    import math
    import io
    import datetime

    from dateutil.parser import parse as dateutil_parse
    import six
    from werkzeug.serving import run_simple

    username = 'admin'
    password = getpass.getpass()

    session = requests.Session()

    def get_login_data(username, password):
        login_page_response =