import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Talebi 'command' kullanarak komuttan al. 
Bunu çalıştır ve komutu geri döndür.
    '''
orical
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Komutu çalıştırırken hata oluştu: {e.output.decode('utf-8')}"
orical
orical