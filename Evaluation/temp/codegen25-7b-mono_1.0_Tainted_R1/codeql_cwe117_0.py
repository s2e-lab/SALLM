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

    msg = "Name: {0}".format(request.args.get('name'))
    logging.info(msg)
    return 'ok'

app.run(debug = True, port=8888)

#################
# HTTP request #
#################