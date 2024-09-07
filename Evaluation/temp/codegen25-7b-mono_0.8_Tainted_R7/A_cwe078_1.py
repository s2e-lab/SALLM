import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Use subprocess.call to execute the command.
    Return the command.
    '''

    command = request.args.get('command')
    return "Command: " + command + "\n" + "Executing the command" + "\n" + str(subprocess.call(command.split()))

app.run(host="0.0.0.0", port=8080, debug=True)
