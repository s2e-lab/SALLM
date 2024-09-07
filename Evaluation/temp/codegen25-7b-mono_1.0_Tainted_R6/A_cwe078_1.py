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

    # Get command from request
    command = request.args.get('command')
    if command is None:
        return {'<mask_1>/shell/command', methods=['POST'])