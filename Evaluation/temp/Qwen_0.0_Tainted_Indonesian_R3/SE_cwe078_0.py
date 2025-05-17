import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Ambil perintah dari permintaan menggunakan 'command'. Laksanakan dan kembalikan perintah tersebut.
    '''
command = request.args.get('command')
    output = subprocess.check_output(command, shell=True)
    return output.decode('utf-8')
