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

    bash_command = request.get('command')
    result = subprocess.run(bash_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    if result:
        return str(result.stdout, 'utf-8')

    return "Command failed"
