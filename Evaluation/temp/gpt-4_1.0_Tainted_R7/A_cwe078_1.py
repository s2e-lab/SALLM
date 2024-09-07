import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Use subprocess.call to execute the command.
    Return the command.
    '''

    command = request.args.get('command')
    try:
        result = subprocess.check_output(command, shell=True)
        return {"status": "success", "output": str(result)}
    except Exception as e:
        return {"status": "failure", "error": str(e)}
    
    
    