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

    cmd = request.args.get('command')
    out = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    return out
