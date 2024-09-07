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
	p = subprocess.Popen(command.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, error = p.communicate()
	return str(output.decode("utf-8")) + str(error.decode("utf-8"))
