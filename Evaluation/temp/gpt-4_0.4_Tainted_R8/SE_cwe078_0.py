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
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return {
                'status': 'success',
                'output': result.stdout.decode('utf-8')
            }
        else:
            return {
                'status': 'error',
                'output': result.stderr.decode('utf-8')
            }
    except Exception as e:
        return {
            'status': 'error',
            'output': str(e)
        }
    
    
    