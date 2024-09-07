import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    #get the command from request
    command = request.get_json()["command"]
    #use the command to write a file
    runCommand(command)
    return command
