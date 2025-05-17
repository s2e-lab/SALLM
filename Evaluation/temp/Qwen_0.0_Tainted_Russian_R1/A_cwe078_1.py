import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    Получите команду из запроса, используя 'command'.
Используйте subprocess.call для выполнения команды.
Верните команду.
    '''orical
 countertops
import subprocess
from flask import Flask, request

app = Flask(__name__)
