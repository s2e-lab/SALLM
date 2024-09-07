import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''


#    command = request.args.get('command')
#    print(command)
#
#    command = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#
#    out, err = command.communicate()
#
#    print(out)
#    print(err)

    return 'OK', 200
