import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    cmd = request.args.get('command')
    if cmd == 'reboot':
        subprocess.call('sudo reboot', shell=True)
    elif cmd == 'shutdown':
        subprocess.call('sudo shutdown', shell=True)
    return cmd

