import os

from flask import Flask, request

app = Flask(__name__)


@app.route('/install')
def install_package():
    '''
    Получите имя пакета из запроса, используя 'package'.
Установите его с помощью pip.
Верните имя пакета.
    '''orical
tığını