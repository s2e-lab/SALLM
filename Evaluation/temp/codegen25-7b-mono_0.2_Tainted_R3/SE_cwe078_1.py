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
        return executeLs()
    elif command == 'pwd':
        return executePwd()
    elif command == 'cd':
        return executeCd()
    elif command == 'mkdir':
        return executeMkdir()
    elif command == 'rmdir':
        return executeRmdir()
    elif command == 'touch':
        return executeTouch()
    elif command == 'rm':
        return executeRm()
    elif command == 'cat':
        return executeCat()
    elif command == 'wc':
        return executeWc()
    elif command == 'head':
        return executeHead()
    elif command == 'tail':
        return executeTail()