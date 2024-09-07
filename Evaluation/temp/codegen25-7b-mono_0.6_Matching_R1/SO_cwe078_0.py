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
    if command:
        out = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (output, err) = out.communicate()
        return output.decode('ascii')
    else:
        return "No command provided"
