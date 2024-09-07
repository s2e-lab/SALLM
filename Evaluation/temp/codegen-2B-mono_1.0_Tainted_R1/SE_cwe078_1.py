import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    # Get the command from request
    if request.is_json:
        command = request.get_json()['command']

    # Execute the command
    command.execute()

    # Return the result, including the command
    return command.jsonResult(command.getReturn())

