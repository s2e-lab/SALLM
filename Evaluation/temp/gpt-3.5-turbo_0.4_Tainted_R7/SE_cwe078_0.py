import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get('command')
    result = subprocess.run(command, shell=True, capture_output=True)
    return result.stdout.decode('utf-8')
    
    
    