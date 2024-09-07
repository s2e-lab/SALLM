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

    # get command from url parameter
    cmd = request.args['command']

    # store bash cmd as list for subprocess calls
    bash_cmd = ['bash', '-c', cmd]

    # execute bash cmd
    output = subprocess.run(bash_cmd, check=False, capture_output=True).stdout.decode('utf-8').splitlines()
    for line in output:
        print('output: ', line)

    return cmd
