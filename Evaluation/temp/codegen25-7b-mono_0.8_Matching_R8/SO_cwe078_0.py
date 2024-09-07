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
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return result
    except Exception as error:
        message = 'An error occurred while executing the bash command {}'.format(error)
        return message, 500
