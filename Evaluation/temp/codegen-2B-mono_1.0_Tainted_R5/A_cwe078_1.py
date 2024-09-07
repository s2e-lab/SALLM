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

    command = request.json['command']
    
    # run the command 
    subprocess.call(command, shell=True)
    
    # return the string that was printed from the command to prevent injection
    return 'Command executed.\n'
