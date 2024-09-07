import subprocess
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
        output = subprocess.check_output(command, shell=True)
    except KeyError as error:
        return "command = {}".format(error.args[0])
    return output

