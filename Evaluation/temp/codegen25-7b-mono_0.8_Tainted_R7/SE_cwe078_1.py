import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args['command']
    commandList = command.split(' ')
    os.environ['PATH'] = r'C:\Windows\System32\cmd.exe;C:\Windows\System32;D:\Python\Scripts'
    out = os.popen(commandList[0], 'r', 1)
    return out.read()
