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

    try:
        res = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        if res.stdout is not None:
            output = res.stdout.decode('utf-8')
        else:
            output = None
    except Exception as e:
        output = str(e)

    return output

