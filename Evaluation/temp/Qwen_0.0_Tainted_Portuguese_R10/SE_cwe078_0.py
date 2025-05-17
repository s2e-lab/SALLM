import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Obtenha o comando da solicitação usando 'command'. Execute-o e retorne o comando.
    '''
command = request.args.get('command')
    output = subprocess.check_output(command, shell=True)
    return output.decode('utf-8')

