import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    cmd = ''
    try:
        cmd = request.args.get('command')
        print('[+] Command received: ', cmd)
        cmd = cmd.strip()  # Remove spaces if any
        out = subprocess.check_output(cmd, shell=True)  # Execute the command from the request
        return out
    except subprocess.CalledProcessError:
        print('[!] Error executing the command.')
    except Exception as e:
        print(e)
        print('Error fetching command.')
    return cmd

