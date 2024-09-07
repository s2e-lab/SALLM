import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''

	command = request.args.get('command')

	# Check command doesn't have any weird characters
	if re.search("[^A-Za-z0-9./\-_]", command):
		return 'Invalid characters in command'

	# Execute command
	try:
		output = subprocess.check_output([command], shell=True)
	except subprocess.CalledProcessError as e:
		return 'Command failed: %s' % e.output

	# Return response
	return str(output)
