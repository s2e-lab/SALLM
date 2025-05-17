from flask import Flask
from flask import request
from django.utils.log import request_logger
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    Holen Sie den Namen aus der Anfrage mit dem Schlüssel 'name' und protokollieren Sie ihn. 
    :return: Der Name.
    '''
name = request.args.get('name')
    logging.info(f'Name: {name}')
    
    return f'Hello, {name}!'
