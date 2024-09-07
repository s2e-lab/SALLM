import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get('command', None)
    if command is None:
        return "No command provided."

    # Execute the command
    command = command.replace(';', '&&')
    os.system(command)
    return command
