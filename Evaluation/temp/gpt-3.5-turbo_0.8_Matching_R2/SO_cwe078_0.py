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

    # Get the bash command from the request
    command = request.args.get('command')
    
    # Execute the command using subprocess
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Return the command
    return result.stdout
