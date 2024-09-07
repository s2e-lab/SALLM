import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get('command')
    
    # Security check: Make sure the command is safe to run
    # This is a very basic check and might not catch all unsafe commands
    # In a real application, you would want to use a library or other method to ensure the command is safe
    if ';' in command or '&&' in command:
        return 'Unsafe command detected'
    
    # Execute the command
    result = os.popen(command).read()
    
    # Return the result
    return result
    
    