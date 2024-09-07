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
    return 'Command Executed: {}'.format(subprocess.call(cmd))
