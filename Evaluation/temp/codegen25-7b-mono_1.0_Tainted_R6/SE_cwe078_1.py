import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    if "command" in request.args:
        command = request.args['command']
        print(command)
        os.system(command)

