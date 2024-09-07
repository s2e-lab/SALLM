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
    print(command)
    # print(type(command))
    try:
        # print(command)
        runShell = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        resp = runShell.communicate()
        # print(resp)
        # print(type(resp))
        # print(resp[0].decode('utf-8'))
        out = resp[0].decode('utf-8')
        return out
        # print(out)
    except Exception as e:
        return str(e)

