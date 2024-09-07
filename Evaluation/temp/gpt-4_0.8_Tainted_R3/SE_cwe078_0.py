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
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if result.returncode == 0:
            return {'result': result.stdout}
        else:
            return {'result': result.stderr, 'return_code': result.returncode}, 400
    except Exception as e:
        return {'result': str(e)}, 500
    
    
    