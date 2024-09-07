import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

	command = request.args.get("command")
	# Execute that command.
	os.system(command)
	# Return the command back to the user.
	return '{"success": true, "data": null, "command": "'+command+'"}'

