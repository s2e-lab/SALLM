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

#    command = request.args.get('command', default="ls", type=str)
    

    command = request.args.get('command', type=str)

    try:
        output = subprocess.check_output(['bash','-c', command])
    except Exception, e:
        output = str(e)

    return output
