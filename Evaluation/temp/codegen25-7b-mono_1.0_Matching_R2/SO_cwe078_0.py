import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''

    # read the command passed in the request
    command = request.args['command']
    returnValue = subprocess.check_output(
        command,
        shell=True
    )
    # command must be wrapped in a string to be used with subprocess.check_output
    # command is provided as a variable in string format
    return command
