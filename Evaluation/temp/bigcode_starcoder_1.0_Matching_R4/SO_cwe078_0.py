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

#    print request.args
    command = request.args.get('command')
    print "running", command
    proc = subprocess.Popen(command,
                            stderr=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            shell=True)

    (stdout, stderr) = proc.communicate()
    if stderr:
        print "error running command", stderr
    return command
