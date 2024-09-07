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

    bashCommand = request.args.get('command')
    # execute_bash() executes the command and returns the output as well as the status code.
    statusCode, output = executeCommand(bashCommand)
    # Output to the client comes with the status code, thus need to filter the first 4 characters.
    output = output[4:]
    return f"{str(statusCode)}\n{output}"
