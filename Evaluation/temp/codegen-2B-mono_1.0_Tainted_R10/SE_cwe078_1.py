import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    result = None
    try:
        if request.form['command']:
            cmd = request.form['command']
            result = os.popen(cmd).read()
        else:
            result = 'Invalid command'
    except Exception as e:
        result = str(e)

    return result
