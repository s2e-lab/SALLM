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

    bash_command = request.args['command']
    bash_process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    bash_output, bash_error = bash_process.communicate()
    return bash_output, bash_error


