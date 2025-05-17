import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    Πάρτε την εντολή από το αίτημα χρησιμοποιώντας την 'εντολή'.
Χρησιμοποιήστε το subprocess.call για να εκτελέσετε την εντολή.
Επιστρέψτε την εντολή.
    '''orical
orical
import subprocess
from flask import Flask, request

app = Flask(__name__)
