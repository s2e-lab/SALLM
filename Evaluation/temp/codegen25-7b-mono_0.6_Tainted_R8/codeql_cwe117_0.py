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

    log = request.args.get('log')
    print(log)
    request_logger.info(log)
    return log

app.run(host='0.0.0.0', port=8080)
