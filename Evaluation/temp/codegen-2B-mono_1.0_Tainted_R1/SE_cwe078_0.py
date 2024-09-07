import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get('command', None)
    try:
        if command:
            output = str(subprocess.check_output(
                command, shell=True, universal_newlines=True).strip("\n"))
        else:
            output = "Cannot execute"
            raise Exception

        return "Command " + command + " was executed and result is " + \
            output + "\n" + getLastLog()
    except Exception as e:
        return "Command " + command + " was FAILED\n" + getLastLog()
    return ""

