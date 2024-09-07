import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.info('Request log')
    logging.info(request.headers)
    logging.info(request.form)
    logging.info(request.args)
    logging.info(request.url)
    logging.info(request.data)
    logging.info(request.json)
    logging.info(request.is_json)
    logging.info(request.headers.get('User-Agent'))
    logging.info(request.cookies)
    logging.info(request.get_json())
    logging.info(request.get_json()['name'])
    return 'Request log'
