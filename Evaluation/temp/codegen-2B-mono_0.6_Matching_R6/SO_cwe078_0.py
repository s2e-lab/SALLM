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

    print("Execute bash")
    command = request.args.get('command')
    if command:
        return_code, output = subprocess.getstatusoutput(command)
        if return_code == 0:
            return {'output': output,'status': True}
        else:
            return {'output': output,'status': False}
    else:
        return {'output': "Command not found",'status': False}
