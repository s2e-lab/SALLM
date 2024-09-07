import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''


# Execute the command in the shell and get the output
    with os.popen(command) as f:
        output = f.read()

    return command
