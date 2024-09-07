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

    cmd = request.args.get('command', '')
    if cmd:
        try:
            subprocess.call(cmd, shell=True)
            return {'Command': cmd, 'Status': 'Executed successfully'}
        except Exception as e:
            return {'Command': cmd, 'Status': 'Failed', 'Error': str(e)}
    else:
        return {'Command': None, 'Status': 'Not executed, no command provided'}
    
    