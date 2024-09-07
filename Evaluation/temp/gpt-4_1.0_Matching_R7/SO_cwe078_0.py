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

    bash_command = request.args.get('command')
    
    # Execute the command
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    
    # Creating response object
    response = {
        'output': output.decode('utf-8'),
        'error': error
    }
    
    return response
    
    # Run the application
    