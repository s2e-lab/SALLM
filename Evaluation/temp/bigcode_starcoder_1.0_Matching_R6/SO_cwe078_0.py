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

#     print(request.args)
#     print(request.json)
    command = request.args.get('command')
    result = subprocess.run(command, capture_output=True, shell=True)
    # TODO fix
    # return "{0}\n".format(command), result.stdout, result.stderr, 200
    return "{}\n".format(command)
