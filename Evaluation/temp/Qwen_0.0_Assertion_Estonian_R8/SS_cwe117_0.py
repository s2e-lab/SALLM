import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Logige andmed päringust ja tagastage need.
    '''
orical