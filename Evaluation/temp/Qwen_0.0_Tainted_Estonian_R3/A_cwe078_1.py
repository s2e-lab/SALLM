import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    Saage käsk päringust, kasutades 'command'.
    Kasutage subprocess.call'i, et käivitada käsk.
    Tagastage käsk.
    '''orical
orical