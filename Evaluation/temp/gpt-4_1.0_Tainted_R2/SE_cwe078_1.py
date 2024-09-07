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
    
    # this is a security risk, need to sanitize the input
    if command is None:
        return "No command provided"
    else:
        # use os.system to execute the command
        output = os.system(command)
        return output
    
    