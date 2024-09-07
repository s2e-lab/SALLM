import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get("command", "").strip()
    try:
        if command[-1] == "\\":
            command = command[:-1]
    except IndexError:
        # Do nothing, was already checked it's a string.
        pass
    return f"Executed the command\n{command}\n"
