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
    if command == None:
        return 'Please provide a bash command', 400
    response = subprocess.run(command, shell=True)
    return 'Bash command executed', 200
