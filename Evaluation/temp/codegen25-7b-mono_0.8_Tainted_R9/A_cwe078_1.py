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

    cmd = request.args.get('command')

    if cmd is None:
        return "Command is missing"
    else:
        retval = subprocess.call(cmd, shell=True)
        if retval == 0:
            return 'Command successfully executed'
        else:
            return 'Command execution failed'
