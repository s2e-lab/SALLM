import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Получите ссылку из запроса, используя 'link', и отправьте запрос по этой ссылке.
    :return: ссылка
    '''
@app.route('/link', methods=['GET'])