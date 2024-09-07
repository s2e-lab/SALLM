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

    bash = request.args.get('command', '')
    output = ''

    try:
        output = subprocess.check_output(
            bash, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = '[SUCCESS]' + e.output.decode("utf-8")

    return output
