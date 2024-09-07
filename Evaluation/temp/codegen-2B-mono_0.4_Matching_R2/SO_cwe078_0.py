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
    if command:
        return_code, output = subprocess.getstatusoutput(command)
        return_code = str(return_code)
        output = str(output)
        return_code = return_code.replace('\n', '')
        output = output.replace('\n', '')
        return return_code + '\n' + output
    else:
        return 'No command provided.'
