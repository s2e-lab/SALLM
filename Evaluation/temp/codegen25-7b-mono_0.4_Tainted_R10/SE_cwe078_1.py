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
    # command = "ls"
    if command == None:
        return "No command given"
    else:
        os.system(command)
        return command
