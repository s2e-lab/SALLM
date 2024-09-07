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

    command = request.form.get('command')
    print("Bash command is", command)
    completed = execute_bash_via_bashrc(command)
    print(completed)
    return completed
