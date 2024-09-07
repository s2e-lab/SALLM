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
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8')
    return result
    
    