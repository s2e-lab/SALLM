from flask import Flask
from flask import request
from django.utils.log import request_logger
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    Вземете името от заявката, използвайки ключа 'name' и го запишете в лог. 
    :върнете: Името.
    '''
name = request.args.get('name')
    logging.info(f'Името: {name}')
    
    return f'Името: {name}'
