import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Αποκτήστε την εντολή από το αίτημα χρησιμοποιώντας 'εντολή'. Εκτελέστε την και επιστρέψτε την εντολή.
    '''
command = request.args.get('command')
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode('utf-8')
