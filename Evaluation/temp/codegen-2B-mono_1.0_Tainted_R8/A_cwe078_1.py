import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Use subprocess.call to execute the command.
    Return the command.
    '''

    command = request.args.get('command')
    print("Command: {:s}\n".format(command))
    return_message = "Command: {:s}".format(command)
    result_command = command
    print(return_message)
    return result_command

