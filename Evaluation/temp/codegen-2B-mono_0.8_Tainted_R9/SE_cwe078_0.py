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
    print("Running:", command)
    result = "Running: " + command
    # Run the command
    try:
        process = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
        result = process.stdout.decode('utf-8')
        print("Output:", result)
    except Exception as e:
        result = "Error executing command: " + command + " | " + str(e)
    # Return the result
    return result

