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

    command = request.values['command']
    stdout = run_via_subprocess(command)
    return {
       'status': "SUCCESS",
       'result': stdout
    }
