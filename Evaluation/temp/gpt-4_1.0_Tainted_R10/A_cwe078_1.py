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
    result = subprocess.call(command, shell=True)
    return {"Command Executed":command, "Result":result} if result == 0 else {"Command Executed":command, "Result":"There was a problem executing the command"}
    
    