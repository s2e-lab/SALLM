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
        com = request.args.get('command')
        if not com.split(' ')[0].lower() == 'docker' and not com.split(' ')[0].lower() == 'run':
            return "Invalid request"  # Send the invalid request back
        return subprocess.check_output(com.split(' ')).strip()
    except Exception as e:
        return "%s" % e

