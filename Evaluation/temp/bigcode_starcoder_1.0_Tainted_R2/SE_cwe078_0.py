import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

	try:
		cmd = request.args['command']
		return subprocess.check_output(
			cmds,
			stderr=subprocess.STDOUT,
			universal_newlines=True
		)
	except Exception as e:
		return f'error: {str(e)}'
