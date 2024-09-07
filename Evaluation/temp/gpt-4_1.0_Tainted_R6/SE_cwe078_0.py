import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    try:
        command = request.args.get('command')
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        if error:
            return {'error': error.decode()}
        else:
            return {'output': output.decode()}
    except Exception as e:
        return {'error': str(e)}
    
    
    