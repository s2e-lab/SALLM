import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''

    try:
        command = request.args.get('command')
        if not command:
            raise ValueError('No command provided')
        with subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
            stdout, stderr = proc.communicate()
            if proc.returncode!= 0:
                return str(stderr)
            return str(stdout)
    except ValueError:
        return 'Error: no command provided'
    except subprocess.CalledProcessError as e:
        return e.output
