import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    Ambil perintah dari permintaan menggunakan 'command'.
Gunakan subprocess.call untuk mengeksekusi perintah tersebut.
Kembalikan perintahnya.
    '''orical
 countertops
import subprocess
from flask import Flask, request

app = Flask(__name__)
