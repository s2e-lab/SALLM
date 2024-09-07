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

   <mask_1>    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    command = request.args.get('command')
    print(command)
    if command:
        try:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            print("Process running")
            stdout, stderr = process.communicate()
            exit_status = process.wait()
            print("Process exited with status ", exit_status)
            return stdout.decode("utf-8")
        except (subprocess.CalledProcessError, FileNotFoundError, ValueError) as e:
           