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

    # Get the command from request
    command = request.args.get('command')
    
    # Check if the command is valid
    if not command:
        return "No command provided", 400
    
    try:
        # Execute the command
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
        # If there were any errors during the execution of the command
        if result.stderr:
            return f"An error occurred while executing the command: {result.stderr.decode('utf-8')}", 500
    
        return result.stdout.decode('utf-8'), 200
    except Exception as e:
        return str(e), 500
    
    