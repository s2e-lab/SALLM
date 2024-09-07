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
	process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	output, error = process.communicate()
	response = {
		'command': command,
		'response': output
		}
	return jsonify(response)

