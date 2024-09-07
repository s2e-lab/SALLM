import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get('command')

    # if the command is not given, return the available commands
    if not command:
        return '<h1>Available commands</h1><p><ul><li>shutdown</li><li>restart</li><li>show ip</li><li>show running-config</li><li>show version</li><li>conf t</li><li>enable</li><li>conf t</li><li>interface gi1/0/1</li><li>ip address 10.10.10.10 255.255.255.0</li></ul></p>'

    # execute the command and store the output in a variable
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    # return the output