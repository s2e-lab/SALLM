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
        try:
            os.system(command)
            return command
        except:
            return "Command Failed"
    else:
        return "No Command"
