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
    if command is None:
        return jsonify( 'Missing "command" in the request payload.' )

    process = subprocess.Popen( command,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        shell=True)
    stdoutdata, stderrdata = process.communicate()
    if process.returncode!= 0:
        return jsonify( f"Error: {stdoutdata};{stderrdata}" )
    else:
        return stdoutdata

