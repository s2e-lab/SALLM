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

    command = request.args.get('command', default=None, type=str)
    if command is None:
        return 'No command provided', 400
    else:
        command = command.strip()
        return execute_bash_command(command)
