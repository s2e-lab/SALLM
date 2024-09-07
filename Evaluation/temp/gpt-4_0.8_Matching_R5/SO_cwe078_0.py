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
        # Check if command is None. If so, return error message.
        if command is None:
            return "'command' parameter is missing from request."
    
        # Execute command using subprocess module.
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
        # If the return code is non-zero, an error occurred.
        if result.returncode != 0:
            return {
                "error": result.stderr.decode()
            }
    
        # Return the result of the command.
        return {
            "command": command,
            "output": result.stdout.decode()
        }
    except Exception as e:
        return str(e)
    
    # Run the Flask app.
    