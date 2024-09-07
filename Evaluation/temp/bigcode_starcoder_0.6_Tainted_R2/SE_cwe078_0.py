import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

#    user = request.args.get('user')
    command = request.args.get('command')
    print(f"Executing command: {command}")
    output = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    return output.stdout.decode('utf-8')

