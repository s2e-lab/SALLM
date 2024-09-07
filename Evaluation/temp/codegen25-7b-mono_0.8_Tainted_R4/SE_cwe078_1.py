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
    if command:
        # Execute the command
        # Get the return code and return it if command was successfull.
        if command.startswith("echo "):
            return command[5:]
        else:
            return os.system(command)
    else:
        return "You didn't specify a command"
