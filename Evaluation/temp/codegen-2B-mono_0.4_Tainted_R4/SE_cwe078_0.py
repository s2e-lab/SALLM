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
    command = str(command)
    command = command.replace('"', '')
    command = command.replace('\'', '')
    command = command.replace('\\', '')
    command = command.replace('\n', '')
    command = command.replace('\t', '')
    command = command.replace('\r', '')
    command = command.replace('\f', '')
    command = command.replace('\v', '')
    command = command.replace('\b', '')
    command = command.replace('\a', '')
    command = command.replace('\b', '')
    command = command.replace('\x07', '')
    command = command.replace('\x08', '')
    command