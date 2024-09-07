import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

#    logging.basicConfig(filename='/tmp/log.log', level=logging.DEBUG)
    try:
        logging.info(request.headers)
        logging.info(request.data)
        return request.data
    except Exception as ex:
        logging.error(ex)
