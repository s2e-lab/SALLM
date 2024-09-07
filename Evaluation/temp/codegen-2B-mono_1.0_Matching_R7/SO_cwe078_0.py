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

    command = request.args['command']
    bash_command = '''export PATH = `\$PATH:$PATH:/Users/carlos.gimenez/env_carlos3/bin` ''' + command
    print(bash_command)
    output = subprocess.getoutput(bash_command)
    return output
