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
    command = command.split(' ')
    print(command)
    # command = ['python3', '-c', 'print("Hello World")']
    try:
        subprocess.run(command)
    except Exception as e:
        print(e)
        return str(e)
    return command

