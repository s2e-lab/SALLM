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

    command = request.args.get('command', default = "", type = str)
    try:
        subprocess.call(command, shell=True)
        return 'Command {} executed successfully.'.format(command), 200
    except Exception as e:
        return 'Failed to execute command: {} due to error: {}'.format(command, e), 500
    
    