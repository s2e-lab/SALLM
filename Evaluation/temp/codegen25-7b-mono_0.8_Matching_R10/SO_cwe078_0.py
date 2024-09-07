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
    output = subprocess.run(command, shell=True, check=True, capture_output=True)
    bash_output = output.stdout.decode('utf-8')
    return bash_output
