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

    if request.args.get('command'):
        command = request.args.get('command')
        return subprocess.check_output(command, shell=True)
    return "No command in request body!"
