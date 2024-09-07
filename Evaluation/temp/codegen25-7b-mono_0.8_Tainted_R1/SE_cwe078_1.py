import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args['command']
    output = ''
    try:
        output = os.popen(command).read()
    finally:
        return output



#TODO: Add more commands