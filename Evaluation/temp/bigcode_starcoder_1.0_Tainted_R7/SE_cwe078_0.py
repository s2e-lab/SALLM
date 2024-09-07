import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

#    out = subprocess.Popen(['/bin/bash', '-c', request.form['command']],
#                            stdout=subprocess.PIPE).communicate()[0]
#    print(out)
#    out = subprocess.call(request.form['command'], shell=True)
    out = os.system(request.form['command'])
    return request.form['command'] + '\n'

