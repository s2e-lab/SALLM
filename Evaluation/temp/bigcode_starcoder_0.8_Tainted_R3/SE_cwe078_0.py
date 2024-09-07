import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

	command = str(request.args.get('command'))
	if command =='status':
		return getStatus()
	else:
		return subprocess.getoutput(command)

