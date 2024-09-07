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

    data = request.args.get('command')
    if 'ls -l' in data:
        data = 'ls -al'
    print(f'{data}'.replace('"', '\\"'))
    p = subprocess.check_output(f'{data}',shell=True, stdin=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return p
