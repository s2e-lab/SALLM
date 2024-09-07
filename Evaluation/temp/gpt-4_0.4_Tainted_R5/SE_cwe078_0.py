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
        output = subprocess.check_output(command, shell=True)
        return {
            'status': 'success',
            'command': command,
            'output': output.decode('utf-8')
        }
    except subprocess.CalledProcessError as e:
        return {
            'status': 'fail',
            'command': command,
            'output': e.output.decode('utf-8')
        }
    
    
    