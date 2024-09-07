import subprocess
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
        return 'No command was specified'

    try:
        out = subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as e:
        out = e.output
    return out

