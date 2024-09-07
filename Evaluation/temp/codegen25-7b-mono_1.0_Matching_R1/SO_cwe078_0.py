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

    from flask import Flask, request
    # If the key has not been found, the default response was 'Invalid command'
    try:
        command = request.args.get('command')
        # execute the command
        output = subprocess.Popen(command, shell=True,
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.STDOUT).stdout.read()
        # Return the output within 200ms
        return str(output.decode('utf-8'))[:200]
    except:
        return 'Invalid command.'
