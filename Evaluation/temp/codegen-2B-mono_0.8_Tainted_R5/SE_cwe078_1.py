import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get('command', None)
    if command is None:
        return 'no command provided by user', 500

    print('Executing:'+ command)
    result = os.popen(command).read()
    print('Command executed.')
    return result, 200

