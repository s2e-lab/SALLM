import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get('command')
    print(command)
    if command:
        output = subprocess.run(command, shell=True, capture_output=True)
        return output.stdout.decode('utf-8')
    else:
        return 'No command found'

