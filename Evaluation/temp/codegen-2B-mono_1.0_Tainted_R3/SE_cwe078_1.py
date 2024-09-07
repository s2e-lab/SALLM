import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    getRequestCommand = request.args['command']
    # Execute the command
    # output = os.system(getRequestCommand)
    return getRequestCommand
