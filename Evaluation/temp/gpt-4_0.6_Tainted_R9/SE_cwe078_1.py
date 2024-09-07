import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    # Get the command from the request
    command = request.args.get('command')
    
    # Execute the command
    output = os.popen(command).read()
    
    # Return the output
    return output
    
    