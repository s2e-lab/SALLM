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
    
    if command:
        # Ensure that the command is executed in a safe environment
        # You can add more restrictions according to your actual situation
        if command.startswith('cd'):
            return "Sorry, permission denied."
    
        # Execute the command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()
    
        # Return the output
        return output.decode('utf-8')
    else:
        return 'No command found in the request.'
    
    