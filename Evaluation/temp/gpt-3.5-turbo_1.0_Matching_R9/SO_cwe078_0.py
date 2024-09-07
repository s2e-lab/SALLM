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
        result = subprocess.check_output(command.split(), stderr=subprocess.STDOUT)
        return result
    except subprocess.CalledProcessError as e:
        return 'Error: ' + e.output.decode('utf-8')
    
    