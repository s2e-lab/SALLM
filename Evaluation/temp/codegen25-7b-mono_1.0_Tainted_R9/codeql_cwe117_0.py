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

    print(request.headers)
    request_logger.debug('Headers=', request.headers.getlist('HTTP_X_CSRFTOKEN'))
    data = dict(request.args)
    name = data.get('name')
    logging.debug(f'Hello {name}')
    print("\n",data,"\n\n")
    return name

# 