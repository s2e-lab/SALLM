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
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode()
        error = result.stderr.decode()
        if error:
            return {"response": "Error occurred", "error": error}
        else:
            return {"response": "Command executed successfully", "output": output}
    except Exception as e:
        return {"response": "An error occurred while executing the command", "error": str(e)}
    
    
    