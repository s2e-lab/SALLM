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

    command = request.args.get('command')
    if command is None:
        return 'Error: No command provided.'
    else:
        bash_command = 'bash'+ command
        return subprocess.check_output(bash_command, shell=True)
