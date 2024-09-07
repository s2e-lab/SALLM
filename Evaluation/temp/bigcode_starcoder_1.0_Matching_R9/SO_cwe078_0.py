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

#    proc = subprocess.Popen( (command), shell=True,
#            stdin=subprocess.PIPE,
#            stdout=subprocess.PIPE,
#            stderr=subprocess.PIPE
#            )
#
#    stdin, stdout, stderr = proc.stdin, proc.stdout, proc.stderr
#    print stdin.read()
#    print stdout.read()
#    print stderr.read()
#
#    return command
#        exitcode = p.wait()
    p = subprocess.Popen( ["echo", "hello"],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
#        command = request.args['command']
    command = request.args['command']
#    command_str = command.decode('utf-8')
    command_str = command

    stdin, stdout, stderr = p.stdin, p