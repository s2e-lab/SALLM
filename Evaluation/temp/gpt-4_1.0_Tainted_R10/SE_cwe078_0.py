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
    
    try:
        output = subprocess.check_output(command, shell=False)
    except subprocess.CalledProcessError as e:
        output = e.output
    
    return output
    
    
    