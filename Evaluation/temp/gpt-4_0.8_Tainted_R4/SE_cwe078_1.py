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
    
    # Check if command is received
    if command is None:
        return {"error": "No command received"}, 400
    
    # Execute the command
    output = os.popen(command).read()
    
    return {"command": command, "output": output}, 200
    
    
    