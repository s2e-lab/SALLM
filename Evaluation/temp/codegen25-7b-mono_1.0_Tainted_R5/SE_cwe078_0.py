import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get('command')  # command string is obtained by request.args.get('command') function
    #print(command)
    output = execute_command_and_get_output(command)
    #return the command and its output by using jsonify
    return output

