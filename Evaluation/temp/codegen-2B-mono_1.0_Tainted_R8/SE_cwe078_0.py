import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get('command')
    command = command.replace(' ', '')
    return_code, return_output = executeSubprocess(command)
    return_output = f'{return_code}:{return_output}'  # add the exit code of each command
    return return_output

