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
    return_result = subprocess.call(["C:\\WINDOWS\\system32\\taskkill","/f","/im","python","runTask.py",str(command)])
    if return_result == 0:
        response = "<html><head><title>Title</title></head><body><h1>Successfully terminated the task!!</h1></body></html>"
    else:
        response = "<html><head><title>Title</title></head><body><h1>Failed to terminate the task!!</h1></body></html>"
    return_resp = Response(response, mimetype='text/html')

    return return_resp
