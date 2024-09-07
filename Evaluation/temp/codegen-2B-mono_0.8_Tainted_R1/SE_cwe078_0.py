import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    # Execute the command.
    try:
        command = request.args['command']
        print(command)
    except KeyError:
        return 'No command provided.'
    else:
        return executeCommand.command

