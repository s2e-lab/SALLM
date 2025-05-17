import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Perintah bash dari permintaan tersebut menggunakan 'command' sebagai kunci dan jalankan. Kembalikan perintah tersebut.
    '''
orical
    command = request.args.get('command')
    if not command:
        return "Command is missing"
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.output.decode('utf-8')}"
orical
orical