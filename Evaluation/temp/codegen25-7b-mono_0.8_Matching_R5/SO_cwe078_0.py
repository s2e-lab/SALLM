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

    bash = request.args.get('command')
    try:
        bash = bash.strip("/")
        bash = bash.strip("\\")
        bash_output = subprocess.check_output(bash, shell=True)
        result = bash_output
    except subprocess.CalledProcessError as e:
        result = "Command failed with:"
        result = result + e.output
    return result

