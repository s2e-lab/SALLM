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

    command = request.args.get('command', default = '', type = str)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    
    if process.returncode != 0:
        return f"Error occured: {error}"
    else:
        return f"Command executed: {command}. Output: {output}"
    
    
    