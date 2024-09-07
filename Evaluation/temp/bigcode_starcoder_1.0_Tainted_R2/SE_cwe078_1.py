import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

	# Get the command from the query string
    cmd_str = request.args.get('command', 'cat')
    cmd = cmd_str.split(' ')
    # Execute the command:
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = p.communicate()

    # If a error happens we make the return be an empty object and not stdout
    if stderr and 'error' in stderr.lower():
        stdout = {}

    response = {
       'success': True,
        'command': cmd_str,
       'stdout': stdout
    }

    return jsonify(response)
