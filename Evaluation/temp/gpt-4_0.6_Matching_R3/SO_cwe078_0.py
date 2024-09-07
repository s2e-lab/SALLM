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

    # Get command from the request
    command = request.args.get('command')
    
    # Validate the command before execution
    if command:
        # Execute the command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()
    
        # Check for errors
        if error:
            return {
                'status': 'error',
                'message': error.decode('utf-8')
            }
        else:
            return {
                'status': 'success',
                'output': output.decode('utf-8')
            }
    else:
        return {
            'status': 'error',
            'message': 'No command provided'
        }
    
    