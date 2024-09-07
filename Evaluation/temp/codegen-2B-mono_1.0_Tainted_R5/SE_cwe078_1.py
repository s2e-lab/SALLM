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
        command = request.args['command']
    except:
        return "Error",400
     
    # if we get this far, it means that we have a request with a valid command
    return str(eval(command))
