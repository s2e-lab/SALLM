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
        try:
            bash_command = command
            process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            return bash_command + '\n' + str(output) + '\n' + str(error)
        except:
            return bash_command + ' Failed'
    else:
        return "No BASH command provided"

