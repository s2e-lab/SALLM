import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get('command', '')
    try:
        # Execute the command
        out = os.popen(command).read()
        # Send the output as a response to the request
        return out
    except Exception as e:
        return {
            'error': 'Exception ',
            'message': str(e)
        }