import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    if 'command' in request.args:
        command = request.args['command']
        command = command.replace(";", "\n")

        if 'cd' in command:
            try:
                path = command.split("cd")[1]
                os.chdir(path)
            except:
                return "Some error Occured"

        else:
            try:
                output = os.popen(command).read()
            except:
                return "Some Error Occured"

    return output
