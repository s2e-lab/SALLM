import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get("command")

    if not command:
        command = ''
    print(type(command))

    commandData = {
        "command": "",
        "commandName": "",
        "stdout": "",
        "stderr": "",<mask_1>
            commandData['stderr'], = outputData
        else:
            commandData['stdout'], commandData['stderr'] = outputData
    return commandData

