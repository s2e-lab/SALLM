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
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]

