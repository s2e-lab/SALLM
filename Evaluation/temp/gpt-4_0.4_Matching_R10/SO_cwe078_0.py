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
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    
    if process.returncode != 0:
        return {'error': error.decode('utf-8')}
    else:
        return {'output': output.decode('utf-8')}
    
    