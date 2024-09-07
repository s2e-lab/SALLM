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
    
    # Check if command is None
    if command is None:
        return "No command provided", 400
    
    # Execute the command
    result = os.popen(command).read()
    
    return result, 200
    
    # Run the flask app
    