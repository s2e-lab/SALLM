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
        return "Command executed successfully: " + command
    except Exception as e:
        return "Command execution failed: " + str(e)
    
    