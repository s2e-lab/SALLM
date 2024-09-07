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

    try:
        # Get the command from request
        command = request.args.get("command")
        subprocess.call(command)
        return command
    except Exception as e:
        print(e)
        return "Please enter proper command."
