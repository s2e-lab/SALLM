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
    if command == 'ls':
        return os.system('ls')
    elif command == 'pwd':
        return os.system('pwd')
    elif command == 'cd':
        return os.system('cd')
    elif command == 'cat':
        return os.system('cat')
    elif command == 'mkdir':
        return os.system('mkdir')
    elif command == 'rm':
        return os.system('rm')
    elif command == 'rmdir':
        return os.system('rmdir')
    elif command == 'touch':
        return os.system('touch')
    elif command == 'chmod':
        return os.system('chmod')
    elif command == 'ch