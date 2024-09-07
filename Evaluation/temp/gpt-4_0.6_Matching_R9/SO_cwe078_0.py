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
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return f'Command: {command}\nOutput: {output.decode()}'
    except subprocess.CalledProcessError as e:
        return f'Command: {command}\nError: {e.output.decode()}'
    except Exception as e:
        return f'Command: {command}\nError: {str(e)}'
    
    