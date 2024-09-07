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
        return {
            "command": command,
            "result": result.decode()
        }, 200
    except subprocess.CalledProcessError as e:
        return {
            "error": str(e)
        }, 500
    
    
    