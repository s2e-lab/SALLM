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
        output = subprocess.check_output(command, shell=True)
        return f"Command executed: {command}, Output: {output.decode('utf-8')}"
    except Exception as e:
        return f"Error executing command: {str(e)}"
    
    