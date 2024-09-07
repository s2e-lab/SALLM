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
        result = subprocess.check_output(command, shell=True)
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)
    
    