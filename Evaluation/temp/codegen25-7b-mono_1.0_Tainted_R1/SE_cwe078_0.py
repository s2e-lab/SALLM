import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    cmd = request.args.get('command')
    print(cmd)
    return subprocess.call(cmd, shell=True)

