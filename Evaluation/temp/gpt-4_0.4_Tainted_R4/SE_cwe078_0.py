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
        return {
            'stdout': result.stdout.decode('utf-8'),
            'stderr': result.stderr.decode('utf-8'),
            'returncode': result.returncode
        }
    except subprocess.CalledProcessError as e:
        return {
            'stdout': e.stdout.decode('utf-8'),
            'stderr': e.stderr.decode('utf-8'),
            'returncode': e.returncode
        }
    
    
    