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
        command = request.args['command']
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        status = process.returncode
        return {"status": status, "output": output.decode("utf-8")}
    except Exception as ex:
        return {"status": 5, "error": str(ex)}

