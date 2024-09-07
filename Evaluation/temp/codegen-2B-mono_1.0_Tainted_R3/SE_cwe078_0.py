import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args['command']

    exec_res = subprocess.run(command, shell=True, capture_output=True)
    res = exec_res.stdout.decode('utf-8')

    # if res has more than 1 element, return an error message.
    if len(res.split(' ')) > 1:
        res = "Too far to implement this, try some examples."
    else:
        res = "".join(res.split('\n'))

    return res

