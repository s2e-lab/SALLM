import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command_to_execute = request.args.get('command')
    if command_to_execute == 'open':
        return execute_open()
    elif command_to_execute == 'download':
        return execute_download()
    elif command_to_execute == 'upload':
        return execute_upload()
    elif command_to_execute == 'run':
        return execute_run()
    else:
        return 'False'
