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
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    
    if error:
        return {
            'status': 'Error',
            'message': error.decode('utf-8')
        }
    else:
        return {
            'status': 'Success',
            'message': output.decode('utf-8')
        }
    
    
    