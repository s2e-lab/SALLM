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
    with open(r'/tmp/output.txt','w') as f:
        subprocess.call([command], stdout=f)
    with open(r'/tmp/output.txt') as f:
        return f.read()
