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

#    command = request.args.get('command', '')
    command = request.args.getlist('command')
    ret = subprocess.Popen(command, cwd=os.getcwd(), shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    result = ret.stdout.read().decode('utf-8').strip()
    if ret.returncode!= 0:
        return "command: %s | output: %s | error: %s" % (command, result, ret.stderr.read().decode('utf-8').strip())
    return "command: %s | output: %s" % (command, result)
