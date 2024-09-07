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
        command = command.replace("\n", "\\n")
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return_string = f"Return code: {result.returncode}\n"
        return_string += f"Stdout: {result.stdout.decode('utf-8')}\n"
        return_string += f"Stderr: {result.stderr.decode('utf-8')}\n"
        return return_string
    else:
        return "No command given."
