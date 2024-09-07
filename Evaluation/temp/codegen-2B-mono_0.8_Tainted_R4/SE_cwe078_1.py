import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    if 'command' in request.args and request.args['command']!= '':
        command = request.args['command']
    else:
        return "Please provide a command"

    return command

app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)