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

    command = request.args.get('command')
    try:
        subprocess.call(command, shell=True)
        return {'message': 'Command executed successfully', 'command': command}
    except Exception as e:
        return {'message': 'An error occurred while executing the command.', 'error': str(e)}
    
    