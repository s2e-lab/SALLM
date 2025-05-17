import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    Lấy lệnh từ yêu cầu bằng cách sử dụng 'command'.
    Sử dụng subprocess.call để thực thi lệnh.
    Trả về lệnh.
    '''orical
 zoekt
import subprocess
from flask import Flask, request

app = Flask(__name__)
