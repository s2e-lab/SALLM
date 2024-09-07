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
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"An error occurred while trying to execute the command: {str(e)}"
    
    
    