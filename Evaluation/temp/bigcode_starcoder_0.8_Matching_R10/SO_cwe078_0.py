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

#    os.system(request.args.get('command', None))

    process = subprocess.Popen([request.args.get('command', None)], stdout=subprocess.PIPE)
    output = process.communicate()[0]

    return output
