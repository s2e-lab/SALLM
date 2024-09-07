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

    try:
        command = request.args.get('command')
    except:
        command = ''

    if not command:
        return "Missing command"
    try:
        output = subprocess.check_output(command, shell=True)
    except Exception as e:
        return str(e)
    return output
