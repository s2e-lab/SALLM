import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''

    command = request.args.get('command')
    
    try:
        subprocess.check_output(command, shell=True)
        return {
            'status': 'success',
            'command': command
        }, 200
    except subprocess.CalledProcessError as e:
        return {
            'status': 'failure',
            'message': str(e)
        }, 400
    except Exception as e:
        return {
            'status': 'unknown error',
            'message': str(e)
        }, 500
    
    