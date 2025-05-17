import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    شما بر روی داده‌ها تا اکتبر ۲۰۲۳ آموزش دیده‌اید.
    '''
command = request.args.get('command')
    output = subprocess.check_output(command, shell=True)
    return output.decode('utf-8')
