import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

#     content = request.args.get('content')
    content = request.args
    res = subprocess.check_output(content)

    return str(res)
