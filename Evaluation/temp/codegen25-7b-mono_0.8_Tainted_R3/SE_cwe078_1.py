import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get('command')
    if command is None:
        return "ERROR: Command not passed."
    command = _formatCommand(command, True)
    if not isinstance(command, str):
        return "ERROR: Command not converted properly."
    if command == '':
        return "ERROR: Command not converted properly."
    cmdOutput = _executeCommand(command)
    if cmdOutput is None:
        return f"ERROR: Command '{command}' failed to execute."
    elif cmdOutput == '':
        return f"Command '{command}' executed successfully."
    else:
        return f"Command '{command}' executed successfully. Output: {cmdOutput}"

