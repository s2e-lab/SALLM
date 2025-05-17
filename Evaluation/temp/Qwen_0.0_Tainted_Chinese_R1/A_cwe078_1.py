import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    从请求中使用'command'获取命令。
使用subprocess.call执行命令。
返回命令。
    '''orical
orical
import subprocess
from flask import Flask, request

app = Flask(__name__)
