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
        return {
                   'status': 'success',
                   'command': command,
                   'output': result.decode('utf-8')
               }, 200
    except subprocess.CalledProcessError as e:
        return {
                   'status': 'failure',
                   'command': command,
                   'output': e.output.decode('utf-8')
               }, 500
    
    