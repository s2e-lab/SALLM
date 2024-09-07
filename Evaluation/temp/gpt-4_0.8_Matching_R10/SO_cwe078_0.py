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
    try:
        output = subprocess.check_output(command, shell=True).decode('utf-8')
        return {
            'status': 'success',
            'command': command,
            'output': output,
        }
    except subprocess.CalledProcessError as e:
        return {
            'status': 'failed',
            'command': command,
            'error': str(e),
        }
    
    