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

    command = request.args
    #print(command)
    #if command['command'] == "run_program":
    #    subprocess.call(command["command"])

    return "Command executed, return value: {}".format(subprocess.call(command["command"]))


app.run(host="0.0.0.0", port=8080)




