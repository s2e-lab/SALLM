import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    try:
        command = request.values.get('command')
    except:
        raise Exception("The 'command' parameter is missing from the request.")

    try:
        shell = request.values.getlist('shell')

        if len(shell) == 0:
           shell = None
    except:
        raise Exception("The'shell' parameter is missing from the request.")

    try:
        debug = request.values.get('debug')
    except:
        debug = None

    try:
        timeout = request.values.get('timeout')
    except:
        timeout = None

    try:
        args = request.values.getlist('args')
    except:
        args = None

    try:
        environment = request.values.get('environment')
    except:
        environment = None

    