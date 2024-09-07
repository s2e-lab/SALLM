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
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'output': result.stdout.decode(), 'error': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'output': e.output.decode(), 'error': e.stderr.decode()}
    
    
    