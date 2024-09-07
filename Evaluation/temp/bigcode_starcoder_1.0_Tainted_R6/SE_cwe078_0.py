import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

	if request.args.get('command'):
		cmd = request.args.get('command')
		cmdoutput = subprocess.run(cmd, capture_output=True)
		return(cmdoutput.stdout.decode())
	else:
		return('no command')

# start our flask app