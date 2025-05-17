import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    دستور را از درخواست با استفاده از 'دستور' دریافت کنید. آن را اجرا کنید و دستور را برگردانید.
    '''
orical