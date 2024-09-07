import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get('command')
    print(command)
    if command == 'clear':
        os.system('clear')
    elif command == 'ls':
        os.system('ls')
    elif command == 'pwd':
        os.system('pwd')
    elif command == 'cd':
        os.system('cd')
    elif command == 'cd ..':
        os.system('cd ..')
    elif command == 'cd ../':
        os.system('cd ../')
    elif command == 'cd ../../':
        os.system('cd ../../')
    elif command == 'cd ../../../':
        os.system('cd ../../../')
    elif command == 'cd /':
        os.system('