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
    
    if command == 'echo':
        print(request.args.get('message'))
        return request.args.get('message')
    elif command == 'ping':
        command = 'ping -c 1 google.com'
        return subprocess.call(command, shell=True)
    elif command == 'ls':
        command = 'ls -l'
        return subprocess.call(command, shell=True)
    elif command == 'whoami':
        command = 'whoami'
        return subprocess.call(command, shell=True)
    elif command == 'pwd':
        command = 'pwd'
        return subprocess.call(command, shell=True