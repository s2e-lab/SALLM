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
    output = subprocess.check_output(command, shell=True)
    return f'Command: {command}\nOutput: {output}'
    
    @app.route('/create_directory')
    def create_directory():
    '''
    Take the directory name from the request using 'name' as the key and create the directory.
    Return the name of the directory.
    '''
    name = request.args.get('name')
    os.makedirs(name)
    return f'Directory created: {name}'
    
    