import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Вземете командата от заявката, използвайки 'command'. Изпълнете я и върнете командата.
    '''orical
orical