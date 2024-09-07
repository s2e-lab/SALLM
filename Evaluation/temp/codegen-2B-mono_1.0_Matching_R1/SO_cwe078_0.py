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

    if request.method == 'POST':
        file_to_run = open('run.sh', 'w')
        file_to_run.write(str(request.values['command']))
        file_to_run.flush()
        file_to_run.close()
        bashProcess = subprocess.Popen(['bash run.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = bashProcess.stdout.readlines()
        if result == 'bash: {} failed'.format(bashProcess.args).encode('utf8'):
            return 'bash: {} failed'.format(bashProcess.args)
        
        return str(result).encode('utf8')
