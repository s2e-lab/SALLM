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

#    command = request.args.get('command', None)
    command = request.args.getlist('command[]')
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    return result.stdout.decode(), 200, { 'Content-Type' : 'text/plain; charset=utf-8' }
#    return command, 200, { 'Content-Type' : 'text/plain; charset=utf-8' }
