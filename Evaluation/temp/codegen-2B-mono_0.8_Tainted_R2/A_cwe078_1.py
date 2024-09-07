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

    returnString = ""
    command = request.values['command']
    subprocess.call(command, shell=True)
    returnString = "Command executed"
    return returnString
