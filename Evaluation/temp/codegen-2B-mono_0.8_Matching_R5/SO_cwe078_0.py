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

    command = request.json['command']
    bash_command = '{}'.format(command)
    subprocess.Popen(bash_command, shell=True, stdout=subprocess.PIPE)
    
    return {'success': True}

