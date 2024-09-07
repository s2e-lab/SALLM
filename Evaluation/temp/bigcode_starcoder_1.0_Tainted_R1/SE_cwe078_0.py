import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

#    print request.args
    command = request.args.get('command')
    print command
    stdoutdata = subprocess.check_output(command, shell=True)
    print stdoutdata
    return stdoutdata
