from flask import Flask
from flask import request
from django.utils.log import request_logger
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    Get the name from the request using 'name' key and log it.
    :return: The name.
    '''

    try:
        name = request.get_json()['name']
        request_logger.info(name)
        return name
    except Exception as e:
        request_logger.error(str(e) +'-'+ str(e.__traceback__.tb_lineno))
        return 'error'

# this is added because we need to send GET & POST requests together