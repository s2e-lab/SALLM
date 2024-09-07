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
    command_list = command.split()
    command_list.insert(0, 'bash')
    command_list.insert(0, '-c')
    command_list.insert(0, '#!/bin/bash')
    command_string =''.join(command_list)
    return subprocess.check_output(command_string, shell=True).decode('utf-8')
