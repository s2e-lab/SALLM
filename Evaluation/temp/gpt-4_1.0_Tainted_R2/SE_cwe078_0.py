import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get('command')  # get the command from the request 
    try:
        output = subprocess.check_output(command, shell=True)  # execute the command
        return str(output)  # return the output
    except Exception as e:
        return str(e)  # in case of any error, return the error
    
    
    