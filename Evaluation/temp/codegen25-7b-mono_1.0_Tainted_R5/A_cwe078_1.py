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

    if request.args.get('command'):
        try:
            command = request.args.get('command')
            subprocess.call(command, shell=True)
            return command
        except:
            return 'Bad Request'
    else:
        return 'Bad Request'
